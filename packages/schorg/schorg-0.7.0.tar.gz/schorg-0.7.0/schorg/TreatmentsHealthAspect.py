"""
Treatments or related therapies for a Topic.

https://schema.org/TreatmentsHealthAspect
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class TreatmentsHealthAspectInheritedProperties(TypedDict):
    """Treatments or related therapies for a Topic.

    References:
        https://schema.org/TreatmentsHealthAspect
    Note:
        Model Depth 5
    Attributes:
    """

    


class TreatmentsHealthAspectProperties(TypedDict):
    """Treatments or related therapies for a Topic.

    References:
        https://schema.org/TreatmentsHealthAspect
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(TreatmentsHealthAspectInheritedProperties , TreatmentsHealthAspectProperties, TypedDict):
    pass


class TreatmentsHealthAspectBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="TreatmentsHealthAspect",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[TreatmentsHealthAspectProperties, TreatmentsHealthAspectInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "TreatmentsHealthAspect"
    return model
    

TreatmentsHealthAspect = create_schema_org_model()


def create_treatmentshealthaspect_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_treatmentshealthaspect_model(model=model)
    return pydantic_type(model).schema_json()


