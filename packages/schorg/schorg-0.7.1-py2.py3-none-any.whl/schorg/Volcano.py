"""
A volcano, like Fujisan.

https://schema.org/Volcano
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class VolcanoInheritedProperties(TypedDict):
    """A volcano, like Fujisan.

    References:
        https://schema.org/Volcano
    Note:
        Model Depth 4
    Attributes:
    """

    


class VolcanoProperties(TypedDict):
    """A volcano, like Fujisan.

    References:
        https://schema.org/Volcano
    Note:
        Model Depth 4
    Attributes:
    """

    


class AllProperties(VolcanoInheritedProperties , VolcanoProperties, TypedDict):
    pass


class VolcanoBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="Volcano",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[VolcanoProperties, VolcanoInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Volcano"
    return model
    

Volcano = create_schema_org_model()


def create_volcano_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_volcano_model(model=model)
    return pydantic_type(model).schema_json()


