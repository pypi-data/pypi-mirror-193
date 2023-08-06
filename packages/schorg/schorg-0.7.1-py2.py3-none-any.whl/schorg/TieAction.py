"""
The act of reaching a draw in a competitive activity.

https://schema.org/TieAction
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class TieActionInheritedProperties(TypedDict):
    """The act of reaching a draw in a competitive activity.

    References:
        https://schema.org/TieAction
    Note:
        Model Depth 4
    Attributes:
    """

    


class TieActionProperties(TypedDict):
    """The act of reaching a draw in a competitive activity.

    References:
        https://schema.org/TieAction
    Note:
        Model Depth 4
    Attributes:
    """

    


class AllProperties(TieActionInheritedProperties , TieActionProperties, TypedDict):
    pass


class TieActionBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="TieAction",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[TieActionProperties, TieActionInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "TieAction"
    return model
    

TieAction = create_schema_org_model()


def create_tieaction_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_tieaction_model(model=model)
    return pydantic_type(model).schema_json()


