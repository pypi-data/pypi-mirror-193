"""
A health profession of a person formally educated and trained in the care of the sick or infirm person.

https://schema.org/Nursing
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class NursingInheritedProperties(TypedDict):
    """A health profession of a person formally educated and trained in the care of the sick or infirm person.

    References:
        https://schema.org/Nursing
    Note:
        Model Depth 5
    Attributes:
    """

    


class NursingProperties(TypedDict):
    """A health profession of a person formally educated and trained in the care of the sick or infirm person.

    References:
        https://schema.org/Nursing
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(NursingInheritedProperties , NursingProperties, TypedDict):
    pass


class NursingBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="Nursing",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[NursingProperties, NursingInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Nursing"
    return model
    

Nursing = create_schema_org_model()


def create_nursing_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_nursing_model(model=model)
    return pydantic_type(model).schema_json()


