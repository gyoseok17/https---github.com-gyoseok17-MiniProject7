from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Profile


class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email', )
