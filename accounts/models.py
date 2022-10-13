from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, is_active=True, is_staff=False, is_admin=False, is_employee=False, is_hr=False, is_accounting=False):
        if not email:
            raise ValueError("Must have Email")
        if not password:
            raise ValueError("Must have Password")

        user_obj = self.model(
            email=self.normalize_email(email)
        )
        user_obj.set_password(password)
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.active = is_active
        user_obj.employee = is_employee
        user.obj.accounting = is_accounting
        user_obj.hr = is_hr
        user_obj.save(using=self._db)

        return user_obj

    def create_staffuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
            is_staff=True,
            is_active=True,
            is_admin=False
        )
        return user

    def create_employee(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
            is_staff=True,
            is_active=True,
            is_employee=True
        )
        return user


    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
            is_staff=True,

            is_active=True,
        )
        return user

class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    mobile_number = models.IntegerField
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(default="", max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(default="", max_length=100)
    nationality = models.CharField(default="", max_length=100)
    birth_date = models.DateField(blank=True, null=True)
    address = models.CharField(default="", max_length=100)
    activate = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    hr = models.BooleanField(default=False)
    accounting = models.BooleanField(default=False)
    employee = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

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
    def is_employee(self):
        return self.employee

    @property
    def is_active(self):
        return True

