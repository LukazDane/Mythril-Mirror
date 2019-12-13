from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class LogInTest(TestCase):
    def setUp(self):
        User.objects.create(id=2, username='test1')
        User.objects.create(id=5, username='test2')
