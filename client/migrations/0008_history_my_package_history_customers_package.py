# Generated by Django 4.0.1 on 2022-04-01 14:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('client', '0007_alter_my_package_find'),
    ]

    operations = [
        migrations.CreateModel(
            name='History_my_package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cust', models.CharField(blank=True, max_length=100, null=True)),
                ('fack', models.CharField(blank=True, max_length=100, null=True)),
                ('service', models.CharField(max_length=100)),
                ('qty', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('price', models.PositiveBigIntegerField()),
                ('special', models.PositiveIntegerField(blank=True, null=True)),
                ('find', models.BooleanField(blank=True, default=True, null=True)),
                ('fdate', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='History_customers_package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pk_name', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('contact', models.PositiveBigIntegerField()),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('advance', models.PositiveIntegerField(blank=True, null=True)),
                ('total', models.PositiveIntegerField(blank=True, null=True)),
                ('fdate', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
