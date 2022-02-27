from django.forms import widgets
import django_filters
from django_filters import DateFilter,CharFilter
from .models import Advanced_salary, Appointment, Local_appointment, Salary
from django import forms

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