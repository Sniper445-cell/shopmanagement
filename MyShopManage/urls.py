from django.urls import path
from . import views

urlpatterns = [
	path('', views.ownerPage, name='ownerPage'),
	path('manager/', views.managePage, name='manager'),
	path('employe/', views.employePage, name='employe'),
]