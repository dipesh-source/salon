from django.contrib import admin
from .models import Account_access, Extend_access

@admin.register(Account_access)
class access(admin.ModelAdmin):
    list_display = ['user','month','set_date','set_time','ex_date','ex_time','fdate']
    
@admin.register(Extend_access)
class access(admin.ModelAdmin):
    list_display = ['user','month','set_date','set_time','ex_date','ex_time','fdate']
    