"""
The act of editing a recipient by replacing an old object with a new object.

https://schema.org/ReplaceAction
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ReplaceActionInheritedProperties(TypedDict):
    """The act of editing a recipient by replacing an old object with a new object.

    References:
        https://schema.org/ReplaceAction
    Note:
        Model Depth 4
    Attributes:
        collection: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A sub property of object. The collection target of the action.
        targetCollection: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A sub property of object. The collection target of the action.
    """

    collection: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    targetCollection: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]


class ReplaceActionProperties(TypedDict):
    """The act of editing a recipient by replacing an old object with a new object.

    References:
        https://schema.org/ReplaceAction
    Note:
        Model Depth 4
    Attributes:
        replacee: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A sub property of object. The object that is being replaced.
        replacer: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A sub property of object. The object that replaces.
    """

    replacee: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    replacer: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class ReplaceActionAllProperties(
    ReplaceActionInheritedProperties, ReplaceActionProperties, TypedDict
):
    pass


class ReplaceActionBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="ReplaceAction", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"collection": {"exclude": True}}
        fields = {"targetCollection": {"exclude": True}}
        fields = {"replacee": {"exclude": True}}
        fields = {"replacer": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        ReplaceActionProperties,
        ReplaceActionInheritedProperties,
        ReplaceActionAllProperties,
    ] = ReplaceActionAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ReplaceAction"
    return model


ReplaceAction = create_schema_org_model()


def create_replaceaction_model(
    model: Union[
        ReplaceActionProperties,
        ReplaceActionInheritedProperties,
        ReplaceActionAllProperties,
    ]
):
    _type = deepcopy(ReplaceActionAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: ReplaceActionAllProperties):
    pydantic_type = create_replaceaction_model(model=model)
    return pydantic_type(model).schema_json()
