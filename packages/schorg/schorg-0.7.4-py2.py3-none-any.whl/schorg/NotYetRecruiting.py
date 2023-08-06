"""
Not yet recruiting.

https://schema.org/NotYetRecruiting
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class NotYetRecruitingInheritedProperties(TypedDict):
    """Not yet recruiting.

    References:
        https://schema.org/NotYetRecruiting
    Note:
        Model Depth 6
    Attributes:
    """


class NotYetRecruitingProperties(TypedDict):
    """Not yet recruiting.

    References:
        https://schema.org/NotYetRecruiting
    Note:
        Model Depth 6
    Attributes:
    """


class NotYetRecruitingAllProperties(
    NotYetRecruitingInheritedProperties, NotYetRecruitingProperties, TypedDict
):
    pass


class NotYetRecruitingBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="NotYetRecruiting", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        NotYetRecruitingProperties,
        NotYetRecruitingInheritedProperties,
        NotYetRecruitingAllProperties,
    ] = NotYetRecruitingAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "NotYetRecruiting"
    return model


NotYetRecruiting = create_schema_org_model()


def create_notyetrecruiting_model(
    model: Union[
        NotYetRecruitingProperties,
        NotYetRecruitingInheritedProperties,
        NotYetRecruitingAllProperties,
    ]
):
    _type = deepcopy(NotYetRecruitingAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of NotYetRecruitingAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: NotYetRecruitingAllProperties):
    pydantic_type = create_notyetrecruiting_model(model=model)
    return pydantic_type(model).schema_json()
