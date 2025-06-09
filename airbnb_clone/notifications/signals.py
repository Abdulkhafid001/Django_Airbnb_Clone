from django.dispatch import receiver
from listings.signals import listing_added
from listings.models import Property
from django.db.models.signals import post_save

@receiver(post_save, Sender=Property)
def send_listing_added_notification(sender, **kwargs):
    '''signal to send a neotification when a listing is added.'''
    print('new listing added!')
   
