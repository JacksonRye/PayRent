from django.urls import path

from . import views

app_name = 'houses'

urlpatterns = [
    # path('upload_house/', views.upload_house, name='upload_house'),
    path('upload_house/', views.UploadHouseView.as_view(), name='upload_house'),

    # path('upload_house/<int:pk>/', views.UploadHouse.as_view(), name='upload_house'),
    path('upload_success/<int:new_house_id>/', views.upload_success, name='upload_success'),
    path('list/', views.HouseListView.as_view(), name='house_list'),
    path('detail/<int:pk>/', views.HouseDetailView.as_view(), name='house_detail'),
]
