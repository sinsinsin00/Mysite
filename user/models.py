from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser, BaseUserManager


class CustomAccountManager(BaseUserManager):
    def create_user(self, email, password):
        user = self.model(email=email, password=password)
        user.set_password(password)
        user.is_staff = False
        user.is_superuser = False
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email=email, password=password)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

    def get_by_natural_key(self, email):
        return self.get(email=email)
    
# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    """
        유저 프로파일 사진
        유저 이름           -> 실제 사용자 이름 
        유저 닉네임         ->  화면에 표기되는 이름
        유저 이메일 주소    ->  회원가입할때 사용하는 아이디
        유저 비밀번호       -> 디폴트 사용
        
    """
    
    profile_image = models.TextField()
    nickname = models.CharField(max_length=24,unique=True)
    username = models.CharField(max_length=24, null=True, default='')
    name = models.CharField(max_length=24)
    email = models.EmailField(unique=True)
    
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    
    objects=CustomAccountManager()
    
    def get_short_name(self):
        return self.email

    def __str__(self):
        return self.email
    
    class Meta:
        db_table = "User"
    

