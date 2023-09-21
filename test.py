from pytz import timezone as pytz_timezone 

target_timezone = pytz_timezone("America/Chicago")
print(type(target_timezone))