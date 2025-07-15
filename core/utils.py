from core.permission_configure import PERMISSION_CONFIG
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

def assign_permission(user, role):
    role_permission = PERMISSION_CONFIG.get(role, {})
    
    for model, permissions in role_permission.items():
        content_type = ContentType.objects.get_for_model(model)
        
        for codename in permissions:
            full_codename = f"{codename}_{model._meta.model_name}"
            try:
                permission = Permission.objects.get(
                    content_type=content_type,
                    codename=full_codename
                )
                user.user_permissions.add(permission)
            except Permission.DoesNotExist:
                print(f"⚠️ Permission '{full_codename}' not found for model '{model.__name__}'")
