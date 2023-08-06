"""
Properties that take Mass as values are of the form '&lt;Number&gt; &lt;Mass unit of measure&gt;'. E.g., '7 kg'.

https://schema.org/Mass
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MassInheritedProperties(TypedDict):
    """Properties that take Mass as values are of the form '&lt;Number&gt; &lt;Mass unit of measure&gt;'. E.g., '7 kg'.

    References:
        https://schema.org/Mass
    Note:
        Model Depth 4
    Attributes:
    """


class MassProperties(TypedDict):
    """Properties that take Mass as values are of the form '&lt;Number&gt; &lt;Mass unit of measure&gt;'. E.g., '7 kg'.

    References:
        https://schema.org/Mass
    Note:
        Model Depth 4
    Attributes:
    """


class MassAllProperties(MassInheritedProperties, MassProperties, TypedDict):
    pass


class MassBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Mass", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        MassProperties, MassInheritedProperties, MassAllProperties
    ] = MassAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Mass"
    return model


Mass = create_schema_org_model()


def create_mass_model(
    model: Union[MassProperties, MassInheritedProperties, MassAllProperties]
):
    _type = deepcopy(MassAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of MassAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: MassAllProperties):
    pydantic_type = create_mass_model(model=model)
    return pydantic_type(model).schema_json()
