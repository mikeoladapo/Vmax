from django.db import models
from django.contrib.auth.models import AbstractBaseUser , BaseUserManager,PermissionsMixin
from django.core.validators import RegexValidator

class CustomUserManager(BaseUserManager):
    def create_user(self,email,password=None,**extra_fields):
        if not email:
            raise ValueError("email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user 
    def create_superuser(self,email,password=None,**extra_fields):
        extra_fields.setdefault("is_staff",True)
        extra_fields.setdefault("is_superuser",True)
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser,PermissionsMixin):
    username_regex = RegexValidator(
        regex=r'^[a-zA-Z0-9_]{3,20}$',
        message=(
        "Username must be 3-20 characters long and can only contain letters, "
        "numbers, and underscores."),
        code="invalid username"
        )
    username = models.CharField(max_length=20,unique=True,
                                validators=[username_regex],
                                error_messages={"unique":"username is already taken"})
    email = models.EmailField(unique=True)
    password = models.CharField()
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    objects = CustomUserManager()
    def __str__(self):
        return self.username
    
class VideoFile(models.Model):
    title = models.CharField(max_length=200)
    video = CloudinaryField("video",blank=False,null=False)
    thumbnail = 
    


