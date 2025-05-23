from django.db import models

class Notification(models.Model):
    message = models.TextField()
    time_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification: {self.message[:50]}..."  # Show first 50 chars

    class Meta:
        ordering = ['-time_posted']  # Newest notifications first
