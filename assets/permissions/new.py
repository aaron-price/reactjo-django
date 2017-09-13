class {action}Permissions(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        user_type = request.user
        is_owner = obj.id == request.user.id

        if request.method == 'GET':
            return request.user.get_allowed
        if request.method == 'POST':
            return user_type.post_allowed
        if request.method == 'PUT':
            return user_type.put_allowed
        if request.method == 'DELETE':
            return user_type.delete_allowed
        return False
