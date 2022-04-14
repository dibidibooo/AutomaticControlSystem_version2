from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import DetailView

from accounts.forms import ProfileForm, ProfileEditForm
from accounts.models import Profile


# class ProfileCreateView(PermissionRequiredMixin, CreateView):
#     model = get_user_model()
#     template_name = 'account/users-list.html'
#     context_object_name = 'user_obj'
#     form_class = ProfileForm
#     permission_required = 'add_user'
#
#     def get_context_data(self, **kwargs):
#         users = User.objects.order_by('id')
#         p = Paginator(users, 8)
#         page = self.request.GET.get('page')
#         if p == None:
#             page = int(1)
#         page_obj = p.get_page(page)
#         context = super().get_context_data(**kwargs)
#         context['heading'] = "Новый пользователь"
#         context['pageview'] = "Пользователи"
#         context['users'] = users
#         context['page_obj'] = page_obj
#         return context
#
#     def form_valid(self, form, edit_form):
#         print(self.request.POST)
#         phone = form.cleaned_data.get('phone')
#         position = form.cleaned_data.get('position')
#         role = form.cleaned_data.get('role')
#         user = form.save()
#         Profile.objects.create(
#             user=user,
#             phone=phone,
#             position=position,
#             role=role
#         )
#
#         if "editprofile" in self.request.POST:
#             id = self.request.POST['id']
#             first_name = edit_form.cleaned_data['first_name']
#             last_name = edit_form.cleaned_data['last_name']
#             phone = edit_form.cleaned_data['phone']
#             position = edit_form.cleaned_data['position']
#             role = edit_form.cleaned_data['role']
#             page_number = self.request.POST['page_number']
#
#             user = User.objects.filter(id=id)
#             user.update(first_name=first_name, last_name=last_name)
#             profile = Profile.objects.get(user_id=id)
#             profile.phone = phone
#             profile.position = position
#             profile.role_id = role
#             profile.save()
#             return redirect('accounts-users')
#         return redirect('accounts-users')
#
#     def form_invalid(self, form):
#         return self.render_to_response(self.get_context_data(form=form, data=self.request.POST))


class ProfileDetailView(DetailView):
    model = get_user_model()
    template_name = 'account/detail.html'
    context_object_name = 'user_obj'
    success_url = 'accounts-users'
    form_class = ProfileEditForm


class ProfileView(PermissionRequiredMixin, View):
    permission_required = 'add_user'

    def get(self, request):
        users = User.objects.order_by('id')
        p = Paginator(users, 8)
        page = request.GET.get('page')
        if p == None:
            page = int(1)
        page_obj = p.get_page(page)
        context = {}
        context['heading'] = "Новый пользователь"
        context['pageview'] = "Пользователи"
        context['users'] = users
        context['page_obj'] = page_obj
        context['form'] = ProfileForm()
        if request.GET.get('userid'):
            pk = request.GET.get('userid')
            user_object = User.objects.get(pk=pk)
            context['user_object'] = user_object
        return render(request, 'account/users-list.html', context)

    def post(self, request):
        if request.method == "POST":
            if "addprofile" in request.POST:
                phone = request.POST['phone']
                position = request.POST['position']
                role = request.POST['role']
                page_number = request.POST['page_number']
                form = ProfileForm(request.POST)
                user = form.save()

                Profile.objects.create(
                    user_id=user.pk,
                    phone=phone,
                    position=position,
                    role_id=role
                )
                return redirect('accounts-users')
            if "editprofile" in request.POST:
                id = request.POST['id']
                first_name = request.POST['first_name']
                last_name = request.POST['last_name']
                phone = request.POST['phone']
                position = request.POST['position']
                role = request.POST['role']
                page_number = request.POST['page_number']

                user = User.objects.filter(id=id)
                user.update(first_name=first_name, last_name=last_name)
                profile = Profile.objects.get(user_id=id)
                profile.phone = phone
                profile.position = position
                profile.role_id = role
                profile.save()
                return redirect('accounts-users')
            if "deleteCustomer" in request.POST:
                print(111)
                id = request.POST['id']
                print(id)
                obj = User.objects.filter(id=id).first()
                print(obj)
                obj.delete()
                return HttpResponse()
            return redirect('accounts-users')
