# Generated by Django 4.2.1 on 2023-06-09 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_alter_task_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1999-12-21'),
            preserve_default=False,
        ),
    ]
