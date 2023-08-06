"""
The act of expressing a positive sentiment about the object. An agent likes an object (a proposition, topic or theme) with participants.

https://schema.org/LikeAction
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class LikeActionInheritedProperties(TypedDict):
    """The act of expressing a positive sentiment about the object. An agent likes an object (a proposition, topic or theme) with participants.

    References:
        https://schema.org/LikeAction
    Note:
        Model Depth 5
    Attributes:
    """

    


class LikeActionProperties(TypedDict):
    """The act of expressing a positive sentiment about the object. An agent likes an object (a proposition, topic or theme) with participants.

    References:
        https://schema.org/LikeAction
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(LikeActionInheritedProperties , LikeActionProperties, TypedDict):
    pass


class LikeActionBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="LikeAction",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[LikeActionProperties, LikeActionInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "LikeAction"
    return model
    

LikeAction = create_schema_org_model()


def create_likeaction_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_likeaction_model(model=model)
    return pydantic_type(model).schema_json()


