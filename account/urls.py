from django.urls import path
from .views import signup, CustomLoginView, logout_form, home_view,CustomPasswordChange, CustomPasswordRest, CustomPasswordResetConfirmView
from django.contrib.auth.views import (LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView, PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetCompleteView)
from .forms import EmailorPhoneAuthentication

app_name = 'account'

urlpatterns = [
    path('login/', CustomLoginView.as_view(authentication_form=EmailorPhoneAuthentication), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password-change/', CustomPasswordChange.as_view(), name='password_change'),
    path('password-reset/', CustomPasswordRest.as_view(), name='password_reset'),
    path('password-reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset/complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('password-reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'), 
    #path('verify/', verify_view, name='verify'),
    path('signup/', signup, name='signup'),
    path('logout/form/', logout_form, name='form'),
    path('', home_view, name='home')
]