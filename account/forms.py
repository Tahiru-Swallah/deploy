from django import forms
from .models import CustomUser, Code
from django.contrib.auth.forms import AuthenticationForm, SetPasswordForm, PasswordChangeForm, PasswordResetForm
from user_profile.models import Profile

class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Enter Your Email'}))


class CustomPasswordChangeForm(PasswordChangeForm):
   old_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter Old password', 'autocomplete': False}))
   new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter New password', 'autocomplete': False}))
   new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm New password', 'autocomplete': False}))
   
class CustomSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter New Password', 'class': 'new_password1'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password', 'class': 'new_password2'}))

class CodeForm(forms.ModelForm):
    number = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter the verification code'}))

    class Meta:
        model = Code
        fields = ['number']

class EmailorPhoneAuthentication(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'autofocus': True, 'placeholder': 'Enter your email or phone number'})
    )
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))


class SignupForm(forms.ModelForm):
    first_name = forms.CharField(max_length=25, widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=25, widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    username = forms.CharField(max_length=25, widget=forms.TextInput(attrs={'placeholder': 'Enter Username eg. @user_01'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Enter Your Email'}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Your Phone Number'}), max_length=15)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))

    class Meta:
        model = CustomUser
        fields = ['first_name','last_name', 'username','email', 'phone_number', 'password']

    def clean_username(self):
        data= self.cleaned_data['username']
        if CustomUser.objects.filter(username=data).exists():
            raise forms.ValidationError('The username you entered exists, change the last number at @user_01 to a different number and try again')
        return data

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Password does not match!, Try again')
        return cd['password2']
    
    def clean_email(self):
        data = self.cleaned_data['email']
        if CustomUser.objects.filter(email=data).exists():
            raise forms.ValidationError('Email already exists!!')
        return data
    
    def clean_phone_number(self):
        data = self.cleaned_data['phone_number']
        if CustomUser.objects.filter(phone_number=data).exists():
            raise forms.ValidationError('Your number already exists')
        return data
    
    def save(self, commit=True):
        user = CustomUser(
            first_name = self.cleaned_data['first_name'],
            last_name = self.cleaned_data['last_name'],
            username = self.cleaned_data['username'],
            email = self.cleaned_data['email'],
            phone_number = self.cleaned_data['phone_number'],
        )
        user.set_password(self.cleaned_data['password'])
        
        if commit:
            user.save()
            Profile.objects.create(user=user)
        return user