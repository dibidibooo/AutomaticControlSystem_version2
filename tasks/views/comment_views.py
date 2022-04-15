from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import CreateView

from ..forms import CommentForm
from ..models import Comment, Task


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comments/create.html'

    def form_valid(self, form):
        task = get_object_or_404(Task, pk=self.kwargs.get('pk'))
        form.instance.task = task
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_redirect_url(self):
        return reverse('tasks-kanbanboard')


class CommentDetailView(View):
    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        task_pk = kwargs.get('task_pk')
        if form.is_valid():
            task = get_object_or_404(Task, pk=task_pk)
            task.comments.create(
                text=request.POST.get("text"),
                author=self.request.user,
            )
        return redirect('tasks-kanbanboard')