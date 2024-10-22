from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Message
from .send_sms import send_sms


@receiver(post_save, sender=Message)
def send_sms_siganal(sender, instance, **kwargs):
    if kwargs['created']:
        print()
        send_sms(instance.location.sub_county, instance.message)
