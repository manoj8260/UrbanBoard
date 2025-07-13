from django.urls import path
from .views import Signup,Login,home,Logout

urlpatterns = [
    path('',Signup,name='signup'),
    path('login/',Login,name='login'),
    path('home/',home,name='home'),
    path('logout/',Logout,name='logout'),
]
