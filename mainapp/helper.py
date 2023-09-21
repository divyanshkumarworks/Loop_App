import uuid
import datetime

def generate_report_id():
	report_id = uuid.uuid4()
	return report_id

def get_last_hour_record(store, utc_time, current_day, current_time):

	last_hour_data = {
		"up_time": 0,
		"down_time": 0,
	}

	is_store_open = store.store_hours.filter(dayOfWeek=current_day,start_time__lte=current_time,end_time__gte=current_time).exists()
	if not is_store_open:
		return last_hour_data
	
	last_hour_record = store.store_status.filter(timestamp_utc__gte=utc_time - datetime.timedelta(hours=1)).order_by('timestamp_utc')

	if last_hour_record:
		print("status", last_hour_record[0].status)
		if last_hour_record[0].status == 1:
			last_hour_data["up_time"] = 60
		else:
			last_hour_data["down_time"] = 60

	return last_hour_data

def get_last_day_record(store, utc_time, current_day, current_time):

	last_day_data = {
		"up_time": 0,
		"down_time": 0,
	}

	last_day = current_day - 1 if current_day > 0 else 6

	is_store_open = store.store_hours.filter(dayOfWeek__gte=last_day,start_time__lte=current_time,end_time__gte=current_time).exists()
	if not is_store_open:
		return last_day_data
	
	last_day_record = store.store_status.filter(timestamp_utc__gte=utc_time - datetime.timedelta(days=1)).order_by('timestamp_utc')

	if last_day_record:
		for record in last_day_record:
			is_in_store_hours = store.store_hours.filter(
				dayOfWeek=record.timestamp_utc.weekday(), 
				start_time__lte=record.timestamp_utc.time(), 
				end_time__gte=record.timestamp_utc.time()
			)
			if not is_in_store_hours:
				continue
			if last_day_record[0].status == 1:
				last_day_data['up_time'] += 1
			else:
				last_day_data['down_time'] += 1

		return last_day_data


def get_last_week_record(store, utc_time, current_day, current_time):

	last_week_data = {
		"up_time": 0,
		"down_time": 0,
	}

	last_week = current_day - 7 if current_day > 0 else 0

	is_store_open = store.store_hours.filter(dayOfWeek__gte=last_week, start_time__lte=current_time, end_time__gte=current_time).exists()
	if not is_store_open:
		return last_week_data

	last_week_record = store.store_status.filter(timestamp_utc__gte=utc_time - datetime.timedelta(days=7)).order_by('timestamp_utc')
	if last_week_record:
		for record in last_week_record:
			is_in_store_hours = store.store_hours.filter(
				dayOfWeek=record.timestamp_utc.weekday(), 
				start_time__lte=record.timestamp_utc.time(), 
				end_time__gte=record.timestamp_utc.time()
			)
			if not is_in_store_hours:
				continue
			if last_week_record[0].status == 1:
				last_week_data['up_time'] += 1
			else:
				last_week_data['down_time'] += 1

		return last_week_data