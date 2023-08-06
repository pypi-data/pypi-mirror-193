"""
Measurement of the back section, for example of a jacket

https://schema.org/WearableMeasurementBack
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class WearableMeasurementBackInheritedProperties(TypedDict):
    """Measurement of the back section, for example of a jacket

    References:
        https://schema.org/WearableMeasurementBack
    Note:
        Model Depth 6
    Attributes:
    """

    


class WearableMeasurementBackProperties(TypedDict):
    """Measurement of the back section, for example of a jacket

    References:
        https://schema.org/WearableMeasurementBack
    Note:
        Model Depth 6
    Attributes:
    """

    


class AllProperties(WearableMeasurementBackInheritedProperties , WearableMeasurementBackProperties, TypedDict):
    pass


class WearableMeasurementBackBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="WearableMeasurementBack",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[WearableMeasurementBackProperties, WearableMeasurementBackInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "WearableMeasurementBack"
    return model
    

WearableMeasurementBack = create_schema_org_model()


def create_wearablemeasurementback_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_wearablemeasurementback_model(model=model)
    return pydantic_type(model).schema_json()


