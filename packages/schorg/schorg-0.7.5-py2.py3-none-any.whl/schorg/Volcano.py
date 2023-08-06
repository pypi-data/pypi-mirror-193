"""
A volcano, like Fujisan.

https://schema.org/Volcano
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class VolcanoInheritedProperties(TypedDict):
    """A volcano, like Fujisan.

    References:
        https://schema.org/Volcano
    Note:
        Model Depth 4
    Attributes:
    """


class VolcanoProperties(TypedDict):
    """A volcano, like Fujisan.

    References:
        https://schema.org/Volcano
    Note:
        Model Depth 4
    Attributes:
    """


class VolcanoAllProperties(VolcanoInheritedProperties, VolcanoProperties, TypedDict):
    pass


class VolcanoBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Volcano", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        VolcanoProperties, VolcanoInheritedProperties, VolcanoAllProperties
    ] = VolcanoAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Volcano"
    return model


Volcano = create_schema_org_model()


def create_volcano_model(
    model: Union[VolcanoProperties, VolcanoInheritedProperties, VolcanoAllProperties]
):
    _type = deepcopy(VolcanoAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of Volcano. Please see: https://schema.org/Volcano"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: VolcanoAllProperties):
    pydantic_type = create_volcano_model(model=model)
    return pydantic_type(model).schema_json()
