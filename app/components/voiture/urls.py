from django.urls import path
from .views import voiture_view_set, show_all, show_detail, create_voiture, update_voiture, delete_voiture

urlpatterns = [
    path('', voiture_view_set, name='apiViewSet'),
    path('voiture-list/', show_all, name='voiture-list'),
    path('voiture-detail/<int:pk>', show_detail, name='voiture-detail'),
    path('voiture-create/', create_voiture, name='voiture-create'),
    path('voiture-update/<int:pk>', update_voiture, name='voiture-update'),
    path('voiture-delete/<int:pk>', delete_voiture, name='voiture-delete'),
]
