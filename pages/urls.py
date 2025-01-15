from django.urls import path
from .views import homeview, loginview, signupview, logoutview, profileview, password_change, forgot_password_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', homeview, name='home'),
    path('login/', loginview, name='login'),
    path('signup/', signupview, name='signup'),
    path('logout/', logoutview, name='logout'),
    path('profile/', profileview, name='profile'),
    path('change-password/', password_change, name='change_password'),
    path('forgot-password/', forgot_password_view, name='forgot_password'),

    path('password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),



]