from django.urls import path, include, reverse_lazy
from . import views
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    path('', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('profile/<int:pk>/', views.ProfileView.as_view(), name='profile'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    # change password urls
    path('password_change/', auth_views.PasswordChangeView.as_view(),
         name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(),
         name='password_change_done'),
    # reset password urls
    path('password_reset/', auth_views.PasswordResetView.as_view(
        success_url=reverse_lazy('accounts:password_reset_done')
    ),
        name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        success_url=reverse_lazy('accounts:password_reset_complete')
    ),
        name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
    path('register/', views.register, name='register'),

]
