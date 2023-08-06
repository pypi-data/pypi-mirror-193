"""
The act of consuming audio content.

https://schema.org/ListenAction
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ListenActionInheritedProperties(TypedDict):
    """The act of consuming audio content.

    References:
        https://schema.org/ListenAction
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


class ListenActionProperties(TypedDict):
    """The act of consuming audio content.

    References:
        https://schema.org/ListenAction
    Note:
        Model Depth 4
    Attributes:
    """


class ListenActionAllProperties(
    ListenActionInheritedProperties, ListenActionProperties, TypedDict
):
    pass


class ListenActionBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="ListenAction", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"actionAccessibilityRequirement": {"exclude": True}}
        fields = {"expectsAcceptanceOf": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        ListenActionProperties,
        ListenActionInheritedProperties,
        ListenActionAllProperties,
    ] = ListenActionAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ListenAction"
    return model


ListenAction = create_schema_org_model()


def create_listenaction_model(
    model: Union[
        ListenActionProperties,
        ListenActionInheritedProperties,
        ListenActionAllProperties,
    ]
):
    _type = deepcopy(ListenActionAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of ListenAction. Please see: https://schema.org/ListenAction"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: ListenActionAllProperties):
    pydantic_type = create_listenaction_model(model=model)
    return pydantic_type(model).schema_json()
