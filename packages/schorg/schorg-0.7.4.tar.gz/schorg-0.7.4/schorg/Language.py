"""
Natural languages such as Spanish, Tamil, Hindi, English, etc. Formal language code tags expressed in [BCP 47](https://en.wikipedia.org/wiki/IETF_language_tag) can be used via the [[alternateName]] property. The Language type previously also covered programming languages such as Scheme and Lisp, which are now best represented using [[ComputerLanguage]].

https://schema.org/Language
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class LanguageInheritedProperties(TypedDict):
    """Natural languages such as Spanish, Tamil, Hindi, English, etc. Formal language code tags expressed in [BCP 47](https://en.wikipedia.org/wiki/IETF_language_tag) can be used via the [[alternateName]] property. The Language type previously also covered programming languages such as Scheme and Lisp, which are now best represented using [[ComputerLanguage]].

    References:
        https://schema.org/Language
    Note:
        Model Depth 3
    Attributes:
    """


class LanguageProperties(TypedDict):
    """Natural languages such as Spanish, Tamil, Hindi, English, etc. Formal language code tags expressed in [BCP 47](https://en.wikipedia.org/wiki/IETF_language_tag) can be used via the [[alternateName]] property. The Language type previously also covered programming languages such as Scheme and Lisp, which are now best represented using [[ComputerLanguage]].

    References:
        https://schema.org/Language
    Note:
        Model Depth 3
    Attributes:
    """


class LanguageAllProperties(LanguageInheritedProperties, LanguageProperties, TypedDict):
    pass


class LanguageBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Language", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        LanguageProperties, LanguageInheritedProperties, LanguageAllProperties
    ] = LanguageAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Language"
    return model


Language = create_schema_org_model()


def create_language_model(
    model: Union[LanguageProperties, LanguageInheritedProperties, LanguageAllProperties]
):
    _type = deepcopy(LanguageAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of LanguageAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: LanguageAllProperties):
    pydantic_type = create_language_model(model=model)
    return pydantic_type(model).schema_json()
