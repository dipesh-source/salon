from django.db.models import Q
import datetime
from .models import Appointment, Appointment_data, Local_appointment, Staff, Timeing
from django.db.models.signals import (
    post_save, pre_save,
    pre_delete, post_delete
)
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

@receiver(post_save, sender=Appointment)
def after_appointment(sender, instance,**kwargs):
    print('my instace ',instance)
    print('all instance ',instance.user)
    # if instance.datex == datetime.date.today():
    after = Appointment_data(user=instance.user, uniq=instance.uniq, 
    customer=instance.customer, phone=instance.phone,
    datex=instance.datex, timex=instance.timex,
    service=instance.service, staff=instance.staff, fdate=instance.fdate)
    after.save()
    # else:
    #     return None

'''
    will handel the upcomming appointment while delete 
'''
@receiver(post_delete, sender=Appointment)
def delete_upcoming(sender, instance, **kwargs):
    print('my delete appointment is successfully')
    print('sender', sender)
    print('instance',instance,instance.datex,'xx',datetime.date.today()) 
    print('data instance ', instance.fdate,instance.customer,instance.datex, instance.timex, instance.staff)
    try:
        if not instance.datex == datetime.date.today():
            my_data = Appointment_data.objects.get(customer=instance.customer, datex=instance.datex, timex=instance.timex, staff=instance.staff)
            my_data.delete()
        else:
            print('today data will not delete')
    except ObjectDoesNotExist:
        return False
    except MultipleObjectsReturned:
        return False

@receiver(post_save, sender=Appointment)
def all_staffwork(sender, instance, **kwargs):
    pass
    # staf  = Staff.objects.get(staff=instance.staff)
    # ap  = Appointment.objects.get(pk=instance.id)


@receiver(post_save, sender=Timeing)
def time_data(sender, instance, created, **kwargs):
    print('sender', sender)
    print('instance', instance)
    print('created', created)
    if not created and instance.staff:
        print('not created data')
        print(instance.staff)
        # updata = Timeing.objects.update()