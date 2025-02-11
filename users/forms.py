from django import forms
from users.models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['email', 'name', 'phone', 'address', 'is_active', 'is_staff']
