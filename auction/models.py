from django.db import models
from django.utils.translation import gettext_lazy as _

from houses.models import House

import datetime


class AuctionSession(models.Model):
    house = models.OneToOneField(House, on_delete=models.CASCADE)
    title = models.CharField(max_length=60)
    description = models.TextField()
    start = models.DateTimeField()
    end = models.DateTimeField()

    def save(self, *args, **kwargs):
        self.title, self.description = 'Auction for House: {} at {}'.format(
            self.house.pk, self.house.address), self.house.description
        super(AuctionSession, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def finished(self):
        return self.end < datetime.datetime.now()

    def in_progress(self):
        return self.end > datetime.datetime.now() and self.start < datetime.datetime.now()

    def future(self):
        return self.start > datetime.datetime.now()

    def status(self):
        if self.end < datetime.datetime.now():
            return _("Finished")
        if self.end > datetime.datetime.now() and self.start < datetime.datetime.now():
            return _("In Progress")
        if self.start > datetime.datetime.now():
            return _("Future")

    def count_lots(self):
        return self.lot_set.all().count()

    # def get_bidding_url(self):
    #     return ("bidding.views.bidding_auctions", (self.pk,))
