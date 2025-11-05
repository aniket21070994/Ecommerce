from django.contrib import admin
from models_manager.models import UserProfile,Order,OrderItem,Product,ProductImage,ProductVariant,Cart,CartItem,Category,Notification,Discount
admin.site.register(UserProfile)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Category)
