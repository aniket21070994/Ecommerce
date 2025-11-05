# from django.db import models
# import uuid
# from catalog.models import Category, Brand

# # Create your models here.
# class Product(models.Model):
#     id=models.IntegerField(primary_key=True,default=uuid.uuid4, editable=False)
#     slug=models.SlugField(unique=True,max_length=200)
#     name=models.CharField()
#     description=models.TextField()
#     category=models.ForeignKey(Category,on_delete=models.CASCADE)
#     brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
#     base_price=models.DecimalField()
#     stock=models.IntegerField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     def __str__(self):
#         return self.name
# class Product_Image(models.Model):
#     product=models.ForeignKey(Product,on_delete=models.CASCADE)
#     image=models.ImageField(upload_to='products')
#     alt_text=models.CharField(max_length=200)
#     def __str__(self):
#         return self.alt_text
# class Product_Variant(models.Model):
#     id=models.IntegerField(primary_key=True,default=uuid.uuid4,editable=False)
#     product=models.ForeignKey(Product,null=False, on_delete=models.CASCADE)
#     sku=models.CharField(unique=True)
#     name=models.CharField(max_length=200)
#     price=models.DecimalField()
#     stock=models.IntegerField()
#     def __str__(self):
#         return self.name




