"""
The drug's cost represents the wholesale acquisition cost of the drug.

https://schema.org/Wholesale
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class WholesaleInheritedProperties(TypedDict):
    """The drug's cost represents the wholesale acquisition cost of the drug.

    References:
        https://schema.org/Wholesale
    Note:
        Model Depth 6
    Attributes:
    """


class WholesaleProperties(TypedDict):
    """The drug's cost represents the wholesale acquisition cost of the drug.

    References:
        https://schema.org/Wholesale
    Note:
        Model Depth 6
    Attributes:
    """


class WholesaleAllProperties(
    WholesaleInheritedProperties, WholesaleProperties, TypedDict
):
    pass


class WholesaleBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Wholesale", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        WholesaleProperties, WholesaleInheritedProperties, WholesaleAllProperties
    ] = WholesaleAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Wholesale"
    return model


Wholesale = create_schema_org_model()


def create_wholesale_model(
    model: Union[
        WholesaleProperties, WholesaleInheritedProperties, WholesaleAllProperties
    ]
):
    _type = deepcopy(WholesaleAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of WholesaleAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: WholesaleAllProperties):
    pydantic_type = create_wholesale_model(model=model)
    return pydantic_type(model).schema_json()
