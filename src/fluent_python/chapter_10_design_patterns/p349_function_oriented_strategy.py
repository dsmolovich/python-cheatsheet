from collections.abc import Sequence
from decimal import Decimal
from typing import NamedTuple, Optional, Callable

class Customer(NamedTuple):
    name: str
    fidelity: int

class LineItem(NamedTuple):
    product: str
    quantity: int
    price: Decimal

    def total(self) -> Decimal:
        return self.price * self.quantity
    
class Order(NamedTuple): # Context
    customer: Customer
    cart: Sequence[LineItem]
    promotion: Optional[Callable[['Order'], Decimal]] = None

    def total(self) -> Decimal:
        totals = (item.total() for item in self.cart)
        return sum(totals, start=Decimal(0))
    
    def due(self) -> Decimal:
        if self.promotion is None:
            discount = Decimal(0)
        else:
            discount = self.promotion(self)
        return self.total() - discount
    
    def __repr__(self):
        return f'<Order total: {self.total():.2f}, due: {self.due():.2f}>'


def fidelity_promo(order: Order) -> Decimal:
    """5% discount for customers with 1000 or more fidelity points"""
    rate = Decimal('0.05')
    if order.customer.fidelity >= 1000:
        return order.total() * rate
    return Decimal(0)

def bulk_item_promo(order: Order) -> Decimal:
    """10% discount for each LineItem with 10 or more units"""
    discount = Decimal(0)
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * Decimal('0.1')
    return discount

def large_order_promo(order: Order) -> Decimal:
    """7% discount for orders with 10 or more distinct items"""
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * Decimal('0.07')
    return Decimal(0)

def _doctest_it():
    """
    >>> joe = Customer('John Doe', 0)
    >>> ann = Customer('Ann Smith', 1_000)
    >>> cart = (LineItem('banana', 4, Decimal('0.5')),
    ...         LineItem('apple', 10, Decimal('1.5')),
    ...         LineItem('watermelon', 5, Decimal(5)))

    >>> Order(joe, cart, fidelity_promo)
    <Order total: 42.00, due: 42.00>

    >>> Order(ann, cart, fidelity_promo)
    <Order total: 42.00, due: 39.90>
    
    >>> banana_cart = (LineItem('banana', 30, Decimal('0.5')),
    ...                 LineItem('apple', 10, Decimal('1.5')))
    >>> Order(joe, banana_cart, bulk_item_promo)
    <Order total: 30.00, due: 28.50>

    >>> large_cart = tuple(LineItem(str(sku), 1, Decimal(1)) for sku in range(10))
    >>> Order(joe, large_cart, large_order_promo)
    <Order total: 10.00, due: 9.30>
    >>> Order(joe, cart, large_order_promo)
    <Order total: 42.00, due: 42.00>
    """
