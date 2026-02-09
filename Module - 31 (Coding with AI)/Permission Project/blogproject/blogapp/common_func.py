from blogapp.models import UserPermissions

def CheckUserPermission(request, access_type, menu_url):
    try:
        user_permission = {
            "can_view": "can_view",
            "can_add": "can_add",
            "can_edit": "can_edit",
            "can_delete": "can_delete"
        }
        
        if request.user.is_superuser:
            return True
        
        check_user_permission = UserPermissions.objects.select_related('menu').filter(
            user_id=request.user.id,
            is_active=True,
            deleted=False,
            menu__menu_url=menu_url,
            **{user_permission[access_type]: True}
        )
        
        if check_user_permission: 
            return True
        else:
            return False
    except Exception as e:
        print("Error in CheckUserPermission:", e)
        return False