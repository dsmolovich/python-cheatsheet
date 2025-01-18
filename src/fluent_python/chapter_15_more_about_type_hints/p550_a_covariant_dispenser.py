"""
Mypy it:
    python -m mypy p550_a_covariant_dispenser.py
Will complain with:
    p550_a_covariant_dispenser.py:37: error: Argument 1 to "install" has incompatible type "BeverageDispenser[Beverage]"; expected "BeverageDispenser[Juice]"  [arg-type]
    Found 1 error in 1 file (checked 1 source file)
"""
from typing import TypeVar, Generic

class Beverage:
    """ Any beverage """

class Juice(Beverage):
    """ Any fruit juice """

class OrangeJuice(Juice):
    """ Orange juice """

T_co = TypeVar('T_co', covariant=True)

class BeverageDispenser(Generic[T_co]):
    """ A dispenser parameterized on the beverage type """
    def __init__(self, beverage: T_co) -> None:
        self.beverage = beverage
    
    def dispense(self) -> T_co:
        return self.beverage

def install(dispencer: BeverageDispenser[Juice]) -> None:
    """ Install fruit juice dispenser """

juice_dispenser = BeverageDispenser(Juice())
install(juice_dispenser) # This is legal to install

beverage_dispenser = BeverageDispenser(Beverage())
install(beverage_dispenser) # Illegal to install

orange_juice_dispenser = BeverageDispenser(OrangeJuice())
install(orange_juice_dispenser) # This is also legal to install
