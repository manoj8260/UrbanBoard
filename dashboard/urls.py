from django.urls import path
from .views import landlord_dashboard,boarder_dashboard

urlpatterns = [
    path('landlord_dashboard/',landlord_dashboard,name='landlord_dashboard'),
    path('boarder_dashboard/',boarder_dashboard,name='boarder_dashboard'),
]
