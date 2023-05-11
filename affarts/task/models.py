from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import datetime

class Color(models.Model):
    name = models.CharField(max_length=255, verbose_name='Цвет')

    def __str__(self):
        return self.name


class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    name = models.CharField(max_length=60, verbose_name='Продавец')

    def __str__(self):
        return self.name


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    name = models.CharField(max_length=60, verbose_name='Покупатель')

    def __str__(self):
        return self.name


class Product(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, verbose_name='Продавец')
    name = models.CharField(max_length=255, verbose_name='Наименование товара')
    color = models.ForeignKey(Color, on_delete=models.CASCADE, verbose_name='Оттенок')
    amount = models.IntegerField(verbose_name='Количество в наличии')
    price = models.IntegerField(verbose_name='Цена за 1шт.')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')

    def __str__(self):
        return self.name


class Comment(models.Model):
    post = models.ForeignKey(Seller, on_delete=models.CASCADE, verbose_name='Комментарии')
    name = models.CharField(max_length=80, verbose_name='Имя')
    email = models.EmailField(verbose_name='Почта')
    body = models.TextField(verbose_name='Поле для комментариев')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Опубликован')
    updated = models.DateTimeField(auto_now=True, verbose_name='Обновлён')
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)


class Order(models.Model):
    STATUS_CHOICES = (
        ('waiting_delivery', 'Ждет доставки'),
        ('delivered', 'Доставлено'),
        ('not_paid', 'Не оплачено'),
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='Покупатель')
    quantity = models.IntegerField(default=1, verbose_name='Количество')
    price_per_item = models.IntegerField(default=None, verbose_name='Цена за штуку')
    price = models.IntegerField(verbose_name='Цена')
    address = models.CharField(max_length=255, default='', blank=True, verbose_name='Адрес')
    phone = models.CharField(max_length=50, default='', blank=True, verbose_name='Телефон')
    date = models.DateField(default=datetime.datetime.today, verbose_name='Дата')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='waiting_delivery',
                              verbose_name='Статус заказа')

    @property
    def total_price(self):
        return self.quantity * self.price_per_item

    def calculate_price(self):
        self.price = self.total_price

    def save(self, *args, **kwargs):
        self.calculate_price()
        super(Order, self).save(*args, **kwargs)

    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date')
