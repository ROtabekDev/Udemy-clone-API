from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.contrib.auth.models import BaseUserManager, PermissionsMixin
from courses.models import Course


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_superuser(self, email, password, name, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)

        if other_fields.get('is_staff') is not True:
            return ValueError('Superuserda is_staff True bo`lishi kerak')

        if other_fields.get('is_superuser') is not True:
            return ValueError('Superuserda is_superuser True bo`lishi kerak')

        return self.create_user(email, password, name, **other_fields)

    def create_user(self, email, password, name, **other_fields):
        if not email:
            raise ValueError('Yaroqli elektron pochta manzilini taqdim etishingiz kerak')

        email = self.normalize_email(email)

        user = self.model(email=email, name=name, **other_fields)

        user.set_password(password)

        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    is_staff = models.BooleanField(default=False)
    paid_courses = models.ManyToManyField(Course)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['name']

    objects=UserManager()

    def __str__(self):
        return self.name+" "+self.email