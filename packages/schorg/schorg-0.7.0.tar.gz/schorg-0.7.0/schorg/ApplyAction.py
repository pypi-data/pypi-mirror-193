"""
The act of registering to an organization/service without the guarantee to receive it.Related actions:* [[RegisterAction]]: Unlike RegisterAction, ApplyAction has no guarantees that the application will be accepted.

https://schema.org/ApplyAction
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ApplyActionInheritedProperties(TypedDict):
    """The act of registering to an organization/service without the guarantee to receive it.Related actions:* [[RegisterAction]]: Unlike RegisterAction, ApplyAction has no guarantees that the application will be accepted.

    References:
        https://schema.org/ApplyAction
    Note:
        Model Depth 4
    Attributes:
    """

    


class ApplyActionProperties(TypedDict):
    """The act of registering to an organization/service without the guarantee to receive it.Related actions:* [[RegisterAction]]: Unlike RegisterAction, ApplyAction has no guarantees that the application will be accepted.

    References:
        https://schema.org/ApplyAction
    Note:
        Model Depth 4
    Attributes:
    """

    


class AllProperties(ApplyActionInheritedProperties , ApplyActionProperties, TypedDict):
    pass


class ApplyActionBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="ApplyAction",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[ApplyActionProperties, ApplyActionInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ApplyAction"
    return model
    

ApplyAction = create_schema_org_model()


def create_applyaction_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_applyaction_model(model=model)
    return pydantic_type(model).schema_json()


