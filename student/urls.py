from unicodedata import name
from django.urls import path,include
from . import views

app_name ='student'

urlpatterns=[
    path('login/',views.loginPage,name='login'),
    path('register/',views.registerPage,name='register'),
    path('',views.Index,name='index'),
    path('page/<int:postid>/',views.postView,name='posts'),
    path('logout/',views.logoutPage , name='logout'),
]