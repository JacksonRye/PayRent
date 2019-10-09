from django.urls import path
from . import views


app_name = 'auction'

urlpatterns = [
    path('auction_add/', views.AuctionAddView.as_view(), name='auction_add'),
    path('auction_details/<int:pk>/', views.AuctionDetailView.as_view(), name='auction_details'),
    path('auction_list/', views.AuctionListView.as_view(), name='auction_list'),
]