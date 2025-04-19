from django.urls import path
from listings.views import listings
urlpatterns = [
    path('', listings, name='airbnb-listings')
]
