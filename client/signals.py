from django.db.models import Q
import datetime
from .models import Appointment, Appointment_data, Local_appointment, Staff, Timeing
from django.db.models.signals import (
    post_save, pre_save,
    pre_delete, post_delete
)
from django.dispatch import receiver


@receiver(pre_delete, sender=Appointment)
def after_appointment(sender, instance,**kwargs):
    print('my instace ',instance)
    print('all instance ',instance.user)
    if not Appointment.objects.get( Q(user=instance.user) & Q(datex__gt = datetime.date.today())):
        after = Appointment_data(user=instance.user, uniq=instance.uniq, 
        customer=instance.customer, phone=instance.phone,
        datex=instance.datex, timex=instance.timex,
        service=instance.service, staff=instance.staff, fdate=instance.fdate)
        after.save()


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
