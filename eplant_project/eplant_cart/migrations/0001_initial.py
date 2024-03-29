# Generated by Django 4.1.5 on 2023-05-08 16:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('eplant_home', '0003_alter_shop_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_id', models.CharField(max_length=200, unique=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eplant_cart.cartlist')),
                ('prod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eplant_home.product')),
            ],
        ),
    ]
