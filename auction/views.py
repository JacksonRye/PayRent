from django.shortcuts import reverse
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import AuctionSessionForm
from .models import AuctionSession


class AuctionListView(ListView):

    model = AuctionSession
    template_name = "auction/auction_list.html"
    context_object_name = "auction_list"


class AuctionAddView(LoginRequiredMixin, CreateView):
    template_name = "auction/auction_add.html"
    form_class = AuctionSessionForm

    def get_success_url(self):
        return reverse('auction:auction_add')


class AuctionDetailView(LoginRequiredMixin, DetailView):
    model = AuctionSession
    template_name = "auction/auction_detail.html"
    context_object_name = "auction"
