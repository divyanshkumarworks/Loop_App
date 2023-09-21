from django.contrib import admin

# Register your models here.

from .models import BusinessHour, Store, StoreReport, StoreStatus, Timezone

admin.site.register(BusinessHour)
admin.site.register(Store)
admin.site.register(StoreReport)
admin.site.register(StoreStatus)
admin.site.register(Timezone)