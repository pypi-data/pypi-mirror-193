"""
A middle school (typically for children aged around 11-14, although this varies somewhat).

https://schema.org/MiddleSchool
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MiddleSchoolInheritedProperties(TypedDict):
    """A middle school (typically for children aged around 11-14, although this varies somewhat).

    References:
        https://schema.org/MiddleSchool
    Note:
        Model Depth 4
    Attributes:
        alumni: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Alumni of an organization.
    """

    alumni: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class MiddleSchoolProperties(TypedDict):
    """A middle school (typically for children aged around 11-14, although this varies somewhat).

    References:
        https://schema.org/MiddleSchool
    Note:
        Model Depth 4
    Attributes:
    """


class MiddleSchoolAllProperties(
    MiddleSchoolInheritedProperties, MiddleSchoolProperties, TypedDict
):
    pass


class MiddleSchoolBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="MiddleSchool", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"alumni": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        MiddleSchoolProperties,
        MiddleSchoolInheritedProperties,
        MiddleSchoolAllProperties,
    ] = MiddleSchoolAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MiddleSchool"
    return model


MiddleSchool = create_schema_org_model()


def create_middleschool_model(
    model: Union[
        MiddleSchoolProperties,
        MiddleSchoolInheritedProperties,
        MiddleSchoolAllProperties,
    ]
):
    _type = deepcopy(MiddleSchoolAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of MiddleSchool. Please see: https://schema.org/MiddleSchool"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: MiddleSchoolAllProperties):
    pydantic_type = create_middleschool_model(model=model)
    return pydantic_type(model).schema_json()
