from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Property


def listings(request):
    if request.user.is_authenticated:
        listings = Property.objects.all()[:4]
        context = {'listings': listings}
        return render(request, 'listings.html', context)
    else:
        return redirect('home', preserve_request=True)
