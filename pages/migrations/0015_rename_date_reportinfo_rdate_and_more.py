# Generated by Django 4.0.4 on 2022-05-24 17:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0014_alter_addlab_labstatus'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reportinfo',
            old_name='Date',
            new_name='RDate',
        ),
        migrations.RenameField(
            model_name='reportinfo',
            old_name='Description',
            new_name='RDescription',
        ),
        migrations.RenameField(
            model_name='reportinfo',
            old_name='Laboratory_ID',
            new_name='RLaboratory_ID',
        ),
        migrations.RenameField(
            model_name='reportinfo',
            old_name='PcNum',
            new_name='RPcNum',
        ),
        migrations.RenameField(
            model_name='reportinfo',
            old_name='ProblemType',
            new_name='RProblemType',
        ),
    ]
