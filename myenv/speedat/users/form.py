from allauth.account.forms import SignupForm
from django import forms
from django.core.exceptions import ValidationError

class CustomSignupForm(SignupForm):
    def clean_email(self):
        email = self.cleaned_data['email']
        if not email.endswith('@sonline20.sen.go.kr'):
            raise ValidationError("Only @sonline20.sen.go.kr emails are allowed.")
        return email
