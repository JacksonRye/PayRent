from django.shortcuts import render
from .models import BookedHouses
from django.views.decorators.http import require_POST
from django.shortcuts import redirect
from houses.models import House
from accounts.models import Profile
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView


@require_POST
def booking_add(request, house_id, username):

    house = House.objects.get(id=house_id)

    house.booked = True

    house.save()

    user = User.objects.get(username=username)

    user = Profile.objects.get(user=user)

    BookedHouses.objects.create(house=house, booked_by=user)

    return redirect('houses:house_list')


class BookedHouseDelete(DeleteView):

    model = BookedHouses
    success_url = reverse_lazy('accounts:dashboard')
