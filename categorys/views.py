from django.shortcuts import render
from models_manager.models import Category,Brand
from .Serializer import CategorySerializer ,BrandSerializer
from rest_framework.views import APIView,status
from rest_framework import response

"---------------------------------------list of category  (get list and create category)--------------------------------------------------------------------------------------------------------------------------------------------------------------------"

class ListCategory(APIView):
    def get(self,request):
        categories=Category.objects.all()
        serializer=CategorySerializer(categories,many=True)
        return response({"message":"category list","categories":serializer.data},status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer=CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response({"message":"category created"},status=status.HTTP_200_OK)
        else:
            return response({"message":"invalid data"},status=status.HTTP_400_BAD_REQUEST)
    
        

"-------------------------------------------------X----------------------------------------------------------------------------------------------------------------------------------------------------------------------------"

"--------------------------------------Update and Delete category---------------------------------------------------------------------------------------------------------------------------------------------------------------------"

class CategoryUpdateDelete(APIView):
    def put(self,request,id):
        category=Category.objects.get(id=id)
        serializer=CategorySerializer(category,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return response({"message":"category updated"},status=status.HTTP_200_OK)
    def delete(self,request,id):
        category=Category.objects.filter(id=id)
        if category:
            category.delete()
            return response({"message":"category deleted"},status=status.HTTP_200_OK)
        else:
            return response({"message":"category not found"},status=status.HTTP_400_BAD_REQUEST)

"---------------------------------------------------X---------------------------------------------------------------------------------------------------------------------------------------------------------------------------"


"--------------------------------------------------------- get and create brand---------------------------------------------------------------------------------------"
class ListBrand(APIView):
    def get(self,request):   
        brands=Brand.objects.all()
        serializer=BrandSerializer(brands,many=True)
        return response({"message":"brand list","brands":serializer.data},status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer=BrandSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response({"message":"brand created"},status=status.HTTP_200_OK)
        else:
            return response({"message":"invalid data"},status=status.HTTP_400_BAD_REQUEST)
"-------------------------------------------------------------------X--------------------------------------------------------------------------------------------------"