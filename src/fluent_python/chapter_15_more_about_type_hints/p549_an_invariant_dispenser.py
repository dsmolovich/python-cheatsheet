"""
Mypy it:
    python -m mypy p549_an_invariant_dispenser.py
Will complain with:
    p549_an_invariant_dispenser.py:35: error: Argument 1 to "install" has incompatible type "BeverageDispenser[Beverage]"; expected "BeverageDispenser[Juice]"  [arg-type]
    p549_an_invariant_dispenser.py:39: error: Argument 1 to "install" has incompatible type "BeverageDispenser[OrangeJuice]"; expected "BeverageDispenser[Juice]"  [arg-type]
    Found 2 errors in 1 file (checked 1 source file)
"""
from typing import TypeVar, Generic

class Beverage:
    """ Any beverage """

class Juice(Beverage):
    """ Any fruit juice """

class OrangeJuice(Juice):
    """ Orange juice """

T = TypeVar('T')

class BeverageDispenser(Generic[T]):
    """ A dispenser parameterized on the beverage type """
    def __init__(self, beverage: T) -> None:
        self.beverage = beverage
    
    def dispense(self) -> T:
        return self.beverage

def install(dispencer: BeverageDispenser[Juice]) -> None:
    """ Install fruit juice dispenser """

juice_dispenser = BeverageDispenser(Juice())
install(juice_dispenser) # This is legale to install

beverage_dispenser = BeverageDispenser(Beverage())
install(beverage_dispenser) # Illegal to install

orange_juice_dispenser = BeverageDispenser(OrangeJuice())
install(orange_juice_dispenser) # Illegal to install
