class {Model}Permissions(permissions.BasePermission):
    message = "You do not have permission."
    def has_permission(self, request, view):
        if request.method == 'POST':
            return check_allowed([{post_users}], request, obj = None)
        elif request.method == 'GET':
            return check_allowed([{get_users}], request, obj = None)
        else:
            return True

    def has_object_permission(self, request, view, obj):
        if request.method == 'PUT':
            return check_allowed([{put_users}], request, obj)
        elif request.method == 'DELETE':
            return check_allowed([{delete_users}], request, obj)
        else:
            return False
