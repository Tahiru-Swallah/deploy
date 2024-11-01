from django.contrib.auth.backends import ModelBackend
from .models import CustomUser
from django.db.models import Q
from user_profile.models import Profile

User = CustomUser

class EmailorPhoneBackend(ModelBackend):
    def authenticate(self, request, username = None, password = None, **kwargs):
       try:
           user = User.objects.get(Q(email=username) | Q(phone_number=username))

       except (User.DoesNotExist, User.MultipleObjectsReturned):
           return None
       
       if user.check_password(password) and self.user_can_authenticate(user):
           return user
       return None
    
def create_profile(backend, user, *args, **kwargs):
    Profile.objects.get_or_create(user=user)