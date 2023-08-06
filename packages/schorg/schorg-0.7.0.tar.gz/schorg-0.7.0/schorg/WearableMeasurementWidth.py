"""
Measurement of the width, for example of shoes

https://schema.org/WearableMeasurementWidth
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class WearableMeasurementWidthInheritedProperties(TypedDict):
    """Measurement of the width, for example of shoes

    References:
        https://schema.org/WearableMeasurementWidth
    Note:
        Model Depth 6
    Attributes:
    """

    


class WearableMeasurementWidthProperties(TypedDict):
    """Measurement of the width, for example of shoes

    References:
        https://schema.org/WearableMeasurementWidth
    Note:
        Model Depth 6
    Attributes:
    """

    


class AllProperties(WearableMeasurementWidthInheritedProperties , WearableMeasurementWidthProperties, TypedDict):
    pass


class WearableMeasurementWidthBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="WearableMeasurementWidth",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[WearableMeasurementWidthProperties, WearableMeasurementWidthInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "WearableMeasurementWidth"
    return model
    

WearableMeasurementWidth = create_schema_org_model()


def create_wearablemeasurementwidth_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_wearablemeasurementwidth_model(model=model)
    return pydantic_type(model).schema_json()


