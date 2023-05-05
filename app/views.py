from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
from django.core.mail import send_mail
# Create your views here.

def registration(request):
    UFO=UserForm()
    PFO=ProfileForm()
    d={'UFO':UFO,'PFO':PFO}
    if request.method=='POST' and request.FILES:
        UFD=UserForm(request.POST)
        PFD=ProfileForm(request.POST,request.FILES)
        if UFD.is_valid() and PFD.is_valid():
            NSUO=UFD.save(commit=False)
            NSUO.set_password(UFD.cleaned_data['password'])
            NSUO.save()
            NSPO=PFD.save(commit=False)
            NSPO=username=NSUO
            NSPO.save()

            send_mail('Registration',
                       "successfully registration is done",
                       '19svdc6081@svdegreecollege.ac.in',
                       [NSUO.email],
                       fail_silently=False

                       )


            return HttpResponse('registration successfully')
        else:
            return HttpResponse('not valid')

    return render(request,'registration.html',d)