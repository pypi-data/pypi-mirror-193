"""
The act of expressing a desire about the object. An agent wants an object.

https://schema.org/WantAction
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class WantActionInheritedProperties(TypedDict):
    """The act of expressing a desire about the object. An agent wants an object.

    References:
        https://schema.org/WantAction
    Note:
        Model Depth 5
    Attributes:
    """

    


class WantActionProperties(TypedDict):
    """The act of expressing a desire about the object. An agent wants an object.

    References:
        https://schema.org/WantAction
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(WantActionInheritedProperties , WantActionProperties, TypedDict):
    pass


class WantActionBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="WantAction",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[WantActionProperties, WantActionInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "WantAction"
    return model
    

WantAction = create_schema_org_model()


def create_wantaction_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_wantaction_model(model=model)
    return pydantic_type(model).schema_json()


