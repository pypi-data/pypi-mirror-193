"""
A moving company.

https://schema.org/MovingCompany
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MovingCompanyInheritedProperties(TypedDict):
    """A moving company.

    References:
        https://schema.org/MovingCompany
    Note:
        Model Depth 5
    Attributes:
    """


class MovingCompanyProperties(TypedDict):
    """A moving company.

    References:
        https://schema.org/MovingCompany
    Note:
        Model Depth 5
    Attributes:
    """


class MovingCompanyAllProperties(
    MovingCompanyInheritedProperties, MovingCompanyProperties, TypedDict
):
    pass


class MovingCompanyBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="MovingCompany", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        MovingCompanyProperties,
        MovingCompanyInheritedProperties,
        MovingCompanyAllProperties,
    ] = MovingCompanyAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MovingCompany"
    return model


MovingCompany = create_schema_org_model()


def create_movingcompany_model(
    model: Union[
        MovingCompanyProperties,
        MovingCompanyInheritedProperties,
        MovingCompanyAllProperties,
    ]
):
    _type = deepcopy(MovingCompanyAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of MovingCompany. Please see: https://schema.org/MovingCompany"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: MovingCompanyAllProperties):
    pydantic_type = create_movingcompany_model(model=model)
    return pydantic_type(model).schema_json()
