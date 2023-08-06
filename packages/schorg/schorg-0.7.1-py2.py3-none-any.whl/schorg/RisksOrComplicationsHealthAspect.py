"""
Information about the risk factors and possible complications that may follow a topic.

https://schema.org/RisksOrComplicationsHealthAspect
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class RisksOrComplicationsHealthAspectInheritedProperties(TypedDict):
    """Information about the risk factors and possible complications that may follow a topic.

    References:
        https://schema.org/RisksOrComplicationsHealthAspect
    Note:
        Model Depth 5
    Attributes:
    """

    


class RisksOrComplicationsHealthAspectProperties(TypedDict):
    """Information about the risk factors and possible complications that may follow a topic.

    References:
        https://schema.org/RisksOrComplicationsHealthAspect
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(RisksOrComplicationsHealthAspectInheritedProperties , RisksOrComplicationsHealthAspectProperties, TypedDict):
    pass


class RisksOrComplicationsHealthAspectBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="RisksOrComplicationsHealthAspect",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[RisksOrComplicationsHealthAspectProperties, RisksOrComplicationsHealthAspectInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "RisksOrComplicationsHealthAspect"
    return model
    

RisksOrComplicationsHealthAspect = create_schema_org_model()


def create_risksorcomplicationshealthaspect_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_risksorcomplicationshealthaspect_model(model=model)
    return pydantic_type(model).schema_json()


