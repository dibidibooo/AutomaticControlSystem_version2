from django.http import request
from django.shortcuts import redirect, render
from django.views import View   
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from allauth.account.views import PasswordSetView,PasswordChangeView
from django.urls import reverse_lazy

# utillity
class DashboardView(LoginRequiredMixin,View):
    def get(self, request):
        greeting = {}
        greeting['heading'] = "Dashboard"
        greeting['pageview'] = "Dashboards"        
        return render(request, 'dashboard/dashboard.html',greeting)


class SaasView(LoginRequiredMixin,View):
    def get(self,request):
        greeting = {}
        greeting['heading'] = "Saas"
        greeting['pageview'] = "Dashboards"
        return render (request,'dashboard/dashboard-saas.html',greeting)

class CryptoView(LoginRequiredMixin,View):
    def get(self,request):
        greeting = {}
        greeting['heading'] = "Crypto" 
        greeting['pageview'] = "Dashboards"
        return render (request,'dashboard/dashboard-crypto.html',greeting)

class BlogView(LoginRequiredMixin,View):
    def get(self,request):
        greeting = {}
        greeting['heading'] = "Blog" 
        greeting['pageview'] = "Dashboards"
        return render (request,'dashboard/dashboard-blog.html',greeting)

class CalendarView(LoginRequiredMixin,View):
    def get(self, request):
        greeting = {}
        greeting['heading'] = "TUI Calendar"
        greeting['pageview'] = "Calendars"
        return render (request, 'calendar.html',greeting)
class CalendarFullView(LoginRequiredMixin,View):
    def get(self, request):
        greeting = {}
        greeting['heading'] = "Full Calendar"
        greeting['pageview'] = "Calendars"
        return render (request, 'calendar-full.html',greeting)
class ChatView(LoginRequiredMixin,View):
    def get(self, request):
        greeting = {}
        greeting['heading'] = "Chat"
        greeting['pageview'] = "Apps"
        return render (request, 'chat-view.html',greeting)

class FileManagerView(LoginRequiredMixin,View):
    def get(self,request):
        greeting = {}
        greeting['heading'] = "File Manager"
        greeting['pageview'] = "Apps"
        return render (request,'filemanager.html',greeting)

# Authentication
class PagesLoginView(View):
    def get(self, request):
        return render(request, 'authentication/pages-login.html')
class PagesRegisterView(View):
    def get(self, request):
        return render(request, 'authentication/pages-register.html')
class PagesRecoverpwView(View):
    def get(self, request):
        return render(request, 'authentication/pages-recoverpw.html')
class PagesLockscreenView(View):
    def get(self, request):
        return render(request, 'authentication/pages-lockscreen.html')

class PagesConfirmmailView(View):
    def get(self, request):
        return render(request, 'authentication/pages-confirmmail.html')

class PagesEmailVerificationView(View):
    def get(self, request):
        return render(request, 'authentication/pages-emailverificationmail.html')

class PagesTwoStepVerificationView(View):
    def get(self, request):
        return render(request, 'authentication/pages-twostepverificationmail.html')
class PagesLogin2View(View):
    def get(self, request):
        return render(request, 'authentication/pages-login-2.html')
class PagesRegister2View(View):
    def get(self, request):
        return render(request, 'authentication/pages-register-2.html')
class PagesRecoverpw2View(View):
    def get(self, request):
        return render(request, 'authentication/pages-recoverpw2.html')
class PagesLockscreen2View(View):
    def get(self, request):
        return render(request, 'authentication/pages-lockscreen2.html')

class PagesConfirmmail2View(View):
    def get(self, request):
        return render(request, 'authentication/pages-confirmmail-2.html')

class PagesEmailVerification2View(View):
    def get(self, request):
        return render(request, 'authentication/pages-emailverificationmail-2.html')

class PagesTwoStepVerification2View(View):
    def get(self, request):
        return render(request, 'authentication/pages-twostepverificationmail-2.html')

class MyPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    success_url = reverse_lazy('dashboard')
class MyPasswordSetView(LoginRequiredMixin, PasswordSetView):
    success_url = reverse_lazy('dashboard')