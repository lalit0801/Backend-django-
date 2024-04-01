from rest_framework import permissions
from. permissions import AdminPermissions

class AdminPermissionsMixin(AdminPermissions):
    permission_classes= [
        permissions.IsAuthenticated,
        AdminPermissions,
    ]