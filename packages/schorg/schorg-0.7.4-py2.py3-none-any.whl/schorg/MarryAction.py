"""
The act of marrying a person.

https://schema.org/MarryAction
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


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


class MarryActionAllProperties(
    MarryActionInheritedProperties, MarryActionProperties, TypedDict
):
    pass


class MarryActionBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="MarryAction", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        MarryActionProperties, MarryActionInheritedProperties, MarryActionAllProperties
    ] = MarryActionAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MarryAction"
    return model


MarryAction = create_schema_org_model()


def create_marryaction_model(
    model: Union[
        MarryActionProperties, MarryActionInheritedProperties, MarryActionAllProperties
    ]
):
    _type = deepcopy(MarryActionAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of MarryActionAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: MarryActionAllProperties):
    pydantic_type = create_marryaction_model(model=model)
    return pydantic_type(model).schema_json()
