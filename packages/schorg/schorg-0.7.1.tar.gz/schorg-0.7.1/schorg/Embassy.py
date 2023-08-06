"""
An embassy.

https://schema.org/Embassy
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class EmbassyInheritedProperties(TypedDict):
    """An embassy.

    References:
        https://schema.org/Embassy
    Note:
        Model Depth 5
    Attributes:
    """

    


class EmbassyProperties(TypedDict):
    """An embassy.

    References:
        https://schema.org/Embassy
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(EmbassyInheritedProperties , EmbassyProperties, TypedDict):
    pass


class EmbassyBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="Embassy",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[EmbassyProperties, EmbassyInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Embassy"
    return model
    

Embassy = create_schema_org_model()


def create_embassy_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_embassy_model(model=model)
    return pydantic_type(model).schema_json()


