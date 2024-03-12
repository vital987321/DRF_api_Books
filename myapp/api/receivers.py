#receivers.py
from django.dispatch import receiver
from django.db.models.signals import pre_save
from myapp.models import Author


@receiver(pre_save, sender=Author)
def pre_save_handler(sender, **kwargs):
    print('Hi from pre_save_handler. Sender:', sender)

