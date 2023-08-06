"""
Book format: Hardcover.

https://schema.org/Hardcover
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class HardcoverInheritedProperties(TypedDict):
    """Book format: Hardcover.

    References:
        https://schema.org/Hardcover
    Note:
        Model Depth 5
    Attributes:
    """

    


class HardcoverProperties(TypedDict):
    """Book format: Hardcover.

    References:
        https://schema.org/Hardcover
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(HardcoverInheritedProperties , HardcoverProperties, TypedDict):
    pass


class HardcoverBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="Hardcover",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[HardcoverProperties, HardcoverInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Hardcover"
    return model
    

Hardcover = create_schema_org_model()


def create_hardcover_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_hardcover_model(model=model)
    return pydantic_type(model).schema_json()


