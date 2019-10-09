from houses.models import House
from django.test import TestCase

house1 = dict(address='No 1 wobasi',
              number_of_rooms=2,
              number_of_toilets=2,
              description="some text",
              price=1000)

house2 = dict(address='No 2 wobasi',
              number_of_rooms=3,
              number_of_toilets=2,
              description="No text",
              price=10000)


class HouseModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # set up non-modified objects used by all tests
        House.objects.create(**house1)

    def test_address_label(self):
        house = House.objects.get(id=1)
        field_label = house._meta.get_field('address').verbose_name
        self.assertEqual(field_label, 'address')

    def test_get_absolute_url(self):
        house = House.objects.get(id=1)

        self.assertEqual(house.get_absolute_url(), '/houses/detail/1/')
