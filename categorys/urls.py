
from django.urls import path
from .views import ListCategory,CategoryUpdateDelete

urlpatterns = [
    path('categories/',ListCategory.as_view()),
    path('categories/<int:id>/',CategoryUpdateDelete.as_view())
]
