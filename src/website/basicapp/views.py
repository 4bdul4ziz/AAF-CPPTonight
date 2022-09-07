from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.shortcuts import render


import math, random
def generateOTP() :
    digits = "0123456789"
    OTP = ""
    for i in range(4) :
        OTP += digits[math.floor(random.random() * 10)]
    return OTP

def send_otp(request):
    email=request.GET.get("email")
    o=generateOTP()
    htmlgen = '<p>Your OTP is <strong>'+o+'</strong></p>'
    print(send_mail('OTP request',o,'<gmail id>',[email],fail_silently=False,html_message=htmlgen))
    print(o)
    return HttpResponse(o)

def home(request):
    return render(request, "home.html")

