from django.urls import path

from .views import ProfileView, ProfileDetailView

urlpatterns = [
    path('users', ProfileView.as_view(), name='accounts-users'),
    path('user/<int:pk>/update', ProfileDetailView.as_view(), name='accounts-update'),
]
