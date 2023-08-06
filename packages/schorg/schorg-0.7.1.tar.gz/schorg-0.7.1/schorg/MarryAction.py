"""
The act of marrying a person.

https://schema.org/MarryAction
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MarryActionInheritedProperties(TypedDict):
    """The act of marrying a person.

    References:
        https://schema.org/MarryAction
    Note:
        Model Depth 4
    Attributes:
    """

    


class MarryActionProperties(TypedDict):
    """The act of marrying a person.

    References:
        https://schema.org/MarryAction
    Note:
        Model Depth 4
    Attributes:
    """

    


class AllProperties(MarryActionInheritedProperties , MarryActionProperties, TypedDict):
    pass


class MarryActionBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="MarryAction",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[MarryActionProperties, MarryActionInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MarryAction"
    return model
    

MarryAction = create_schema_org_model()


def create_marryaction_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_marryaction_model(model=model)
    return pydantic_type(model).schema_json()


