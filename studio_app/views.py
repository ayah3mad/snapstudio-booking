from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import FormView #???
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm 
from django.contrib.auth.decorators import login_required


#FBV
# Home page view
def home_view(request):
    return render(request, 'home.html')

# Services page view
def services_view(request):
    return render(request, 'services.html')

# Booking creation page view
@login_required
def booking_create(request):
    return render(request, 'booking/booking.html')

# Booking history page view
@login_required
def booking_list(request):
    return render(request, 'booking/booking_history.html')#not sure about this 

# User profile page view
@login_required
def profile_view(request):
    return render(request, 'profile.html')


# CBV for user signup
class SignUpView(CreateView):
    form_class = CustomUserCreationForm  
    template_name = "registration/signup.html"
    success_url = reverse_lazy("log in") 