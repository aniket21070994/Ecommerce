from rest_framework import response,status
from models_manager.models import Cart,CartItem
from rest_framework.views import APIView
from .Serializer import CartSerializer,CartItemSerializer
from models_manager.Permissions import User

" ------------for operation on single cart---------------------------------------------------------------"
class CartHandlear(APIView):
    permission_classes=[User]
    def get(self,request):
        user=request.user
        cart=Cart.object.all(user=user)
        cartItem=CartItem.objects.all(user=cart.user)
        
        if cartItem:
            send_serializer=CartItemSerializer(data=cartItem)
            return response({"message":"cart details","cart":Cart})
        else: 
            return response({"message":"cart not found"},status=status.HTTP_400_BAD_REQUEST)
    
    def post(self,request):
        user=request.user
        recived_cart_serializer=CartSerializer(data=request.data)
        if recived_cart_serializer.is_valid():
            recived_cart_serializer.save()
            return response({"message":"item added to cart"},status=status.HTTP_200_OK)
        else:
            return response({"message":"data is invalide"},status=status.HTTP_400_BAD_REQUEST)

"------------------------- cart item updater and deleter--------------------------------------------------------------------------------------------------------------"

class CartSpecificUserHandler(APIView):
   permission_classes=[User]
   def put(self,request,pk):
       cartItems=CartItem.objects.all(id=pk)
       cart_send_serializer=CartItemSerializer(cartItems,data=request.data)
       if cart_send_serializer.is_valid():
           cart_send_serializer.save()
           return response({"message":"item updated"},status=status.HTTP_200_OK)
       
       return response({"message":"data is invalid"},status=status.HTTP_400_BAD_REQUEST)
   

   def delete(self,request,pk):
       CartItems=CartItem.objects.all(id=pk)
       CartItems.delete()
       return response({"message":"item deleted"},status=status.HTTP_200_OK)
            
"------------------------------------XX---------------------------------------------------------------------------------------------------------"