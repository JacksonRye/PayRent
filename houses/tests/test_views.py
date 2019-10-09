from django.test import TestCase
from django.contrib.auth.models import User
from accounts.models import Profile
from django.shortcuts import reverse
from houses.models import House


class HouseListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # create 13 houses

        for house_id in range(13):
            House.objects.create(
                address=f'No {house_id} wobasi',
                number_of_rooms=house_id,
                number_of_toilets=house_id,
                description=f"some text  {house_id}",
                price=house_id
            )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/houses/list/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('houses:house_list'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('houses:house_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'houses/list.html')

    def test_list_all_houses(self):
        response = self.client.get(reverse('houses:house_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.context['house_list']) == 13)


class HouseDetailViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        house1 = dict(address='No 1 wobasi',
                      number_of_rooms=2,
                      number_of_toilets=2,
                      description="some text",
                      price=1000)

        

        House.objects.create(**house1)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('houses:house_detail', args=[1]))
        self.assertEqual(response.status_code, 200)

    def test_view_exists_at_correct_url(self):
        response = self.client.get('/houses/detail/1/')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_context(self):
        response = self.client.get(reverse('houses:house_detail', args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['house'], House)

    def test_view_uses_correct_template(self):
        response = self.client.get(
            reverse('houses:house_detail', args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'houses/detail.html')

class UploadHouseViewTest(TestCase):

    def setUp(self):

        test_user1 = User.objects.create_user(
            username='testuser1', password='DJANGO13')
        test_user2 = User.objects.create_user(
            username='testuser2', password='DJANGO13')

        Profile.objects.create(user=test_user1, account_type='landlord')
        Profile.objects.create(user=test_user2)

        test_user1.save()
        test_user2.save()

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('houses:upload_house'))
        self.assertRedirects(response, '/?next=/houses/upload_house/')

    def test_logged_in_uses_correct_template(self):
        login = self.client.login(username='testuser1', password='DJANGO13')
        response = self.client.get(reverse('houses:upload_house'))
        print(response.context)

        # Check our user is logged in
        self.assertEqual(str(response.context['user']), 'testuser1')
        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)

        # Check we used correct template
        self.assertTemplateUsed(response, 'houses/upload_form.html')

    def test_redirect_if_not_landlord(self):
        login = self.client.login(username='testuser2', password='DJANGO13')
        response = self.client.get(reverse('houses:upload_house'))

        self.assertEqual(response.status_code, 302)
