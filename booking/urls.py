from django.urls import path
from . import views

app_name = 'booking'

urlpatterns = [
    path('add/<int:house_id>/<str:username>/',
         views.booking_add, name='booking_add'),
    path('delete/<int:pk>/', views.BookedHouseDelete.as_view(),
         name='booking_delete'),
]
