# hotels/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    confirmed_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password', 'confirmed_password', 'is_staff', 'is_active')

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already in use. Please choose a different one.")
        return email

    def clean_confirmed_password(self):
        password1 = self.cleaned_data.get("password1")
        confirmed_password = self.cleaned_data.get("confirmed_password")
        if password1 and confirmed_password and password1 != confirmed_password:
            raise forms.ValidationError("Passwords do not match.")
        return confirmed_password