"""
Active, but not recruiting new participants.

https://schema.org/ActiveNotRecruiting
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ActiveNotRecruitingInheritedProperties(TypedDict):
    """Active, but not recruiting new participants.

    References:
        https://schema.org/ActiveNotRecruiting
    Note:
        Model Depth 6
    Attributes:
    """


class ActiveNotRecruitingProperties(TypedDict):
    """Active, but not recruiting new participants.

    References:
        https://schema.org/ActiveNotRecruiting
    Note:
        Model Depth 6
    Attributes:
    """


class ActiveNotRecruitingAllProperties(
    ActiveNotRecruitingInheritedProperties, ActiveNotRecruitingProperties, TypedDict
):
    pass


class ActiveNotRecruitingBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="ActiveNotRecruiting", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        ActiveNotRecruitingProperties,
        ActiveNotRecruitingInheritedProperties,
        ActiveNotRecruitingAllProperties,
    ] = ActiveNotRecruitingAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ActiveNotRecruiting"
    return model


ActiveNotRecruiting = create_schema_org_model()


def create_activenotrecruiting_model(
    model: Union[
        ActiveNotRecruitingProperties,
        ActiveNotRecruitingInheritedProperties,
        ActiveNotRecruitingAllProperties,
    ]
):
    _type = deepcopy(ActiveNotRecruitingAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: ActiveNotRecruitingAllProperties):
    pydantic_type = create_activenotrecruiting_model(model=model)
    return pydantic_type(model).schema_json()
