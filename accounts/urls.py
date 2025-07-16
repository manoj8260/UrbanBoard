from django.urls import path
from accounts.views import Signup,Signin,home,Logout ,password_reset_request,password_reset_done,password_reset_complete,password_reset_confirm
from .views import Signup,Signin,home,Logout,activate_account
urlpatterns = [
    path('',Signup,name='signup'),
    path('login/',Signin,name='signin'),
    path('home/',home,name='home'),
    path('logout/',Logout,name='signout'),    
    #forget password  urls
    path("password-reset/", password_reset_request, name="password_reset"),
    path("password-reset/done/", password_reset_done, name="password_reset_done"),
    path("reset/<uidb64>/<token>/", password_reset_confirm, name="password_reset_confirm"),
    path("reset/done/", password_reset_complete, name="password_reset_complete"),

    path('activate/<int:user_id>/',activate_account,name='activate_account'),

]
