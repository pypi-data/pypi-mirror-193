"""
Specifies that product returns must be made at a kiosk.

https://schema.org/ReturnAtKiosk
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ReturnAtKioskInheritedProperties(TypedDict):
    """Specifies that product returns must be made at a kiosk.

    References:
        https://schema.org/ReturnAtKiosk
    Note:
        Model Depth 5
    Attributes:
    """

    


class ReturnAtKioskProperties(TypedDict):
    """Specifies that product returns must be made at a kiosk.

    References:
        https://schema.org/ReturnAtKiosk
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(ReturnAtKioskInheritedProperties , ReturnAtKioskProperties, TypedDict):
    pass


class ReturnAtKioskBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="ReturnAtKiosk",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[ReturnAtKioskProperties, ReturnAtKioskInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ReturnAtKiosk"
    return model
    

ReturnAtKiosk = create_schema_org_model()


def create_returnatkiosk_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_returnatkiosk_model(model=model)
    return pydantic_type(model).schema_json()


