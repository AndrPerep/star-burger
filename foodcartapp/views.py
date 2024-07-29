import json

import django.db.utils
import phonenumbers
from django.http import JsonResponse
from django.http.request import RawPostDataException
from django.templatetags.static import static
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Product, Order, OrderElement


def banners_list_api(request):
    # FIXME move data to db?
    return JsonResponse([
        {
            'title': 'Burger',
            'src': static('burger.jpg'),
            'text': 'Tasty Burger at your door step',
        },
        {
            'title': 'Spices',
            'src': static('food.jpg'),
            'text': 'All Cuisines',
        },
        {
            'title': 'New York',
            'src': static('tasty.jpg'),
            'text': 'Food is incomplete without a tasty dessert',
        }
    ], safe=False, json_dumps_params={
        'ensure_ascii': False,
        'indent': 4,
    })


def product_list_api(request):
    products = Product.objects.select_related('category').available()

    dumped_products = []
    for product in products:
        dumped_product = {
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'special_status': product.special_status,
            'description': product.description,
            'category': {
                'id': product.category.id,
                'name': product.category.name,
            } if product.category else None,
            'image': product.image.url,
            'restaurant': {
                'id': product.id,
                'name': product.name,
            }
        }
        dumped_products.append(dumped_product)
    return JsonResponse(dumped_products, safe=False, json_dumps_params={
        'ensure_ascii': False,
        'indent': 4,
    })


@api_view(['POST'])
def register_order(request):
    try:
        order = json.loads(request.body.decode())
    except RawPostDataException:
        order = request.data
    try:
        for product in order['products']:
            id = product['product']
            if not id in Product.objects.values_list('id', flat=True):
                content = {f'products: Недопустимый первичный ключ {id}'}
                return Response(content, status=status.HTTP_400_BAD_REQUEST)
        if order['products'] == []:
            content = {'products: Этот список не может быть пустым.'}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
        elif order['phonenumber'] == '':
            content = {'phonenumber: Это поле не может быть пустым.'}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
        elif not phonenumbers.is_valid_number(phonenumbers.parse(order['phonenumber'])):
            content = {'phonenumber: Введен некорректный номер телефона.'}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
        elif isinstance(order['firstname'], list):
            content = {'firstname: Not a valid string.'}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                created_order = Order.objects.create(
                    first_name=order['firstname'],
                    last_name=order['lastname'],
                    phone=order['phonenumber'],
                    address=order['address']
                )

                try:
                    for product in order['products']:
                        OrderElement(
                            order=created_order,
                            product=Product.objects.get(id=product['product']),
                            quantity=product['quantity']
                        ).save()
                except TypeError:
                    if isinstance(order['products'], str):
                        return JsonResponse({
                            'error': 'products: Ожидался list со значениями, но был получен "str".'
                        })
                    elif order['products'] == None:
                        return JsonResponse({
                            'error': 'products: Это поле не может быть пустым.'
                        })
                    else:
                        return JsonResponse({
                            'error': 'KeyError'
                        })
                except KeyError:
                    return JsonResponse({
                        'error': 'products: Обязательное поле.'
                    })
                return JsonResponse({
                })

            except django.db.utils.IntegrityError:
                content = {'error': 'firstname, lastname, phonenumber, address: Обязательное поле.'}
                return Response(content, status=status.HTTP_400_BAD_REQUEST)
    except KeyError:
        content = {'error': 'firstname, lastname, phonenumber, address: Обязательное поле.'}
        return Response(content, status=status.HTTP_400_BAD_REQUEST)
