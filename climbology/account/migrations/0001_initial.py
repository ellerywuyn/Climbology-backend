# Generated by Django 4.2.7 on 2023-12-08 02:03

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
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(blank=True, max_length=50)),
                ('height', models.FloatField(blank=True, null=True)),
                ('weight', models.FloatField(blank=True, null=True)),
                ('wingspan', models.FloatField(blank=True, null=True)),
                ('ape_index', models.FloatField(blank=True, null=True)),
                ('num_pull_ups', models.IntegerField(blank=True, null=True)),
                ('num_chin_ups', models.IntegerField(blank=True, null=True)),
                ('num_push_ups', models.IntegerField(blank=True, null=True)),
                ('climbing_style', models.CharField(blank=True, max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
