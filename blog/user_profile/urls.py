from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

app_name='user_profile'

urlpatterns = [
    path('', views.view_profile, name='view_profile'),
    path('reg/', views.view_reg, name='view_reg'),
    path('logout/',LogoutView.as_view(),name='logout')
]