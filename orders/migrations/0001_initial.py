# Generated by Django 5.2.4 on 2025-07-28 13:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('customer_name', models.CharField(max_length=255)),
                ('customer_phone', models.CharField(max_length=20)),
                ('customer_address', models.TextField()),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_method', models.CharField(choices=[('COD', 'Cod'), ('BANK_TRANSFER', 'Bank Transfer'), ('CREDIT_CARD', 'Credit Card')], default='COD', max_length=255)),
                ('order_status', models.CharField(choices=[('PENDING', 'Pending'), ('CONFIRMED', 'Confirmed'), ('PROCESSING', 'Processing'), ('SHIPPED', 'Shipped'), ('DELIVERED', 'Delivered'), ('CANCELLED', 'Cancelled')], default='PENDING', max_length=255)),
                ('ordered_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='orders', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'orders',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('quantity', models.PositiveIntegerField()),
                ('price_at_order', models.DecimalField(decimal_places=2, max_digits=10)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='orders.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='products.product')),
            ],
            options={
                'db_table': 'order_items',
            },
        ),
        migrations.AddIndex(
            model_name='order',
            index=models.Index(fields=['user'], name='idx_orders_user_id'),
        ),
        migrations.AddIndex(
            model_name='orderitem',
            index=models.Index(fields=['order'], name='idx_order_items_order_id'),
        ),
        migrations.AddIndex(
            model_name='orderitem',
            index=models.Index(fields=['product'], name='idx_order_items_product_id'),
        ),
    ]
