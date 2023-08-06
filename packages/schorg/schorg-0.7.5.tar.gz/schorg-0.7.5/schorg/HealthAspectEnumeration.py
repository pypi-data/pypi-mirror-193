"""
HealthAspectEnumeration enumerates several aspects of health content online, each of which might be described using [[hasHealthAspect]] and [[HealthTopicContent]].

https://schema.org/HealthAspectEnumeration
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class HealthAspectEnumerationInheritedProperties(TypedDict):
    """HealthAspectEnumeration enumerates several aspects of health content online, each of which might be described using [[hasHealthAspect]] and [[HealthTopicContent]].

    References:
        https://schema.org/HealthAspectEnumeration
    Note:
        Model Depth 4
    Attributes:
        supersededBy: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Relates a term (i.e. a property, class or enumeration) to one that supersedes it.
    """

    supersededBy: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class HealthAspectEnumerationProperties(TypedDict):
    """HealthAspectEnumeration enumerates several aspects of health content online, each of which might be described using [[hasHealthAspect]] and [[HealthTopicContent]].

    References:
        https://schema.org/HealthAspectEnumeration
    Note:
        Model Depth 4
    Attributes:
    """


class HealthAspectEnumerationAllProperties(
    HealthAspectEnumerationInheritedProperties,
    HealthAspectEnumerationProperties,
    TypedDict,
):
    pass


class HealthAspectEnumerationBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="HealthAspectEnumeration", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"supersededBy": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        HealthAspectEnumerationProperties,
        HealthAspectEnumerationInheritedProperties,
        HealthAspectEnumerationAllProperties,
    ] = HealthAspectEnumerationAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "HealthAspectEnumeration"
    return model


HealthAspectEnumeration = create_schema_org_model()


def create_healthaspectenumeration_model(
    model: Union[
        HealthAspectEnumerationProperties,
        HealthAspectEnumerationInheritedProperties,
        HealthAspectEnumerationAllProperties,
    ]
):
    _type = deepcopy(HealthAspectEnumerationAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of HealthAspectEnumeration. Please see: https://schema.org/HealthAspectEnumeration"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: HealthAspectEnumerationAllProperties):
    pydantic_type = create_healthaspectenumeration_model(model=model)
    return pydantic_type(model).schema_json()
