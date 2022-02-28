from django.http import BadHeaderError, HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.core.mail import send_mail
from django.db.models import Q
from .filter import App_filter, Local_filter, Salary_filter, Advanced_filter
from datetime import date, timedelta
from django.utils import timezone
from django.conf import settings

from smtplib import SMTPAuthenticationError, SMTPConnectError, SMTPDataError, SMTPException, SMTPNotSupportedError, SMTPRecipientsRefused, SMTPResponseException, SMTPSenderRefused
import datetime
from .forms import (
    AdvanceSalary_form, Localappointment_form, Staff_form, Timeing_form, Salary_form, Service_form,
    Local_appointment, Appointment_form,
    Gallery_form, Feedback_form, Appointment_form,
)
from .models import (
    Advanced_salary, Appointment_data, Purchase, Staff, Timeing, Service, Salary,
    Product,
    Local_appointment,
    Gallery, Feedback, Appointment,
)


@user_passes_test(lambda u: u.is_authenticated, login_url='/')
def client_home(request):
    if request.method == 'POST' and 'appoint' in request.POST:
        appf = Appointment_form(request.POST)
        if appf.is_valid():
            un = appf.cleaned_data['uniq']
            cu = appf.cleaned_data['customer']
            ph = appf.cleaned_data['phone']
            dt = appf.cleaned_data['datex']
            tm = appf.cleaned_data['timex']
            ser = appf.cleaned_data['service']
            # stf = appf.cleaned_data['staff']
            sff = request.POST.get('mystf')
            print('dipesh ###########################', sff)
            try:
                lela = Staff.objects.get(Q(user=request.user) & Q(name=sff))
            except ObjectDoesNotExist:
                return HttpResponse('<h1 style="margin-top:50px; color:red;"><center>Your Data Has Incorrect, Check Again Or Refresh The Page</center></h1>')
            except MultipleObjectsReturned:
                return HttpResponse(f'''<center><h1><span style="color:red"> {sff}</span> Is Already Exist So, Take Another Staff Name</h1></center>''')
            '''
                if not working in future 
                so, change the date validation
            '''
            # if datetime.date.today() == dt:
            apt = Appointment(user=request.user, uniq=un, customer=cu,
                              phone=ph, datex=dt, timex=tm, service=ser, staff=lela)
            apt.save()
            messages.success(request, 'Appointment Book Successfully')

            appf = Appointment_form()
            #     messages.success(request, 'Appointment Book Successfully')
            # elif dt >= datetime.date.today():
            #     what = Appointment_data(user=request.user, uniq=un, customer=cu,
            #                   phone=ph, datex=dt, timex=tm, service=ser, staff=lela)
            #     what.save()
            #     messages.success(request, 'Appointment Book Successfully')
            # else:
            #     messages.error(request,f'''Selected {dt}, Select Correct Date''')
    else:
        appf = Appointment_form()
    if request.method == 'POST' and 'btnstf' in request.POST:
        stffm = Staff_form(request.POST, request.FILES)
        if stffm.is_valid():
            pf = stffm.cleaned_data['profile']
            nm = stffm.cleaned_data['name']
            phn = stffm.cleaned_data['phone']
            em = stffm.cleaned_data['email']
            sv = stffm.cleaned_data['service']
            change = remove(nm)
            if Staff.objects.filter(Q(user=request.user) & Q(name=nm)).exists():
                messages.error(
                    request, f'{nm} is already exists, take another name')
                x = Staff.objects.filter(Q(user=request.user) & Q(service=sv))
                print(x, '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
            else:
                sf = Staff(user=request.user, profile=pf,
                           name=change, phone=phn, email=em, service=sv)
                sf.save()
                stffm = Staff_form()
                messages.success(request, 'staff is added')
    else:
        stffm = Staff_form()
    app = Appointment.objects.filter(user=request.user).count()
    today = Appointment.objects.filter(
        Q(user=request.user) & Q(datex=datetime.date.today())).count()
    today_ap = Appointment.objects.filter(
        Q(user=request.user) & Q(datex=datetime.date.today()))
    upcome = Appointment.objects.filter(
        Q(user=request.user) & Q(datex__gt=datetime.date.today())).count()
    upapp = Appointment.objects.filter(
        Q(user=request.user) & Q(datex__gt=datetime.date.today()))
    allapp = Appointment.objects.filter(
        Q(user=request.user) & Q(datex=datetime.date.today())).order_by('id').reverse()
    form = App_filter(request.GET, queryset=allapp)
    data = form.qs
    apsf = Appointment.objects.all().filter(user=request.user)
    stfff = Staff.objects.filter(user=request.user)
    x = datetime.datetime.now()
    y = timedelta(hours=1)
    next = Appointment.objects.filter(Q(user=request.user) & Q(
        datex=datetime.date.today()) & Q(timex__range=(x, x+y))).order_by('id').reverse()
    nxct = Appointment.objects.filter(Q(user=request.user) & Q(
        datex=datetime.date.today()) & Q(timex__range=(x, x+y))).count()
    a = datetime.datetime.now()
    b = timedelta(hours=2)
    by = Appointment.objects.filter(Q(user=request.user) & Q(
        datex=datetime.date.today()) & Q(timex__range=(x-y, x)))
    user_staff = Staff.objects.filter(user=request.user)
    print('ttttttttttttttiming ------------', x-y, 'currrrrrent time ', x)
    print(by, "+++===========================+++")
    print(allapp.query )
    context = {'form': form, 'my_staff': user_staff, 'staform': stffm, 'nextapp': next, 'nexnt': nxct, 'stff': stfff, 'upapp': upapp,
               'toapp': today_ap, 'apsf': apsf, 'appform': appf, 'total': app, 'today': today, 'upcome': upcome, 'allapp': data}
    return render(request, 'client/layout.html', context)


def remove(sname):
    return sname.replace(" ", "")


@user_passes_test(lambda u: u.is_authenticated, login_url='/')
def client_test(request):
    return render(request, 'client/home.html')


@user_passes_test(lambda u: u.is_authenticated, login_url='/')
def delete_appointment(request, delid):
    try:
        apd = Appointment.objects.get(pk=delid)
        messages.success(request, "Appoi't Deleted Successfully")
    except ObjectDoesNotExist:
        return HttpResponse("<h1>Data Not Found<br></h1>ObjectDoesNotExist Exception Occur...<small><small/>")
    apd.delete()
    return redirect('/client/homepage/')


@user_passes_test(lambda u: u.is_authenticated, login_url='/')
def in_time(request):
    if request.method == 'POST':
        tim = Timeing_form(request.POST)
        if tim.is_valid():
            sff = request.POST.get('mystf')
            try:
                lela = Staff.objects.get(Q(user=request.user) & Q(name=sff))
            except ObjectDoesNotExist:
                return HttpResponseNotFound('<h1 style="margin-top:50px; color:red;"><center>Your Data Has Incorrect, Check Again Or Refresh The Page</center></h1>')
            except MultipleObjectsReturned:
                return HttpResponseNotFound('<h1 style="margin-top:50px; color:red;"><center>Your Data Returning Multiple, Multiple Object Returning...</center></h1>')
            if Timeing.objects.filter(Q(user=request.user) & Q(in_date=datetime.date.today()) & Q(staff=lela)).exists():
                x = Timeing.objects.filter(Q(user=request.user) & Q(
                    in_date=datetime.date.today()) & Q(staff=lela))
                messages.error(request, f'''{sff} Is Already Alive''')
            else:
                stime = Timeing(user=request.user, staff=lela)
                stime.save()
                tim = Timeing_form()
                messages.success(request, f'''{lela} In Time Is Saved''')
    else:
        tim = Timeing_form()

    stfff = Staff.objects.filter(user=request.user)
    mytime = Timeing.objects.filter(
        Q(user=request.user) & Q(in_date=datetime.date.today()))
    print('#############################', mytime.query)
    today = Appointment.objects.filter(
        Q(user=request.user) & Q(datex=datetime.date.today())).count()
    today_ap = Appointment.objects.filter(
        Q(user=request.user) & Q(datex=datetime.date.today()))
    upcome = Appointment_data.objects.filter(
        Q(user=request.user) & Q(datex__gt=datetime.date.today())).count()
    upapp = Appointment_data.objects.filter(
        Q(user=request.user) & Q(datex__gt=datetime.date.today()))
    app = Appointment_data.objects.filter(user=request.user).count()
    x = datetime.datetime.now()
    y = timedelta(hours=1)
    next = Appointment.objects.filter(Q(user=request.user) & Q(
        datex=datetime.date.today()) & Q(timex__range=(x, x+y))).order_by('id').reverse()
    # print(next.query)
    nxct = Appointment.objects.filter(Q(user=request.user) & Q(
        datex=datetime.date.today()) & Q(timex__range=(x, x+y))).count()
    context = {'tform': tim, 'nextapp': next, 'mytime': mytime, 'nexnt': nxct, 'total': app,
               'stff': stfff, 'today': today, 'toapp': today_ap, 'upcome': upcome, 'upapp': upapp}
    return render(request, 'client/intime.html', context)

'''
    function will delete upcomming apppointment
'''
def upcomeing_delete(request,updele):
    try:
        up_delete = Appointment.objects.get(pk=updele)
    except ObjectDoesNotExist:
        return HttpResponseNotFound('<h1 style="margin-top:50px; color:red;"><center>Your Data Has Incorrect, Check Again Or Refresh The Page</center></h1>')
    except MultipleObjectsReturned:
        return HttpResponseNotFound('<h1 style="margin-top:50px; color:red;"><center>Your Data Returning Multiple, Multiple Object Returning...</center></h1>')
    up_delete.delete()
    return redirect('/client/homepage/')
'''
    will render the out time for the staff member
'''


@user_passes_test(lambda u: u.is_authenticated, login_url='/')
def out_time(request, upout):
    if request.method == 'POST':
        try:
            upid = Timeing.objects.get(pk=upout)
        except ObjectDoesNotExist:
            return HttpResponseNotFound('<h1 style="color">Your Data In Now Found</h1>')
        # upid = Timeing.objects.get(pk=upout)
        upfm = Timeing_form(request.POST, instance=upid)
        if upfm.is_valid():
            upfm.save()
            messages.success(request, 'Out-Time is updated')
    else:
        # upid = Timeing.objects.get(pk=upout)
        try:
            upid = Timeing.objects.get(pk=upout)
        except ObjectDoesNotExist:
            return HttpResponseNotFound('<h1 style="color:red;">Your Data Is Not Found</h1>')
        print('_______________ my post request ________________')
    upfm = Timeing_form(instance=upid)
    stfff = Staff.objects.filter(user=request.user)
    print('#############################', stfff)
    today = Appointment.objects.filter(
        Q(user=request.user) & Q(datex=datetime.date.today())).count()
    today_ap = Appointment.objects.filter(
        Q(user=request.user) & Q(datex=datetime.date.today()))
    upcome = Appointment.objects.filter(
        Q(user=request.user) & Q(datex__gt=datetime.date.today())).count()
    upapp = Appointment.objects.filter(
        Q(user=request.user) & Q(datex__gt=datetime.date.today()))
    app = Appointment.objects.filter(user=request.user).count()
    x = datetime.datetime.now()
    y = timedelta(hours=1)
    next = Appointment.objects.filter(Q(user=request.user) & Q(
        datex=datetime.date.today()) & Q(timex__range=(x, x+y))).order_by('id').reverse()
    # print(next.query)
    nxct = Appointment.objects.filter(Q(user=request.user) & Q(
        datex=datetime.date.today()) & Q(timex__range=(x, x+y))).count()
    context = {'upform': upfm, 'nextapp': next, 'nexnt': nxct, 'total': app,
               'stff': stfff, 'today': today, 'toapp': today_ap, 'upcome': upcome, 'upapp': upapp}
    return render(request, 'client/outtime.html', context)


@user_passes_test(lambda u: u.is_authenticated, login_url='/')
def local_app(request):
    if request.method == 'POST':
        loform = Localappointment_form(request.POST)
        if loform.is_valid():
            nm = loform.cleaned_data['name']
            ph = loform.cleaned_data['phone']
            em = loform.cleaned_data['email']
            ser = loform.cleaned_data['service']
            stf = loform.cleaned_data['staff']
            dt = loform.cleaned_data['datex']
            tm = loform.cleaned_data['timex']
            local = Local_appointment(
                user=request.user, name=nm, phone=ph, email=em, service=ser, staff=stf, datex=dt, timex=tm)
            local.save()
            messages.success(request, 'Appointment Is saved')
            loform = Localappointment_form()
    else:
        loform = Localappointment_form()
    return render(request, 'client/local_app.html', {'form': loform})


'''
    will return all the local appointment
'''


@user_passes_test(lambda u: u.is_authenticated, login_url='/')
def view_localapp(request):
    all = Local_appointment.objects.filter(user=request.user).count()
    local = Local_appointment.objects.filter(
        user=request.user).order_by('id').reverse()
    form = Local_filter(request.GET, queryset=local)
    all_data = form.qs
    ltoday = Local_appointment.objects.filter(
        Q(user=request.user) & Q(datex=datetime.date.today()))
    todayco = Local_appointment.objects.filter(
        Q(user=request.user) & Q(datex=datetime.date.today())).count()
    upcome = Local_appointment.objects.filter(
        Q(user=request.user) & Q(datex__gt=datetime.date.today())).count()
    miss = Local_appointment.objects.filter(
        Q(user=request.user) & Q(datex__lt=datetime.date.today())).count()
    context = {'data': all_data, 'form': form, 'all': all,
               'ltoday': ltoday, 'todayco': todayco, 'upcome': upcome, 'miss': miss}
    return render(request, 'client/view_local.html', context)


'''
    function will delete local appointment
'''


@user_passes_test(lambda u: u.is_authenticated, login_url='/')
def local_delete(request, ldel):
    try:
        loc = Local_appointment.objects.get(pk=ldel)
    except ObjectDoesNotExist:
        return HttpResponseNotFound('<h1 style="color:red;">Your Appointment Not Found</h1>')
    loc.delete()
    messages.success(request, 'Appointment Deleted...')
    return redirect('/client/get-local-app/')


'''
    will send the email for the user
'''


@user_passes_test(lambda u: u.is_authenticated, login_url='/')
def send_myemail(request):
    if request.method == 'POST':
        sl = request.user
        x = request
        nm = request.POST.get('name')
        em = request.POST.get('email')
        lk = request.POST.get('link')
        send_mylink(sl, nm, em, lk, request)
    return render(request, 'client/send_mail.html')


def send_mylink(salon, name, email, link, request):
    sub = f'Feedback For  {salon}'
    mes = 'I hope you loved our services'
    fr = settings.EMAIL_HOST_USER
    re = [email]
    ht = f"""
        <h1 style="color:blue;">Hi, {name}</h1><hr>
        <h2 style="color:red;">Give Your Best Feedback For Us....</h2>
        <h3>Click Below The Link</h3> <br>
        <h2><a href="{link}">{link}</a></h2>
    """
    try:
        send_mail(subject=sub, message=mes, from_email=fr,
                  recipient_list=re, html_message=ht, fail_silently=False)
        messages.success(request, 'Email Is Sent To Your Customer')
    except BadHeaderError:
        messages.error(request, 'Invalid Header Found')
    except SMTPAuthenticationError:
        messages.error(request, 'AuthenticationError In Your System')
    except SMTPDataError:
        messages.error(request, 'Data Error')
    except SMTPConnectError:
        messages.error(request, 'Connection Error')
    except SMTPRecipientsRefused:
        messages.error(request, 'Recipients Refused')
    except SMTPSenderRefused:
        messages.error(request, 'Sender Refused')
    except SMTPNotSupportedError:
        messages.error(request, 'NotSupported Error Occur')
    except SMTPResponseException:
        messages.error(request, 'Email Response Exception Error Occur')
    except SMTPException as e:
        messages.error(request, 'There was an error sending an email.' + e)
    except:
        messages.error(request, '"Mail Sending Failed!"')


''' 
    will return the feedback form the client
'''


def feedback(request):
    if request.method == 'POST':
        fm = Feedback_form(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            ph = fm.cleaned_data['phone']
            fe = fm.cleaned_data['feed']
            feed = Feedback(user=request.user, name=nm, phone=ph, feed=fe)
            feed.save()
            fm = Feedback_form()
            messages.success(
                request, 'Feedback Is Send, will soon meet you...')
    else:
        fm = Feedback_form()
    return render(request, 'client/feed.html', {'form': fm})


'''
    admin will update the staff for salon
'''


@user_passes_test(lambda u: u.is_authenticated, login_url='/')
def staff_update(request, stup):
    if request.method == 'POST':
        try:
            sff = Staff.objects.get(pk=stup)
        except ObjectDoesNotExist:
            return HttpResponseNotFound('<h1 style="color:red;">Your Data Not Found</h1>')
        fm = Staff_form(request.POST, instance=sff)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'staff updated successfully')
            return redirect('/client/get-my-staff/')
    else:
        try:
            sff = Staff.objects.get(pk=stup)
        except ObjectDoesNotExist:
            return HttpResponseNotFound('<h1 style="color:red;">Your Data Not Found</h1>')
        fm = Staff_form(instance=sff)
    context = {'form': fm}
    return render(request, 'client/up_staff.html', context)


'''
    will return staf data for the update
'''


@user_passes_test(lambda u: u.is_authenticated, login_url='/')
def get_staff_update(request):
    data = Staff.objects.filter(user=request.user)
    return render(request, 'client/get_staff.html', {'data': data})


def error_404_view(request, exception):
    return render(request, 'client/error_404.html')


'''
    will give all the staff data for the delete
'''


@user_passes_test(lambda u: u.is_authenticated, login_url='/')
def get_delete_staff(request):
    data = Staff.objects.filter(user=request.user)
    return render(request, 'client/del_staff.html', {'data': data})


'''
    remove/delete staf member
'''


@user_passes_test(lambda u: u.is_authenticated, login_url='/')
def delete_staff(request, rst):
    try:
        dest = Staff.objects.get(pk=rst)
    except ObjectDoesNotExist:
        return HttpResponseNotFound('<h1 style="color:red;">Your Data Not Found</h1>')
    dest.delete()
    messages.success(request, 'staff deleted successfully')
    return redirect('/client/homepage/')


'''
    will display all the feedback
'''


@user_passes_test(lambda u: u.is_authenticated, login_url='/')
def view_feedback(request):
    data = Feedback.objects.filter(user=request.user)
    return render(request, 'client/view_feed.html', {'data': data})


'''
    will delete all the feedback
'''


@user_passes_test(lambda u: u.is_authenticated, login_url='/')
def delete_feedback(request, fld):
    fed = Feedback.objects.get(pk=fld)
    fed.delete()
    messages.success(request, 'Feedback deleted successfully')
    return redirect('/client/homepage/')


'''
    admin will read single feedack
'''


@user_passes_test(lambda u: u.is_authenticated, login_url='/')
def read_feedback(request, re):
    try:
        refeed = Feedback.objects.get(pk=re)
    except ObjectDoesNotExist:
        return HttpResponseNotFound('<h1 style="color:red;">Your Data Not Found</h1>')
    return render(request, 'client/read_feed.html', {'data': refeed})


'''
    function will store the all salon services
'''


@user_passes_test(lambda u: u.is_authenticated, login_url='/')
def service(request):
    if request.method == 'POST':
        sfm = Service_form(request.POST, request.FILES)
        if sfm.is_valid():
            nm = sfm.cleaned_data['name']
            im = sfm.cleaned_data['img']
            tx = sfm.cleaned_data['text']
            co = sfm.cleaned_data['cost']
            ser = Service(user=request.user, name=nm, img=im, text=tx, cost=co)
            ser.save()
            messages.success(request, 'service add successfully')
            sfm = Service_form()
    else:
        sfm = Service_form()
    data = Service.objects.filter(user=request.user)
    return render(request, 'client/service.html', {'form': sfm, 'data': data})


'''
    will return staff to get todays work
'''


@user_passes_test(lambda u: u.is_authenticated, login_url='/')
def today_work(request):
    to_wk = Staff.objects.filter(user=request.user)
    context = {'data': to_wk}
    return render(request, 'client/today_work.html', context)


'''
    will return all the todays work for all staff by URL
'''


@user_passes_test(lambda u: u.is_authenticated, login_url='/')
def get_today_work(request, sname):
    try:
        ssff = Staff.objects.get(Q(user=request.user) & Q(name=sname))
    except ObjectDoesNotExist:
        return HttpResponseNotFound('<h1 style="color:red;">Your Data Not Found By Object Not Found</h1>')
    except MultipleObjectsReturned:
        return HttpResponseNotFound('<h1 style="color:red;">Your Data Not Found By Multiple Object Return</h1>')
    towork = Appointment_data.objects.filter(
        Q(user=request.user) & Q(datex=datetime.date.today()) & Q(staff=ssff))
    towork_count = Appointment_data.objects.filter(
        Q(user=request.user) & Q(datex=datetime.date.today()) & Q(staff=ssff)).count()
    context = {'data': towork, 'sname': sname, 'total': towork_count}
    return render(request, 'client/get_today.html', context)


'''
    will return all the last month work of every 
    staff member 
'''


@user_passes_test(lambda u: u.is_authenticated, login_url='/')
def last_month_data(request, ssname):
    last_day_of_prev_month = date.today().replace(day=1) - timedelta(days=1)
    start_day_of_prev_month = date.today().replace(
        day=1) - timedelta(days=last_day_of_prev_month.day)

    # For printing results
    print("First day of prev month:", start_day_of_prev_month)
    print("Last day of prev month:", last_day_of_prev_month)
    try:
        ssfff = Staff.objects.get(Q(user=request.user) & Q(name=ssname))
    except ObjectDoesNotExist:
        return HttpResponseNotFound('<h1 style="color:red;">Your Data Not Found By Object Not Found</h1>')
    except MultipleObjectsReturned:
        return HttpResponseNotFound('<h1 style="color:red;">Your Data Not Found By Multiple Object Return</h1>')
    data = Appointment_data.objects.filter(Q(user=request.user) & Q(staff=ssfff) & Q(
        datex__range=(start_day_of_prev_month, last_day_of_prev_month))).order_by('id').reverse()
    print(data.query)
    return render(request, 'client/lastm.html', {'data': data})


'''
    get all current user staff to get last month work
'''


@user_passes_test(lambda u: u.is_authenticated, login_url='/')
def month_work(request):
    mo_wk = Staff.objects.filter(user=request.user)
    context = {'data': mo_wk}
    return render(request, 'client/month_work.html', context)


'''
    will fatch all the flexible smooth data as per the 
    client have enter and date and time
'''


@user_passes_test(lambda u: u.is_authenticated, login_url='/')
def get_smooth(request):
    start = request.GET.get('myfs')
    end = request.GET.get('myls')
    print(start, end)
    result = Appointment_data.objects.filter(Q(user=request.user) & Q(
        datex__range=(start, end))).order_by('id').reverse()
    cnt = Appointment_data.objects.filter(
        Q(user=request.user) & Q(datex__range=(start, end))).count()
    print(result.query)
    context = {'data': result, 'start': start, 'end': end, 'ent': cnt}
    return render(request, 'client/smooth.html', context)


'''
    render the product templates
'''


@user_passes_test(lambda u: u.is_authenticated, login_url='/')
def product_file(request):
    if request.method == 'POST' and 'prt' in request.POST:
        img = request.FILES.get('img')
        nm = request.POST.get('name')
        pri = request.POST.get('price')
        qt = request.POST.get('qty')
        tx = request.POST.get('text')
        print('########################################')
        print(img, nm, pri, qt, tx)
        if Product.objects.filter(Q(user=request.user) & Q(name=nm)).exists():
            xx = Product.objects.filter(Q(user=request.user) & Q(name=nm))
            print(xx.query, '00000000000000000000000000000')
            messages.error(request, f'''{nm} is already exists in product''')
        else:
            pro = Product(user=request.user, img=img, name=nm,
                          price=pri, total=qt, text=tx)
            pro.save()
            messages.success(request, 'product add successfully')
    if request.method == 'POST' and 'sale' in request.POST:
        ppro = request.POST.get('pro')
        pnm = request.POST.get('pname')
        pph = request.POST.get('pphone')
        pqt = request.POST.get('pqty')
        try:
            pproduct = Product.objects.get(Q(user=request.user) & Q(name=ppro))
            z = int(pproduct.total)
            q = int(pqt)
            if q > z:
                messages.error(
                    request, f'''{pqt} {ppro} not available in stock''')
            else:
                we = int(pqt)
                get_qty = int(pproduct.price) * int(we)
                pur = Purchase(user=request.user, product=pproduct,
                               name=pnm, phone=pph, price=get_qty, qty=pqt)
                pur.save()
                messages.success(request, 'records is stored')
                up = z-q
                product_update = Product.objects.filter(
                    Q(user=request.user) & Q(name=ppro)).update(total=up)
        except ObjectDoesNotExist:
            return HttpResponseNotFound('<h1 style="color:red;">Your Data Not Found By Object Not Found</h1>')
        except MultipleObjectsReturned:
            return HttpResponseNotFound('<h1 style="color:red;">Your Data Not Found By Multiple Object Returning</h1>')
    data = Product.objects.filter(user=request.user)
    pro_data = Product.objects.filter(user=request.user)
    context = {'data': data, 'pro': pro_data}
    return render(request, 'client/product.html', context)


'''
    will render page for the staff salary
'''


@user_passes_test(lambda u: u.is_authenticated, login_url='/')
def staff_salary(request):
    if request.method == 'POST':
        fm = Salary_form(request.POST)
        if fm.is_valid():
            sff = request.POST.get('mystf')
            try:
                lela = Staff.objects.get(Q(user=request.user) & Q(name=sff))
            except ObjectDoesNotExist:
                return HttpResponseNotFound('<h1 style="margin-top:50px; color:red;"><center>Your Data Has Incorrect, Check Again Or Refresh The Page</center></h1>')
            except MultipleObjectsReturned:
                return HttpResponseNotFound('<h1 style="margin-top:50px; color:red;"><center>Your Data Returning Multiple, Multiple Object Returning...</center></h1>')
            pay = fm.cleaned_data['pay']
            ex = fm.cleaned_data['extra']
            month = fm.cleaned_data['month']
            # try:
            # if Advanced_salary.objects.filter( Q(user=request.user) & Q(staff=lela) ):
            #     try:
            #         adst = Advanced_salary.objects.get( Q(user=request.user) & Q(staff=lela) )
            #     except ObjectDoesNotExist:
            #         return HttpResponseNotFound('<h1 style="margin-top:50px; color:red;"><center>Your Data Has Incorrect, Check Again Or Refresh The Page</center></h1>')
            #     except MultipleObjectsReturned:
            #         return HttpResponseNotFound('<h1 style="margin-top:50px; color:red;"><center>Your Data Returning Multiple, Multiple Object Returning...</center></h1>')
            #     print('2222222222222222222222222222222222222',adst)
            sala = Salary(user=request.user,staff=lela,pay=pay,extra=ex,month=month)
            sala.save()
            messages.success(request,f'''{lela} salary has serve''')
            fm = Salary_form()
            # else:
                # sala = Salary(user=request.user,staff=lela,pay=pay,extra=ex,month=month)
                # sala.save()
                # messages.success(request,'salary has stored')
                # fm = Salary_form()
            # except ObjectDoesNotExist: 
            #     return HttpResponseNotFound('<h1 style="margin-top:50px; color:red;"><center>while store advanced salary object it does not exist</center></h1>')

    else:
        fm = Salary_form()
    stfff = Staff.objects.filter(user=request.user)
    context = {'form':fm,'stff':stfff}
    return render(request, 'client/salary.html',context)

'''
    for the advanced salary of the staff
'''
@user_passes_test(lambda u: u.is_authenticated, login_url='/')
def advanced_salary(request):
    if request.method == 'POST':
        fm = AdvanceSalary_form(request.POST)
        if fm.is_valid():
            sff = request.POST.get('mystf')
            try:
                lela = Staff.objects.get(Q(user=request.user) & Q(name=sff))
            except ObjectDoesNotExist:
                return HttpResponseNotFound('<h1 style="margin-top:50px; color:red;"><center>Your Data Has Incorrect, Check Again Or Refresh The Page</center></h1>')
            except MultipleObjectsReturned:
                return HttpResponseNotFound('<h1 style="margin-top:50px; color:red;"><center>Your Data Returning Multiple, Multiple Object Returning...</center></h1>')
            ad_pay = fm.cleaned_data['pay']
            ad_month = fm.cleaned_data['month']
            ad_pay = Advanced_salary(user=request.user,staff=lela, pay=ad_pay,month=ad_month)
            ad_pay.save()
            fm = AdvanceSalary_form()
            messages.success(request,'advanced salary has provide')
    else:
        fm = AdvanceSalary_form()
    stfff = Staff.objects.filter(user=request.user)
    context = {'form':fm,'stff':stfff}
    return render(request,'client/ad_salary.html',context)

'''
    will render all the salary data of the staff
'''


@user_passes_test(lambda u: u.is_authenticated, login_url='/')
def salary_data(request):
    stfff = Staff.objects.filter(user=request.user)
    context = {'stff':stfff}
    return render(request, 'client/salary_data.html',context)

'''
    function will fatch staff month salary
'''
def get_month_salary(request,get_sl):
    try:
        data = Staff.objects.get( Q(user=request.user) & Q(name=get_sl) )
    except ObjectDoesNotExist:
        return HttpResponseNotFound('<h1 style="margin-top:50px; color:red;"><center>Your Data Has Incorrect, Check Again Or Refresh The Page</center></h1>')
    except MultipleObjectsReturned:
        return HttpResponseNotFound('<h1 style="margin-top:50px; color:red;"><center>Your Data Returning Multiple, Multiple Object Returning...</center></h1>')
    my_salary = Salary.objects.filter( Q(user=request.user) & Q(staff=data) )
    form = Salary_filter(request.GET, queryset=my_salary)
    all_data = form.qs
    view_adv = Advanced_salary.objects.filter(user=request.user)
    ad_form = Advanced_filter(request.GET, queryset=view_adv)
    ad_data = ad_form.qs
    print('checkkkkkkkkkkkkkkkkkkkkkk',view_adv)
    context = {'salary':all_data,'name':data,'form':form,'view_ad':ad_data,'ad_form':ad_form}
    return render(request,'client/get_salary.html',context)

'''
    will return the generatr the TIMEING report 
'''


@user_passes_test(lambda u: u.is_authenticated, login_url='/')
def time_report(request):
    mo_time = Staff.objects.filter(user=request.user)
    context = {'data': mo_time}
    return render(request, 'client/time_report.html', context)


'''
    will give today timing
'''


@user_passes_test(lambda u: u.is_authenticated, login_url='/')
def today_time_work(request):
    data = Timeing.objects.filter(Q(user=request.user) & Q(
        in_date=datetime.date.today()) & Q(out_date=datetime.date.today()))
    print(datetime.datetime.now())
    context = {'data': data}
    return render(request, 'client/today_time.html', context)


'''
    will return all the staff member for to get 
    last month timing
'''


@user_passes_test(lambda u: u.is_authenticated, login_url='/')
def display_timing_rec(request, rec):
    last_day_of_prev_month = date.today().replace(day=1) - timedelta(days=1)
    start_day_of_prev_month = date.today().replace(
        day=1) - timedelta(days=last_day_of_prev_month.day)
    try:
        time_rec = Staff.objects.get(Q(user=request.user) & Q(name=rec))
    except ObjectDoesNotExist:
        return HttpResponseNotFound('<h1 style="color:red;">Your Data Not Found By Object Not Found</h1>')
    except MultipleObjectsReturned:
        return HttpResponseNotFound('<h1 style="color:red;">Your Data Not Found By Multiple Object Return</h1>')
    data = Timeing.objects.filter(Q(user=request.user) & Q(staff=time_rec) & Q(
        in_date__range=(start_day_of_prev_month, last_day_of_prev_month)))
    print(data.query)
    context = {'data': data, 'name': rec}
    return render(request, 'client/time_records.html', context)
