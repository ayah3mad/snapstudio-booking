from django.db import models
from django.contrib.auth.models import User  # using built-in User model

# ------------------------
# Service Model
# ------------------------
class Service(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    description = models.TextField(null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    duration = models.CharField(max_length=50, null=False) # e.g. "1 hour", "30 minutes"
    image = models.ImageField(upload_to='images/services/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# ------------------------
# Booking Model
# ------------------------
class Booking(models.Model):
    STATUS_CHOICES = [
        ('Scheduled', 'Scheduled'),
        ('Cancelled', 'Cancelled'),
        ('Completed', 'Completed'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Scheduled')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.service.name} on {self.date} at {self.time}"


# ------------------------
# Feedback Model
# ------------------------
class Feedback(models.Model):
    id = models.BigAutoField(primary_key=True)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    rating = models.IntegerField(null=True, blank=True)  
    comment = models.TextField(null=True, blank=True)    
    created_at = models.DateTimeField(auto_now_add=True)
    featured = models.BooleanField(default=False)


    def __str__(self):
        return f"Feedback by {self.user.username} for {self.booking.service.name}"
