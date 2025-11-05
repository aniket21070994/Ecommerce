# from django.db import models
# from django .contrib.auth.models import User

# import uuid
# # Create your models here.
# class Cart (models.Model):
#     id=models.IntegerField(primary_key=True,default=uuid.uuid4)
#     user=models.ForeignKey(User,on_delete=models.CASCADE,null=False)
#     created_at=models.DateTimeField(auto_now_add=True)
#     def __str__(self):
#         return self.created_at