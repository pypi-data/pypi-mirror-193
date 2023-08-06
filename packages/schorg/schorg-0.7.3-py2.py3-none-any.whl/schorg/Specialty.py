"""
Any branch of a field in which people typically develop specific expertise, usually after significant study, time, and effort.

https://schema.org/Specialty
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class SpecialtyInheritedProperties(TypedDict):
    """Any branch of a field in which people typically develop specific expertise, usually after significant study, time, and effort.

    References:
        https://schema.org/Specialty
    Note:
        Model Depth 4
    Attributes:
        supersededBy: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Relates a term (i.e. a property, class or enumeration) to one that supersedes it.
    """

    supersededBy: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class SpecialtyProperties(TypedDict):
    """Any branch of a field in which people typically develop specific expertise, usually after significant study, time, and effort.

    References:
        https://schema.org/Specialty
    Note:
        Model Depth 4
    Attributes:
    """


class SpecialtyAllProperties(
    SpecialtyInheritedProperties, SpecialtyProperties, TypedDict
):
    pass


class SpecialtyBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Specialty", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"supersededBy": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        SpecialtyProperties, SpecialtyInheritedProperties, SpecialtyAllProperties
    ] = SpecialtyAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Specialty"
    return model


Specialty = create_schema_org_model()


def create_specialty_model(
    model: Union[
        SpecialtyProperties, SpecialtyInheritedProperties, SpecialtyAllProperties
    ]
):
    _type = deepcopy(SpecialtyAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: SpecialtyAllProperties):
    pydantic_type = create_specialty_model(model=model)
    return pydantic_type(model).schema_json()
