from django.urls import path
from urbanstay.views import(create_flat_listing ,load_cities ,book_flat,
                            EditFlatView ,DeleteFlatView,FlatDetailView)
urlpatterns=[      
    path('flat/create/', create_flat_listing, name='create_flat_listing'),
    path('ajax/load-cities/', load_cities, name='load_cities'),
    path('book/<int:flat_id>/',book_flat,name='flat_book'),
        path('flat-detail/<int:pk>/', FlatDetailView.as_view(), name='flat_detail'),
    path('flat-edit/<int:pk>/',EditFlatView.as_view(),name='flat_edit') ,
    path('flat/<int:pk>/delete/', DeleteFlatView.as_view(), name='flat_delete'),
]