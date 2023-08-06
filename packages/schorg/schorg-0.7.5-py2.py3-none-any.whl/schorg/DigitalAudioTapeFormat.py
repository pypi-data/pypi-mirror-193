"""
DigitalAudioTapeFormat.

https://schema.org/DigitalAudioTapeFormat
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class DigitalAudioTapeFormatInheritedProperties(TypedDict):
    """DigitalAudioTapeFormat.

    References:
        https://schema.org/DigitalAudioTapeFormat
    Note:
        Model Depth 5
    Attributes:
    """


class DigitalAudioTapeFormatProperties(TypedDict):
    """DigitalAudioTapeFormat.

    References:
        https://schema.org/DigitalAudioTapeFormat
    Note:
        Model Depth 5
    Attributes:
    """


class DigitalAudioTapeFormatAllProperties(
    DigitalAudioTapeFormatInheritedProperties,
    DigitalAudioTapeFormatProperties,
    TypedDict,
):
    pass


class DigitalAudioTapeFormatBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="DigitalAudioTapeFormat", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        DigitalAudioTapeFormatProperties,
        DigitalAudioTapeFormatInheritedProperties,
        DigitalAudioTapeFormatAllProperties,
    ] = DigitalAudioTapeFormatAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "DigitalAudioTapeFormat"
    return model


DigitalAudioTapeFormat = create_schema_org_model()


def create_digitalaudiotapeformat_model(
    model: Union[
        DigitalAudioTapeFormatProperties,
        DigitalAudioTapeFormatInheritedProperties,
        DigitalAudioTapeFormatAllProperties,
    ]
):
    _type = deepcopy(DigitalAudioTapeFormatAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of DigitalAudioTapeFormat. Please see: https://schema.org/DigitalAudioTapeFormat"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: DigitalAudioTapeFormatAllProperties):
    pydantic_type = create_digitalaudiotapeformat_model(model=model)
    return pydantic_type(model).schema_json()
