from django import forms
from .models import Booking, Feedback, Service
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [ 'date', 'time'] #'service',

class FeedbackForm(forms.Form):
    model = Feedback
    rating = forms.IntegerField(min_value=1, max_value=5)
    comment = forms.CharField(widget=forms.Textarea, required=False)


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name'] 


class ServiceForm(forms.ModelForm):
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "rows": 2,       # initial height
                "cols": 40,      # width
                "style": "resize:vertical;"  # allow resizing vertically only
            }
        )
    )

    class Meta:
        model = Service
        fields = ['name', 'price', 'duration', 'image', 'description']
