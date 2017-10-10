from rest_framework import permissions

def isActive(request):
    return request.user.is_active

def isAnon(request):
    return request.user.is_anonymous()

def isAuth(request):
    return not request.user.is_anonymous()

def isOwner(request, obj):
    if type(obj.owner) == int:
        return request.user.id == obj.owner
    else:
        return request.user.id == obj.owner.id

def isStaff(request):
    return request.user.is_staff

def isSuperuser(request):
    return request.user.is_superuser

def check_allowed(allowed_users, request, obj = None):
    # Return True if Any of the checks pass.

    for user in allowed_users:
        if user == 'Active' and isActive(request):
            return True
        elif user == 'Anonymous' and isAnon(request):
            return True
        elif user == 'Anyone':
            return True
        elif user == 'Nobody':
            return False
        elif user == 'Authenticated' and isAuth(request):
            return True
        elif user == 'Owner' and isOwner(request, obj):
            return True
        elif user == 'Staff' and isStaff(request):
            return True
        elif user == 'Superuser' and isSuperuser(request):
            return True

    # Return False if None of the checks pass.
    return False
