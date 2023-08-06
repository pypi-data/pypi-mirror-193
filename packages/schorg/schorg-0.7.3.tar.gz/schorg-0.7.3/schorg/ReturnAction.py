"""
The act of returning to the origin that which was previously received (concrete objects) or taken (ownership).

https://schema.org/ReturnAction
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ReturnActionInheritedProperties(TypedDict):
    """The act of returning to the origin that which was previously received (concrete objects) or taken (ownership).

    References:
        https://schema.org/ReturnAction
    Note:
        Model Depth 4
    Attributes:
        toLocation: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A sub property of location. The final location of the object or the agent after the action.
        fromLocation: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A sub property of location. The original location of the object or the agent before the action.
    """

    toLocation: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    fromLocation: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class ReturnActionProperties(TypedDict):
    """The act of returning to the origin that which was previously received (concrete objects) or taken (ownership).

    References:
        https://schema.org/ReturnAction
    Note:
        Model Depth 4
    Attributes:
        recipient: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A sub property of participant. The participant who is at the receiving end of the action.
    """

    recipient: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class ReturnActionAllProperties(
    ReturnActionInheritedProperties, ReturnActionProperties, TypedDict
):
    pass


class ReturnActionBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="ReturnAction", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"toLocation": {"exclude": True}}
        fields = {"fromLocation": {"exclude": True}}
        fields = {"recipient": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        ReturnActionProperties,
        ReturnActionInheritedProperties,
        ReturnActionAllProperties,
    ] = ReturnActionAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ReturnAction"
    return model


ReturnAction = create_schema_org_model()


def create_returnaction_model(
    model: Union[
        ReturnActionProperties,
        ReturnActionInheritedProperties,
        ReturnActionAllProperties,
    ]
):
    _type = deepcopy(ReturnActionAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: ReturnActionAllProperties):
    pydantic_type = create_returnaction_model(model=model)
    return pydantic_type(model).schema_json()
