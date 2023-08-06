"""
A list of possible levels for the legal validity of a legislation.

https://schema.org/LegalValueLevel
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class LegalValueLevelInheritedProperties(TypedDict):
    """A list of possible levels for the legal validity of a legislation.

    References:
        https://schema.org/LegalValueLevel
    Note:
        Model Depth 4
    Attributes:
        supersededBy: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Relates a term (i.e. a property, class or enumeration) to one that supersedes it.
    """

    supersededBy: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class LegalValueLevelProperties(TypedDict):
    """A list of possible levels for the legal validity of a legislation.

    References:
        https://schema.org/LegalValueLevel
    Note:
        Model Depth 4
    Attributes:
    """


class LegalValueLevelAllProperties(
    LegalValueLevelInheritedProperties, LegalValueLevelProperties, TypedDict
):
    pass


class LegalValueLevelBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="LegalValueLevel", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"supersededBy": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        LegalValueLevelProperties,
        LegalValueLevelInheritedProperties,
        LegalValueLevelAllProperties,
    ] = LegalValueLevelAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "LegalValueLevel"
    return model


LegalValueLevel = create_schema_org_model()


def create_legalvaluelevel_model(
    model: Union[
        LegalValueLevelProperties,
        LegalValueLevelInheritedProperties,
        LegalValueLevelAllProperties,
    ]
):
    _type = deepcopy(LegalValueLevelAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of LegalValueLevel. Please see: https://schema.org/LegalValueLevel"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: LegalValueLevelAllProperties):
    pydantic_type = create_legalvaluelevel_model(model=model)
    return pydantic_type(model).schema_json()
