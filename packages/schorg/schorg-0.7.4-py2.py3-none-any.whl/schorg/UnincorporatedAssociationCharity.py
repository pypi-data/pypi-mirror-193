"""
UnincorporatedAssociationCharity: Non-profit type referring to a charitable company that is not incorporated (UK).

https://schema.org/UnincorporatedAssociationCharity
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class UnincorporatedAssociationCharityInheritedProperties(TypedDict):
    """UnincorporatedAssociationCharity: Non-profit type referring to a charitable company that is not incorporated (UK).

    References:
        https://schema.org/UnincorporatedAssociationCharity
    Note:
        Model Depth 6
    Attributes:
    """


class UnincorporatedAssociationCharityProperties(TypedDict):
    """UnincorporatedAssociationCharity: Non-profit type referring to a charitable company that is not incorporated (UK).

    References:
        https://schema.org/UnincorporatedAssociationCharity
    Note:
        Model Depth 6
    Attributes:
    """


class UnincorporatedAssociationCharityAllProperties(
    UnincorporatedAssociationCharityInheritedProperties,
    UnincorporatedAssociationCharityProperties,
    TypedDict,
):
    pass


class UnincorporatedAssociationCharityBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="UnincorporatedAssociationCharity", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        UnincorporatedAssociationCharityProperties,
        UnincorporatedAssociationCharityInheritedProperties,
        UnincorporatedAssociationCharityAllProperties,
    ] = UnincorporatedAssociationCharityAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "UnincorporatedAssociationCharity"
    return model


UnincorporatedAssociationCharity = create_schema_org_model()


def create_unincorporatedassociationcharity_model(
    model: Union[
        UnincorporatedAssociationCharityProperties,
        UnincorporatedAssociationCharityInheritedProperties,
        UnincorporatedAssociationCharityAllProperties,
    ]
):
    _type = deepcopy(UnincorporatedAssociationCharityAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of UnincorporatedAssociationCharityAllProperties"
            )
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: UnincorporatedAssociationCharityAllProperties):
    pydantic_type = create_unincorporatedassociationcharity_model(model=model)
    return pydantic_type(model).schema_json()
