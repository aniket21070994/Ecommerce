
from django.urls import path
from .views import PaymentHandlear,successHandler,cancelHandler,stripHookHandler
urlpatterns = [
    path("",PaymentHandlear.as_view(),name="payment" ),
    path("success-payment/",successHandler.as_view(),name="success-payment"),
    path("cancel-payment/",cancelHandler.as_view(),name="cancel-payment"),
    path("stripe-hook/",stripHookHandler.as_view(),name="stripe-hook")
]
