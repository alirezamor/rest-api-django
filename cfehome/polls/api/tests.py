from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model


User = get_user_model()


class BlogPostApiTestCase(APITestCase):
    def setUp(self):
      user = User(username='testcfeUser', email='test@test.com')
      user.set_password("somerandompassword")
