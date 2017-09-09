class {Title}ViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.{Title}Serializer
    queryset = models.{Title}.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.Create{Title},)
