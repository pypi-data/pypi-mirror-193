"""
The act of rejecting to/adopting an object.Related actions:* [[AcceptAction]]: The antonym of RejectAction.

https://schema.org/RejectAction
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class RejectActionInheritedProperties(TypedDict):
    """The act of rejecting to/adopting an object.Related actions:* [[AcceptAction]]: The antonym of RejectAction.

    References:
        https://schema.org/RejectAction
    Note:
        Model Depth 5
    Attributes:
    """


class RejectActionProperties(TypedDict):
    """The act of rejecting to/adopting an object.Related actions:* [[AcceptAction]]: The antonym of RejectAction.

    References:
        https://schema.org/RejectAction
    Note:
        Model Depth 5
    Attributes:
    """


class RejectActionAllProperties(
    RejectActionInheritedProperties, RejectActionProperties, TypedDict
):
    pass


class RejectActionBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="RejectAction", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        RejectActionProperties,
        RejectActionInheritedProperties,
        RejectActionAllProperties,
    ] = RejectActionAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "RejectAction"
    return model


RejectAction = create_schema_org_model()


def create_rejectaction_model(
    model: Union[
        RejectActionProperties,
        RejectActionInheritedProperties,
        RejectActionAllProperties,
    ]
):
    _type = deepcopy(RejectActionAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of RejectAction. Please see: https://schema.org/RejectAction"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: RejectActionAllProperties):
    pydantic_type = create_rejectaction_model(model=model)
    return pydantic_type(model).schema_json()
