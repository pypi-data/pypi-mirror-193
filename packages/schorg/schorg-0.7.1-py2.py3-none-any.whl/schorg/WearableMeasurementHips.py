"""
Measurement of the hip section, for example of a skirt

https://schema.org/WearableMeasurementHips
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class WearableMeasurementHipsInheritedProperties(TypedDict):
    """Measurement of the hip section, for example of a skirt

    References:
        https://schema.org/WearableMeasurementHips
    Note:
        Model Depth 6
    Attributes:
    """

    


class WearableMeasurementHipsProperties(TypedDict):
    """Measurement of the hip section, for example of a skirt

    References:
        https://schema.org/WearableMeasurementHips
    Note:
        Model Depth 6
    Attributes:
    """

    


class AllProperties(WearableMeasurementHipsInheritedProperties , WearableMeasurementHipsProperties, TypedDict):
    pass


class WearableMeasurementHipsBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="WearableMeasurementHips",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[WearableMeasurementHipsProperties, WearableMeasurementHipsInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "WearableMeasurementHips"
    return model
    

WearableMeasurementHips = create_schema_org_model()


def create_wearablemeasurementhips_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_wearablemeasurementhips_model(model=model)
    return pydantic_type(model).schema_json()


