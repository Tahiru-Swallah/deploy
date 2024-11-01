from django import forms
from account.models import CustomUser
from .models import Profile

class UserEditForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'phone_number'
        ]

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'profile_photo'
        ]