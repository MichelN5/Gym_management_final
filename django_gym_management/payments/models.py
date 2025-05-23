from django.db import models
from members.models import Member


class FeePackage(models.Model):
    name = models.CharField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.CharField(max_length=50)  # e.g., "1 month", "3 months", "1 year"
    def __str__(self):
        return f"{self.name} - ${self.price} ({self.duration}) "




class Bill(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('paid', 'Paid'),
       
    ]

    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='bills')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Bill #{self.id} - {self.member.name} - {self.amount}"

    class Meta:
        ordering = ['-created_at']