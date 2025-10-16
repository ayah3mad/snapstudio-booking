from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm, UserUpdateForm, ServiceForm, BookingForm, FeedbackForm
from .models import Service, Booking, Feedback
from django.contrib.auth.decorators import user_passes_test


# ------------------------
# Home & Services
# ------------------------
def home_view(request):
    # Get featured feedback with user and service details
    featured_feedbacks = Feedback.objects.filter(featured=True).select_related('user', 'booking__service')
    return render(request, 'home.html', {'featured_feedbacks': featured_feedbacks})

def services_view(request):
    services = Service.objects.all()
    return render(request, 'services/services.html', {'services': services})


# ------------------------
# Authentication & Profile
# ------------------------
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")

@login_required
def profile_view(request):
    return render(request, 'profile/profile.html')

class ProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'profile/profile.html'
    context_object_name = 'user'

    def get_object(self, queryset=None):
        return self.request.user

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'profile/profile_edit.html'
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        return self.request.user

class ProfileDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return self.request.user
    
 # ------------------------
# Admin Mixins & Views
# ------------------------
class AdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser

class UserListView(LoginRequiredMixin, AdminRequiredMixin, ListView):
    model = User
    template_name = 'admin/user_cards.html'
    context_object_name = 'users'

    def get_queryset(self):
        return User.objects.filter(is_superuser=False)

class DeleteUserByAdminView(LoginRequiredMixin, AdminRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        user = get_object_or_404(User, pk=pk)
        if not user.is_superuser:
            user.delete()
            messages.success(request, "User deleted successfully.")
        else:
            messages.error(request, "You cannot delete an admin user.")
        return redirect('user_list')
    
# ------------------------
# Services CRUD (Admin)
# ------------------------
class ServiceListView(ListView):
    model = Service
    template_name = 'services/services.html'
    context_object_name = 'services'

class ServiceCreateView(LoginRequiredMixin, AdminRequiredMixin, CreateView):
    model = Service
    form_class = ServiceForm
    template_name = 'services/service_form.html'
    success_url = reverse_lazy('services')

class ServiceUpdateView(LoginRequiredMixin, AdminRequiredMixin, UpdateView):
    model = Service
    form_class = ServiceForm
    template_name = 'services/service_form.html'
    success_url = reverse_lazy('services')

class ServiceDeleteView(LoginRequiredMixin, AdminRequiredMixin, DeleteView):
    model = Service
    template_name = 'services/service_confirm_delete.html'
    success_url = reverse_lazy('services')

# ------------------------
# Booking (User + Admin)
# ------------------------

class BookingCreateView(LoginRequiredMixin, CreateView):
    model = Booking
    form_class = BookingForm
    template_name = 'booking/booking_form.html'
    success_url = reverse_lazy('booking_list')
    login_url = '/login/'  # redirect if not logged in

    def form_valid(self, form):
        form.instance.user = self.request.user  # assign current user
        form.instance.status = 'Scheduled'      # default status
        return super().form_valid(form)

class BookingListView(LoginRequiredMixin, ListView):
    model = Booking
    template_name = 'booking/booking_list.html'
    context_object_name = 'bookings'
    login_url = '/login/'

    def get_queryset(self):
        # show only the bookings of the current user
        return Booking.objects.filter(user=self.request.user).order_by('-date', '-time')
    

class AdminBookingListView(LoginRequiredMixin, ListView):
    model = Booking
    template_name = 'booking/admin_booking_list.html'
    context_object_name = 'bookings'
    login_url = '/login/'  # redirect if not logged in

    def test_func(self):
        return self.request.user.is_staff  
    
    def get_queryset(self):
        # Show all bookings
        return Booking.objects.all().order_by('-date', '-time')

@user_passes_test(lambda u: u.is_staff)
def update_booking_status(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)

    if request.method == "POST":
        new_status = request.POST.get("status")
        if new_status in ["Scheduled", "Cancelled", "Completed"]:
            booking.status = new_status
            booking.save()

    return redirect('admin_booking_list')


# ------------------------
# Feedback (Admin)
# ------------------------  
# Admin
class AdminFeedbackListView(LoginRequiredMixin, AdminRequiredMixin, ListView):
    model = Feedback
    template_name = 'admin/admin_feedback_list.html' 
    context_object_name = 'feedbacks'

@login_required
@login_required
@user_passes_test(lambda u: u.is_superuser)
def feature_feedback(request, fb_id):
    fb = get_object_or_404(Feedback, id=fb_id)
    fb.featured = True
    fb.save()
    messages.success(request, "Feedback has been marked as featured.")
    return redirect('admin_feedback_list')

@login_required
@user_passes_test(lambda u: u.is_superuser)
def delete_feedback(request, fb_id):
    fb = get_object_or_404(Feedback, id=fb_id)
    fb.delete()
    messages.success(request, "Feedback has been deleted.")
    return redirect('admin_feedback_list')


# User 
class FeedbackCreateView(LoginRequiredMixin, CreateView):
    model = Feedback
    form_class = FeedbackForm
    template_name = 'feedback/feedback_form.html'

    def dispatch(self, request, *args, **kwargs):
        self.booking = get_object_or_404(Booking, id=kwargs['booking_id'], user=request.user)
        if Feedback.objects.filter(booking=self.booking).exists():
            messages.info(request, "You already submitted feedback for this booking.")
            return redirect('booking_list')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.booking = self.booking
        messages.success(self.request, "Your feedback has been submitted successfully!")  # Success message
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('booking_list')