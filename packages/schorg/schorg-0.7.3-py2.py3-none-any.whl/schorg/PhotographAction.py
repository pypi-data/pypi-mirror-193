"""
The act of capturing still images of objects using a camera.

https://schema.org/PhotographAction
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class PhotographActionInheritedProperties(TypedDict):
    """The act of capturing still images of objects using a camera.

    References:
        https://schema.org/PhotographAction
    Note:
        Model Depth 4
    Attributes:
    """


class PhotographActionProperties(TypedDict):
    """The act of capturing still images of objects using a camera.

    References:
        https://schema.org/PhotographAction
    Note:
        Model Depth 4
    Attributes:
    """


class PhotographActionAllProperties(
    PhotographActionInheritedProperties, PhotographActionProperties, TypedDict
):
    pass


class PhotographActionBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="PhotographAction", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        PhotographActionProperties,
        PhotographActionInheritedProperties,
        PhotographActionAllProperties,
    ] = PhotographActionAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "PhotographAction"
    return model


PhotographAction = create_schema_org_model()


def create_photographaction_model(
    model: Union[
        PhotographActionProperties,
        PhotographActionInheritedProperties,
        PhotographActionAllProperties,
    ]
):
    _type = deepcopy(PhotographActionAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: PhotographActionAllProperties):
    pydantic_type = create_photographaction_model(model=model)
    return pydantic_type(model).schema_json()
