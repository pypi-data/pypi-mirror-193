"""
An enumeration of genders.

https://schema.org/GenderType
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class GenderTypeInheritedProperties(TypedDict):
    """An enumeration of genders.

    References:
        https://schema.org/GenderType
    Note:
        Model Depth 4
    Attributes:
        supersededBy: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Relates a term (i.e. a property, class or enumeration) to one that supersedes it.
    """

    supersededBy: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class GenderTypeProperties(TypedDict):
    """An enumeration of genders.

    References:
        https://schema.org/GenderType
    Note:
        Model Depth 4
    Attributes:
    """


class GenderTypeAllProperties(
    GenderTypeInheritedProperties, GenderTypeProperties, TypedDict
):
    pass


class GenderTypeBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="GenderType", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"supersededBy": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        GenderTypeProperties, GenderTypeInheritedProperties, GenderTypeAllProperties
    ] = GenderTypeAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "GenderType"
    return model


GenderType = create_schema_org_model()


def create_gendertype_model(
    model: Union[
        GenderTypeProperties, GenderTypeInheritedProperties, GenderTypeAllProperties
    ]
):
    _type = deepcopy(GenderTypeAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of GenderType. Please see: https://schema.org/GenderType"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: GenderTypeAllProperties):
    pydantic_type = create_gendertype_model(model=model)
    return pydantic_type(model).schema_json()
