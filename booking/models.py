from django.db import models
from houses.models import House
from accounts.models import Profile
from django.urls import reverse


class BookedHouses(models.Model):

    house = models.OneToOneField(House, on_delete=models.CASCADE, related_name='booked_house')
    booked_by = models.OneToOneField(
        Profile, on_delete=models.CASCADE, related_name='booked')

    def __str__(self):
        return 'House: {} booked by {}'.format(self.house, self.booked_by)

    # def get_absolute_url(self):
    #     return reverse('houses:house_detail', args=[self.house.pk])
