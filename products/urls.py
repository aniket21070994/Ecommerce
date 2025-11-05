
from django.urls import path
from .views import ProductView,ProductWithParams,ProductVariantView,ProductImage


urlpatterns = [
    path('product/',ProductView.as_view()),
    path('product/<int:id>/',ProductWithParams.as_view()),
    path('product/<int:id>/variant/',ProductVariantView.as_view()),
    path('product/<int:id>/image/',ProductImage.as_view()),
         
]
