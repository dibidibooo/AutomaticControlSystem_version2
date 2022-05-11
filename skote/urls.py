from django.contrib import admin
from django.urls import path, include
from skote import views
from .views import MyPasswordSetView, MyPasswordChangeView
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),

    # Dashboards View
    path('', views.DashboardView.as_view(), name='dashboard'),
    # Projects
    path('projects/', include('projects.urls')),
    # Tasks
    path('tasks/', include('tasks.urls')),
    # Authencation
    # path('authentication/',include('authentication.urls')),
    # Pages
    path('pages/', include('pages.urls')),
    # Allauth
    path('account/', include('allauth.urls')),
    path('auth-logout/', TemplateView.as_view(template_name="account/logout-success.html"), name='pages-logout'),
    path('auth-lockscreen/', TemplateView.as_view(template_name="account/lock-screen.html"), name='pages-lockscreen'),
    # Custum change password done page redirect
    path('accounts/password/change/', login_required(MyPasswordChangeView.as_view()), name="account_change_password"),
    # Custum set password done page redirect
    path('accounts/password/set/', login_required(MyPasswordSetView.as_view()), name="account_set_password"),
    path('accounts/', include('accounts.urls')),
    path('api/', include('project_api.urls')),
]
