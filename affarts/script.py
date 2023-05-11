import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "affarts.settings")
django.setup()

from task.models import *
from django.db.models import Max

result = {}


for customer in Customer.objects.all():
    for order in Order.get_orders_by_customer(customer.id):
        seller_name = order.product.seller.name
        if seller_name not in result:
            result[seller_name] = {'customers': [], 'total': 0}
        result[seller_name]['customers'].append(customer.name)
        result[seller_name]['total'] += order.total_price


print([{'Продавец': k, 'Покупатели': v['customers'], 'Общая цена': v['total']} for k, v in result.items()])
