class {Model}Permissions(permissions.BasePermission):
    message = "You do not have permission."
    def has_permission(self, request, view):
        # List view
        if request.method == 'GET' and view.action == 'list':
            return check_allowed(['list_users'], request)
        # Create
        elif request.method == 'POST':
            return check_allowed(['post_users'], request)
        else:
            return True

    def has_object_permission(self, request, view, obj = None):
        # Details view
        if request.method == 'GET':
            return check_allowed(['details_users'], request, obj)
        # Update
        if request.method == 'PUT':
            return check_allowed(['put_users'], request, obj)
        # Delete
        elif request.method == 'DELETE':
            return check_allowed(['delete_users'], request, obj)
        else:
            return False
