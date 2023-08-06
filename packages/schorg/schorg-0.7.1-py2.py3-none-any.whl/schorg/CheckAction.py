"""
An agent inspects, determines, investigates, inquires, or examines an object's accuracy, quality, condition, or state.

https://schema.org/CheckAction
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class CheckActionInheritedProperties(TypedDict):
    """An agent inspects, determines, investigates, inquires, or examines an object's accuracy, quality, condition, or state.

    References:
        https://schema.org/CheckAction
    Note:
        Model Depth 4
    Attributes:
    """

    


class CheckActionProperties(TypedDict):
    """An agent inspects, determines, investigates, inquires, or examines an object's accuracy, quality, condition, or state.

    References:
        https://schema.org/CheckAction
    Note:
        Model Depth 4
    Attributes:
    """

    


class AllProperties(CheckActionInheritedProperties , CheckActionProperties, TypedDict):
    pass


class CheckActionBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="CheckAction",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[CheckActionProperties, CheckActionInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "CheckAction"
    return model
    

CheckAction = create_schema_org_model()


def create_checkaction_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_checkaction_model(model=model)
    return pydantic_type(model).schema_json()


