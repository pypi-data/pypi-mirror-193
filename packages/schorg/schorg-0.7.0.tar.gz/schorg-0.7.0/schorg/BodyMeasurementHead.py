"""
Maximum girth of head above the ears. Used, for example, to fit hats.

https://schema.org/BodyMeasurementHead
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class BodyMeasurementHeadInheritedProperties(TypedDict):
    """Maximum girth of head above the ears. Used, for example, to fit hats.

    References:
        https://schema.org/BodyMeasurementHead
    Note:
        Model Depth 6
    Attributes:
    """

    


class BodyMeasurementHeadProperties(TypedDict):
    """Maximum girth of head above the ears. Used, for example, to fit hats.

    References:
        https://schema.org/BodyMeasurementHead
    Note:
        Model Depth 6
    Attributes:
    """

    


class AllProperties(BodyMeasurementHeadInheritedProperties , BodyMeasurementHeadProperties, TypedDict):
    pass


class BodyMeasurementHeadBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="BodyMeasurementHead",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[BodyMeasurementHeadProperties, BodyMeasurementHeadInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "BodyMeasurementHead"
    return model
    

BodyMeasurementHead = create_schema_org_model()


def create_bodymeasurementhead_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_bodymeasurementhead_model(model=model)
    return pydantic_type(model).schema_json()


