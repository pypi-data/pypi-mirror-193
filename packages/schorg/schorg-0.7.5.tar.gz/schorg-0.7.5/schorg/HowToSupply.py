"""
A supply consumed when performing the instructions for how to achieve a result.

https://schema.org/HowToSupply
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class HowToSupplyInheritedProperties(TypedDict):
    """A supply consumed when performing the instructions for how to achieve a result.

    References:
        https://schema.org/HowToSupply
    Note:
        Model Depth 5
    Attributes:
        requiredQuantity: (Optional[Union[List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]], str, SchemaOrgObj, StrictInt, StrictFloat]]): The required quantity of the item(s).
    """

    requiredQuantity: NotRequired[
        Union[
            List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]],
            str,
            SchemaOrgObj,
            StrictInt,
            StrictFloat,
        ]
    ]


class HowToSupplyProperties(TypedDict):
    """A supply consumed when performing the instructions for how to achieve a result.

    References:
        https://schema.org/HowToSupply
    Note:
        Model Depth 5
    Attributes:
        estimatedCost: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The estimated cost of the supply or supplies consumed when performing instructions.
    """

    estimatedCost: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class HowToSupplyAllProperties(
    HowToSupplyInheritedProperties, HowToSupplyProperties, TypedDict
):
    pass


class HowToSupplyBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="HowToSupply", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"requiredQuantity": {"exclude": True}}
        fields = {"estimatedCost": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        HowToSupplyProperties, HowToSupplyInheritedProperties, HowToSupplyAllProperties
    ] = HowToSupplyAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "HowToSupply"
    return model


HowToSupply = create_schema_org_model()


def create_howtosupply_model(
    model: Union[
        HowToSupplyProperties, HowToSupplyInheritedProperties, HowToSupplyAllProperties
    ]
):
    _type = deepcopy(HowToSupplyAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of HowToSupply. Please see: https://schema.org/HowToSupply"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: HowToSupplyAllProperties):
    pydantic_type = create_howtosupply_model(model=model)
    return pydantic_type(model).schema_json()
