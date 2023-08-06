"""
The act of expressing a difference of opinion with the object. An agent disagrees to/about an object (a proposition, topic or theme) with participants.

https://schema.org/DisagreeAction
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class DisagreeActionInheritedProperties(TypedDict):
    """The act of expressing a difference of opinion with the object. An agent disagrees to/about an object (a proposition, topic or theme) with participants.

    References:
        https://schema.org/DisagreeAction
    Note:
        Model Depth 5
    Attributes:
    """

    


class DisagreeActionProperties(TypedDict):
    """The act of expressing a difference of opinion with the object. An agent disagrees to/about an object (a proposition, topic or theme) with participants.

    References:
        https://schema.org/DisagreeAction
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(DisagreeActionInheritedProperties , DisagreeActionProperties, TypedDict):
    pass


class DisagreeActionBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="DisagreeAction",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[DisagreeActionProperties, DisagreeActionInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "DisagreeAction"
    return model
    

DisagreeAction = create_schema_org_model()


def create_disagreeaction_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_disagreeaction_model(model=model)
    return pydantic_type(model).schema_json()


