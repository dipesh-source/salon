# Generated by Django 4.0.1 on 2022-03-25 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0005_purchase_pro_name_alter_purchase_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='my_package',
            name='find',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
