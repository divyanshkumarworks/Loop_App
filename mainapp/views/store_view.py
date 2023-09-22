from django.views import View
from mainapp.helper import generate_report_id, get_last_hour_record, get_last_day_record, get_last_week_record
from mainapp.models import Store, StoreStatus, StoreReport, BusinessHour
from django.utils import timezone
from django.http import JsonResponse
from pytz import timezone as pytz_timezone
import csv
import tempfile
import os
import threading
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt, name='dispatch')
class StoreView(View):
	def get(self, request):

		store_report = StoreReport.objects.create()

		def create_report_thread(report_id):
			try:
				store = Store.objects.all()[:200]
				i = 1
				csv_data = []
				for entry in store:
					
					print(i)
					i += 1

					#get stores status
					tz = entry.timezone_id.timezone if entry.timezone_id.timezone else 'America/Chicago'
					target_timezone = pytz_timezone(tz)

					utc_time = StoreStatus.objects.all().order_by('-timestamp_utc').first().timestamp_utc
					local_time = utc_time.astimezone(target_timezone)
					current_day = local_time.weekday()
					current_time = local_time.time()

					last_hour_data = get_last_hour_record(entry, utc_time, current_day, current_time)

					last_day_data = get_last_day_record(entry, utc_time, current_day, current_time)

					last_week_data = get_last_week_record(entry, utc_time, current_day, current_time)

					csv_data.append(
						[
							entry.store_id, 
							last_hour_data["up_time"], 
							last_day_data["up_time"], 
							last_week_data["up_time"], 
							last_hour_data["down_time"], 
							last_day_data["down_time"], 
							last_week_data["down_time"]
						]
					)


				with tempfile.TemporaryDirectory() as temp_dir:
					temp_file_path = os.path.join(temp_dir, f"{report_id}.csv")

					with open(temp_file_path, "w", newline='') as csv_file:
						csv_writer = csv.writer(csv_file)
						csv_writer.writerow(["store_id", "uptime_last_hour(in minutes)", "uptime_last_day(in hours)", "update_last_week(in hours)", "downtime_last_hour(in minutes)", "downtime_last_day(in hours)", "downtime_last_week(in hours)"])
						for data in csv_data:
							csv_writer.writerow(data)

					store_report.report_created.save(f"{report_id}.csv", open(temp_file_path, "rb"))
					store_report.report_status = "Completed"
					store_report.save()
			
			except Exception as error:
				return JsonResponse({'messgae': str(error)}, status=500)


		thread = threading.Thread(target=create_report_thread, args=(store_report.id,))
		thread.start()

		return JsonResponse({'report_id': store_report.id}, status=200)

	def post(self, request, report_id):

		try:
			store_report = StoreReport.objects.get(id=report_id)
		except StoreReport.DoesNotExist:
			return JsonResponse({'message': 'Invalid report_id'}, status=200)

		if store_report.report_status == "Completed":
			report_url = os.path.join(settings.MEDIA_ROOT, store_report.report_created.name)
			return JsonResponse({'status': 'Complete', 'csv_file': report_url}, status=200)
		else:
			return JsonResponse({'status': 'Running'}, status=200)