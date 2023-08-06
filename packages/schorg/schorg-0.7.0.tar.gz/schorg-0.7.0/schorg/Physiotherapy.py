"""
The practice of treatment of disease, injury, or deformity by physical methods such as massage, heat treatment, and exercise rather than by drugs or surgery.

https://schema.org/Physiotherapy
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class PhysiotherapyInheritedProperties(TypedDict):
    """The practice of treatment of disease, injury, or deformity by physical methods such as massage, heat treatment, and exercise rather than by drugs or surgery.

    References:
        https://schema.org/Physiotherapy
    Note:
        Model Depth 5
    Attributes:
    """

    


class PhysiotherapyProperties(TypedDict):
    """The practice of treatment of disease, injury, or deformity by physical methods such as massage, heat treatment, and exercise rather than by drugs or surgery.

    References:
        https://schema.org/Physiotherapy
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(PhysiotherapyInheritedProperties , PhysiotherapyProperties, TypedDict):
    pass


class PhysiotherapyBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="Physiotherapy",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[PhysiotherapyProperties, PhysiotherapyInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Physiotherapy"
    return model
    

Physiotherapy = create_schema_org_model()


def create_physiotherapy_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_physiotherapy_model(model=model)
    return pydantic_type(model).schema_json()


