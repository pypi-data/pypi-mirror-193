"""
The female gender.

https://schema.org/Female
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class FemaleInheritedProperties(TypedDict):
    """The female gender.

    References:
        https://schema.org/Female
    Note:
        Model Depth 5
    Attributes:
    """


class FemaleProperties(TypedDict):
    """The female gender.

    References:
        https://schema.org/Female
    Note:
        Model Depth 5
    Attributes:
    """


class FemaleAllProperties(FemaleInheritedProperties, FemaleProperties, TypedDict):
    pass


class FemaleBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Female", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        FemaleProperties, FemaleInheritedProperties, FemaleAllProperties
    ] = FemaleAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Female"
    return model


Female = create_schema_org_model()


def create_female_model(
    model: Union[FemaleProperties, FemaleInheritedProperties, FemaleAllProperties]
):
    _type = deepcopy(FemaleAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: FemaleAllProperties):
    pydantic_type = create_female_model(model=model)
    return pydantic_type(model).schema_json()
