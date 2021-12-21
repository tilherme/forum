from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email=None, password=None):
        if not email:
            raise ValueError(_('Users must have an email'))

        user = self.model(
            email=email,
        )

        user.set_password(password)
        user.save(using=self._db)

        return user
    def create_superuser(self, email, password):
        user = self.create_user(
            email=email,
            password=password,
        )

        user.is_admin = True
        user.save(using=self._db)

        return user
        @classmethod
        def create_from_dict(cls, d):
            return cls.objects.create() 

class User(AbstractBaseUser):
    name = models.CharField(max_length=255, blank=True,null=True)
    email = models.EmailField(unique=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    is_admin = models.BooleanField(default=False)
    active = models.BooleanField(default=False)
    cpf = models.CharField(max_length=255, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now=True)
   
    objects = UserManager()

    USERNAME_FIELD = 'email'

    def get_short_name(self):
        return self.name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
