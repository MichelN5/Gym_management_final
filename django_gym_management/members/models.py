from django.db import models
from django.contrib.auth.models import User


class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Link to a user
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20, unique=True)
    fee_package = models.ForeignKey("payments.FeePackage", on_delete=models.CASCADE)

    def __str__(self):
        return self.name
