from django.urls import path
from .views import Signup,Signin,home,Logout,activate_account

urlpatterns = [
    path('',Signup,name='signup'),
    path('login/',Signin,name='signin'),
    path('home/',home,name='home'),
    path('logout/',Logout,name='signout'),
    path('activate/<int:user_id>/',activate_account,name='activate_account'),
]
