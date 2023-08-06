"""
The day of the week between Wednesday and Friday.

https://schema.org/Thursday
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ThursdayInheritedProperties(TypedDict):
    """The day of the week between Wednesday and Friday.

    References:
        https://schema.org/Thursday
    Note:
        Model Depth 5
    Attributes:
    """


class ThursdayProperties(TypedDict):
    """The day of the week between Wednesday and Friday.

    References:
        https://schema.org/Thursday
    Note:
        Model Depth 5
    Attributes:
    """


class ThursdayAllProperties(ThursdayInheritedProperties, ThursdayProperties, TypedDict):
    pass


class ThursdayBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Thursday", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        ThursdayProperties, ThursdayInheritedProperties, ThursdayAllProperties
    ] = ThursdayAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Thursday"
    return model


Thursday = create_schema_org_model()


def create_thursday_model(
    model: Union[ThursdayProperties, ThursdayInheritedProperties, ThursdayAllProperties]
):
    _type = deepcopy(ThursdayAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of Thursday. Please see: https://schema.org/Thursday"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: ThursdayAllProperties):
    pydantic_type = create_thursday_model(model=model)
    return pydantic_type(model).schema_json()
