"""
Indicates a document for which the text is conclusively what the law says and is legally binding. (E.g. the digitally signed version of an Official Journal.)  Something "Definitive" is considered to be also [[AuthoritativeLegalValue]].

https://schema.org/DefinitiveLegalValue
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class DefinitiveLegalValueInheritedProperties(TypedDict):
    """Indicates a document for which the text is conclusively what the law says and is legally binding. (E.g. the digitally signed version of an Official Journal.)  Something "Definitive" is considered to be also [[AuthoritativeLegalValue]].

    References:
        https://schema.org/DefinitiveLegalValue
    Note:
        Model Depth 5
    Attributes:
    """


class DefinitiveLegalValueProperties(TypedDict):
    """Indicates a document for which the text is conclusively what the law says and is legally binding. (E.g. the digitally signed version of an Official Journal.)  Something "Definitive" is considered to be also [[AuthoritativeLegalValue]].

    References:
        https://schema.org/DefinitiveLegalValue
    Note:
        Model Depth 5
    Attributes:
    """


class DefinitiveLegalValueAllProperties(
    DefinitiveLegalValueInheritedProperties, DefinitiveLegalValueProperties, TypedDict
):
    pass


class DefinitiveLegalValueBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="DefinitiveLegalValue", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        DefinitiveLegalValueProperties,
        DefinitiveLegalValueInheritedProperties,
        DefinitiveLegalValueAllProperties,
    ] = DefinitiveLegalValueAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "DefinitiveLegalValue"
    return model


DefinitiveLegalValue = create_schema_org_model()


def create_definitivelegalvalue_model(
    model: Union[
        DefinitiveLegalValueProperties,
        DefinitiveLegalValueInheritedProperties,
        DefinitiveLegalValueAllProperties,
    ]
):
    _type = deepcopy(DefinitiveLegalValueAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of DefinitiveLegalValue. Please see: https://schema.org/DefinitiveLegalValue"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: DefinitiveLegalValueAllProperties):
    pydantic_type = create_definitivelegalvalue_model(model=model)
    return pydantic_type(model).schema_json()
