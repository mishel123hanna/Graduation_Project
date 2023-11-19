from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
import random, string

@receiver(post_save, sender=get_user_model())
def create_activation_code(sender, instance, created, **kwargs):
    if created:
        code = ''.join(random.choices(string.digits, k=6))
        instance.activation_code = code
        instance.save()