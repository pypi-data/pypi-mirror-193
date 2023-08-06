"""
Maximum girth of bust. Used, for example, to fit women's suits.

https://schema.org/BodyMeasurementBust
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class BodyMeasurementBustInheritedProperties(TypedDict):
    """Maximum girth of bust. Used, for example, to fit women's suits.

    References:
        https://schema.org/BodyMeasurementBust
    Note:
        Model Depth 6
    Attributes:
    """

    


class BodyMeasurementBustProperties(TypedDict):
    """Maximum girth of bust. Used, for example, to fit women's suits.

    References:
        https://schema.org/BodyMeasurementBust
    Note:
        Model Depth 6
    Attributes:
    """

    


class AllProperties(BodyMeasurementBustInheritedProperties , BodyMeasurementBustProperties, TypedDict):
    pass


class BodyMeasurementBustBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="BodyMeasurementBust",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[BodyMeasurementBustProperties, BodyMeasurementBustInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "BodyMeasurementBust"
    return model
    

BodyMeasurementBust = create_schema_org_model()


def create_bodymeasurementbust_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_bodymeasurementbust_model(model=model)
    return pydantic_type(model).schema_json()


