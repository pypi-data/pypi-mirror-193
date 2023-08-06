"""
Nonprofit501c10: Non-profit type referring to Domestic Fraternal Societies and Associations.

https://schema.org/Nonprofit501c10
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class Nonprofit501c10InheritedProperties(TypedDict):
    """Nonprofit501c10: Non-profit type referring to Domestic Fraternal Societies and Associations.

    References:
        https://schema.org/Nonprofit501c10
    Note:
        Model Depth 6
    Attributes:
    """


class Nonprofit501c10Properties(TypedDict):
    """Nonprofit501c10: Non-profit type referring to Domestic Fraternal Societies and Associations.

    References:
        https://schema.org/Nonprofit501c10
    Note:
        Model Depth 6
    Attributes:
    """


class Nonprofit501c10AllProperties(
    Nonprofit501c10InheritedProperties, Nonprofit501c10Properties, TypedDict
):
    pass


class Nonprofit501c10BaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Nonprofit501c10", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        Nonprofit501c10Properties,
        Nonprofit501c10InheritedProperties,
        Nonprofit501c10AllProperties,
    ] = Nonprofit501c10AllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Nonprofit501c10"
    return model


Nonprofit501c10 = create_schema_org_model()


def create_nonprofit501c10_model(
    model: Union[
        Nonprofit501c10Properties,
        Nonprofit501c10InheritedProperties,
        Nonprofit501c10AllProperties,
    ]
):
    _type = deepcopy(Nonprofit501c10AllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: Nonprofit501c10AllProperties):
    pydantic_type = create_nonprofit501c10_model(model=model)
    return pydantic_type(model).schema_json()
