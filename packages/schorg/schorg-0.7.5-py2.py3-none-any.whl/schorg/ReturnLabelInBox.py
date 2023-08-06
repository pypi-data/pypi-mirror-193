"""
Specifies that a return label will be provided by the seller in the shipping box.

https://schema.org/ReturnLabelInBox
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ReturnLabelInBoxInheritedProperties(TypedDict):
    """Specifies that a return label will be provided by the seller in the shipping box.

    References:
        https://schema.org/ReturnLabelInBox
    Note:
        Model Depth 5
    Attributes:
    """


class ReturnLabelInBoxProperties(TypedDict):
    """Specifies that a return label will be provided by the seller in the shipping box.

    References:
        https://schema.org/ReturnLabelInBox
    Note:
        Model Depth 5
    Attributes:
    """


class ReturnLabelInBoxAllProperties(
    ReturnLabelInBoxInheritedProperties, ReturnLabelInBoxProperties, TypedDict
):
    pass


class ReturnLabelInBoxBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="ReturnLabelInBox", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        ReturnLabelInBoxProperties,
        ReturnLabelInBoxInheritedProperties,
        ReturnLabelInBoxAllProperties,
    ] = ReturnLabelInBoxAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ReturnLabelInBox"
    return model


ReturnLabelInBox = create_schema_org_model()


def create_returnlabelinbox_model(
    model: Union[
        ReturnLabelInBoxProperties,
        ReturnLabelInBoxInheritedProperties,
        ReturnLabelInBoxAllProperties,
    ]
):
    _type = deepcopy(ReturnLabelInBoxAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of ReturnLabelInBox. Please see: https://schema.org/ReturnLabelInBox"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: ReturnLabelInBoxAllProperties):
    pydantic_type = create_returnlabelinbox_model(model=model)
    return pydantic_type(model).schema_json()
