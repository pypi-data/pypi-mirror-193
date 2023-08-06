"""
The act of rejecting to/adopting an object.Related actions:* [[AcceptAction]]: The antonym of RejectAction.

https://schema.org/RejectAction
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class RejectActionInheritedProperties(TypedDict):
    """The act of rejecting to/adopting an object.Related actions:* [[AcceptAction]]: The antonym of RejectAction.

    References:
        https://schema.org/RejectAction
    Note:
        Model Depth 5
    Attributes:
    """

    


class RejectActionProperties(TypedDict):
    """The act of rejecting to/adopting an object.Related actions:* [[AcceptAction]]: The antonym of RejectAction.

    References:
        https://schema.org/RejectAction
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(RejectActionInheritedProperties , RejectActionProperties, TypedDict):
    pass


class RejectActionBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="RejectAction",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[RejectActionProperties, RejectActionInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "RejectAction"
    return model
    

RejectAction = create_schema_org_model()


def create_rejectaction_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_rejectaction_model(model=model)
    return pydantic_type(model).schema_json()


