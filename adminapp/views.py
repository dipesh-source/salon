from django.shortcuts import redirect, render
from adminapp.models import Account_access, Extend_access
from .forms import ( 
    Register_form, Changepassword_form, Login_form,
    UpdateClient_profile, Access_form
)
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from .forms import Register_form
from django.http import HttpResponseNotFound


'''
    admin will Log-in by there function
'''
def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = Login_form(data = request.POST,request=request)
            if fm.is_valid():
                us = fm.cleaned_data['username']
                pas = fm.cleaned_data['password']
                au = authenticate(username = us,password = pas)
                if au is not None:
                    login(request, au)
                    if request.user.is_superuser:
                        return HttpResponseRedirect('/myadmin/mainpage/')
                    elif request.user.is_authenticated:
                        return HttpResponseRedirect('/client/homepage/')
                    else:
                        return None
            else:
                messages.error(request, 'check username or password')
        else:
            fm = Login_form()
        return render(request, 'adminapp/login.html',{'form':fm})
    elif request.user.is_superuser:
        return redirect('/myadmin/mainpage/')
    else: 
        return redirect('/client/homepage/')

'''
    it is remder homepage of software
'''
@user_passes_test(lambda u : u.is_superuser, login_url='/')
def homepage(request):  
    if request.method == 'POST':
        fm = Register_form(request.POST)
        if fm.is_valid():
            name = fm.save()
            messages.success(request,f'''{name} profile is created''')
    else:
        fm = Register_form()
    data = User.objects.all().order_by('id').reverse()
    context = {'form':fm,'data':data}
    return render(request, 'adminapp/admin_home.html',context)

'''
    delets access
'''
def delete_access_data(request,del_data):
    try:
        apd = Extend_access.objects.get(pk=del_data)
        messages.success(request, "Data Deleted")
    except ObjectDoesNotExist:
        return HttpResponse("<h1>Data Not Found<br></h1>ObjectDoesNotExist Exception Occur...<small><small/>")
    apd.delete()
    return redirect('/myadmin/give-access/')

'''
    will update(extends) client account access
'''
@user_passes_test(lambda u : u.is_superuser, login_url='/')
def update_access(request,upacc):
    if request.method == 'POST':
        dt = Account_access.objects.get(pk=upacc)
        fm = Access_form(request.POST, instance=dt)
        if fm.is_valid():
            fm.save()
            messages.success(request,f'''{dt.user} profile is updated''')
    else:
        try:
            dt = Account_access.objects.get(pk=upacc)
        except ObjectDoesNotExist:
            return HttpResponseNotFound('<h1 style="color:red;">Your Data Is Not Found</h1>')
        fm = Access_form(instance=dt)
    data = Extend_access.objects.filter(user=dt.user)
    context = {'form':fm,'data':data}
    return render(request,'adminapp/update_access.html',context)

'''
    will give access to the new memeber
'''
@user_passes_test(lambda u : u.is_superuser, login_url='/')
def give_access(request):
    if request.method == 'POST':
        fm = Access_form(request.POST)
        if fm.is_valid():
            us = fm.cleaned_data['user']
            mo = fm.cleaned_data['month']
            sd = fm.cleaned_data['set_date']
            st = fm.cleaned_data['set_time']
            ed = fm.cleaned_data['ex_date']
            et = fm.cleaned_data['ex_time']
              
            if Account_access.objects.filter(user=us).exists():
                messages.success(request,f'''{us} alredy exists''')
            else:
                data = Account_access(user=us,month=mo,set_date=sd,set_time=st,ex_date=ed,ex_time=et)
                data.save()
                fm = Access_form()
                messages.success(request,'data saves carefully')
    else:
        fm = Access_form()
    data = Account_access.objects.all()
    context = {'form':fm,'data':data}
    return render(request,'adminapp/access.html',context)

'''
    will return client data for the updat informations
'''
@user_passes_test(lambda u : u.is_superuser, login_url='/')
def update_client(request,uid):
    if request.method == 'POST':
        dt = User.objects.get(pk=uid)
        fm = UpdateClient_profile(request.POST, instance=dt)
        if fm.is_valid():
            name = fm.save()
            messages.success(request,f'''{name} profile is updated''')
    else:
        try:
            dt = User.objects.get(pk=uid)
        except ObjectDoesNotExist:
            return HttpResponseNotFound('<h1 style="color:red;">Your Data Is Not Found</h1>')
        fm = UpdateClient_profile(instance=dt)
    context = {'form':fm}
    return render(request,'adminapp/update_data.html',context)
'''
    user or admin will logout from this function
'''
def logout_view(request):
    logout(request)
    return redirect('/')