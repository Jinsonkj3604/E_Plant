# Generated by Django 4.1.5 on 2023-05-08 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eplant_home', '0002_product_category_product_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shop',
            options={'ordering': ('name',), 'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
    ]