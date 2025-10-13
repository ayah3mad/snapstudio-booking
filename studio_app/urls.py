from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('services/', views.services_view, name='services'),
    path('booking/', views.booking_create, name='booking'),
    path('booking/history/', views.booking_list, name='booking_list'), #not sure about this 
    path('profile/', views.profile_view, name='profile'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
]