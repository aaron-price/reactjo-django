class UserProfileManager(BaseUserManager):
    def create_user(self, title_list, password=None):
        if not email:
            raise ValueError('Users must have an email address.')

        email = self.normalize_email(email)
        user = self.model(assignment_list)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, title_list, password):
        user = self.create_user(title_list, password)
        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    field_strings
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = [required_list]

    def get_short_name(self):
        return self.name

    @property
    def owner(self):
        return self.pk
