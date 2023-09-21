from django.db import models
from .timezone import Timezone

class Store(models.Model):
	store_id = models.BigIntegerField(primary_key=True,unique=True)
	timezone_id = models.ForeignKey(Timezone, on_delete=models.PROTECT, null=True)

	def __str__(self):
		return f"store id: {self.store_id}"

