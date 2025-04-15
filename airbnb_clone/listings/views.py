from django.http import HttpResponse
from django.shortcuts import redirect, render


def home(request):
    if request.user.is_authenticated:
        return HttpResponse('Welcome Home Yslcodes')
    else:
        return redirect('login', preserve_request=True)
