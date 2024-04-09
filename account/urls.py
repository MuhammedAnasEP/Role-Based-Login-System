from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.loginview, name='login'),
    path('register/', views.register, name='register'),
    path('adminpage/', views.admin, name='adminpage'),
    path('customerpage/', views.customer, name='customerpage'),
    path('employee/', views.employee, name='employeepage'),

]
