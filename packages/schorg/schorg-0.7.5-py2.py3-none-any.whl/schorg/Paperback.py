"""
Book format: Paperback.

https://schema.org/Paperback
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class PaperbackInheritedProperties(TypedDict):
    """Book format: Paperback.

    References:
        https://schema.org/Paperback
    Note:
        Model Depth 5
    Attributes:
    """


class PaperbackProperties(TypedDict):
    """Book format: Paperback.

    References:
        https://schema.org/Paperback
    Note:
        Model Depth 5
    Attributes:
    """


class PaperbackAllProperties(
    PaperbackInheritedProperties, PaperbackProperties, TypedDict
):
    pass


class PaperbackBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Paperback", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        PaperbackProperties, PaperbackInheritedProperties, PaperbackAllProperties
    ] = PaperbackAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Paperback"
    return model


Paperback = create_schema_org_model()


def create_paperback_model(
    model: Union[
        PaperbackProperties, PaperbackInheritedProperties, PaperbackAllProperties
    ]
):
    _type = deepcopy(PaperbackAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of Paperback. Please see: https://schema.org/Paperback"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: PaperbackAllProperties):
    pydantic_type = create_paperback_model(model=model)
    return pydantic_type(model).schema_json()
