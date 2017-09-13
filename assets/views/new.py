class {title}ViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.{title}Serializer
    queryset = models.{title}.objects.all()
    authentication_classes = (TokenAuthentication,)
    {permissions}
