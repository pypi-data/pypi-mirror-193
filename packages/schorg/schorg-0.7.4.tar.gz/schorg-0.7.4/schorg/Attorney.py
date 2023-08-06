"""
Professional service: Attorney. This type is deprecated - [[LegalService]] is more inclusive and less ambiguous.

https://schema.org/Attorney
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class AttorneyInheritedProperties(TypedDict):
    """Professional service: Attorney. This type is deprecated - [[LegalService]] is more inclusive and less ambiguous.

    References:
        https://schema.org/Attorney
    Note:
        Model Depth 5
    Attributes:
    """


class AttorneyProperties(TypedDict):
    """Professional service: Attorney. This type is deprecated - [[LegalService]] is more inclusive and less ambiguous.

    References:
        https://schema.org/Attorney
    Note:
        Model Depth 5
    Attributes:
    """


class AttorneyAllProperties(AttorneyInheritedProperties, AttorneyProperties, TypedDict):
    pass


class AttorneyBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Attorney", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        AttorneyProperties, AttorneyInheritedProperties, AttorneyAllProperties
    ] = AttorneyAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Attorney"
    return model


Attorney = create_schema_org_model()


def create_attorney_model(
    model: Union[AttorneyProperties, AttorneyInheritedProperties, AttorneyAllProperties]
):
    _type = deepcopy(AttorneyAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of AttorneyAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AttorneyAllProperties):
    pydantic_type = create_attorney_model(model=model)
    return pydantic_type(model).schema_json()
