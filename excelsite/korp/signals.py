from django.db.models.signals import post_save
from django.dispatch import receiver
from korp.models import *


@receiver(post_save,sender=Ofis)
@receiver(post_save,sender=Torg)
@receiver(post_save,sender=Tc)
@receiver(post_save,sender=Proizv)
@receiver(post_save,sender=Sklad)
@receiver(post_save,sender=Psn)
@receiver(post_save,sender=Land)
@receiver(post_save,sender=Flat)
def make_idl(sender, instance, created, **kwargs):
    if created:
        instance.idl=str(instance.categ) + '-'+ str(instance.pk)+ '-' + 'gebocommers'
        instance.save()










