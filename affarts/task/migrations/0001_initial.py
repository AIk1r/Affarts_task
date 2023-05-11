# Generated by Django 4.2.1 on 2023-05-11 15:47

import datetime
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
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Цвет')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Покупатель')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Продавец')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Наименование товара')),
                ('amount', models.IntegerField(verbose_name='Количество в наличии')),
                ('price', models.IntegerField(verbose_name='Цена за 1шт.')),
                ('is_published', models.BooleanField(default=True, verbose_name='Публикация')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.color', verbose_name='Оттенок')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.seller', verbose_name='Продавец')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1, verbose_name='Количество')),
                ('price_per_item', models.IntegerField(verbose_name='Цена за штуку')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('address', models.CharField(blank=True, default='', max_length=255, verbose_name='Адрес')),
                ('phone', models.CharField(blank=True, default='', max_length=50, verbose_name='Телефон')),
                ('date', models.DateField(default=datetime.datetime.today, verbose_name='Дата')),
                ('status', models.CharField(choices=[('waiting_delivery', 'Ждет доставки'), ('delivered', 'Доставлено'), ('not_paid', 'Не оплачено')], default='waiting_delivery', max_length=20, verbose_name='Статус заказа')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.customer', verbose_name='Покупатель')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.product', verbose_name='Товар')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, verbose_name='Имя')),
                ('email', models.EmailField(max_length=254, verbose_name='Почта')),
                ('body', models.TextField(verbose_name='Поле для комментариев')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Опубликован')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлён')),
                ('active', models.BooleanField(default=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.seller', verbose_name='Комментарии')),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
