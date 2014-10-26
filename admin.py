from .models import *
from django.contrib import admin

class SmsUserAdmin(admin.ModelAdmin):
    list_display  = ('name', 'number', 'email')
    search_fields = ['name', 'number', 'email']


admin.site.register(SmsUser, SmsUserAdmin)