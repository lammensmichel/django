# Generated by Django 4.2.17 on 2024-12-16 20:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_rename_due_data_todo_due_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todolist',
            options={'verbose_name': 'Todo List', 'verbose_name_plural': 'Todo Lists'},
        ),
    ]
