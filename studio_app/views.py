from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import FormView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import CustomUserCreationForm , UserUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import redirect


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
    return render(request, 'profile/profile.html')


# CBV for user signup
class SignUpView(CreateView):
    form_class = CustomUserCreationForm  
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login") 

# CBV for user profile
class ProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'profile/profile.html'
    context_object_name = 'user'

    def get_object(self, queryset=None):
        return self.request.user
    
class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name =  'profile/profile_edit.html'
    success_url = reverse_lazy('profile') 

    def get_object(self, queryset=None):
        return self.request.user 

class ProfileDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return self.request.user

