from django.contrib import admin
from .models import *


class SellerAdmin(admin.ModelAdmin):
    list_display = ('name', 'user')


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'user')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('seller', 'name', 'color', 'amount', 'price', 'is_published',)
    list_display_links = ('name', 'seller')
    search_fields = ('name',)
    list_editable = ('is_published',)
    list_filter = ('is_published', 'name', 'seller', 'amount')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')


class ColorAdmin(admin.ModelAdmin):
    list_display = ('name',)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('product', 'customer', 'quantity', 'price_per_item', 'price', 'date',)
    list_filter = ('status', 'date')
    search_fields = ('product', 'customer', 'data')


admin.site.register(Color, ColorAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Seller, SellerAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Order, OrderAdmin)
