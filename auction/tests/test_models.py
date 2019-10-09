import datetime
from auction.models import AuctionSession
from django.test import TestCase
from houses.models import House
from .test_forms import house1
from django.utils import timezone


class AuctionSessionTest(TestCase):

    def setUp(self):
        houseA = House.objects.create(**house1)
        AuctionSession.objects.create(house=houseA,
                                      start=timezone.now(),
                                      end=timezone.now() + datetime.timedelta(days=1))

    def test_finished(self):
        auction1 = AuctionSession.objects.get(id=1)
        auction1.start = timezone.now() - datetime.timedelta(days=1)
        auction1.end = timezone.now()

        auction1.save()

        self.assertTrue(auction1.start < auction1.end)

    def test_in_progress(self):
        auction1 = AuctionSession.objects.get(id=1)
        auction1.start = timezone.now() - datetime.timedelta(days=1)
        auction1.end = timezone.now() + datetime.timedelta(days=1)

        self.assertTrue(auction1.end > timezone.now()
                        and auction1.start < timezone.now())


    def test_future(self):
        auction1 = AuctionSession.objects.get(id=1)
        auction1.start = timezone.now() + datetime.timedelta(days=1)

        self.assertTrue(auction1.start > timezone.now())