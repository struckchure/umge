'''
    Delivery utilities
'''
from ip2geotools.databases.noncommercial import DbIpCity

from delivery.models import Order
from delivery.serializers import OrderSerializer
from accounts.serializers import UserSerializer


def group_rider_orders(orders):
    users = []
    grouped_data = []

    for order in orders:
        if order.user.username not in users:
            users.append(order.user.username)

            user_orders = Order.objects\
                .filter(user=order.user, status=Order.STATUS.PENDING)\
                .order_by('-updated')
            serialized_orders = OrderSerializer(user_orders, many=True).data

            user_order_data = {
                'user': UserSerializer(order.user).data,
                'orders': serialized_orders
            }

            grouped_data.append(user_order_data)

    return grouped_data


def get_coordinates(ip_address):
    response = DbIpCity.get(ip_address, api_key='free')

    return response.to_json()
