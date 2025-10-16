from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import BookingCreateView, BookingListView, AdminBookingListView, update_booking_status

urlpatterns = [
    path('', views.home_view, name='home'),

    # Auth
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.SignUpView.as_view(), name='signup'),

    # Profile
    path('profile/', views.profile_view, name='profile'),
    path('profile/edit/', views.ProfileUpdateView.as_view(), name='profile_update'),
    path('profile/delete/', views.ProfileDeleteView.as_view(), name='delete_account'),

    # Admin Users
    path('dashboard/users/', views.UserListView.as_view(), name='user_list'),
    path('dashboard/users/delete/<int:pk>/', views.DeleteUserByAdminView.as_view(), name='delete_account_by_admin'),

    # Services
    path('services/', views.ServiceListView.as_view(), name='services'),
    path('services/add/', views.ServiceCreateView.as_view(), name='service_add'),
    path('services/edit/<int:pk>/', views.ServiceUpdateView.as_view(), name='service_edit'),
    path('services/delete/<int:pk>/', views.ServiceDeleteView.as_view(), name='service_delete'),

    # Bookings
    path('booking/create/', BookingCreateView.as_view(), name='create_booking'),
    path('booking/list/', BookingListView.as_view(), name='booking_list'),
    path('booking/admin/', AdminBookingListView.as_view(), name='admin_booking_list'),
     path('booking/<int:booking_id>/update-status/', update_booking_status, name='update_booking_status'),
]