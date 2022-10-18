# Generated by Django 4.0.6 on 2022-10-17 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsapp', '0002_alter_person_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='address',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='person',
            name='date_of_birth',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10),
        ),
        migrations.AlterField(
            model_name='person',
            name='mail_id',
            field=models.EmailField(max_length=200),
        ),
    ]
