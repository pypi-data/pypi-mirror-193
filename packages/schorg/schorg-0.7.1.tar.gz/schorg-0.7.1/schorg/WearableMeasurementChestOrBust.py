"""
Measurement of the chest/bust section, for example of a suit

https://schema.org/WearableMeasurementChestOrBust
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class WearableMeasurementChestOrBustInheritedProperties(TypedDict):
    """Measurement of the chest/bust section, for example of a suit

    References:
        https://schema.org/WearableMeasurementChestOrBust
    Note:
        Model Depth 6
    Attributes:
    """

    


class WearableMeasurementChestOrBustProperties(TypedDict):
    """Measurement of the chest/bust section, for example of a suit

    References:
        https://schema.org/WearableMeasurementChestOrBust
    Note:
        Model Depth 6
    Attributes:
    """

    


class AllProperties(WearableMeasurementChestOrBustInheritedProperties , WearableMeasurementChestOrBustProperties, TypedDict):
    pass


class WearableMeasurementChestOrBustBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="WearableMeasurementChestOrBust",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[WearableMeasurementChestOrBustProperties, WearableMeasurementChestOrBustInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "WearableMeasurementChestOrBust"
    return model
    

WearableMeasurementChestOrBust = create_schema_org_model()


def create_wearablemeasurementchestorbust_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_wearablemeasurementchestorbust_model(model=model)
    return pydantic_type(model).schema_json()


