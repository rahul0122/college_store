# Generated by Django 4.0.6 on 2022-10-17 07:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmsapp', '0003_alter_person_address_alter_person_date_of_birth_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='City',
            new_name='Course',
        ),
        migrations.RenameModel(
            old_name='Country',
            new_name='Department',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='country',
            new_name='department',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='city',
            new_name='course',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='country',
            new_name='department',
        ),
    ]
