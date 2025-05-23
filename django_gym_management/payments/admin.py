from django.contrib import admin
import payments.models as models
# Register your models here.

admin.site.register(models.FeePackage)
admin.site.register(models.Bill)