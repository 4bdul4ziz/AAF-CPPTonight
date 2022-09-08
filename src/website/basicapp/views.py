import email
from http import server
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.shortcuts import render


import math, random, smtplib
def generateOTP():
    digits = "0123456789"
    OTP = ""
    for i in range(4) :
        OTP += digits[math.floor(random.random() * 10)]
    return OTP

def send_email(request):
    smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('<gmail id>','<gmail password>')
    msg = '<p>Your OTP is <strong>'+o+'</strong></p>'
    server.sendmail('<gmail id>',email,msg)
    server.quit()
    return HttpResponse(o)


def send_otp(request):
    email=request.GET.get("email")
    o=generateOTP()
    htmlgen = '<p>Your OTP is <strong>'+o+'</strong></p>'
    print(send_mail('OTP', htmlgen, '<gmail id>', [email], fail_silently=False))
    print(o)
    return HttpResponse(o)

def home(request):
    return render(request,'home.html')

""" def verify(request):
    return render(request,'verify.html') """

def loanApply(request):
    return render(request,'loanApplyPage.html')

def pages(request):
    return render(request,'pages.html')
    

    

