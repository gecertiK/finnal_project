import json
from .models import Order, OrderItem, Customer
from books.models import Book


def cookie_cart(request):
    try:
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart = {}
    items = []
    order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
    for i in cart:
        try:
            if (cart[i]['quantity'] > 0):

                product = Book.objects.get(id=i)
                total = (product.price * cart[i]['quantity'])
                order['get_cart_total'] += total
                order['get_cart_items'] += cart[i]['quantity']
                item = {
                    'id': product.id,
                    'book': {
                        'id': product.id,
                        'title': product.title,
                        'price': product.price,
                        'quantity_value': product.count
                    },
                    'quantity': cart[i]['quantity'],
                    'digital': product.digital, 'get_total': total,
                }
                items.append(item)
                if product.digital is False:
                    order['shipping'] = True
        except:
            pass
    return {'order': order, 'items': items}


def cart_data(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all().order_by('-id')
    else:
        cookie_data = cookie_cart(request)
        order = cookie_data['order']
        items = cookie_data['items']
    return {'order': order, 'items': items}


def guest_order(request, data):
    name = data['form']['name']
    email = data['form']['email']
    cookie_data = cookie_cart(request)
    items = cookie_data['items']
    customer, created = Customer.objects.get_or_create(
        email=email,
    )
    customer.name = name
    customer.save()

    order = Order.objects.create(
        guest=customer,
        complete=False,
    )
    for item in items:
        product = Book.objects.get(id=item['id'])
        order_item = OrderItem.objects.create(
            book=product,
            order=order,
            quantity=(item['quantity'] if item['quantity'] > 0 else -1 * item['quantity']),
        )
    return customer, order
