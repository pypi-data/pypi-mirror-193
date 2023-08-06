"""
A type of medical procedure that involves noninvasive techniques.

https://schema.org/NoninvasiveProcedure
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class NoninvasiveProcedureInheritedProperties(TypedDict):
    """A type of medical procedure that involves noninvasive techniques.

    References:
        https://schema.org/NoninvasiveProcedure
    Note:
        Model Depth 6
    Attributes:
    """


class NoninvasiveProcedureProperties(TypedDict):
    """A type of medical procedure that involves noninvasive techniques.

    References:
        https://schema.org/NoninvasiveProcedure
    Note:
        Model Depth 6
    Attributes:
    """


class NoninvasiveProcedureAllProperties(
    NoninvasiveProcedureInheritedProperties, NoninvasiveProcedureProperties, TypedDict
):
    pass


class NoninvasiveProcedureBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="NoninvasiveProcedure", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        NoninvasiveProcedureProperties,
        NoninvasiveProcedureInheritedProperties,
        NoninvasiveProcedureAllProperties,
    ] = NoninvasiveProcedureAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "NoninvasiveProcedure"
    return model


NoninvasiveProcedure = create_schema_org_model()


def create_noninvasiveprocedure_model(
    model: Union[
        NoninvasiveProcedureProperties,
        NoninvasiveProcedureInheritedProperties,
        NoninvasiveProcedureAllProperties,
    ]
):
    _type = deepcopy(NoninvasiveProcedureAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: NoninvasiveProcedureAllProperties):
    pydantic_type = create_noninvasiveprocedure_model(model=model)
    return pydantic_type(model).schema_json()
