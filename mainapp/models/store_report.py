from django.db import models
from .store import Store

class StoreReport(models.Model):
	report_status = models.CharField(max_length=255, default="Running")
	report_created = models.FileField(upload_to="reports",null=True,blank=True)

	def __str__(self):
		return f"store id: {self.store_id.store_id} report"

	