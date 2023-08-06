"""
A list of possible statuses for the legal force of a legislation.

https://schema.org/LegalForceStatus
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class LegalForceStatusInheritedProperties(TypedDict):
    """A list of possible statuses for the legal force of a legislation.

    References:
        https://schema.org/LegalForceStatus
    Note:
        Model Depth 5
    Attributes:
    """


class LegalForceStatusProperties(TypedDict):
    """A list of possible statuses for the legal force of a legislation.

    References:
        https://schema.org/LegalForceStatus
    Note:
        Model Depth 5
    Attributes:
    """


class LegalForceStatusAllProperties(
    LegalForceStatusInheritedProperties, LegalForceStatusProperties, TypedDict
):
    pass


class LegalForceStatusBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="LegalForceStatus", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        LegalForceStatusProperties,
        LegalForceStatusInheritedProperties,
        LegalForceStatusAllProperties,
    ] = LegalForceStatusAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "LegalForceStatus"
    return model


LegalForceStatus = create_schema_org_model()


def create_legalforcestatus_model(
    model: Union[
        LegalForceStatusProperties,
        LegalForceStatusInheritedProperties,
        LegalForceStatusAllProperties,
    ]
):
    _type = deepcopy(LegalForceStatusAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of LegalForceStatusAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: LegalForceStatusAllProperties):
    pydantic_type = create_legalforcestatus_model(model=model)
    return pydantic_type(model).schema_json()
