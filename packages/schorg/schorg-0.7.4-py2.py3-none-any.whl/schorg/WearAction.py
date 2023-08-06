"""
The act of dressing oneself in clothing.

https://schema.org/WearAction
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class WearActionInheritedProperties(TypedDict):
    """The act of dressing oneself in clothing.

    References:
        https://schema.org/WearAction
    Note:
        Model Depth 5
    Attributes:
    """


class WearActionProperties(TypedDict):
    """The act of dressing oneself in clothing.

    References:
        https://schema.org/WearAction
    Note:
        Model Depth 5
    Attributes:
    """


class WearActionAllProperties(
    WearActionInheritedProperties, WearActionProperties, TypedDict
):
    pass


class WearActionBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="WearAction", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        WearActionProperties, WearActionInheritedProperties, WearActionAllProperties
    ] = WearActionAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "WearAction"
    return model


WearAction = create_schema_org_model()


def create_wearaction_model(
    model: Union[
        WearActionProperties, WearActionInheritedProperties, WearActionAllProperties
    ]
):
    _type = deepcopy(WearActionAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of WearActionAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: WearActionAllProperties):
    pydantic_type = create_wearaction_model(model=model)
    return pydantic_type(model).schema_json()
