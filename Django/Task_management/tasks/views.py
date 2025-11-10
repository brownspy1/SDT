from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def manager_dashbord(request):
    return render(request,'dashbord/manager-dashbord.html')
def user_dashbord(request):
    return render(request,'dashbord/user-dashbord.html')
def test(request):
    return render(request,'test.html')