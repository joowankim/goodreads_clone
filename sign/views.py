from django.shortcuts import render
from django.http import HttpResponse

def sign_up(request):
    return render(request, 'sign/signup.html')