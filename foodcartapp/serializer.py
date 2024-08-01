from rest_framework.serializers import ModelSerializer
from .models import Product, Order, OrderElement


class ProductSerializer(ModelSerializer):
    class Meta:
        model = OrderElement
        fields = ['id']


class OrderSerializer(ModelSerializer):
    products = ProductSerializer()
    def create_order(self, order):
        created_order = Order.objects.create(
            firstname=order["firstname"],
            lastname=order["lastname"],
            phone=order["phone"],
            address=order["address"]
        )

        for product in order["products"]:
            OrderElement.objects.create(
                order=created_order,
                product=Product.objects.get(id=product["product"]),
                quantity=product["quantity"]
            )

    class Meta:
        model = Order
        fields = ['firstname', 'lastname', 'phone', 'address', 'products']
