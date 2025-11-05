# from django.db import models
# from django.contrib.auth.models import User

# class UserProfile(models.Model):
#     class Role(models.TextChoices):
#         SUPER_ADMIN = 'SUPER_ADMIN', 'Super Admin'
#         ADMIN = 'ADMIN', 'Admin'
#         USER = 'USER', 'User'

#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
#     phone_number = models.CharField(max_length=15, blank=True, null=True)
#     date_of_birth = models.DateField(blank=True, null=True)
#     gender = models.CharField(max_length=10, blank=True, null=True)
#     profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
#     default_address = models.ForeignKey('Address', on_delete=models.SET_NULL, null=True, blank=True)
#     role = models.CharField(max_length=20, choices=Role.choices, default=Role.USER)

#     def __str__(self):
#         return f"{self.user.username}'s profile"


# class Address(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)
#     street = models.CharField(max_length=255)
#     city = models.CharField(max_length=100)
#     state = models.CharField(max_length=100)
#     country = models.CharField(max_length=100)
#     zipcode = models.CharField(max_length=20)
#     is_default = models.BooleanField(default=False)

#     def __str__(self):
#         return f"{self.name}, {self.street}, {self.city}"
