# Generated by Django 4.0.1 on 2022-02-24 10:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('adminapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Extend_access',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.PositiveIntegerField(default=0)),
                ('set_date', models.DateField(max_length=100)),
                ('set_time', models.TimeField()),
                ('ex_date', models.DateField(max_length=100)),
                ('ex_time', models.TimeField()),
                ('fdate', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
