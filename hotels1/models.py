
# hotels/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    email = models.CharField(50)
    password = models.CharField(40)
    # confirmed_password = models.CharField(40)

    def __str__(self):
        return self.username
