"""
Mypy it:
    python -m mypy p552_contravariant_trash_can.py 
Will complain with:
    p552_contravariant_trash_can.py:28: error: Argument 1 to "deploy" has incompatible type "TrashCan[Compostable]"; expected "TrashCan[Biodegradable]"  [arg-type]
    Found 1 error in 1 file (checked 1 source file)
"""

from typing import TypeVar, Generic

class Refuse:
    """ Any refuse """

class Biodegradable(Refuse):
    """ Biodegradable refuse """

class Compostable(Biodegradable):
    """ Compostable refuse """

T_contra = TypeVar('T_contra', contravariant=True)

class TrashCan(Generic[T_contra]):
    def put(self, refuse: T_contra) -> None:
        """ Store trash until dumped """

def deploy(trash_can: TrashCan[Biodegradable]):
    """ Deploy a trash can for diodegradable refuse """

bio_can: TrashCan[Biodegradable] = TrashCan()
deploy(bio_can) # This is legal

trash_can: TrashCan[Refuse] = TrashCan()
deploy(trash_can) # This is also legal as it accepts Biodegradable

compost_can: TrashCan[Compostable] = TrashCan()
deploy(compost_can) # Illegal as it does not accept Biodegradable
