"""
The drug's cost represents the maximum reimbursement paid by an insurer for the drug.

https://schema.org/ReimbursementCap
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ReimbursementCapInheritedProperties(TypedDict):
    """The drug's cost represents the maximum reimbursement paid by an insurer for the drug.

    References:
        https://schema.org/ReimbursementCap
    Note:
        Model Depth 6
    Attributes:
    """


class ReimbursementCapProperties(TypedDict):
    """The drug's cost represents the maximum reimbursement paid by an insurer for the drug.

    References:
        https://schema.org/ReimbursementCap
    Note:
        Model Depth 6
    Attributes:
    """


class ReimbursementCapAllProperties(
    ReimbursementCapInheritedProperties, ReimbursementCapProperties, TypedDict
):
    pass


class ReimbursementCapBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="ReimbursementCap", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        ReimbursementCapProperties,
        ReimbursementCapInheritedProperties,
        ReimbursementCapAllProperties,
    ] = ReimbursementCapAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ReimbursementCap"
    return model


ReimbursementCap = create_schema_org_model()


def create_reimbursementcap_model(
    model: Union[
        ReimbursementCapProperties,
        ReimbursementCapInheritedProperties,
        ReimbursementCapAllProperties,
    ]
):
    _type = deepcopy(ReimbursementCapAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of ReimbursementCap. Please see: https://schema.org/ReimbursementCap"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: ReimbursementCapAllProperties):
    pydantic_type = create_reimbursementcap_model(model=model)
    return pydantic_type(model).schema_json()
