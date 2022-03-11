# from adminsortable.fields import SortableForeignKey
# from adminsortable.models import SortableMixin
# from django.contrib.auth import get_user_model
# from django.db import models
# from model_utils.models import TimeStampedModel
#
# User = get_user_model()
# # Create your models here.
# class Priority(models.TextChoices):
#     HIGH = "H", "High"
#     MEDIUM = "M", "Medium"
#     LOW = "L", "Low"
#
#
# class Task(SortableMixin, TimeStampedModel):
#     title = models.CharField(max_length=255)
#     description = models.TextField(blank=True)
#     assignees = models.ManyToManyField(User, related_name="tasks")
#     priority = models.CharField(
#         max_length=1, choices=Priority.choices, default=Priority.MEDIUM
#     )
#     task_order = models.PositiveIntegerField(default=0, editable=False, db_index=True)
#
#     def __str__(self):
#         return f"{self.id} - {self.title}"
#
#     class Meta:
#         ordering = ["task_order"]
#
#
# class Comment(TimeStampedModel):
#     task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="comments")
#     author = models.ForeignKey(User, on_delete=models.PROTECT, related_name="comments")
#     text = models.TextField()
#
#     class Meta:
#         ordering = ["created"]