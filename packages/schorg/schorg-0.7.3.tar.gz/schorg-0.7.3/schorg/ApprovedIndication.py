"""
An indication for a medical therapy that has been formally specified or approved by a regulatory body that regulates use of the therapy; for example, the US FDA approves indications for most drugs in the US.

https://schema.org/ApprovedIndication
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ApprovedIndicationInheritedProperties(TypedDict):
    """An indication for a medical therapy that has been formally specified or approved by a regulatory body that regulates use of the therapy; for example, the US FDA approves indications for most drugs in the US.

    References:
        https://schema.org/ApprovedIndication
    Note:
        Model Depth 4
    Attributes:
    """


class ApprovedIndicationProperties(TypedDict):
    """An indication for a medical therapy that has been formally specified or approved by a regulatory body that regulates use of the therapy; for example, the US FDA approves indications for most drugs in the US.

    References:
        https://schema.org/ApprovedIndication
    Note:
        Model Depth 4
    Attributes:
    """


class ApprovedIndicationAllProperties(
    ApprovedIndicationInheritedProperties, ApprovedIndicationProperties, TypedDict
):
    pass


class ApprovedIndicationBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="ApprovedIndication", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        ApprovedIndicationProperties,
        ApprovedIndicationInheritedProperties,
        ApprovedIndicationAllProperties,
    ] = ApprovedIndicationAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ApprovedIndication"
    return model


ApprovedIndication = create_schema_org_model()


def create_approvedindication_model(
    model: Union[
        ApprovedIndicationProperties,
        ApprovedIndicationInheritedProperties,
        ApprovedIndicationAllProperties,
    ]
):
    _type = deepcopy(ApprovedIndicationAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: ApprovedIndicationAllProperties):
    pydantic_type = create_approvedindication_model(model=model)
    return pydantic_type(model).schema_json()
