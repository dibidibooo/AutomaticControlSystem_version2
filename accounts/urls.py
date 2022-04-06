from django.urls import path

from .views import ProfileCreateView

urlpatterns = [
    path('users', ProfileCreateView.as_view(), name='accounts-users'),
]
