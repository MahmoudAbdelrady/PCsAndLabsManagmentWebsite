# Generated by Django 4.0.4 on 2022-05-22 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0011_remove_addlab_labstatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='addlab',
            name='LabStatus',
            field=models.CharField(blank=True, max_length=18, null=True),
        ),
    ]