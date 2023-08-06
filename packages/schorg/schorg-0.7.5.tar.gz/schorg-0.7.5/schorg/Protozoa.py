"""
Single-celled organism that causes an infection.

https://schema.org/Protozoa
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ProtozoaInheritedProperties(TypedDict):
    """Single-celled organism that causes an infection.

    References:
        https://schema.org/Protozoa
    Note:
        Model Depth 6
    Attributes:
    """


class ProtozoaProperties(TypedDict):
    """Single-celled organism that causes an infection.

    References:
        https://schema.org/Protozoa
    Note:
        Model Depth 6
    Attributes:
    """


class ProtozoaAllProperties(ProtozoaInheritedProperties, ProtozoaProperties, TypedDict):
    pass


class ProtozoaBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Protozoa", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        ProtozoaProperties, ProtozoaInheritedProperties, ProtozoaAllProperties
    ] = ProtozoaAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Protozoa"
    return model


Protozoa = create_schema_org_model()


def create_protozoa_model(
    model: Union[ProtozoaProperties, ProtozoaInheritedProperties, ProtozoaAllProperties]
):
    _type = deepcopy(ProtozoaAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of Protozoa. Please see: https://schema.org/Protozoa"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: ProtozoaAllProperties):
    pydantic_type = create_protozoa_model(model=model)
    return pydantic_type(model).schema_json()
