from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('services/', views.services_view, name='services'),
    path('booking/', views.booking_create, name='booking'),
    path('booking/history/', views.booking_list, name='booking_list'), #not sure about this 
    path('profile/', views.profile_view, name='profile'),
    path('signup/', views.SignUpView.as_view(), name='signup'),

    # Authentication URLs
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.SignUpView.as_view(), name='signup'),

    
]