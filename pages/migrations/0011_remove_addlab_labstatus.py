# Generated by Django 4.0.4 on 2022-05-22 10:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0010_addlab_labstatus'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addlab',
            name='LabStatus',
        ),
    ]