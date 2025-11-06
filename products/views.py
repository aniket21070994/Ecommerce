from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from models_manager.models import Product, ProductVariant,ProductImage
from .Serializer import ProductSerializer,ProductVariantSerializer,ProductImageSerializer
from products.Permission import Admin,User,SuperAdmin



"--------------------------------Get Product Listn  & Create Product <list:All , create:Admin/SuperAdmin>------------------------------------------------------------------------------------------------------------------------------------------------------"
class ProductView(APIView):
    permission_classes=[User|Admin|SuperAdmin]
    def get(self,request):
        products=Product.objects.all()
        serializer=ProductSerializer(products,many=True)
        return Response({"message":"product list","products":serializer.data},status=status.HTTP_200_OK)
    
    def post(self,request):
        if request.user.userProfile=="USER":
            return Response({"message":"you are not allowed to create product"},status=status.HTTP_400_BAD_REQUEST)
        
        serializer=ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"product created"},status=status.HTTP_200_OK)
        else:
            return Response({"message":"invalid data"},status=status.HTTP_400_BAD_REQUEST)

"-------------------------------------------X--------------------------------------------------------------------------------------------------------------------------------------------------------"

"----------------------------- product specific operations (get , update , delete)<get:All , update:Admin/SuperAdmin , delete:Admin/SuperAdmin>------------------------------------------------------------------------------------------------------------------"
class ProductWithParams(APIView):
    permission_classes=[User|Admin|SuperAdmin]
    def get(self,request,id):
        product=Product.objects.filter(id=id)
        if product:
            serializer=ProductSerializer(product)
            return Response({"message":"product","product":serializer.data},status=status.HTTP_200_OK)
        else:
            return Response({"message":"product not found"},status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,id):
        product=product.objects.filter(id=id)
        if product:
            serializer=ProductSerializer(product,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"message":"product updated"},status=status.HTTP_200_OK)
            else:
                return Response({"message":"invalid data"},status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message":"product not found"},status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,id):
        product=Product.objects.filter(id=id)
        if product:
            product.delete()
            return Response({"message":"product deleted"},status=status.HTTP_200_OK)
        else:
            return Response({'message':'product not found'},status=status.HTTP_400_BAD_REQUEST)


class ProductVariantView(APIView):
    def post(self,request,id):
        product=Product.objects.filter(id=id)
        if product:
            serializer=ProductVariantSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message":"product variant created"},status=status.HTTP_200_OK)
        return Response({"message":"invalid data"},status=status.HTTP_400_BAD_REQUEST)

"-----------------------------------------------------X--------------------------------------------------------------------------------------------------------------------------------------------------------------------"

"------------------------------------------------Product Image operation (upload image to product)<admin/SuperAdmin>--------------------------------------------------------------------------------------------------------"

class ProductImage(APIView):
    permission_classes=[Admin|SuperAdmin]
    def post(self,request,id):
        product=Product.objects.filter(id=id)
        if product:
            serializer=ProductImageSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message":"product image updated"},status=status.HTTP_200_OK)
        
        return Response({"message":"invalid data"},status=status.HTTP_400_BAD_REQUEST)
    
"----------------------------------------------------------X------------------------------------------------------------------------------------------------------------------------------------------------------------------"