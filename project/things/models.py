from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin

from .directionOfFile import images_upload


class Country(models.Model):
   country_name=models.CharField(max_length=256,blank=True)
   def __str__(self):
        return self.country_name

class User_table(models.Model):
    id=models.IntegerField(blank=True,primary_key=True)
    country= models.ForeignKey(Country,blank=True, on_delete=models.CASCADE)
    university=models.CharField(max_length=256,blank=True)
    speciality=models.CharField(max_length=524,blank=True)
    checking=models.BooleanField(default=False)
    score=models.IntegerField(blank=True,null=True) 
    string=models.CharField(max_length=1024,blank=True,default='')
    date=models.DateField(auto_now_add=True, blank=True)
    Notcorrect=models.CharField(max_length=1024,blank=True,default='')
    def __int__(self):
        return self.id


class Test(models.Model):
    number=models.IntegerField();
    SECTION_TYPE = (
        (1, 'English'),
        (2, 'Russion'),
    );
    sections = models.PositiveSmallIntegerField(choices=SECTION_TYPE);
    question=models.TextField(default='')
    img=models.ImageField(upload_to=images_upload,default='',blank=True)
    second_part=models.TextField(default='',blank=True)
    A=models.CharField(max_length=1024)
    B=models.CharField(max_length=1024)
    C=models.CharField(max_length=1024)
    D=models.CharField(max_length=1024 ,blank=True,default="")
    E=models.CharField(max_length=1024 ,blank=True,default="")
    answer=models.CharField(max_length=256)
    data=models.DateField(default="2018-01-01")
    def __str__(self):
        return self.answer


class UserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_admin', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_admin', True)
        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UserManager()

    @property
    def is_staff(self):
        return self.is_admin