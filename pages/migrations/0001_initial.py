# Generated by Django 4.0.4 on 2022-05-18 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lab',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Laboratory_ID', models.IntegerField(max_length=7)),
                ('Laboratory_Name', models.CharField(max_length=20)),
                ('Laboratory_Number', models.IntegerField(max_length=3)),
                ('Floor_Number', models.IntegerField(max_length=2)),
                ('NumOfPcs', models.IntegerField(max_length=2)),
                ('LabCapacity', models.IntegerField(max_length=3)),
                ('NumOfChairs', models.IntegerField(max_length=3)),
                ('LabStatus', models.CharField(max_length=18)),
            ],
        ),
    ]
