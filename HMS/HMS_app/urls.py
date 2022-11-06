from django import views
from django.contrib import admin
from django.urls import path
from HMS_app import views
urlpatterns = [
    path('',views.login,name="login"),
    path('auth',views.auth,name="auth"),
    path('add', views.add,name="add"),
    path('addrecord/', views.addrecord, name='addrecord'),
    path('update/<int:id>', views.update, name='update'),
    path('update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
    #path('delete', views.delete,name="delete"),
    path('delete/<int:id>', views.delete, name='delete'),
]