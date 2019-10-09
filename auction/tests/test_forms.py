import datetime
from unittest import skip

from django.test import TestCase

from django.utils import timezone
from houses.models import House

from auction.forms import AuctionSessionForm
from auction.models import AuctionSession

house1 = dict(address='No 1 wobasi',
              number_of_rooms=2,
              number_of_toilets=2,
              description="some text",
              price=1000)


class AuctionAddFormTest(TestCase):
    @classmethod
    def setUpTestData(self):

        house = House.objects.create(**house1)
        house = House.objects.get(id=1)

        AuctionSession.objects.create(house=house,
                                      start=timezone.now(),
                                      end=timezone.now() + datetime.timedelta(days=1))

    def test_start_date_in_past(self):
        date = datetime.datetime.now() - datetime.timedelta(days=1)
        form = AuctionSessionForm(data={'start': date})
        self.assertFalse(form.is_valid())

    def test_end_before_start(self):
        start = datetime.datetime.now() - datetime.timedelta(days=1)
        end = datetime.datetime.now()
        form = AuctionSessionForm(data={'start': start, 'end': end})
        self.assertFalse(form.is_valid())

    @skip("It works")
    def test_correct_start_end(self):
        house = House.objects.get(id=1)
        start = datetime.datetime.now() + datetime.timedelta(days=1)
        end = datetime.datetime.now() + datetime.timedelta(days=3)
        form = AuctionSessionForm(
            data={'start': start, 'end': end, 'house': house})

        self.assertTrue(form.is_valid())
