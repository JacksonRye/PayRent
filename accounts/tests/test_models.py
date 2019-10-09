from django.test import TestCase
from django.contrib.auth.models import User
from accounts.models import Profile


class ProfileModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):

        for number, account_type in enumerate(['landlord', 'tenant', 'false_user']):
            User.objects.create_user(
                username=f'testuser{number}', password='DJANGO13')
            Profile.objects.create(user=User.objects.get(username=f'testuser{number}'), account_type=account_type
                                   )

    def test_false_account_type_fails(self):
        false_user = Profile.objects.get(id=3)
        self.assertNotIn(false_user.account_type, Profile.ACCOUNT_TYPES )
