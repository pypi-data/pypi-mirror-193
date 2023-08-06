"""
A school.

https://schema.org/School
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class SchoolInheritedProperties(TypedDict):
    """A school.

    References:
        https://schema.org/School
    Note:
        Model Depth 4
    Attributes:
        alumni: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Alumni of an organization.
    """

    alumni: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class SchoolProperties(TypedDict):
    """A school.

    References:
        https://schema.org/School
    Note:
        Model Depth 4
    Attributes:
    """


class SchoolAllProperties(SchoolInheritedProperties, SchoolProperties, TypedDict):
    pass


class SchoolBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="School", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"alumni": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        SchoolProperties, SchoolInheritedProperties, SchoolAllProperties
    ] = SchoolAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "School"
    return model


School = create_schema_org_model()


def create_school_model(
    model: Union[SchoolProperties, SchoolInheritedProperties, SchoolAllProperties]
):
    _type = deepcopy(SchoolAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: SchoolAllProperties):
    pydantic_type = create_school_model(model=model)
    return pydantic_type(model).schema_json()
