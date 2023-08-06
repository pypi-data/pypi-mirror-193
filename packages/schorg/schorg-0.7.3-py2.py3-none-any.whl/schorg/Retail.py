"""
The drug's cost represents the retail cost of the drug.

https://schema.org/Retail
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class RetailInheritedProperties(TypedDict):
    """The drug's cost represents the retail cost of the drug.

    References:
        https://schema.org/Retail
    Note:
        Model Depth 6
    Attributes:
    """


class RetailProperties(TypedDict):
    """The drug's cost represents the retail cost of the drug.

    References:
        https://schema.org/Retail
    Note:
        Model Depth 6
    Attributes:
    """


class RetailAllProperties(RetailInheritedProperties, RetailProperties, TypedDict):
    pass


class RetailBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Retail", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        RetailProperties, RetailInheritedProperties, RetailAllProperties
    ] = RetailAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Retail"
    return model


Retail = create_schema_org_model()


def create_retail_model(
    model: Union[RetailProperties, RetailInheritedProperties, RetailAllProperties]
):
    _type = deepcopy(RetailAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: RetailAllProperties):
    pydantic_type = create_retail_model(model=model)
    return pydantic_type(model).schema_json()
