import imp
from django import forms
from django.contrib.auth.forms import UserChangeForm, AuthenticationForm, PasswordChangeForm, SetPasswordForm, UserCreationForm
from django.contrib.auth.models import User
from .models import Account_access

'''
    for give account access for dead line
'''
class Access_form(forms.ModelForm):
    class Meta:
        model = Account_access
        fields = ['user','month','set_date','set_time','ex_date','ex_time']
        labels = {
            'user':'select member',
            'month':'Enter Month',
            'set_date':'Starting Date',
            'set_time':'Starting Time',
            'ex_date':'Expiry Date',
            'ex_time':'Expiry Time',
        }
        widgets = {
            'user':forms.Select(attrs={'class':'form-control'}),
            'month':forms.NumberInput(attrs={'class':'form-control'}),
            'set_date':forms.DateInput(attrs={'type':'date','class':'form-control'}),
            'set_time':forms.TimeInput(attrs={'type':'time','class':'form-control'}),
            'ex_date':forms.DateInput(attrs={'type':'date','class':'form-control'}),
            'ex_time':forms.TimeInput(attrs={'type':'time','class':'form-control'}),
        }
        error_messages = {
            'user':{'required':'select client'},
            'month':{'required':'enter the data'},
            'set_date':{'required':'select start date'},
            'set_time':{'required':'select start time'},
            'ex_date':{'required':'select exp date'},
            'ex_time':{'required':'select exp time'},
        }
'''
    update the client information
'''
class UpdateClient_profile(UserChangeForm):
    username = forms.CharField(max_length=100,label_suffix='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Username'}), error_messages={'required':'enter username'})
    first_name = forms.CharField(required=False,max_length=100,label_suffix='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter First Name'}))
    last_name = forms.CharField(required=False,max_length=100,label_suffix='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Last Name'}))
    email = forms.CharField(max_length=100,label_suffix='',widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Email Id'}),error_messages={'required':'enter email id'},required=True)
    # is_active = forms.CharField(label='Active User',label_suffix='',widget=forms.CheckboxInput(attrs={'class':'form-check-input','type':'checkbox'}))
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','is_active','is_staff','is_superuser']

'''
    will create user (register)
'''
class Register_form(UserCreationForm):
    username = forms.CharField(max_length=100,label_suffix='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Username'}), error_messages={'required':'enter username'})
    first_name = forms.CharField(required=False,max_length=100,label_suffix='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter First Name'}))
    last_name = forms.CharField(required=False,max_length=100,label_suffix='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Last Name'}))
    email = forms.CharField(max_length=100,label_suffix='',widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Email Id'}),error_messages={'required':'enter email id'},required=True)
    password1 = forms.CharField(label_suffix='',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter password'}),error_messages={'required':'enter password'})
    password2 = forms.CharField(label_suffix='',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Confirm password'}),error_messages={'required':'enter confirm password'})
    # is_active = forms.CharField(label='Active User',label_suffix='',widget=forms.CheckboxInput(attrs={'class':'form-check-input','type':'checkbox'}))
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','is_active','is_staff','is_superuser','password1','password2']


'''
    will login to admin panel for admin Or normal user
'''
class Login_form(AuthenticationForm):
    username = forms.CharField(label='Enter Username',label_suffix='',widget=forms.TextInput(attrs={'class':'form-colntrol'}),error_messages={'required':'Please, enter username'})
    password = forms.CharField(label='Enter Password',label_suffix='',widget=forms.PasswordInput(attrs={'class':'form-control'}),error_messages={'required':'enter your password'})
    class Meta:
        model = User
        fields = ['username','password']

'''
    will change password from the own session (without Email)
'''
class Changepassword_form(PasswordChangeForm):
    old_password = forms.CharField(label='enter old password',label_suffix='',widget=forms.PasswordInput(attrs={'class':'form-control'}),error_messages={'required':'old password required'})
    new_password1 = forms.CharField(label='set new password',label_suffix='',widget=forms.PasswordInput(attrs={'class':'form-control'}),error_messages={'required':'enter new password'})
    new_password2 =  forms.CharField(label='confirm password',label_suffix='',widget=forms.PasswordInput(attrs={'class':'form-control'}),error_messages={'required':'confirm new password'})
    class Meta:
        model = User
        fields = ['old_password','new_password1','new_password2']