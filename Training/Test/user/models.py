from tkinter import N
from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password


##create User Model Here
class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password=None, **extrafeilds):
        #use of this value Errors
        if not email:
            raise ValueError("Email must be Provided")
        if not password:
            raise ValueError("Password must be Provided")

        user = self.model(
            email=self.normalize_email(email),
            **extrafeilds
        )

        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        import pdb; pdb.set_trace()
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password=password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        import pdb; pdb.set_trace()
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password=password, **extra_fields)


# Create your models here.

class User(AbstractUser, PermissionsMixin):
    ###if we put null=True blank=True in email it will create an exception in _create_user methods
    email = models.EmailField(unique=True, max_length=254)
    username = None

    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'




class Laptops(models.Model):
    name=models.CharField(max_length=30)
    model_no=models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.name


class Person(models.Model):
    name=models.CharField(max_length=30)
    laptop=models.OneToOneField(Laptops, on_delete=models.CASCADE, related_name='ownedBy')

    def __str__(self) -> str:
        return self.name

class Team(models.Model):
    team_name=models.CharField(max_length=900)
    team_members=models.IntegerField()

    def __str__(self) -> str:
        return self.team_name



class Product(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE, null=False, blank=False)
    name=models.CharField(max_length=200)
    description=models.TextField(max_length=500)

    def __str__(self) -> str:
        return self.name