"""
Girth of body just below the bust. Used, for example, to fit women's swimwear.

https://schema.org/BodyMeasurementUnderbust
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class BodyMeasurementUnderbustInheritedProperties(TypedDict):
    """Girth of body just below the bust. Used, for example, to fit women's swimwear.

    References:
        https://schema.org/BodyMeasurementUnderbust
    Note:
        Model Depth 6
    Attributes:
    """

    


class BodyMeasurementUnderbustProperties(TypedDict):
    """Girth of body just below the bust. Used, for example, to fit women's swimwear.

    References:
        https://schema.org/BodyMeasurementUnderbust
    Note:
        Model Depth 6
    Attributes:
    """

    


class AllProperties(BodyMeasurementUnderbustInheritedProperties , BodyMeasurementUnderbustProperties, TypedDict):
    pass


class BodyMeasurementUnderbustBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="BodyMeasurementUnderbust",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[BodyMeasurementUnderbustProperties, BodyMeasurementUnderbustInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "BodyMeasurementUnderbust"
    return model
    

BodyMeasurementUnderbust = create_schema_org_model()


def create_bodymeasurementunderbust_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_bodymeasurementunderbust_model(model=model)
    return pydantic_type(model).schema_json()


