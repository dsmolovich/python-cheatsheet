from decimal import Decimal
from p349_function_oriented_strategy import (
    Customer, Order, LineItem,
    fidelity_promo, bulk_item_promo, large_order_promo,
)

joe = Customer('John Doe', 0)
ann = Customer('Ann Smith', 1_000)

cart = (LineItem('banana', 4, Decimal('0.5')),
        LineItem('apple', 10, Decimal('1.5')),
        LineItem('watermelon', 5, Decimal(5)))
banana_cart = (LineItem('banana', 30, Decimal('0.5')),
               LineItem('apple', 10, Decimal('1.5')))
large_cart = tuple(LineItem(str(sku), 1, Decimal(1)) for sku in range(10))

promos = [fidelity_promo, bulk_item_promo, large_order_promo]

def best_promo(order: Order):
    """Compute the best discount available"""
    return max(promo(order) for promo in promos)

def _doctest_it():
    """
    >>> Order(joe, large_cart, best_promo)  # Best promotion is: large_order_promo
    <Order total: 10.00, due: 9.30>

    >>> Order(joe, banana_cart, best_promo)  # Best promotion is: bulk_item_promo
    <Order total: 30.00, due: 28.50>

    >>> Order(ann, cart, best_promo)  # Best promotion is: fidelity_promo
    <Order total: 42.00, due: 39.90>
    """
