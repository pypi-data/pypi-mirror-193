"""
Lists or enumerations—for example, a list of cuisines or music genres, etc.

https://schema.org/Enumeration
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class EnumerationInheritedProperties(TypedDict):
    """Lists or enumerations—for example, a list of cuisines or music genres, etc.

    References:
        https://schema.org/Enumeration
    Note:
        Model Depth 3
    Attributes:
    """


class EnumerationProperties(TypedDict):
    """Lists or enumerations—for example, a list of cuisines or music genres, etc.

    References:
        https://schema.org/Enumeration
    Note:
        Model Depth 3
    Attributes:
        supersededBy: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Relates a term (i.e. a property, class or enumeration) to one that supersedes it.
    """

    supersededBy: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]


class EnumerationAllProperties(
    EnumerationInheritedProperties, EnumerationProperties, TypedDict
):
    pass


class EnumerationBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Enumeration", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"supersededBy": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        EnumerationProperties, EnumerationInheritedProperties, EnumerationAllProperties
    ] = EnumerationAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Enumeration"
    return model


Enumeration = create_schema_org_model()


def create_enumeration_model(
    model: Union[
        EnumerationProperties, EnumerationInheritedProperties, EnumerationAllProperties
    ]
):
    _type = deepcopy(EnumerationAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of EnumerationAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: EnumerationAllProperties):
    pydantic_type = create_enumeration_model(model=model)
    return pydantic_type(model).schema_json()
