from django.shortcuts import render
from  rest_framework.views import APIView
import stripe
from Ecommerce.settings import PRIVATE_KEY,PUBLIC_KEY
from rest_framework import response
stripe.api_key=PRIVATE_KEY
# Create your views here.

class PaymentHandlear(APIView):
    def post(self,request):
        amount=request.data.get('amount')
        if amount:
            try:
              payment=stripe.checkout.Session.create(
                line_items=[
                    {
                        'price_data':{
                            'currency':'usd',
                            'product_data':{
                                'name':'product',
                            },
                            'unit_amount':1000,
                        },
                        'quantity':1
                    }
                ],
                mode='payment',
                success_url='http://localhost:3000/success',
                cancel_url='http://localhost:3000/cancel'
              )
              return response({'session_id':payment.id,"url":payment.url})
            except Exception as e:
                return response({'error':str(e)})
                


