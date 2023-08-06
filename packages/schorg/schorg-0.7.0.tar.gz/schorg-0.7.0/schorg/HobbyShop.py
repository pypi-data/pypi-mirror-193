"""
A store that sells materials useful or necessary for various hobbies.

https://schema.org/HobbyShop
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class HobbyShopInheritedProperties(TypedDict):
    """A store that sells materials useful or necessary for various hobbies.

    References:
        https://schema.org/HobbyShop
    Note:
        Model Depth 5
    Attributes:
    """

    


class HobbyShopProperties(TypedDict):
    """A store that sells materials useful or necessary for various hobbies.

    References:
        https://schema.org/HobbyShop
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(HobbyShopInheritedProperties , HobbyShopProperties, TypedDict):
    pass


class HobbyShopBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="HobbyShop",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[HobbyShopProperties, HobbyShopInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "HobbyShop"
    return model
    

HobbyShop = create_schema_org_model()


def create_hobbyshop_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_hobbyshop_model(model=model)
    return pydantic_type(model).schema_json()


