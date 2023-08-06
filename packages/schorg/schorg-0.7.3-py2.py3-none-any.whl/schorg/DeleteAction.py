"""
The act of editing a recipient by removing one of its objects.

https://schema.org/DeleteAction
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class DeleteActionInheritedProperties(TypedDict):
    """The act of editing a recipient by removing one of its objects.

    References:
        https://schema.org/DeleteAction
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


class DeleteActionProperties(TypedDict):
    """The act of editing a recipient by removing one of its objects.

    References:
        https://schema.org/DeleteAction
    Note:
        Model Depth 4
    Attributes:
    """


class DeleteActionAllProperties(
    DeleteActionInheritedProperties, DeleteActionProperties, TypedDict
):
    pass


class DeleteActionBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="DeleteAction", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"collection": {"exclude": True}}
        fields = {"targetCollection": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        DeleteActionProperties,
        DeleteActionInheritedProperties,
        DeleteActionAllProperties,
    ] = DeleteActionAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "DeleteAction"
    return model


DeleteAction = create_schema_org_model()


def create_deleteaction_model(
    model: Union[
        DeleteActionProperties,
        DeleteActionInheritedProperties,
        DeleteActionAllProperties,
    ]
):
    _type = deepcopy(DeleteActionAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: DeleteActionAllProperties):
    pydantic_type = create_deleteaction_model(model=model)
    return pydantic_type(model).schema_json()
