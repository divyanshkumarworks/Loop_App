from django.db import models
from .store import Store

DayofWeek = (
	(0, "Monday"),
	(1, "Tuesday"),
	(2, "Wednesday"),
	(3, "Thursday"),
	(4, "Friday"),
	(5, "Saturday"),
	(6, "Sunday"),
)

class BusinessHour(models.Model):
	store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name="store_hours")
	dayOfWeek = models.IntegerField(choices=DayofWeek)
	start_time = models.TimeField()
	end_time = models.TimeField()

	def __str__(self):
		day_of_week = self.get_dayOfWeek_display()
		return f"{self.store.store_id} {day_of_week} works {self.start_time} to {self.end_time}"