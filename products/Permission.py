from rest_framework.permissions import BasePermission

class Admin(BasePermission):
    def has_permission(self,request,view):
        if request.user.userProfile=="admin" | request.user.userProfile=="Admin":
            return True
        else:
            return False
class SuperAdmin(BasePermission):
    def has_permission(self,request,view):
        if request.user.userProfile=="SuperAdmin" | request.user.userProfile=="SUPER_ADMIN":
            return True
        else:
            return False

class User(BasePermission):
    def has_permission(self,request,view):
        if request.user.userProfile=="User" | request.user.userProfile=="USER":
            if request.method=="GET":
                return True
            return False
        else:
            return False