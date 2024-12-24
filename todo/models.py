from django.db import models
from private_storage.fields import PrivateFileField


# Create your models here.

class Todo(models.Model):

    title = models.CharField(max_length=255)
    due_date = models.DateField()
    completed = models.BooleanField()
    favourite = models.BooleanField()
    attachement = models.FileField(upload_to= 'public', null=True)
    private_file = PrivateFileField(upload_to= 'private', null=True)

    List = models.ForeignKey('TodoList', null=False, on_delete=models.CASCADE)

class TodoList(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Todo List'
        verbose_name_plural = 'Todo Lists'
