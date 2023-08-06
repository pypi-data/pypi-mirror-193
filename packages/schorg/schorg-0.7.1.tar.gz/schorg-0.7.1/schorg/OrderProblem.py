"""
OrderStatus representing that there is a problem with the order.

https://schema.org/OrderProblem
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


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

    


class AllProperties(OrderProblemInheritedProperties , OrderProblemProperties, TypedDict):
    pass


class OrderProblemBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="OrderProblem",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[OrderProblemProperties, OrderProblemInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "OrderProblem"
    return model
    

OrderProblem = create_schema_org_model()


def create_orderproblem_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_orderproblem_model(model=model)
    return pydantic_type(model).schema_json()


