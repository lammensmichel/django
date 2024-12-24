# Generated by Django 4.2.17 on 2024-12-24 09:31

from django.db import migrations
import private_storage.fields
import private_storage.storage.files


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_todo_attachement'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='private_file',
            field=private_storage.fields.PrivateFileField(null=True, storage=private_storage.storage.files.PrivateFileSystemStorage(), upload_to='private'),
        ),
    ]