from rest_framework import permissions

def isActive(request):
    return request.user.is_active

def isAnon(request):
    return request.user.is_anonymous()

def isAuth(request):
    return not request.user.is_anonymous()

def isOwner(request, obj):
    return request.user == obj.owner

def isStaff(request):
    return request.user.is_staff

def isSuperuser(request):
    return request.user.is_superuser

def check_allowed(allowed_users, request, obj = None):
    # Return false if any of the checks don't pass.
    for user in allowed_users:
        if user == 'Active' and not isActive(request):
            return False
        elif user == 'Anonymous' and not isAnon(request):
            return False
        elif user == 'Authenticated' and not isAuth(request):
            return False
        elif user == 'Owner' and not isOwner(request, obj):
            return False
        elif user == 'Staff' and not isStaff(request):
            return False
        elif user == 'Superuser' and not isSuperuser(request):
            return False

    # If everything passed, then return True
    return True
