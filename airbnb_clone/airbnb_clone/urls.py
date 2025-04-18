from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('listings.urls')),
    path('auth/', include('airbnb_auth.urls')),
    path("accounts/", include("allauth.urls")), # new
    path('admin/', admin.site.urls),
]
