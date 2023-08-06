"""
The act of starting or activating a device or application (e.g. starting a timer or turning on a flashlight).

https://schema.org/ActivateAction
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ActivateActionInheritedProperties(TypedDict):
    """The act of starting or activating a device or application (e.g. starting a timer or turning on a flashlight).

    References:
        https://schema.org/ActivateAction
    Note:
        Model Depth 4
    Attributes:
    """

    


class ActivateActionProperties(TypedDict):
    """The act of starting or activating a device or application (e.g. starting a timer or turning on a flashlight).

    References:
        https://schema.org/ActivateAction
    Note:
        Model Depth 4
    Attributes:
    """

    


class AllProperties(ActivateActionInheritedProperties , ActivateActionProperties, TypedDict):
    pass


class ActivateActionBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="ActivateAction",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[ActivateActionProperties, ActivateActionInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ActivateAction"
    return model
    

ActivateAction = create_schema_org_model()


def create_activateaction_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_activateaction_model(model=model)
    return pydantic_type(model).schema_json()


