from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Property

def listings(request):
    if request.user.is_authenticated:
        return HttpResponse(Property.objects.all())
    else:
        return redirect('home', preserve_request=True)
