"""
A medical device used for therapeutic purposes.

https://schema.org/Therapeutic
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class TherapeuticInheritedProperties(TypedDict):
    """A medical device used for therapeutic purposes.

    References:
        https://schema.org/Therapeutic
    Note:
        Model Depth 6
    Attributes:
    """

    


class TherapeuticProperties(TypedDict):
    """A medical device used for therapeutic purposes.

    References:
        https://schema.org/Therapeutic
    Note:
        Model Depth 6
    Attributes:
    """

    


class AllProperties(TherapeuticInheritedProperties , TherapeuticProperties, TypedDict):
    pass


class TherapeuticBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="Therapeutic",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[TherapeuticProperties, TherapeuticInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Therapeutic"
    return model
    

Therapeutic = create_schema_org_model()


def create_therapeutic_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_therapeutic_model(model=model)
    return pydantic_type(model).schema_json()


