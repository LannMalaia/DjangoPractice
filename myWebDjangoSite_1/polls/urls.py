from django.contrib import admin
from django.urls import path
from polls import views


app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    # path('logininfo/', views.logininfo, name='logininfo'),
    path('result/<str:loginresult>/', views.result, name='loginresult')
]