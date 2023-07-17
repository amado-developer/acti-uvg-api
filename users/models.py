from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, password2):
        if password != password2:
            raise ValueError('passwords does not match')
        else:
            user = self.model(
                email=self.normalize_email(email),
            )
            user.set_password(password)
            # user.save()
            return user


class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_director = models.BooleanField(default=False)
    is_organization = models.BooleanField(default=False)
    email = models.EmailField(unique=True, blank=False, null=False, default='')
    username = models.CharField(max_length=100, unique=True)
    USERNAME_FIELD = 'email'
    objects = CustomUserManager()
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Student(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=100)
    student_id = models.IntegerField(default=0)
    email = models.EmailField(unique=True)


class Director(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=100)
    career = models.CharField(max_length=100)
    email = models.EmailField(unique=True)


class Organization(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=100)
    manager = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
