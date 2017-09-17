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

def check_allowed(allowed_users, request, obj):
    # Return false if any of the checks don't pass.
    for user in allowed_users:
        if user == 'active' and not isActive(request):
            return False
        elif user == 'anonymous' and not isAnon(request):
            return False
        elif user == 'authenticated' and not isAuth(request):
            return False
        elif user == 'owner' and not isOwner(request, obj):
            return False
        elif user == 'staff' and not isStaff(request):
            return False
        elif user == 'superuser' and not isSuperuser(request):
            return False

    # If everything passed, then return True
    return True
