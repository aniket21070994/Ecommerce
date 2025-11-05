# from django.db import models
# from django.contrib.auth.models import User
# import uuid

# # Create your models here.
# class Order(models.Model):
#     id=models.IntegerField(primary_key=True,default=uuid.uuid4)
#     user=models.ForeignKey(User, on_delete=models.CASCADE)
#     address=models.ForeignKey(address,null=False)
#     total_amount=models.DecimalField(10,2)
#     discount=models.DecimalField(10,2,null=False)
#     grand_total=models.DecimalField(10,2)
#     payment_status=models.
#     #complete this remaining part payment_status  Enum(PENDING, PAID, FAILED) Payment status 
# # order_status Enum(PENDING, APPROVED, SHIPPED, 
# # DELIVERED, CANCELLED) Order progress 
# # created_at DateTime Order creation time 
# # approved_by FK → User (nullable)
  