"""
Content that discusses and explains how a particular health-related topic works, e.g. in terms of mechanisms and underlying science.

https://schema.org/HowItWorksHealthAspect
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class HowItWorksHealthAspectInheritedProperties(TypedDict):
    """Content that discusses and explains how a particular health-related topic works, e.g. in terms of mechanisms and underlying science.

    References:
        https://schema.org/HowItWorksHealthAspect
    Note:
        Model Depth 5
    Attributes:
    """


class HowItWorksHealthAspectProperties(TypedDict):
    """Content that discusses and explains how a particular health-related topic works, e.g. in terms of mechanisms and underlying science.

    References:
        https://schema.org/HowItWorksHealthAspect
    Note:
        Model Depth 5
    Attributes:
    """


class HowItWorksHealthAspectAllProperties(
    HowItWorksHealthAspectInheritedProperties,
    HowItWorksHealthAspectProperties,
    TypedDict,
):
    pass


class HowItWorksHealthAspectBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="HowItWorksHealthAspect", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        HowItWorksHealthAspectProperties,
        HowItWorksHealthAspectInheritedProperties,
        HowItWorksHealthAspectAllProperties,
    ] = HowItWorksHealthAspectAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "HowItWorksHealthAspect"
    return model


HowItWorksHealthAspect = create_schema_org_model()


def create_howitworkshealthaspect_model(
    model: Union[
        HowItWorksHealthAspectProperties,
        HowItWorksHealthAspectInheritedProperties,
        HowItWorksHealthAspectAllProperties,
    ]
):
    _type = deepcopy(HowItWorksHealthAspectAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of HowItWorksHealthAspect. Please see: https://schema.org/HowItWorksHealthAspect"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: HowItWorksHealthAspectAllProperties):
    pydantic_type = create_howitworkshealthaspect_model(model=model)
    return pydantic_type(model).schema_json()
