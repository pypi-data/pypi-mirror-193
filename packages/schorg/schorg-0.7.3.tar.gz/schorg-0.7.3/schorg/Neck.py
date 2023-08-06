"""
Neck assessment with clinical examination.

https://schema.org/Neck
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class NeckInheritedProperties(TypedDict):
    """Neck assessment with clinical examination.

    References:
        https://schema.org/Neck
    Note:
        Model Depth 5
    Attributes:
    """


class NeckProperties(TypedDict):
    """Neck assessment with clinical examination.

    References:
        https://schema.org/Neck
    Note:
        Model Depth 5
    Attributes:
    """


class NeckAllProperties(NeckInheritedProperties, NeckProperties, TypedDict):
    pass


class NeckBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Neck", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        NeckProperties, NeckInheritedProperties, NeckAllProperties
    ] = NeckAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Neck"
    return model


Neck = create_schema_org_model()


def create_neck_model(
    model: Union[NeckProperties, NeckInheritedProperties, NeckAllProperties]
):
    _type = deepcopy(NeckAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: NeckAllProperties):
    pydantic_type = create_neck_model(model=model)
    return pydantic_type(model).schema_json()
