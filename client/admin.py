from django.contrib import admin
from .models import (
    Advanced_salary, Product, Purchase,
    Staff, Appointment, Appointment_data,
    Local_appointment, Service,
    Salary, Gallery, Feedback, Timeing,
    Package_name, Create_packages,
    Customers_package, My_package
)

@admin.register(Package_name)
class Pack_name(admin.ModelAdmin):
    list_display = ['id','user','name','total','fdate']

@admin.register(Create_packages)
class Pack_name(admin.ModelAdmin):
    list_display = ['id','user','name','fack','service','qty','price','special','fdate']

@admin.register(Customers_package)
class Pack_name(admin.ModelAdmin):
    list_display = ['id','user','pk_names','pk_name','name','contact','email','advance','total','fdate']

@admin.register(My_package)
class Pack_name(admin.ModelAdmin):
    list_display = ['id','user','customers','cust','fack','service','qty','price','special','fdate']


# @admin.register(Staffwork)
# class staff(admin.ModelAdmin):
#     list_display = ['id','staff_member','appointment_data']


@admin.register(Staff)
class staff(admin.ModelAdmin):
    list_display = ['id','user','profile','name','phone','email','service','fdate']


@admin.register(Timeing)
class time(admin.ModelAdmin):
    list_display = ['id','user','staff','in_date','in_time','out_date','out_time','fdate','tell']


@admin.register(Service)
class serv(admin.ModelAdmin):
    list_display = ['id','user','name','img','text','cost','fdate']



@admin.register(Advanced_salary)
class ad_salar(admin.ModelAdmin):
    list_display = ['id','user','staff','pay','month','fdate','ftime']

@admin.register(Salary)
class salar(admin.ModelAdmin):
    list_display = ['id','user','staff','pay','extra','month','advance','fdate','ftime']


@admin.register(Product)
class prod(admin.ModelAdmin):
    list_display = ['id','user','name','price','total','img','text','fdate']

@admin.register(Purchase)
class Purchase(admin.ModelAdmin):
    list_display = ['id','user','product','pro_name','name','phone','price','qty','fdate']

# @admin.register(Membership)
# class member(admin.ModelAdmin):
#     list_display = ['id','user','name','package','discount','more','start_date','end_date','fdate']


@admin.register(Local_appointment)
class local(admin.ModelAdmin):
    list_display = ['id','user','name','phone','email','service','staff','datex','timex','fdate']


@admin.register(Feedback)
class feed(admin.ModelAdmin):
    list_display = ['id','user','name','phone','feed','fdate']


@admin.register(Gallery)
class gall(admin.ModelAdmin):
    list_display = ['id','user','name','gall','fdate']


# @admin.register(Advance_salary)
# class adva_sala(admin.ModelAdmin):
#     list_display = ['id','user','staff','pay','when','fdate']


@admin.register(Appointment)
class appoint(admin.ModelAdmin):
    list_display = ['id','user','uniq','customer','phone','datex','timex','service','staff','fdate']


@admin.register(Appointment_data)
class appoint(admin.ModelAdmin):
    list_display = ['id','user','uniq','customer','phone','datex','timex','service','staff','fdate']


# @admin.register(After_appoitnment)
# class after(admin.ModelAdmin):
#     list_display = ['id','cust','when','service','amount','staff_member','fdate']


 

# @admin.register(Package)
# class staff(admin.ModelAdmin):
#     list_display = ['id','name','service','free','text','amount','fdate']

