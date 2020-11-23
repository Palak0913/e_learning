
from django.db import models

from django.contrib.auth.models import AbstractBaseUser,BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self,username, email, password=None,is_staff=False, is_active=True, is_admin=False):
        
        if not username:
            raise ValueError("user must have a username")
        if not email:
            raise ValueError('users must have a email')
        if not password:
            raise ValueError('user must have a password')

        user_obj = self.model(
            username=username,
            email=email
        )
        user_obj.set_password(password)
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.active = is_active
        user_obj.save(using=self._db)
        return user_obj

    def create_superuser(self, username,email, password=None):
        user = self.create_user(
            username,
            email,
            password=password,
            is_staff=True,
            is_admin=True,

        )
        return user





class User(AbstractBaseUser):
    username = models.CharField(max_length=150,)
    email = models.EmailField('email address', unique=True)
    active = models.BooleanField(default=True)
    staff       = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]

    objects = UserManager()

    def __str__(self):
        return f"{self.email}"

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):

        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active


