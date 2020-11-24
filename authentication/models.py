from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token


class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None,**extra_fields):

        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),**extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):

        user = self.create_user(
            email,
            password=password

        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser):
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    company_name = models.CharField(null=True, blank=True, max_length=120)
    last_login = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_shopper = models.BooleanField(default=False)
    is_merchant = models.BooleanField(default=False)
    is_manufacturer = models.BooleanField(default=False)
    is_shipper = models.BooleanField(default=False)
    is_distributor = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    address = models.CharField(max_length=254, null=True, blank=True)
    state = models.CharField(max_length=15, null=True, blank=True)
    telephone = PhoneNumberField(null=True, unique=True)
    bio = models.CharField(max_length=256, null=True, blank=True)
    company_reg = models.CharField(max_length=15, null=True, blank=True)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    def get_full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)


location_options = [('Lagos Only', 'Lagos Only'), ('Abuja Only', 'Abuja Only'), ('Port Harcourt Only',
                    'Port Harcourt Only'), ('South-South', 'South-South'), ('South-East', 'South-East'), ('South-West',
                    'South-West'), ('North-East', 'North-East'), ('North-Central', 'North-Central'), ('North-West',
                    'North-West'), ('All Regions', 'All Regions')]

transport_type = [('Bike', 'Bike'), ('MiniBus', 'MiniBus')]


class Shipper(models.Model):
    engine_number = models.IntegerField()
    registration_number = models.IntegerField()
    registration_name = models.CharField(max_length=55)
    year_of_purchase = models.IntegerField()
    brand = models.CharField(max_length=25)
    vehicle_type = models.CharField(max_length=25, choices=transport_type)
    license_number = models.IntegerField()
    extra_info = models.TextField()
    region = models.CharField(max_length=25, choices=location_options)
    is_created = models.BooleanField(default=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.name


@receiver(post_save, sender=CustomUser)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)