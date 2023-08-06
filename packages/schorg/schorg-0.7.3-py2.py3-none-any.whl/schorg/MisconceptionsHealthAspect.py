"""
Content about common misconceptions and myths that are related to a topic.

https://schema.org/MisconceptionsHealthAspect
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MisconceptionsHealthAspectInheritedProperties(TypedDict):
    """Content about common misconceptions and myths that are related to a topic.

    References:
        https://schema.org/MisconceptionsHealthAspect
    Note:
        Model Depth 5
    Attributes:
    """


class MisconceptionsHealthAspectProperties(TypedDict):
    """Content about common misconceptions and myths that are related to a topic.

    References:
        https://schema.org/MisconceptionsHealthAspect
    Note:
        Model Depth 5
    Attributes:
    """


class MisconceptionsHealthAspectAllProperties(
    MisconceptionsHealthAspectInheritedProperties,
    MisconceptionsHealthAspectProperties,
    TypedDict,
):
    pass


class MisconceptionsHealthAspectBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="MisconceptionsHealthAspect", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        MisconceptionsHealthAspectProperties,
        MisconceptionsHealthAspectInheritedProperties,
        MisconceptionsHealthAspectAllProperties,
    ] = MisconceptionsHealthAspectAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MisconceptionsHealthAspect"
    return model


MisconceptionsHealthAspect = create_schema_org_model()


def create_misconceptionshealthaspect_model(
    model: Union[
        MisconceptionsHealthAspectProperties,
        MisconceptionsHealthAspectInheritedProperties,
        MisconceptionsHealthAspectAllProperties,
    ]
):
    _type = deepcopy(MisconceptionsHealthAspectAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: MisconceptionsHealthAspectAllProperties):
    pydantic_type = create_misconceptionshealthaspect_model(model=model)
    return pydantic_type(model).schema_json()
