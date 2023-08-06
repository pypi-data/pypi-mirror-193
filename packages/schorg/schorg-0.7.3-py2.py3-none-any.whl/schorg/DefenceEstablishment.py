"""
A defence establishment, such as an army or navy base.

https://schema.org/DefenceEstablishment
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class DefenceEstablishmentInheritedProperties(TypedDict):
    """A defence establishment, such as an army or navy base.

    References:
        https://schema.org/DefenceEstablishment
    Note:
        Model Depth 5
    Attributes:
    """


class DefenceEstablishmentProperties(TypedDict):
    """A defence establishment, such as an army or navy base.

    References:
        https://schema.org/DefenceEstablishment
    Note:
        Model Depth 5
    Attributes:
    """


class DefenceEstablishmentAllProperties(
    DefenceEstablishmentInheritedProperties, DefenceEstablishmentProperties, TypedDict
):
    pass


class DefenceEstablishmentBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="DefenceEstablishment", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        DefenceEstablishmentProperties,
        DefenceEstablishmentInheritedProperties,
        DefenceEstablishmentAllProperties,
    ] = DefenceEstablishmentAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "DefenceEstablishment"
    return model


DefenceEstablishment = create_schema_org_model()


def create_defenceestablishment_model(
    model: Union[
        DefenceEstablishmentProperties,
        DefenceEstablishmentInheritedProperties,
        DefenceEstablishmentAllProperties,
    ]
):
    _type = deepcopy(DefenceEstablishmentAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: DefenceEstablishmentAllProperties):
    pydantic_type = create_defenceestablishment_model(model=model)
    return pydantic_type(model).schema_json()
