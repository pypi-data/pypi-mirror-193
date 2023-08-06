"""
Enumerated options related to a ContactPoint.

https://schema.org/ContactPointOption
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ContactPointOptionInheritedProperties(TypedDict):
    """Enumerated options related to a ContactPoint.

    References:
        https://schema.org/ContactPointOption
    Note:
        Model Depth 4
    Attributes:
        supersededBy: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Relates a term (i.e. a property, class or enumeration) to one that supersedes it.
    """

    supersededBy: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]


class ContactPointOptionProperties(TypedDict):
    """Enumerated options related to a ContactPoint.

    References:
        https://schema.org/ContactPointOption
    Note:
        Model Depth 4
    Attributes:
    """


class ContactPointOptionAllProperties(
    ContactPointOptionInheritedProperties, ContactPointOptionProperties, TypedDict
):
    pass


class ContactPointOptionBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="ContactPointOption", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"supersededBy": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        ContactPointOptionProperties,
        ContactPointOptionInheritedProperties,
        ContactPointOptionAllProperties,
    ] = ContactPointOptionAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ContactPointOption"
    return model


ContactPointOption = create_schema_org_model()


def create_contactpointoption_model(
    model: Union[
        ContactPointOptionProperties,
        ContactPointOptionInheritedProperties,
        ContactPointOptionAllProperties,
    ]
):
    _type = deepcopy(ContactPointOptionAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of ContactPointOptionAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: ContactPointOptionAllProperties):
    pydantic_type = create_contactpointoption_model(model=model)
    return pydantic_type(model).schema_json()
