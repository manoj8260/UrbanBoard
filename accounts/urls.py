from django.urls import path
from accounts.views import Signup,Signin,home,Logout ,password_reset_request,password_reset_done,password_reset_complete,password_reset_confirm,google_role_redirect,select_role
from .views import Signup,Signin,home,Logout,activate_account
from .views import clear_sesion
urlpatterns = [
    path('',home,name='home'),
    path('register/',Signup,name='signup'),
    path('login/',Signin,name='signin'),
    path('logout/',Logout,name='signout'),
    
    path('google_redirect/', google_role_redirect, name='google_redirect'),
    path('select_role/', select_role, name='select_role'), 
      
    #forget password  urls
    path("password-reset/", password_reset_request, name="password_reset"),
    path("password-reset/done/", password_reset_done, name="password_reset_done"),
    path("reset/<uidb64>/<token>/", password_reset_confirm, name="password_reset_confirm"),
    path("reset/done/", password_reset_complete, name="password_reset_complete"),

    path('activate/<uidb64>/',activate_account,name='activate_account'),
    path('clear/',clear_sesion)

]
