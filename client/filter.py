from django.forms import widgets
import django_filters
from django_filters import DateFilter,CharFilter
from .models import (Advanced_salary, Appointment, 
Local_appointment,
Purchase, Salary, History_customers_package,
History_my_package
 )
from django import forms

'''
    history of my packages
'''
class History_package_filter(django_filters.FilterSet):
    class Meta:
        model = History_my_package
        fields = ['cust','fack','service']

'''
    history of customers packages
'''
class History_customer_filter(django_filters.FilterSet):
    class Meta:
        model = History_customers_package
        fields = ['pk_name','name','contact']


'''
    django filter API for the data the data
'''
class App_filter(django_filters.FilterSet):
    class Meta:
        model = Appointment
        fields = ['phone','customer','datex']
       
'''
    django filter API for the data the data
'''
class Local_filter(django_filters.FilterSet):
    class Meta:
        model = Local_appointment
        fields = ['phone','name','datex']

'''
    for salary filter
'''
class Salary_filter(django_filters.FilterSet):
    class Meta:
        model = Salary
        fields = ['month','fdate']       

'''
    advanced salary filter
'''
class Advanced_filter(django_filters.FilterSet):
    class Meta:
        model = Advanced_salary
        fields = ['month','fdate']
  
'''
    product sales data
'''
class Product_sales(django_filters.FilterSet):
    class Meta:
        model = Purchase
        fields = ['product','name','phone']










# class AutherFilter(django_filters.FilterSet):
#     start_date = DateFilter(
#         field_name="our date name fielfs Ex. fdate = models... ",lookup_expr='gte')
#     end_date = DateFilter(
#         field_name="our date name fielfs Ex. fdate = models... ",lookup_expr='lte')
#     note = CharFilter(field_name='note',lookup_expr='icontains')
#     class Meta:
#         model = Author
#         fields = ['name']
#         exclude = ['fdate']