"""
Pathogenic bacteria that cause bacterial infection.

https://schema.org/Bacteria
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class BacteriaInheritedProperties(TypedDict):
    """Pathogenic bacteria that cause bacterial infection.

    References:
        https://schema.org/Bacteria
    Note:
        Model Depth 6
    Attributes:
    """


class BacteriaProperties(TypedDict):
    """Pathogenic bacteria that cause bacterial infection.

    References:
        https://schema.org/Bacteria
    Note:
        Model Depth 6
    Attributes:
    """


class BacteriaAllProperties(BacteriaInheritedProperties, BacteriaProperties, TypedDict):
    pass


class BacteriaBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Bacteria", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        BacteriaProperties, BacteriaInheritedProperties, BacteriaAllProperties
    ] = BacteriaAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Bacteria"
    return model


Bacteria = create_schema_org_model()


def create_bacteria_model(
    model: Union[BacteriaProperties, BacteriaInheritedProperties, BacteriaAllProperties]
):
    _type = deepcopy(BacteriaAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of BacteriaAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: BacteriaAllProperties):
    pydantic_type = create_bacteria_model(model=model)
    return pydantic_type(model).schema_json()
