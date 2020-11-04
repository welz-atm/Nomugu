from rest_framework import serializers
from authentication.models import CustomUser, Shipper
from django_countries.serializer_fields import CountryField


class MerchantRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ('pk', 'name', 'first_name', 'last_name', 'email', 'address', 'state', 'country', 'telephone', 'bio',
                  'is_merchant')

    def save(self, **kwargs):
        user = CustomUser(first_name=self.validated_data['first_name'],
                          last_name=self.validated_data['last_name'],
                          email=self.validated_data['email'],
                          telephone=self.validated_data['telephone'],
                          is_merchant=self.validated_data['is_merchant'],
                          address=self.validated_data['address'],
                          state=self.validated_data['state'],
                          country=self.validated_data['country'],
                          bio=self.validated_data['bio'])
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password == password2:
            user.set_password(password)
            user.save()
            return user
        else:
            raise serializers.ValidationError({'Password': 'Passwords must match'})


class ShopperRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    telephone = CountryField()

    class Meta:
        model = CustomUser
        fields = ('pk', 'first_name', 'last_name', 'email', 'telephone', 'is_shopper', 'password', )
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def save(self, **kwargs):
        user = CustomUser(first_name=self.validated_data['first_name'],
                          last_name=self.validated_data['last_name'],
                          email=self.validated_data['email'],
                          telephone=self.validated_data['telephone'],
                          is_shipper=self.validated_data['is_shopper'],)
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password == password2:
            user.set_password(password)
            user.save()
            return user
        else:
            raise serializers.ValidationError({'Password': 'Passwords must match'})


class ShipperRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'address', 'state', 'country', 'telephone', 'is_shipper')

    def save(self, **kwargs):
        user = CustomUser(first_name=self.validated_data['first_name'],
                          last_name=self.validated_data['last_name'],
                          email=self.validated_data['email'],
                          telephone=self.validated_data['telephone'],
                          is_shipper=self.validated_data['is_shipper'],
                          address=self.validated_data['address'],
                          state=self.validated_data['state'],
                          country=self.validated_data['country'])
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password == password2:
            user.set_password(password)
            user.save()
            return user
        else:
            raise serializers.ValidationError({'Password': 'Passwords must match'})


class ShipperDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shipper
        fields = ('vehicle_type', 'registration_name', 'registration_number', 'license_number', 'engine_number', 'brand',
                  'year_of_purchase', 'region', 'price', 'unit', 'extra_weight', 'extra_info')


class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('pk', 'name', 'first_name', 'last_name', 'email', 'address', 'state', 'country', 'telephone', 'bio',
                  'is_merchant', 'is_shipper', 'is_shopper', )


class PasswordChangeSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    confirm_new_password = serializers.CharField(required=True)