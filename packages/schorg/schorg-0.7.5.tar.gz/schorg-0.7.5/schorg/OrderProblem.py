"""
OrderStatus representing that there is a problem with the order.

https://schema.org/OrderProblem
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class OrderProblemInheritedProperties(TypedDict):
    """OrderStatus representing that there is a problem with the order.

    References:
        https://schema.org/OrderProblem
    Note:
        Model Depth 6
    Attributes:
    """


class OrderProblemProperties(TypedDict):
    """OrderStatus representing that there is a problem with the order.

    References:
        https://schema.org/OrderProblem
    Note:
        Model Depth 6
    Attributes:
    """


class OrderProblemAllProperties(
    OrderProblemInheritedProperties, OrderProblemProperties, TypedDict
):
    pass


class OrderProblemBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="OrderProblem", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        OrderProblemProperties,
        OrderProblemInheritedProperties,
        OrderProblemAllProperties,
    ] = OrderProblemAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "OrderProblem"
    return model


OrderProblem = create_schema_org_model()


def create_orderproblem_model(
    model: Union[
        OrderProblemProperties,
        OrderProblemInheritedProperties,
        OrderProblemAllProperties,
    ]
):
    _type = deepcopy(OrderProblemAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of OrderProblem. Please see: https://schema.org/OrderProblem"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: OrderProblemAllProperties):
    pydantic_type = create_orderproblem_model(model=model)
    return pydantic_type(model).schema_json()
