# Generated by Django 4.2.17 on 2024-12-24 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_alter_todolist_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='attachement',
            field=models.FileField(null=True, upload_to='public'),
        ),
    ]