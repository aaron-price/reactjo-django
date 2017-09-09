class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating, reading, and updating profiles."""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)

class LoginViewSet(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(LoginViewSet, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])

        return Response({
            'token': token.key,
            'id': token.user_id,
            "name": request.data.get('username')
        })
