"""
The female gender.

https://schema.org/Female
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class FemaleInheritedProperties(TypedDict):
    """The female gender.

    References:
        https://schema.org/Female
    Note:
        Model Depth 5
    Attributes:
    """

    


class FemaleProperties(TypedDict):
    """The female gender.

    References:
        https://schema.org/Female
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(FemaleInheritedProperties , FemaleProperties, TypedDict):
    pass


class FemaleBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="Female",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[FemaleProperties, FemaleInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Female"
    return model
    

Female = create_schema_org_model()


def create_female_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_female_model(model=model)
    return pydantic_type(model).schema_json()


