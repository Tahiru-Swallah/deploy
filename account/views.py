from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .models import CustomUser
from django.contrib.auth import get_backends
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetView, PasswordResetConfirmView
from .forms import SignupForm, EmailorPhoneAuthentication, CodeForm, CustomSetPasswordForm, CustomPasswordChangeForm, CustomPasswordResetForm
from django.contrib.auth.forms import AuthenticationForm

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .utils import send_sms

from user_profile.models import Profile

@login_required
def home_view(request):
    custom = CustomUser.objects.exclude(id=request.user.id)
    return render(request, 'home.html', {'custom': custom})

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    form_class = CustomSetPasswordForm

    def get_success_url(self):
        return reverse_lazy('account:login')
    
class CustomPasswordRest(PasswordResetView):
    form_class = CustomPasswordResetForm

    def get_success_url(self):
        return reverse_lazy('account:password_reset_done')
    
class CustomPasswordChange(PasswordChangeView):
    form_class = CustomPasswordChangeForm
    template_name = 'registration/password_change_form.html'

    def get_success_url(self):
        return reverse_lazy('account:login')
    
class CustomLoginView(LoginView):
    template_name = 'registration/login.html'


    def get_success_url(self): 
        return reverse_lazy('products:product_list')


""" def verify_view(request):
    form = CodeForm(request.POST)
    request.session['pk'] = request.user.pk
    pk = request.session.get('pk')
    if pk:
        user = CustomUser.objects.get(pk=pk)
        code = user.code
        code_user = f'{user.first_name}: {code}'
        if not request.POST:
            print(code_user)
            #send_sms(code, user.phone_number, user.first_name)
        if form.is_valid():
            num = form.cleaned_data.get('number')
            if str(code) == num:
                code.save()
                login(request, user, backend='account.authenticated.EmailorPhoneBackend')
                return redirect('account:home')
            else:
                return render(request, 'verify.html', {'error': 'The code you entered is wrong try again'})
    return render(
        request,
        'verify.html',
        {'form': form}
    )
 """
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('account:login')
    else:
        form = SignupForm()
    return render(
        request,
        'registration/signup.html',
        {'form': form}
    )

def logout_form(request):
    return render(request, 'registration/logout_form.html', {})