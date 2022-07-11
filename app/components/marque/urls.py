from django.urls import path
from .views import marque_view_set, show_all, show_detail, create_marque, update_marque, delete_marque

urlpatterns = [
    path('', marque_view_set, name='apiViewSet'),
    path('marque-list/', show_all, name='marque-list'),
    path('marque-detail/<int:pk>', show_detail, name='marque-detail'),
    path('marque-create/', create_marque, name='marque-create'),
    path('marque-update/<int:pk>', update_marque, name='marque-update'),
    path('marque-delete/<int:pk>', delete_marque, name='marque-delete'),
]
