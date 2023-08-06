"""
Content about the benefits and advantages of usage or utilization of topic.

https://schema.org/BenefitsHealthAspect
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class BenefitsHealthAspectInheritedProperties(TypedDict):
    """Content about the benefits and advantages of usage or utilization of topic.

    References:
        https://schema.org/BenefitsHealthAspect
    Note:
        Model Depth 5
    Attributes:
    """


class BenefitsHealthAspectProperties(TypedDict):
    """Content about the benefits and advantages of usage or utilization of topic.

    References:
        https://schema.org/BenefitsHealthAspect
    Note:
        Model Depth 5
    Attributes:
    """


class BenefitsHealthAspectAllProperties(
    BenefitsHealthAspectInheritedProperties, BenefitsHealthAspectProperties, TypedDict
):
    pass


class BenefitsHealthAspectBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="BenefitsHealthAspect", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        BenefitsHealthAspectProperties,
        BenefitsHealthAspectInheritedProperties,
        BenefitsHealthAspectAllProperties,
    ] = BenefitsHealthAspectAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "BenefitsHealthAspect"
    return model


BenefitsHealthAspect = create_schema_org_model()


def create_benefitshealthaspect_model(
    model: Union[
        BenefitsHealthAspectProperties,
        BenefitsHealthAspectInheritedProperties,
        BenefitsHealthAspectAllProperties,
    ]
):
    _type = deepcopy(BenefitsHealthAspectAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of BenefitsHealthAspectAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: BenefitsHealthAspectAllProperties):
    pydantic_type = create_benefitshealthaspect_model(model=model)
    return pydantic_type(model).schema_json()
