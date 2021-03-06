# Generated by Django 3.0 on 2021-04-10 09:08

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
            name='Complaintbox',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(max_length=100)),
                ('p_email', models.EmailField(max_length=50)),
                ('p_complaint', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='ImProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('impf', models.ImageField(default='profile.png', upload_to='Profiles/')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=10)),
                ('uid', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
