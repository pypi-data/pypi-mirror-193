"""
Withdrawn.

https://schema.org/Withdrawn
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class WithdrawnInheritedProperties(TypedDict):
    """Withdrawn.

    References:
        https://schema.org/Withdrawn
    Note:
        Model Depth 6
    Attributes:
    """

    


class WithdrawnProperties(TypedDict):
    """Withdrawn.

    References:
        https://schema.org/Withdrawn
    Note:
        Model Depth 6
    Attributes:
    """

    


class AllProperties(WithdrawnInheritedProperties , WithdrawnProperties, TypedDict):
    pass


class WithdrawnBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="Withdrawn",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[WithdrawnProperties, WithdrawnInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Withdrawn"
    return model
    

Withdrawn = create_schema_org_model()


def create_withdrawn_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_withdrawn_model(model=model)
    return pydantic_type(model).schema_json()


