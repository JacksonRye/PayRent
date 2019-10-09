from django.test import TestCase
from django.urls import reverse
from accounts.models import Profile, User
from accounts.forms import UserRegistrationForm
from unittest import skip


class UserRegistrationFormTest(TestCase):

    @classmethod
    def setUpTestData(self):
        testuser1 = User.objects.create_user(
            username='testuser1', password='DJANGO13')
        Profile.objects.create(user=testuser1)

    def test_false_user_type(self):
        form = UserRegistrationForm(data={
            'account_type': 'false_user',
            'username': 'testuser1',
            'password': 'DJANGO13',
            'password2': 'DJANGO13',
            'first_name': 'test',
            'last_name': 'user',
            'email': 'testuser@django.com'
        })

        self.assertFalse(form.is_valid())

    def test_clean_password_wrong(self):
        form = UserRegistrationForm(data={
            'account_type': 'landlord',
            'username': 'testuser1',
            'password': 'DJANGO13',
            'password2': 'DJANGO11',
            'first_name': 'test',
            'last_name': 'user',
            'email': 'testuser@django.com'
        })

        self.assertFalse(form.is_valid())

    @skip("Django takes care")
    def test_clean_password_correct(self):
        form = UserRegistrationForm(data={
            'account_type': 'landlord',
            'username': 'testuser1',
            'password': 'DJANGO13',
            'password2': 'DJANGO13',
            'first_name': 'test',
            'last_name': 'user',
            'email': 'testuser@django.com'
        })

        self.assertTrue(form.is_valid())


