from django.db.models.signals import pre_save, post_save, request_finished
from django.dispatch import receiver
from myapp.models import Author

@receiver(request_finished)
def request_finished_handler(sender, **kwargs):
    print('Hi from request_finished_handler')


@receiver(pre_save, sender=Author)
def pre_save_handler(sender, **kwargs):
    print('Hi from pre_save_handler')

@receiver(post_save, sender=Author)
def post_save_handler(sender, **kwargs):
    print('Hi from post_save_handler')

