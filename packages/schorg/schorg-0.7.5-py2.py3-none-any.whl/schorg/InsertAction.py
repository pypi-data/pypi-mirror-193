"""
The act of adding at a specific location in an ordered collection.

https://schema.org/InsertAction
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class InsertActionInheritedProperties(TypedDict):
    """The act of adding at a specific location in an ordered collection.

    References:
        https://schema.org/InsertAction
    Note:
        Model Depth 5
    Attributes:
    """


class InsertActionProperties(TypedDict):
    """The act of adding at a specific location in an ordered collection.

    References:
        https://schema.org/InsertAction
    Note:
        Model Depth 5
    Attributes:
        toLocation: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A sub property of location. The final location of the object or the agent after the action.
    """

    toLocation: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class InsertActionAllProperties(
    InsertActionInheritedProperties, InsertActionProperties, TypedDict
):
    pass


class InsertActionBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="InsertAction", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"toLocation": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        InsertActionProperties,
        InsertActionInheritedProperties,
        InsertActionAllProperties,
    ] = InsertActionAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "InsertAction"
    return model


InsertAction = create_schema_org_model()


def create_insertaction_model(
    model: Union[
        InsertActionProperties,
        InsertActionInheritedProperties,
        InsertActionAllProperties,
    ]
):
    _type = deepcopy(InsertActionAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of InsertAction. Please see: https://schema.org/InsertAction"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: InsertActionAllProperties):
    pydantic_type = create_insertaction_model(model=model)
    return pydantic_type(model).schema_json()
