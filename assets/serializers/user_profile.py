class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserProfile
        fields = (
            'id'fields_list,
            'owner',
            'password',
            'is_staff',
            'is_superuser',
            'is_active',
        )
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = models.UserProfile(validated_list
        )
        user.set_password(validated_data['password'])
        user.save()

        return user
