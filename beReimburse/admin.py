from django.contrib import admin

# Register your models here.
from django.contrib import admin
from beReimburse import models

admin.site.register(models.Reimburse)
admin.site.register(models.Employee)