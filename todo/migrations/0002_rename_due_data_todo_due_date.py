# Generated by Django 4.2.17 on 2024-12-16 14:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='due_data',
            new_name='due_date',
        ),
    ]
