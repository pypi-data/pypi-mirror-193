"""
The act of resuming a device or application which was formerly paused (e.g. resume music playback or resume a timer).

https://schema.org/ResumeAction
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ResumeActionInheritedProperties(TypedDict):
    """The act of resuming a device or application which was formerly paused (e.g. resume music playback or resume a timer).

    References:
        https://schema.org/ResumeAction
    Note:
        Model Depth 4
    Attributes:
    """

    


class ResumeActionProperties(TypedDict):
    """The act of resuming a device or application which was formerly paused (e.g. resume music playback or resume a timer).

    References:
        https://schema.org/ResumeAction
    Note:
        Model Depth 4
    Attributes:
    """

    


class AllProperties(ResumeActionInheritedProperties , ResumeActionProperties, TypedDict):
    pass


class ResumeActionBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="ResumeAction",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[ResumeActionProperties, ResumeActionInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ResumeAction"
    return model
    

ResumeAction = create_schema_org_model()


def create_resumeaction_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_resumeaction_model(model=model)
    return pydantic_type(model).schema_json()


