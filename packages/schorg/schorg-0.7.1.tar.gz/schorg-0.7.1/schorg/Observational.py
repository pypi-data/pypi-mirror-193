"""
An observational study design.

https://schema.org/Observational
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ObservationalInheritedProperties(TypedDict):
    """An observational study design.

    References:
        https://schema.org/Observational
    Note:
        Model Depth 6
    Attributes:
    """

    


class ObservationalProperties(TypedDict):
    """An observational study design.

    References:
        https://schema.org/Observational
    Note:
        Model Depth 6
    Attributes:
    """

    


class AllProperties(ObservationalInheritedProperties , ObservationalProperties, TypedDict):
    pass


class ObservationalBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="Observational",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[ObservationalProperties, ObservationalInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Observational"
    return model
    

Observational = create_schema_org_model()


def create_observational_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_observational_model(model=model)
    return pydantic_type(model).schema_json()


