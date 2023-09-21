import csv
from Loop_App.wsgi import *
from django.db import transaction
from mainapp.models import Store, Timezone, StoreStatus, BusinessHour

from datetime import datetime

format_string = "%Y-%m-%d %H:%M:%S.%f %Z"

# with open('csv/timezone.csv', mode='r') as csv_file: 
# 	csv_reader = csv.DictReader(csv_file) 

# 	for item in csv_reader:
# 		store_id = item["store_id"]
# 		timezone_str = item["timezone_str"]
# 		timezone_id = 0

# 		try:
# 			with transaction.atomic():
# 				timezone = Timezone.objects.get(timezone=timezone_str)
# 				timezone_id = timezone
# 		except Exception as e:
# 			timezone = Timezone(timezone=timezone_str)
# 			timezone.save()
# 			timezone_id = timezone

# 		with transaction.atomic():
# 			store = Store(store_id=store_id, timezone_id=timezone_id)
# 			store.save()

data = []
i = 0

with open('csv/store_status.csv', mode='r') as csv_file:
	csv_reader = csv.DictReader(csv_file)

	for item in csv_reader:

		store = None
		status = None

		if item['status'] == "active":
			status = 1
		elif item['status'] == "inactive":
			status = 0
		
		datetime_str = item['timestamp_utc']
		datetime_utc = None
		if "." in datetime_str:
			datetime_utc = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S.%f %Z')
		else:
			datetime_utc = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S %Z')

		try:
			store = Store.objects.get(store_id=item['store_id'])		
			store = store
		except Exception as e:
			timezone = Timezone.objects.get(timezone='America/Chicago')
			with transaction.atomic():
				store = Store(store_id=item['store_id'], timezone_id=timezone)
				store.save()
				store = store

		data.append(StoreStatus(
			store_id=store.store_id, 
			status=status, 
			timestamp_utc=datetime_utc
			))

		if len(data) >= 1000:
			StoreStatus.objects.bulk_create(data)
			data = []

		print(i)
		i += 1

	if data:
		BusinessHour.objects.bulk_create(data)

# 		with transaction.atomic():
# 			status = StoreStatus(store_id=store.store_id, status=status, timestamp_utc=datetime_utc)
# 			status.save()

# 		print(f'Status with store id {store.store_id} saved')

# data = []

# with open('csv/Menu_hours.csv', 'r') as file:
# 	reader = csv.DictReader(file)
# 	store_id = None
# 	for row in reader:
# 		try:
# 			store = Store.objects.get(store_id=row['store_id'])		
# 			store_id = store
# 		except Exception as e:
# 			timezone = Timezone.objects.get(timezone='America/Chicago')
# 			with transaction.atomic():
# 				store = Store(store_id=row['store_id'], timezone_id=timezone)
# 				store.save()
# 				store_id = store

# 		data.append(BusinessHour(
# 			store = store_id,
# 			dayOfWeek=row['day'],
# 			start_time=row['start_time_local'],
# 			end_time=row['end_time_local']
# 			))

# 		print(data)

	# 	if len(data) >= 1000:
	# 		BusinessHour.objects.bulk_create(data)
	# 		data = []

	# if data:
	# 	BusinessHour.objects.bulk_create(data)

