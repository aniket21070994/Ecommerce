
from django.urls import path
from .views import CartHandlear,CartSpecificUserHandler
urlpatterns = [
   
    path('add/',CartHandlear.as_view(),name='add_cart'),
    path('update/<int:pk>/',CartSpecificUserHandler.as_view(),name='update_cart'),
    path('remove/<int:pk>/',CartSpecificUserHandler.as_view(),name='delete_cart'),
    path('',CartHandlear.as_view(),name='cart')
]
