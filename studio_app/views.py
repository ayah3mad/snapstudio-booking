from django.shortcuts import render

# Home page view
def home_view(request):
    return render(request, 'home.html')

# Services page view
def services_view(request):
    return render(request, 'services.html')

# Booking creation page view
def booking_create(request):
    return render(request, 'booking/booking.html')

# Booking history page view
def booking_list(request):
    return render(request, 'booking/booking_history.html')#not sure about this 

# User profile page view
def profile_view(request):
    return render(request, 'profile.html')