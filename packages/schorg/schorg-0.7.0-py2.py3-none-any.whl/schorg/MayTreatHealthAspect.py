"""
Related topics may be treated by a Topic.

https://schema.org/MayTreatHealthAspect
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MayTreatHealthAspectInheritedProperties(TypedDict):
    """Related topics may be treated by a Topic.

    References:
        https://schema.org/MayTreatHealthAspect
    Note:
        Model Depth 5
    Attributes:
    """

    


class MayTreatHealthAspectProperties(TypedDict):
    """Related topics may be treated by a Topic.

    References:
        https://schema.org/MayTreatHealthAspect
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(MayTreatHealthAspectInheritedProperties , MayTreatHealthAspectProperties, TypedDict):
    pass


class MayTreatHealthAspectBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="MayTreatHealthAspect",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[MayTreatHealthAspectProperties, MayTreatHealthAspectInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MayTreatHealthAspect"
    return model
    

MayTreatHealthAspect = create_schema_org_model()


def create_maytreathealthaspect_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_maytreathealthaspect_model(model=model)
    return pydantic_type(model).schema_json()


