from django.test import TestCase
from accounts.models import Profile, User
from django.urls import reverse


class DashBoardTest(TestCase):

    @classmethod
    def setUpTestData(self):
        testuser1 = User.objects.create_user(
            username='testuser1', password='DJANGO13')
        Profile.objects.create(user=testuser1, account_type='landlord')

    def test_view_uses_correct_template(self):
        login = self.client.login(username='testuser1', password='DJANGO13')
        response = self.client.get(reverse('accounts:dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'houses/list.html')

    def test_view_exists_at_desired_location(self):
        login = self.client.login(
            username='testuser1', password='DJANGO13')
        response = self.client.get('/dashboard/')

        self.assertEqual(response.status_code, 200)

    def test_view_accessible_by_name(self):
        login = self.client.login(
            username='testuser1', password='DJANGO13')
        response = self.client.get(reverse('accounts:dashboard'))

        self.assertEqual(response.status_code, 200)


class RegistrationTest(TestCase):

    @classmethod
    def setUpTestData(self):
        testuser1 = User.objects.create_user(
            username='testuser1', password='DJANGO13')
        Profile.objects.create(user=testuser1, account_type='landlord')

    def test_GET_uses_correct_template(self):
        response = self.client.get(reverse('accounts:register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/register.html')

    def test_POST_uses_correct_template(self):
        response = self.client.post(reverse('accounts:register'), {'account_type': 'landlord',
                                                                   'username': 'testuser1',
                                                                   'password': 'DJANGO13',
                                                                   'password2': 'DJANGO11',
                                                                   'first_name': 'test',
                                                                   'last_name': 'user',
                                                                   'email': 'testuser@django.com'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/register.html')

    def test_view_accessible_by_name(self):
        response = self.client.get(reverse('accounts:register'))
        self.assertEqual(response.status_code, 200)

    def test_view_exists_at_desired_location(self):
        response = self.client.get('/register/')
        self.assertEqual(response.status_code, 200)
