class {Model}Permissions(permissions.BasePermission):
    message = "You do not have permission."
    def has_permission(self, request, view):
        if request.method == 'GET':
            return check_allowed(['anyone'], request)
        elif request.method == 'POST':
            return check_allowed(['authenticated'], request)
        else:
            return True

    def has_object_permission(self, request, view, obj = None):
        if request.method == 'GET':
            return check_allowed(['anyone'], request, obj)
        if request.method == 'PUT':
            return check_allowed(['owner'], request, obj)
        elif request.method == 'DELETE':
            return check_allowed(['owner'], request, obj)
        else:
            return False
