# Generated by Django 2.1.5 on 2019-02-21 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='Car',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='ContactEmail',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='CreationTime',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='DOB',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='EduVerified',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='EduVerifyTime',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='FBID',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='Gender',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='PhoneNum',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='ProfilePic',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='SchoolEmail',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='SchoolName',
        ),
    ]
