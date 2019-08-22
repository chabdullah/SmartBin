from django.contrib import admin

# Register your models here.

from .models import Materials, ThrownTrash

admin.site.register(Materials)
admin.site.register(ThrownTrash)