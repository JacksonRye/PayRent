from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render, reverse
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView

from accounts.models import Profile

from .forms import HouseUploadForm
from .models import House, HouseImage


class HouseListView(LoginRequiredMixin, ListView):
    context_object_name = 'house_list'
    template_name = 'houses/list.html'
    queryset = House.objects.all()


class HouseDetailView(LoginRequiredMixin, DetailView):
    model = House
    template_name = 'houses/detail.html'
    context_object_name = 'house'

    def post(self, request, *args, **kwargs):
        super(HouseDetailView, self).post(*args, **kwargs)


def has_profile(user):
    return (Profile.objects.filter(user=user).exists() and user.profile.account_type == 'landlord')


@method_decorator(user_passes_test(has_profile), name='dispatch')
class UploadHouseView(LoginRequiredMixin, CreateView):
    model = House
    form_class = HouseUploadForm
    exclude = ('pub_date', 'slug', 'booked')
    template_name = 'houses/upload_form.html'
    context_object_name = 'new_house'

    def get_success_url(self):
        return reverse('houses:upload_success', args=[self.object.id])

    def form_valid(self, form):
        self.object = form.save()
        HouseImage.objects.create(house=self.object,
                                  image=self.request.FILES['images'])
        return super().form_valid(form)


def upload_success(request, new_house_id):

    new_house = get_object_or_404(House, id=new_house_id)

    return render(request, 'houses/upload_success.html', {'new_house': new_house})
