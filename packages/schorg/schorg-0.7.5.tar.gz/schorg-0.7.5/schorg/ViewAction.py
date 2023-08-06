"""
The act of consuming static visual content.

https://schema.org/ViewAction
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ViewActionInheritedProperties(TypedDict):
    """The act of consuming static visual content.

    References:
        https://schema.org/ViewAction
    Note:
        Model Depth 4
    Attributes:
        actionAccessibilityRequirement: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A set of requirements that must be fulfilled in order to perform an Action. If more than one value is specified, fulfilling one set of requirements will allow the Action to be performed.
        expectsAcceptanceOf: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): An Offer which must be accepted before the user can perform the Action. For example, the user may need to buy a movie before being able to watch it.
    """

    actionAccessibilityRequirement: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    expectsAcceptanceOf: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]


class ViewActionProperties(TypedDict):
    """The act of consuming static visual content.

    References:
        https://schema.org/ViewAction
    Note:
        Model Depth 4
    Attributes:
    """


class ViewActionAllProperties(
    ViewActionInheritedProperties, ViewActionProperties, TypedDict
):
    pass


class ViewActionBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="ViewAction", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"actionAccessibilityRequirement": {"exclude": True}}
        fields = {"expectsAcceptanceOf": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        ViewActionProperties, ViewActionInheritedProperties, ViewActionAllProperties
    ] = ViewActionAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ViewAction"
    return model


ViewAction = create_schema_org_model()


def create_viewaction_model(
    model: Union[
        ViewActionProperties, ViewActionInheritedProperties, ViewActionAllProperties
    ]
):
    _type = deepcopy(ViewActionAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of ViewAction. Please see: https://schema.org/ViewAction"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: ViewActionAllProperties):
    pydantic_type = create_viewaction_model(model=model)
    return pydantic_type(model).schema_json()
