# Generated by Django 2.1.7 on 2019-04-17 04:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FBID', models.CharField(blank=True, max_length=50, null=True)),
                ('FullName', models.CharField(blank=True, max_length=100, null=True)),
                ('SchoolEmail', models.EmailField(blank=True, max_length=254, null=True)),
                ('ContactEmail', models.EmailField(blank=True, max_length=254, null=True)),
                ('PhoneNum', models.CharField(blank=True, max_length=20, null=True)),
                ('Gender', models.CharField(blank=True, max_length=20, null=True)),
                ('DOB', models.DateField(blank=True, null=True)),
                ('SchoolName', models.CharField(blank=True, max_length=50, null=True)),
                ('ProfilePic', models.BinaryField(blank=True, null=True)),
                ('EduVerified', models.BooleanField(blank=True, default=False, null=True)),
                ('EduVerifyTime', models.DateTimeField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
