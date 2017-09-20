class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating, reading, and updating profiles."""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)

class LoginViewSet(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(LoginViewSet, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        user = models.UserProfile.objects.filter(id=token.user_id).first()

        return Response({
            'token': token.key,
            'id': token.user_id,
            'name': request.data.get('username'),
            'is_staff': user.is_staff,
            'is_superuser': user.is_superuser,
            'is_active': user.is_active,
        })
