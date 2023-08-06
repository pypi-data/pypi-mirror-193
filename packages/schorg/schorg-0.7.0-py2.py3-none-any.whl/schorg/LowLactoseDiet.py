"""
A diet appropriate for people with lactose intolerance.

https://schema.org/LowLactoseDiet
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class LowLactoseDietInheritedProperties(TypedDict):
    """A diet appropriate for people with lactose intolerance.

    References:
        https://schema.org/LowLactoseDiet
    Note:
        Model Depth 5
    Attributes:
    """

    


class LowLactoseDietProperties(TypedDict):
    """A diet appropriate for people with lactose intolerance.

    References:
        https://schema.org/LowLactoseDiet
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(LowLactoseDietInheritedProperties , LowLactoseDietProperties, TypedDict):
    pass


class LowLactoseDietBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="LowLactoseDiet",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[LowLactoseDietProperties, LowLactoseDietInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "LowLactoseDiet"
    return model
    

LowLactoseDiet = create_schema_org_model()


def create_lowlactosediet_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_lowlactosediet_model(model=model)
    return pydantic_type(model).schema_json()


