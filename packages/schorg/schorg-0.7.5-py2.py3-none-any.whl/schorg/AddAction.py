"""
The act of editing by adding an object to a collection.

https://schema.org/AddAction
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class AddActionInheritedProperties(TypedDict):
    """The act of editing by adding an object to a collection.

    References:
        https://schema.org/AddAction
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


class AddActionProperties(TypedDict):
    """The act of editing by adding an object to a collection.

    References:
        https://schema.org/AddAction
    Note:
        Model Depth 4
    Attributes:
    """


class AddActionAllProperties(
    AddActionInheritedProperties, AddActionProperties, TypedDict
):
    pass


class AddActionBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="AddAction", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"collection": {"exclude": True}}
        fields = {"targetCollection": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        AddActionProperties, AddActionInheritedProperties, AddActionAllProperties
    ] = AddActionAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "AddAction"
    return model


AddAction = create_schema_org_model()


def create_addaction_model(
    model: Union[
        AddActionProperties, AddActionInheritedProperties, AddActionAllProperties
    ]
):
    _type = deepcopy(AddActionAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of AddAction. Please see: https://schema.org/AddAction"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: AddActionAllProperties):
    pydantic_type = create_addaction_model(model=model)
    return pydantic_type(model).schema_json()
