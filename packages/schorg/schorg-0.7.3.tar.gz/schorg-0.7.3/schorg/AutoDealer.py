"""
An car dealership.

https://schema.org/AutoDealer
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class AutoDealerInheritedProperties(TypedDict):
    """An car dealership.

    References:
        https://schema.org/AutoDealer
    Note:
        Model Depth 5
    Attributes:
    """


class AutoDealerProperties(TypedDict):
    """An car dealership.

    References:
        https://schema.org/AutoDealer
    Note:
        Model Depth 5
    Attributes:
    """


class AutoDealerAllProperties(
    AutoDealerInheritedProperties, AutoDealerProperties, TypedDict
):
    pass


class AutoDealerBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="AutoDealer", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        AutoDealerProperties, AutoDealerInheritedProperties, AutoDealerAllProperties
    ] = AutoDealerAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "AutoDealer"
    return model


AutoDealer = create_schema_org_model()


def create_autodealer_model(
    model: Union[
        AutoDealerProperties, AutoDealerInheritedProperties, AutoDealerAllProperties
    ]
):
    _type = deepcopy(AutoDealerAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AutoDealerAllProperties):
    pydantic_type = create_autodealer_model(model=model)
    return pydantic_type(model).schema_json()
