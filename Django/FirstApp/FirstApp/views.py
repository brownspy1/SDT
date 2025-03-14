from django.http import HttpResponse
from django.shortcuts import render

def Home(request):
    # return HttpResponse("<h1>You are in Home page</h1>")
    return render(request,'website/home.html')
def About(request):
    return HttpResponse("<h1>You are in About page</h1>")
def Contact(request):
    return HttpResponse("<h1>You are in Contact page</h1>")