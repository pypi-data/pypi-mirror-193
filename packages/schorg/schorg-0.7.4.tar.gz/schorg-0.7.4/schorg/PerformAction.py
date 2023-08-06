"""
The act of participating in performance arts.

https://schema.org/PerformAction
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class PerformActionInheritedProperties(TypedDict):
    """The act of participating in performance arts.

    References:
        https://schema.org/PerformAction
    Note:
        Model Depth 4
    Attributes:
        event: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Upcoming or past event associated with this place, organization, or action.
        audience: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): An intended audience, i.e. a group for whom something was created.
    """

    event: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    audience: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]


class PerformActionProperties(TypedDict):
    """The act of participating in performance arts.

    References:
        https://schema.org/PerformAction
    Note:
        Model Depth 4
    Attributes:
        entertainmentBusiness: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A sub property of location. The entertainment business where the action occurred.
    """

    entertainmentBusiness: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]


class PerformActionAllProperties(
    PerformActionInheritedProperties, PerformActionProperties, TypedDict
):
    pass


class PerformActionBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="PerformAction", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"event": {"exclude": True}}
        fields = {"audience": {"exclude": True}}
        fields = {"entertainmentBusiness": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        PerformActionProperties,
        PerformActionInheritedProperties,
        PerformActionAllProperties,
    ] = PerformActionAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "PerformAction"
    return model


PerformAction = create_schema_org_model()


def create_performaction_model(
    model: Union[
        PerformActionProperties,
        PerformActionInheritedProperties,
        PerformActionAllProperties,
    ]
):
    _type = deepcopy(PerformActionAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of PerformActionAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: PerformActionAllProperties):
    pydantic_type = create_performaction_model(model=model)
    return pydantic_type(model).schema_json()
