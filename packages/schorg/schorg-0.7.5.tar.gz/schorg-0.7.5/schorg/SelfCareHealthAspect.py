"""
Self care actions or measures that can be taken to sooth, health or avoid a topic. This may be carried at home and can be carried/managed by the person itself.

https://schema.org/SelfCareHealthAspect
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class SelfCareHealthAspectInheritedProperties(TypedDict):
    """Self care actions or measures that can be taken to sooth, health or avoid a topic. This may be carried at home and can be carried/managed by the person itself.

    References:
        https://schema.org/SelfCareHealthAspect
    Note:
        Model Depth 5
    Attributes:
    """


class SelfCareHealthAspectProperties(TypedDict):
    """Self care actions or measures that can be taken to sooth, health or avoid a topic. This may be carried at home and can be carried/managed by the person itself.

    References:
        https://schema.org/SelfCareHealthAspect
    Note:
        Model Depth 5
    Attributes:
    """


class SelfCareHealthAspectAllProperties(
    SelfCareHealthAspectInheritedProperties, SelfCareHealthAspectProperties, TypedDict
):
    pass


class SelfCareHealthAspectBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="SelfCareHealthAspect", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        SelfCareHealthAspectProperties,
        SelfCareHealthAspectInheritedProperties,
        SelfCareHealthAspectAllProperties,
    ] = SelfCareHealthAspectAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "SelfCareHealthAspect"
    return model


SelfCareHealthAspect = create_schema_org_model()


def create_selfcarehealthaspect_model(
    model: Union[
        SelfCareHealthAspectProperties,
        SelfCareHealthAspectInheritedProperties,
        SelfCareHealthAspectAllProperties,
    ]
):
    _type = deepcopy(SelfCareHealthAspectAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of SelfCareHealthAspect. Please see: https://schema.org/SelfCareHealthAspect"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: SelfCareHealthAspectAllProperties):
    pydantic_type = create_selfcarehealthaspect_model(model=model)
    return pydantic_type(model).schema_json()
