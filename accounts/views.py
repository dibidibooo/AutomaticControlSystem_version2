from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import redirect
from django.views.generic import CreateView

from accounts.forms import ProfileForm
from accounts.models import Profile


class ProfileCreateView(PermissionRequiredMixin, CreateView):
    model = get_user_model()
    template_name = 'account/users-list.html'
    context_object_name = 'user_obj'
    form_class = ProfileForm
    permission_required = 'add_user'

    def get_context_data(self, **kwargs):
        users = User.objects.order_by('id')
        p = Paginator(users, 8)
        page = self.request.GET.get('page')
        if p == None:
            page = int(1)
        page_obj = p.get_page(page)
        context = super().get_context_data(**kwargs)
        context['heading'] = "Новый пользователь"
        context['pageview'] = "Пользователи"
        context['users'] = users
        context['page_obj'] = page_obj
        return context

    def form_valid(self, form):
        phone = form.cleaned_data.get('phone')
        position = form.cleaned_data.get('position')
        role = form.cleaned_data.get('role')
        user = form.save()
        Profile.objects.create(
            user=user,
            phone=phone,
            position=position,
            role=role
        )
        return redirect('accounts-users')

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form, data=self.request.POST))