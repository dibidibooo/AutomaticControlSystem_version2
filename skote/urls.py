from django.contrib import admin
from django.urls import path, include, re_path
from allauth.account import views as acc_views
from accounts.views import CustomLoginView
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
    # path('account/', include('allauth.urls')),
    path("account/signup/", acc_views.signup, name="account_signup"),
    path("account/logout/", acc_views.logout, name="account_logout"),
    path(
        "account/password/change/",
        acc_views.password_change,
        name="account_change_password",
    ),
    path("account/password/set/", acc_views.password_set, name="account_set_password"),
    path("inactive/", acc_views.account_inactive, name="account_inactive"),
    # E-mail
    path("account/email/", acc_views.email, name="account_email"),
    path(
        "account/confirm-email/",
        acc_views.email_verification_sent,
        name="account_email_verification_sent",
    ),
    re_path(
        r"^confirm-email/(?P<key>[-:\w]+)/$",
        acc_views.confirm_email,
        name="account_confirm_email",
    ),
    # password reset
    path("account/password/reset/", acc_views.password_reset, name="account_reset_password"),
    path(
        "account/password/reset/done/",
        acc_views.password_reset_done,
        name="account_reset_password_done",
    ),
    re_path(
        r"^password/reset/key/(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)/$",
        acc_views.password_reset_from_key,
        name="account_reset_password_from_key",
    ),
    path(
        "account/password/reset/key/done/",
        acc_views.password_reset_from_key_done,
        name="account_reset_password_from_key_done",
    ),
    path('account/login/', CustomLoginView.as_view(), name='account_login'),
    path('auth-logout/', TemplateView.as_view(template_name="account/logout-success.html"), name='pages-logout'),
    # Custum change password done page redirect
    path('accounts/password/change/', login_required(MyPasswordChangeView.as_view()), name="account_change_password"),
    # Custum set password done page redirect
    path('accounts/password/set/', login_required(MyPasswordSetView.as_view()), name="account_set_password"),
    path('accounts/', include('accounts.urls')),
    path('api/', include('project_api.urls')),
]
