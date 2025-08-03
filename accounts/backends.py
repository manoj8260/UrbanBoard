from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q

User = get_user_model()

class  EmailOrPhoneBackend(ModelBackend):
    def authenticate(self, request, username = None, password = None, **kwargs):
        print(username,'-')
        try:
            user = User.objects.filter(Q(email__iexact = username) | Q(phone__iexact = username)).first()
            print(user)
        except User.DoesNotExist:
            User().set_password(password) # mitigate timing attacks
            return None
        
        if password and user.check_password(password) and   self.user_can_authenticate(user)  :     
             return user
        return None 