from django.urls import path
from .views import landlord_dashboard,boarder_dashboard,load_cities,create_flat_listing,book_flat

urlpatterns = [
    path('landlord_dashboard/',landlord_dashboard,name='landlord_dashboard'),
    path('boarder_dashboard/',boarder_dashboard,name='boarder_dashboard'),
    
    
    path('flat/create/', create_flat_listing, name='create_flat_listing'),
    path('ajax/load-cities/', load_cities, name='load_cities'),
    path('book/<int:flat_id>/',book_flat,name='book_flat'),
    
]
