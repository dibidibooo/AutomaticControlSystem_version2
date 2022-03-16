from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class UserGridView(LoginRequiredMixin,View):
    def get(self , request):
        context = {
            'heading':"User Grid",
            'pageview':"Contacts",
        }
        return render (request,'contacts/usergrid.html',context)

class UserListView(LoginRequiredMixin,View):
    def get(self , request):
        context = {
            'heading':"User List",
            'pageview':"Contacts",
        }
        return render (request,'contacts/userlist.html',context)

class ProfileView(LoginRequiredMixin,View):
    def get(self , request):
        context = {
            'heading':"Profile",
            'pageview':"Contacts",
        }
        return render (request,'contacts/profile.html',context)