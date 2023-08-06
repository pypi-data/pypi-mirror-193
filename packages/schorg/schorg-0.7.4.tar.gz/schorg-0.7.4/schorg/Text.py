"""
Data type: Text.

https://schema.org/Text
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class TextInheritedProperties(TypedDict):
    """Data type: Text.

    References:
        https://schema.org/Text
    Note:
        Model Depth 5
    Attributes:
    """


class TextProperties(TypedDict):
    """Data type: Text.

    References:
        https://schema.org/Text
    Note:
        Model Depth 5
    Attributes:
    """


class TextAllProperties(TextInheritedProperties, TextProperties, TypedDict):
    pass


class TextBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Text", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        TextProperties, TextInheritedProperties, TextAllProperties
    ] = TextAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Text"
    return model


Text = create_schema_org_model()


def create_text_model(
    model: Union[TextProperties, TextInheritedProperties, TextAllProperties]
):
    _type = deepcopy(TextAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of TextAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: TextAllProperties):
    pydantic_type = create_text_model(model=model)
    return pydantic_type(model).schema_json()
