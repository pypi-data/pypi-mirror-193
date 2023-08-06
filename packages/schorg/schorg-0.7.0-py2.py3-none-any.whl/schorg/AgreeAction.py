"""
The act of expressing a consistency of opinion with the object. An agent agrees to/about an object (a proposition, topic or theme) with participants.

https://schema.org/AgreeAction
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class AgreeActionInheritedProperties(TypedDict):
    """The act of expressing a consistency of opinion with the object. An agent agrees to/about an object (a proposition, topic or theme) with participants.

    References:
        https://schema.org/AgreeAction
    Note:
        Model Depth 5
    Attributes:
    """

    


class AgreeActionProperties(TypedDict):
    """The act of expressing a consistency of opinion with the object. An agent agrees to/about an object (a proposition, topic or theme) with participants.

    References:
        https://schema.org/AgreeAction
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(AgreeActionInheritedProperties , AgreeActionProperties, TypedDict):
    pass


class AgreeActionBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="AgreeAction",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[AgreeActionProperties, AgreeActionInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "AgreeAction"
    return model
    

AgreeAction = create_schema_org_model()


def create_agreeaction_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_agreeaction_model(model=model)
    return pydantic_type(model).schema_json()


