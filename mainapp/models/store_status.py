from django.db import models
from .store import Store

Status = (
	(0,"Inactive"),
	(1,"Active"),
	)

class StoreStatus(models.Model):
	store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name="store_status")
	timestamp_utc = models.DateTimeField(null=True, blank=True, auto_now_add=True)
	status = models.IntegerField(choices=Status)


	def __str__(self):
		return f"Store id: {self.store.store_id} status is {self.status} and timestamp_utc {self.timestamp_utc}"


