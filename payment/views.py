from django.shortcuts import render
from  rest_framework.views import APIView
import stripe
from Ecommerce.settings import secrate_stripe_key
from rest_framework.response import Response
from rest_framework import status
stripe.api_key=secrate_stripe_key


"""---------------payment handlear (Stripe)----------------------------------"""
class PaymentHandlear(APIView):
    def post(self,request):
        amount=request.data.get('amount')
        product=request.data.get('product')
        qty=request.data.get('qty')

        if amount:
            try:
              payment=stripe.checkout.Session.create(
                line_items=[
                    {
                        'price_data':{
                            'currency':'usd',
                            'product_data':{
                                'name':product,
                            },
                            'unit_amount':int(amount*100),
                        },
                        'quantity':qty
                    }
                ],
                mode='payment',
                success_url='http://localhost:8000/payment/success-payment/',
                cancel_url='http://localhost:8000/payment/cancel-payment/'
              )
              return Response({'session_id':payment.id,"url":payment.url})
            except Exception as e:
                return Response({'error':str(e)})
        else:
            return Response({"message":"amount is required","produt":"product is required","qty":"qty is required"},status=status.HTTP_400_BAD_REQUEST)



"---------------call back url handlear----------------------------------------------------------------------------------------------------------------------------------"
class successHandler(APIView):
    def get(self,request):
        return Response({"message":"payement successfull"},status=status.HTTP_200_OK)

class cancelHandler(APIView):
    def get(self,request):
        return Response({"message":"payement canceled"},status=status.HTTP_200_OK)






"----------------------stripe hook operation not active yet sine no buissness acount--------------------------------------------------------------------------------"

class stripHookHandler(APIView):
    def post(self,request):
        print(request.data)
        return Response({"message":"recived update"},status=status.HTTP_200_OK)