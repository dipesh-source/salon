from .models import Account_access, Extend_access
from django.contrib.auth.signals import user_logged_in
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver


@receiver(post_save, sender=Account_access)
def acc_extend(sender, instance, created, **kwargs):
    print('sender', sender, instance)
    data = Extend_access(user=instance.user,month=instance.month,set_date= instance.set_date,set_time= instance.set_time,ex_date= instance.ex_date,ex_time=instance.ex_date)
    data.save()
    

 