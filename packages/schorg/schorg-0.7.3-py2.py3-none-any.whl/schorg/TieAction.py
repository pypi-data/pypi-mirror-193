"""
The act of reaching a draw in a competitive activity.

https://schema.org/TieAction
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


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


class TieActionAllProperties(
    TieActionInheritedProperties, TieActionProperties, TypedDict
):
    pass


class TieActionBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="TieAction", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        TieActionProperties, TieActionInheritedProperties, TieActionAllProperties
    ] = TieActionAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "TieAction"
    return model


TieAction = create_schema_org_model()


def create_tieaction_model(
    model: Union[
        TieActionProperties, TieActionInheritedProperties, TieActionAllProperties
    ]
):
    _type = deepcopy(TieActionAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: TieActionAllProperties):
    pydantic_type = create_tieaction_model(model=model)
    return pydantic_type(model).schema_json()
