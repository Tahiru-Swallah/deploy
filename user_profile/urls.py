from django.urls import path
from .views import edit, user_profile

app_name = 'user_profile' 

urlpatterns = [
    path('edit/', edit, name='profile_edit'),
    path('<username>/', user_profile, name='profile')
]