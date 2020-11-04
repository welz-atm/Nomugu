from django.test import TestCase
from django.urls import reverse
from authentication.models import CustomUser
from product.models import Product,Category


class TestProduct(TestCase):
    def setUp(self):
        self.merchant = CustomUser.objects.create_user(name='Welz Inc',first_name='Ay',last_name='Shols',
                                                       email='w@nomugu.com',address='1,Abiona Ikorodu',
                                                       state='Lagos',country='Nigeria',telephone='08167847286',
                                                       password='test123',is_merchant=True)
        self.category = Category.objects.create(name='Computers/Laptops')
        self.product = Product.objects.create(title='HP 15 Laptop- Intel Core I3- 1TB HDD- 6GB RAM- Windows 10- HD 620- 2.4GHz',
                                              name='Laptop',
                                              brand='HP',
                                              description='Beautifully made',
                                              color='Black',
                                              image='sample.png',
                                              price='198000',
                                              shipping='Free Shipping within lagos',
                                              quantity='8',
                                              category=self.category,
                                              merchant=self.merchant)


class TestAddProduct(TestProduct,TestCase):
    def test_add_product(self):
        product = Product.objects.get(name='Laptop')
        self.assertEqual(product.name,'Laptop')


class TestProductViews(TestProduct,TestCase):
    def test_my_product_view(self):
        self.client.login(email='w@nomugu.com',password='test123')
        url = reverse('my_product')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code,200)

    def test_edit_product(self):
        self.client.login(email='w@nomugu.com', password='test123')
        resp = self.client.get(reverse('edit_product',kwargs={'pk':self.product.pk}))
        self.assertEqual(resp.status_code, 200)

    def test_delete_product(self):
        self.client.login(email='w@nomugu.com', password='test123')
        url = reverse('delete_product',kwargs={'pk':self.product.pk})
        resp = self.client.delete(url)
        self.assertEqual(resp.status_code, 302)


class TestAddCategory(TestProduct,TestCase):
    def test_category_creation(self):
        self.client.login(username='w@nomugu.com',password='test123')
        url = reverse('create_category')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code,200)

    def test_edit_category(self):
        self.client.login(username='w@nomugu.com',password='test123')
        url=reverse('edit_category',kwargs={'pk':self.category.pk})
        resp=self.client.get(url)
        self.assertEqual(resp.status_code,200)

    def test_all_categories(self):
        self.client.login(username='w@nomugu.com',password='test123')
        url=reverse('all_categories')
        resp=self.client.get(url)
        self.assertEqual(resp.status_code,200)

    def test_delete_category(self):
        self.client.login(username='w@nomugu.com',password='test123')
        url=reverse('delete_category',kwargs={'pk': self.category.pk})
        resp=self.client.delete(url)
        self.assertEqual(resp.status_code,302)


class TestProductDetail(TestProduct,TestCase):
    def test_product_detail(self):
        url=reverse('detail',kwargs={'pk':self.product.id})
        resp=self.client.get(url)
        self.assertEqual(resp.status_code,200)


class TestAddProductForm(TestProduct,TestCase):
    def test_add_product_form(self):
        self.client.login(email='w@nomugu.com',password='test123')
        url = reverse('add_product')
        data = {
                 'title':'HP 15 Laptop- Intel Core I3- 1TB HDD- 6GB RAM- Windows 10- HD 620- 2.4GHz',
                 'name':'Laptop',
                 'brand':'HP',
                 'description':'Beautifully made',
                 'image':'sample.png',
                 'weight':20,
                 'price':'198000',
                 'shipping':'Free Shipping within lagos',
                 'quantity':'8',
                 'category': self.category,
                 'merchant': self.merchant
               }
        resp = self.client.post(url,data)
        self.assertEqual(resp.status_code,200)
