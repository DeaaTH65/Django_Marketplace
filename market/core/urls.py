from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import LoginForm



urlpatterns = [
    path('', views.index, name='home'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/<str:pk>', views.profile, name='profile'),
    path('update_profile/', views.update_profile, name='update_profile'),
]
