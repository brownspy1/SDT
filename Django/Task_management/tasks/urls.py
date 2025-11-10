from django.urls import path
from tasks.views import manager_dashbord,user_dashbord,test
urlpatterns = [
    path("manager/",manager_dashbord),
    path("user/",user_dashbord),
    path("test/",test)
]
