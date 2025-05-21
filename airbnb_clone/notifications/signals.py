from django.dispatch import receiver
from listings.signals import listing_added


@receiver(listing_added)
def send_listing_added_notification(sender, **kwargs):
    '''signal to send a neotification when a listing is added.'''
   
