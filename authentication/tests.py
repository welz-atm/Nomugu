from django.test import TestCase, Client
from django.urls import reverse
from authentication.models import CustomUser
from django.contrib.auth import authenticate
from authentication.forms import shopper_signupform, merchant_signupform


class TestCustomUser(TestCase):
    def setUp(self):
        self.client = Client()
        self.user_shopper = CustomUser.objects.create_user(first_name='Tope',last_name='Shols',email='t@nomugu.com',
                                                           password='test123',is_shopper=True,telephone='08167847286')
        self.user_shopper.save()
        self.user_merchant=CustomUser.objects.create_user(name='Welz Inc',first_name='Ay',last_name='Shols',
                                                          email='w@nomugu.com',address='1,Abiona Ikorodu',
                                                          state='Lagos',country='Nigeria',telephone='08167847286',
                                                          password='test123', is_merchant=True)
        self.user_merchant.save()

    def tearDown(self):
        self.user_shopper.delete()
        self.user_merchant.delete()

    def test_shopper_creation(self):
        shopper = CustomUser.objects.get(first_name='Tope')
        self.assertEqual(shopper.first_name, 'Tope')

    def test_merchant_creation(self):
        merchant = CustomUser.objects.get(name='Welz Inc')
        self.assertEqual(merchant.name, 'Welz Inc')


class TestViews(TestCustomUser, TestCase):

    def test_shopper_signup_view(self):
        url=reverse('register_user')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)

    def test_merchant_signup_view(self):
        url = reverse('register_merchant')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)

    def test_edit_merchant_profile_view(self):
        self.client.login(email='w@nomugu.com',password='test123')
        url = reverse('edit_merchant_profile')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code,200)

    def test_edit_shopper_profile_view(self):
        self.client.login(email='t@nomugu.com',password='test123')
        url = reverse('edit_shopper_profile')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code,200)

    def test_change_merchant_password_view(self):
        self.client.login(email='w@nomugu.com', password='test123')
        url = reverse('change_shopper_password')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code,200)

    def test_change_shopper_password_view(self):
        self.client.login(email='t@nomugu.com', password='test123')
        url = reverse('change_shopper_password')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code,200)

    def test_shopper_profile_view(self):
        self.client.login(email='t@nomugu.com', password='test123')
        url = reverse('shopper_profile')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code,200)

    def test_merchant_profile_view(self):
        self.client.login(email='w@nomugu.com', password='test123')
        url = reverse('merchant_profile')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code,200)

    def test_login_merchant_view(self):
        url = reverse('login_merchant')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code,200)

    def test_login_shopper_view(self):
        url = reverse('login')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code,200)


class TestSignIn(TestCustomUser, TestCase):
    def shopper_login(self):
        user = authenticate(email= 't@nomugu.com',password= 'test123')
        self.assertTrue((user is not None) and user.is_authenticated)

    def shopper_invalid_login(self):
        user = authenticate(email= 't@nomugu.com',password= 'test12')
        self.assertFalse((user is not None) and user.is_authenticated)

    def merchant_login(self):
        user = authenticate(email= 'w@nomugu.com',password= 'test123')
        self.assertTrue((user is not None) and user.is_authenticated)

    def merchant_invalid_login(self):
        user = authenticate(email= 'w@nomugu.com',password= 'test12')
        self.assertFalse((user is not None) and user.is_authenticated)


class TestEditForm(TestCustomUser,TestCase):
    def test_shopper_edit_form(self):
        self.client.login(email='t@nomugu.com',password='test123')
        data = {'first_name': self.user_shopper.first_name,
                'last_name': self.user_shopper.last_name,
                'email': self.user_shopper.email,
                'telephone': '08167847268',
                'password1': 'test123',
                }
        url = reverse('edit_shopper_profile')
        resp = self.client.post(url,data)
        self.assertEqual(resp.status_code,200)

    def test_merchant_edit_form(self):
        self.client.login(email='w@nomugu.com', password='test123')
        user = self.user_merchant
        data= { 'name': user.name,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email,
                'address': user.address,
                'state': user.state,
                'country': 'Ghana',
                'telephone': user.telephone,
                'password1': 'test123',
                'is_merchant': user.is_merchant
                }

        url = reverse('edit_merchant_profile')
        resp = self.client.post(url, data)
        self.assertEqual(resp.status_code, 200)


class TestSignUpForm(TestCase):

    def test_shopper_signup_form(self):
        data = {'email': 't@nomugu.com',
                'first_name': 'Tope',
                'last_name': 'Shols',
                'telephone': '08167847286',
                'password1': 'test123',
                'password2': 'test123',
                'is_shopper': True
                }

        form = shopper_signupform(data=data)
        self.assertTrue(form.is_valid())

    def test_merchant_signup_form(self):
        data = {'name': 'Welz Inc',
                'first_name': 'Tope',
                'last_name': 'Shols',
                'email': 'a@nomugu.com',
                'address': '1,Abiona',
                'state': 'Lagos',
                'country': 'Nigeria',
                'telephone': '08167847286',
                'is_merchant': True,
                'password1': 'test123',
                'password2': 'test123'
                }
        form = merchant_signupform(data=data)
        self.assertTrue(form.is_valid())