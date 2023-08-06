"""
Represents the length, for example of a dress

https://schema.org/WearableMeasurementLength
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class WearableMeasurementLengthInheritedProperties(TypedDict):
    """Represents the length, for example of a dress

    References:
        https://schema.org/WearableMeasurementLength
    Note:
        Model Depth 6
    Attributes:
    """

    


class WearableMeasurementLengthProperties(TypedDict):
    """Represents the length, for example of a dress

    References:
        https://schema.org/WearableMeasurementLength
    Note:
        Model Depth 6
    Attributes:
    """

    


class AllProperties(WearableMeasurementLengthInheritedProperties , WearableMeasurementLengthProperties, TypedDict):
    pass


class WearableMeasurementLengthBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="WearableMeasurementLength",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[WearableMeasurementLengthProperties, WearableMeasurementLengthInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "WearableMeasurementLength"
    return model
    

WearableMeasurementLength = create_schema_org_model()


def create_wearablemeasurementlength_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_wearablemeasurementlength_model(model=model)
    return pydantic_type(model).schema_json()


