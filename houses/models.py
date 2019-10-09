from django.db import models
from django.urls import reverse


class House(models.Model):
    address = models.TextField()
    number_of_rooms = models.PositiveSmallIntegerField(default=1)
    number_of_toilets = models.PositiveSmallIntegerField(default=0)
    description = models.TextField()
    price = models.PositiveIntegerField()
    pub_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.address

    def get_absolute_url(self):
        return reverse('houses:house_detail', args=[self.pk])


class HouseImage(models.Model):
    house = models.ForeignKey(
        House, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(blank=True, upload_to='photo/%Y/%m/%d')

    def __str__(self):
        return 'Image for {}'.format(self.house.address)
