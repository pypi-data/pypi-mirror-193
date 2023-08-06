"""
Content about how, when, frequency and dosage of a topic.

https://schema.org/UsageOrScheduleHealthAspect
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class UsageOrScheduleHealthAspectInheritedProperties(TypedDict):
    """Content about how, when, frequency and dosage of a topic.

    References:
        https://schema.org/UsageOrScheduleHealthAspect
    Note:
        Model Depth 5
    Attributes:
    """


class UsageOrScheduleHealthAspectProperties(TypedDict):
    """Content about how, when, frequency and dosage of a topic.

    References:
        https://schema.org/UsageOrScheduleHealthAspect
    Note:
        Model Depth 5
    Attributes:
    """


class UsageOrScheduleHealthAspectAllProperties(
    UsageOrScheduleHealthAspectInheritedProperties,
    UsageOrScheduleHealthAspectProperties,
    TypedDict,
):
    pass


class UsageOrScheduleHealthAspectBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="UsageOrScheduleHealthAspect", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        UsageOrScheduleHealthAspectProperties,
        UsageOrScheduleHealthAspectInheritedProperties,
        UsageOrScheduleHealthAspectAllProperties,
    ] = UsageOrScheduleHealthAspectAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "UsageOrScheduleHealthAspect"
    return model


UsageOrScheduleHealthAspect = create_schema_org_model()


def create_usageorschedulehealthaspect_model(
    model: Union[
        UsageOrScheduleHealthAspectProperties,
        UsageOrScheduleHealthAspectInheritedProperties,
        UsageOrScheduleHealthAspectAllProperties,
    ]
):
    _type = deepcopy(UsageOrScheduleHealthAspectAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: UsageOrScheduleHealthAspectAllProperties):
    pydantic_type = create_usageorschedulehealthaspect_model(model=model)
    return pydantic_type(model).schema_json()
