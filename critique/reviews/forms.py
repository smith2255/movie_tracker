from django import forms    
from django.contrib.auth.models import User
from . import models

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'password'
        ]
        widgets = {
            'password': forms.PasswordInput(attrs={}),
        }


class ReviewForm(forms.ModelForm):

    class Meta:
        model = models.Review
        fields = [
            'viewed_on',
            'was_reviewed',
            'details',
            'rating',
        ]
        widgets = {
            'details': forms.Textarea(attrs={'cols': 50, 'rows': 4}),
        }
        labels = {
            'was_reviewed': 'Would you like to review the movie?',
            'viewed_on': 'When did you watch this movie?',
            'details': 'Please type your review',
            'rating': 'What would you rate it out of ten?'
        }