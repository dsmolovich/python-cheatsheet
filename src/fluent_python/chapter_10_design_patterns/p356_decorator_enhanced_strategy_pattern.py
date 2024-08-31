import typing as t
from decimal import Decimal
from p349_function_oriented_strategy import (
    Customer, Order, LineItem,
)
from p352_choosing_best_strategy import (
    joe, ann,
    cart, banana_cart, large_cart,
    best_promo
)

Promotion = t.Callable[[Order], Decimal]

promos: list[Promotion] = []

def promotion(promo: Promotion):
    promos.append(promo)
    return promo


@promotion
def fidelity(order: Order) -> Decimal:
    """5% discount for customers with 1000 or more fidelity points"""
    rate = Decimal('0.05')
    if order.customer.fidelity >= 1000:
        return order.total() * rate
    return Decimal(0)

@promotion
def bulk_item_promo(order: Order) -> Decimal:
    """10% discount for each LineItem with 10 or more units"""
    discount = Decimal(0)
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * Decimal('0.1')
    return discount

@promotion
def large_order_promo(order: Order) -> Decimal:
    """7% discount for orders with 10 or more distinct items"""
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * Decimal('0.07')
    return Decimal(0)


def _doctest_it():
    """
    >>> Order(joe, large_cart, best_promo)  # Best promotion is: large_order_promo
    <Order total: 10.00, due: 9.30>

    >>> Order(joe, banana_cart, best_promo)  # Best promotion is: bulk_item_promo
    <Order total: 30.00, due: 28.50>

    >>> Order(ann, cart, best_promo)  # Best promotion is: fidelity_promo
    <Order total: 42.00, due: 39.90>
    """
