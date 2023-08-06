"""
The act of producing a visual/graphical representation of an object, typically with a pen/pencil and paper as instruments.

https://schema.org/DrawAction
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class DrawActionInheritedProperties(TypedDict):
    """The act of producing a visual/graphical representation of an object, typically with a pen/pencil and paper as instruments.

    References:
        https://schema.org/DrawAction
    Note:
        Model Depth 4
    Attributes:
    """

    


class DrawActionProperties(TypedDict):
    """The act of producing a visual/graphical representation of an object, typically with a pen/pencil and paper as instruments.

    References:
        https://schema.org/DrawAction
    Note:
        Model Depth 4
    Attributes:
    """

    


class AllProperties(DrawActionInheritedProperties , DrawActionProperties, TypedDict):
    pass


class DrawActionBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="DrawAction",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[DrawActionProperties, DrawActionInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "DrawAction"
    return model
    

DrawAction = create_schema_org_model()


def create_drawaction_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_drawaction_model(model=model)
    return pydantic_type(model).schema_json()


