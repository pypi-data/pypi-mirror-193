"""
Book format: Ebook.

https://schema.org/EBook
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class EBookInheritedProperties(TypedDict):
    """Book format: Ebook.

    References:
        https://schema.org/EBook
    Note:
        Model Depth 5
    Attributes:
    """


class EBookProperties(TypedDict):
    """Book format: Ebook.

    References:
        https://schema.org/EBook
    Note:
        Model Depth 5
    Attributes:
    """


class EBookAllProperties(EBookInheritedProperties, EBookProperties, TypedDict):
    pass


class EBookBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="EBook", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        EBookProperties, EBookInheritedProperties, EBookAllProperties
    ] = EBookAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "EBook"
    return model


EBook = create_schema_org_model()


def create_ebook_model(
    model: Union[EBookProperties, EBookInheritedProperties, EBookAllProperties]
):
    _type = deepcopy(EBookAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: EBookAllProperties):
    pydantic_type = create_ebook_model(model=model)
    return pydantic_type(model).schema_json()
