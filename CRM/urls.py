from django.urls import path

from . import views

urlpatterns = [
	#Leave as empty string for base url

	path('orders/', views.orders, name="orders"),


]