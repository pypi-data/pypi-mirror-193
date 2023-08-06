"""
The act of expressing a desire about the object. An agent wants an object.

https://schema.org/WantAction
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


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


class WantActionAllProperties(
    WantActionInheritedProperties, WantActionProperties, TypedDict
):
    pass


class WantActionBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="WantAction", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        WantActionProperties, WantActionInheritedProperties, WantActionAllProperties
    ] = WantActionAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "WantAction"
    return model


WantAction = create_schema_org_model()


def create_wantaction_model(
    model: Union[
        WantActionProperties, WantActionInheritedProperties, WantActionAllProperties
    ]
):
    _type = deepcopy(WantActionAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of WantAction. Please see: https://schema.org/WantAction"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: WantActionAllProperties):
    pydantic_type = create_wantaction_model(model=model)
    return pydantic_type(model).schema_json()
