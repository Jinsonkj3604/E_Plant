# Generated by Django 4.1.5 on 2023-05-29 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eplant_cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]