from django.shortcuts import render, redirect
from .models import user
from .forms import *
from django.http import HttpResponseRedirect
from django.urls import reverse


def home(request):
    if request.method == 'POST':
        n = request.POST.get("name")
        p = request.POST.get("pwd")
        t = user(name = n, password = p, email = "", photo = "/home.png")
        t.save()
        return HttpResponseRedirect("/%i" %t.pk)

    return render(request, 'home/index.html')


def about(request):
    return render(request, 'home/about.html')


def communications(request):
    return render(request, 'home/communications.html')


def faq(request):
    return render(request, 'home/faq.html')


def signin(request):
    if request.method == 'POST':
        n = request.POST.get("name")
        p = request.POST.get("pwd")
        t = user.objects.get(name = n)
        if t.password == p:
            return HttpResponseRedirect("/%i" %t.pk)

    return render(request, 'home/signin.html')


def signup(request):
    if request.method == 'POST':
        n = request.POST.get("name")
        p = request.POST.get("pwd")
        t = user(name=n, password=p, email="", photo="/home.png")
        t.save()
        return HttpResponseRedirect("/%i" % t.pk)

    return render(request, 'home/signup.html')
