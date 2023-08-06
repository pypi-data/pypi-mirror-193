"""
A diet restricted to certain foods or preparations for cultural, religious, health or lifestyle reasons. 

https://schema.org/RestrictedDiet
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class RestrictedDietInheritedProperties(TypedDict):
    """A diet restricted to certain foods or preparations for cultural, religious, health or lifestyle reasons.

    References:
        https://schema.org/RestrictedDiet
    Note:
        Model Depth 4
    Attributes:
        supersededBy: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Relates a term (i.e. a property, class or enumeration) to one that supersedes it.
    """

    supersededBy: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class RestrictedDietProperties(TypedDict):
    """A diet restricted to certain foods or preparations for cultural, religious, health or lifestyle reasons.

    References:
        https://schema.org/RestrictedDiet
    Note:
        Model Depth 4
    Attributes:
    """


class RestrictedDietAllProperties(
    RestrictedDietInheritedProperties, RestrictedDietProperties, TypedDict
):
    pass


class RestrictedDietBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="RestrictedDiet", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"supersededBy": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        RestrictedDietProperties,
        RestrictedDietInheritedProperties,
        RestrictedDietAllProperties,
    ] = RestrictedDietAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "RestrictedDiet"
    return model


RestrictedDiet = create_schema_org_model()


def create_restricteddiet_model(
    model: Union[
        RestrictedDietProperties,
        RestrictedDietInheritedProperties,
        RestrictedDietAllProperties,
    ]
):
    _type = deepcopy(RestrictedDietAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: RestrictedDietAllProperties):
    pydantic_type = create_restricteddiet_model(model=model)
    return pydantic_type(model).schema_json()
