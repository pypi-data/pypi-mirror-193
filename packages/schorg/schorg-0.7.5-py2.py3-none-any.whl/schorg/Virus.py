"""
Pathogenic virus that causes viral infection.

https://schema.org/Virus
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class VirusInheritedProperties(TypedDict):
    """Pathogenic virus that causes viral infection.

    References:
        https://schema.org/Virus
    Note:
        Model Depth 6
    Attributes:
    """


class VirusProperties(TypedDict):
    """Pathogenic virus that causes viral infection.

    References:
        https://schema.org/Virus
    Note:
        Model Depth 6
    Attributes:
    """


class VirusAllProperties(VirusInheritedProperties, VirusProperties, TypedDict):
    pass


class VirusBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Virus", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        VirusProperties, VirusInheritedProperties, VirusAllProperties
    ] = VirusAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Virus"
    return model


Virus = create_schema_org_model()


def create_virus_model(
    model: Union[VirusProperties, VirusInheritedProperties, VirusAllProperties]
):
    _type = deepcopy(VirusAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of Virus. Please see: https://schema.org/Virus"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: VirusAllProperties):
    pydantic_type = create_virus_model(model=model)
    return pydantic_type(model).schema_json()
