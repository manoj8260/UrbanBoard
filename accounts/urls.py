from django.urls import path
from .views import Signup,Signin,home,Logout

urlpatterns = [
    path('',Signup,name='signup'),
    path('login/',Signin,name='signin'),
    path('home/',home,name='home'),
    path('logout/',Logout,name='signout'),
]
