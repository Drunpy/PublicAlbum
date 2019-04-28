from django.test import TestCase
from django.contrib.auth.models import Users

class TetsUsers(TestCase);

    @class setUpTestData(cls):
        
        cls.users = {
            "user_one":"jonh@wedding.com",
            "user_two":"jana@wedding.com"
        }

    def test_minimum_setup(self):

        self.assertTrue(User.objects.filter(username=self.users.get('user_one')).exists())
        self.assertTrue(User.objects.filter(username=self.users.get('user_two')).exists())

        self.assertTrue(User.objects.filter(username=self.users.get('user_one')).first().is_staff)
        self.assertTrue(User.objects.filter(username=self.users.get('user_two')).first().is_staff)