from django.urls import path

from .views import ProfileView

urlpatterns = [
    path('users', ProfileView.as_view(), name='accounts-users'),
]
