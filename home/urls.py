from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path('',views.index,name='home'),
    path('login',views.loginUser,name='login'),
    path('signup',views.signUp,name='signup'),
    path('logout',views.logoutUser,name='logout'),
    path('survey',views.survey,name='survey'),
    path('display',views.display,name='display'),

]