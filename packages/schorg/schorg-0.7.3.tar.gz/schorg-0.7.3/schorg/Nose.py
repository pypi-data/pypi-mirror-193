"""
Nose function assessment with clinical examination.

https://schema.org/Nose
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class NoseInheritedProperties(TypedDict):
    """Nose function assessment with clinical examination.

    References:
        https://schema.org/Nose
    Note:
        Model Depth 5
    Attributes:
    """


class NoseProperties(TypedDict):
    """Nose function assessment with clinical examination.

    References:
        https://schema.org/Nose
    Note:
        Model Depth 5
    Attributes:
    """


class NoseAllProperties(NoseInheritedProperties, NoseProperties, TypedDict):
    pass


class NoseBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Nose", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        NoseProperties, NoseInheritedProperties, NoseAllProperties
    ] = NoseAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Nose"
    return model


Nose = create_schema_org_model()


def create_nose_model(
    model: Union[NoseProperties, NoseInheritedProperties, NoseAllProperties]
):
    _type = deepcopy(NoseAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: NoseAllProperties):
    pydantic_type = create_nose_model(model=model)
    return pydantic_type(model).schema_json()
