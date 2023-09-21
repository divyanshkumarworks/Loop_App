from django.db import models

class Timezone(models.Model):
	timezone = models.CharField(max_length=100)

	def __str__(self):
		return f"{self.timezone}"