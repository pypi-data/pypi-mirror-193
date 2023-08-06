"""
Beauty salon.

https://schema.org/BeautySalon
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class BeautySalonInheritedProperties(TypedDict):
    """Beauty salon.

    References:
        https://schema.org/BeautySalon
    Note:
        Model Depth 5
    Attributes:
    """

    


class BeautySalonProperties(TypedDict):
    """Beauty salon.

    References:
        https://schema.org/BeautySalon
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(BeautySalonInheritedProperties , BeautySalonProperties, TypedDict):
    pass


class BeautySalonBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="BeautySalon",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[BeautySalonProperties, BeautySalonInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "BeautySalon"
    return model
    

BeautySalon = create_schema_org_model()


def create_beautysalon_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_beautysalon_model(model=model)
    return pydantic_type(model).schema_json()


