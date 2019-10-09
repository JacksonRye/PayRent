from django.test import TestCase
from auction.models import AuctionSession
from houses.models import House
from django.utils import timezone
import datetime
from django.urls import reverse
from django.contrib.auth.models import User
from accounts.models import Profile


class AuctionListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):

        # create 13 Auction session

        for id in range(13):
            house = House.objects.create(
                address=f'No {id} wobasi',
                number_of_rooms=id,
                number_of_toilets=id,
                description=f"some text  {id}",
                price=id)

            AuctionSession.objects.create(house=house,
                                          start=timezone.now(),
                                          end=timezone.now() + datetime.timedelta(days=1))

    def test_list_all_auctions(self):
        response = self.client.get(reverse('auction:auction_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.context['auction_list']) == 13)

    def test_view_exists_at_desired_location(self):
        response = self.client.get('/auction/auction_list/')
        self.assertEqual(response.status_code, 200)

    def test_view_accessible_by_name(self):
        response = self.client.get(reverse('auction:auction_list'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('auction:auction_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'auction/auction_list.html')


class AuctionAddViewTest(TestCase):

    def setUp(self):
        house = House.objects.create(
            address=f'No 1 wobasi',
            number_of_rooms=10,
            number_of_toilets=2,
            description=f"some text",
            price=1000)

        AuctionSession.objects.create(house=house,
                                      start=timezone.now(),
                                      end=timezone.now() + datetime.timedelta(days=1))

        testuser1 = User.objects.create_user(
            username='testuser1', password='DJANGO13')
        Profile.objects.create(user=testuser1,
                               account_type='tenant')

    def test_url_accessible_by_name(self):
        self.client.login(username='testuser1', password='DJANGO13')
        # user1 = Profile.objects.get(id=1)
        response = self.client.get(reverse('auction:auction_add'))
        self.assertEqual(response.status_code, 200)

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('auction:auction_add'))
        self.assertRedirects(response, '/?next=/auction/auction_add/')

    def test_url_in_correct_location(self):
        self.client.login(username='testuser1', password='DJANGO13')

        response = self.client.get('/auction/auction_add/')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        self.client.login(username='testuser1', password='DJANGO13')
        response = self.client.get(reverse('auction:auction_add'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'auction/auction_add.html')


class AuctionDetailViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):

        house = House.objects.create(
            address=f'No 1 wobasi',
            number_of_rooms=10,
            number_of_toilets=2,
            description=f"some text",
            price=1000)

        AuctionSession.objects.create(house=house,
                                      start=timezone.now(),
                                      end=timezone.now() + datetime.timedelta(days=1))

        testuser1 = User.objects.create_user(
            username='testuser1', password='DJANGO13')
        Profile.objects.create(user=testuser1,
                               account_type='tenant')

    def test_view_accessible_by_name(self):
        self.client.login(username='testuser1', password='DJANGO13')
        response = self.client.get(reverse('auction:auction_details', args=[1]))
        self.assertEqual(response.status_code, 200)


    def test_view_exists_at_desired_location(self):
        self.client.login(username='testuser1', password='DJANGO13')
        response = self.client.get('/auction/auction_details/1/')
        self.assertEqual(response.status_code, 200)

    def test_view_redirects_when_not_logged_in(self):
        response = self.client.get(reverse('auction:auction_details', args=[1]))
        self.assertRedirects(response, '/?next=/auction/auction_details/1/')

    def test_view_uses_correct_context(self):
        self.client.login(username='testuser1', password='DJANGO13')
        response = self.client.get(reverse('auction:auction_details', args=[1]))
        self.assertIsInstance(response.context['auction'], AuctionSession)

    def test_view_uses_correct_template(self):
        self.client.login(username='testuser1', password='DJANGO13')
        response = self.client.get(reverse('auction:auction_details', args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'auction/auction_detail.html')

