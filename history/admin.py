from django.contrib import admin

# Register your models here.

from .models import Materials, ThrownTrash

admin.site.register(Materials)

class ThrownThrashAdmin(admin.ModelAdmin):
    fields = ['material', 'weight', 'thrown_date']
    list_display = ('material', 'weight', 'thrown_date')

admin.site.register(ThrownTrash, ThrownThrashAdmin)