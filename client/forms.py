from datetime import date
from django.forms import forms, widgets
from django import forms
from .models import (
    Staff, Appointment, Appointment_data,
    Local_appointment, Service,
    Salary, Gallery, Feedback, Timeing,
    Advanced_salary,Package_name, My_package,
    Create_packages, Customers_package
)
#####################  all the packages code hehe   ####################

'''
    create package name form
'''
class Package_name_form(forms.ModelForm):
    class Meta:
        model = Package_name
        fields = ['name','total']
        labels = {
            'name':'Create Package Name',
            'total':'Total Price Of Package'
        }
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'total':forms.NumberInput(attrs={'class':'form-control'}),
        }
        error_messages = {
            'name':{'required':'Please, create name'},
        }

    
'''
    will create package form
'''
class Create_package_form(forms.ModelForm):
    class Meta:
        model = Create_packages
        fields = ['service','qty','price']
        labels = {
            # 'fack':'Select Name',
            'service':'Enter Service Name',
            'qty':'Enter quentity',
            'price':'Enter Points'
        }
        widgets = {
            'service':forms.TextInput(attrs={'class':'form-control'}),
            'qty':forms.NumberInput(attrs={'class':'form-control'}),
            'price':forms.NumberInput(attrs={'class':'form-control'}),
        }
        error_messages = {
            'service':{'required':'enter service name'},
            'qty':{'required':'enter qty'},
            'price':{"required":'enter points'}
        }

'''
    create the customers packages form
'''
class Customers_package_form(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request") # store value of request 
        xxx = Package_name.objects.filter(user=self.request.user)
        # self.fields['pk_name'] = Package_name.objects.filter(user=self.request.user)
        print(self.request.user, xxx) 
        super().__init__(*args, **kwargs)

    def clean(self):
        print(self.request.user) # request now available here also
        pass
    # pk_name = forms.ModelChoiceField(queryset=Package_name.objects.all(),label='Select Name',widget=forms.Select(attrs={'class':'form-control'}))
    class Meta:
        model = Customers_package
        fields = ['name','contact','email','advance','total']
        labels = {
            'pk_name':'select package',
            'name':'Enter Name',
            'contact':'Enter Contact Number',
            'advance':'Advance Payment',
            'total':'Total Payment'
        }
        widgets = {
            # 'pk_name':forms.ModelChoiceField(queryset=Create_packages.objects.all()),
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'contact':forms.NumberInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'advance':forms.NumberInput(attrs={'class':'form-control'}),
            'total':forms.NumberInput(attrs={'class':'form-control'}),
        }
        error_messages = {
            'pk_name':{'required':'Select Package'},
            'name':{'required':'enter name'},
            'contact':{'required':'enter phone number'},
        }

        

#####################  all the packages code hehe   ####################


'''
    staff form
'''
class Staff_form(forms.ModelForm):
    profile = forms.ImageField(required=False,widget=forms.FileInput())
    class Meta:
        model = Staff
        fields = ['profile','name','phone','email','service']
        labels = {
            'profile':'Select member Image',
            'name':'Enter Member Name',
            'phone':'Enter Contact Number',
            'email':'Enter Email Id',
            'service':'Add Work'
        }
        error_messages = {
            'name':{'required':'enter the member name'},
            'phone':{'required':'enter phone number'},
        }
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'phone':forms.NumberInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'service':forms.TextInput(attrs={'class':'form-control'}),
        }
'''
    appointment form
'''
class Appointment_form(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['uniq','customer','phone','datex','timex','service','staff']
        labels = {
            'uniq':'Create Unique Name',
            'customer':'Enter Name',
            'phone':'Contact Number',
            'datex':'Select Date',
            'timex':'Select Time',
            'service':'Enter what service',
            'staff':'Select Satff Member',
        }
        widgets = {
            'uniq':forms.TextInput(attrs={'class':'form-control'}),
            'customer':forms.TextInput(attrs={'class':'form-control'}),
            'phone':forms.NumberInput(attrs={'class':'form-control'}),
            'datex':forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'timex':forms.TimeInput(attrs={'class':'form-control','type':'time'}),
            'service':forms.TextInput(attrs={'class':'form-control'}),
            'staff':forms.Select(attrs={'class':'form-control'}),
        }
        error_messages = {
            'customer':{'required':'please, enter customer name'},
            'phone':{'required':'enter phone number'},
            'datex':{'required':'select appointment Date'},
            'timex':{'required':'select appointment Time'},
        }
    
'''
    local appointment forms
'''
class Localappointment_form(forms.ModelForm):
    class Meta:
        model = Local_appointment
        fields = ['name','phone','email','service','staff','datex','timex']
        labels = {
            'name':'Enter Customer Name',
            'phone':'Enter Phone Number',
            'email':'Enter Email Id',
            'service':'Enter Service',
            'staff':'Staff Member',
            'datex':'Select Date',
            'timex':'Select Time',
        }
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'phone':forms.NumberInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'service':forms.TextInput(attrs={'class':'form-control'}),
            'staff':forms.TextInput(attrs={'class':'form-control'}),
            'datex':forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'timex':forms.TimeInput(attrs={'class':'form-control','type':'time'}),
        }
        error_messages = {
            'name':{'required':'enter the customer name'},
            'phone':{'required':'enter contact number'},
            'datex':{'required':'please, select Date'},
            'timex':{'required':'please, select Time'},
        }

'''
    service forms
'''
class Service_form(forms.ModelForm):
    # img = forms.CharField(required=False, label='Select Img',label_suffix='',
    # widget=forms.FileInput()
    # )
    class Meta:
        model = Service
        fields = ['name','img','text','cost']
        labels = {
            'name':'Service Name',
            'img':'Select Service Image',
            'text':'Note For Service',
            'cost':'Price',
        }
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'text':forms.TextInput(attrs={'class':'form-control'}),
            'cost':forms.NumberInput(attrs={'class':'form-control'}),
        }
        error_messages = {
            'name':{'required':'enter the service name'},
            'cost':{'required':'price is required'},
        }

'''
    salary forms
'''
class Salary_form(forms.ModelForm):
    class Meta:
        model = Salary
        fields = ['pay','extra','month']
        labels = {
            'pay':'Payment',
            'extra':'Extra',
            'date':'Select Date'
        }
        widgets = {
            'pay':forms.NumberInput(attrs={'class':'form-control'}),
            'extra':forms.NumberInput(attrs={'class':'form-control'}),
            'month':forms.DateInput(attrs={'class':'form-control','type':'month'}),
        }
        error_messages = {
            'name':{'required':'enter payment'},
            'month':{'required':'select payment month'},
        }

'''
   pay advanced salary forms
'''
class AdvanceSalary_form(forms.ModelForm):
    class Meta:
        model = Advanced_salary
        fields = ['pay','month']
        labels = {
            'pay':'Payment',
            'month':'Select month'
        }
        widgets = {
            'pay':forms.NumberInput(attrs={'class':'form-control'}),
            'month':forms.DateInput(attrs={'class':'form-control','type':'month'}),
        }
        error_messages = {
            'name':{'required':'enter payment'},
            'datex':{'required':'select payment date'},
        }

'''
    gallery forms
'''
class Gallery_form(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ['name','gall']
        labels = {
            'name':'Enter post name',
            'gall':'Select Image'
        }
        widgets = {
            'name':forms.Textarea(attrs={'class':'form-control'}),
            # 'gall':forms.DateInput(attrs={'class':'form-control','type':'date'}),
        }
        error_messages = {
            'name':{'required':'enter image name'},
            'gall':{'required':'select image'},
        }

'''
    feedback form
'''
class Feedback_form(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name','phone','feed']
        labels = {
            'name':'Enter Your Name',
            'phone':'Phone Number',
            'feed':'Your Feedback',
        }
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'phone':forms.NumberInput(attrs={'class':'form-control'}),
            'feed':forms.Textarea(attrs={'class':'form-control'}),
        }
        error_messages = {
            'name':{'required':'enter your name'},
            'phone':{'required':'must be phone number'},
            'feed':{'required':'write your Feedback'},
        }

'''
    timing form
'''
class Timeing_form(forms.ModelForm):
    # staff = forms.Select(widget=forms.Select(attrs={'disabled':'disabled'}))
    class Meta:
        model  = Timeing
        fields = ['staff']
        widgets = {
            # 'staff':forms.Select(attrs={'class':'form-control'})
        }
        # labels = {
        #     'staff':'Select Staff Member',
        #     'in_time':'Select In Time',
        #     'out_time':'Select Out Time',
        # }
        # widgets = {
        #     'in_time':forms.DateTimeInput(attrs={'class':'form-control','type':'datetime-local'}),
        #     'out_time':forms.DateTimeInput(attrs={'class':'form-control','type':'datetime-local'}),
        # }
        # error_messages = {
        #     'in_time':{'required':'please, select In-Time'},
        #     # 'out_time':{'required':'please, select Out-Time'},
        # }
        # widgets = {
        #     'staff' : forms.Select()
        # }