from django.urls import path
from . import views
urlpatterns =[
    path('',views.index,name='index'),
    path('loginpage',views.loginpage,name='loginpage'),
    path('signuppage',views.signuppage,name='signuppage'),
   # path('homepage',views.homepage,name='homepage'),
]
