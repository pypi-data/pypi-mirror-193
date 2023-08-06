"""
The act of obtaining an object under an agreement to return it at a later date. Reciprocal of LendAction.Related actions:* [[LendAction]]: Reciprocal of BorrowAction.

https://schema.org/BorrowAction
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class BorrowActionInheritedProperties(TypedDict):
    """The act of obtaining an object under an agreement to return it at a later date. Reciprocal of LendAction.Related actions:* [[LendAction]]: Reciprocal of BorrowAction.

    References:
        https://schema.org/BorrowAction
    Note:
        Model Depth 4
    Attributes:
        toLocation: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A sub property of location. The final location of the object or the agent after the action.
        fromLocation: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A sub property of location. The original location of the object or the agent before the action.
    """

    toLocation: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    fromLocation: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class BorrowActionProperties(TypedDict):
    """The act of obtaining an object under an agreement to return it at a later date. Reciprocal of LendAction.Related actions:* [[LendAction]]: Reciprocal of BorrowAction.

    References:
        https://schema.org/BorrowAction
    Note:
        Model Depth 4
    Attributes:
        lender: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A sub property of participant. The person that lends the object being borrowed.
    """

    lender: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class BorrowActionAllProperties(
    BorrowActionInheritedProperties, BorrowActionProperties, TypedDict
):
    pass


class BorrowActionBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="BorrowAction", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"toLocation": {"exclude": True}}
        fields = {"fromLocation": {"exclude": True}}
        fields = {"lender": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        BorrowActionProperties,
        BorrowActionInheritedProperties,
        BorrowActionAllProperties,
    ] = BorrowActionAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "BorrowAction"
    return model


BorrowAction = create_schema_org_model()


def create_borrowaction_model(
    model: Union[
        BorrowActionProperties,
        BorrowActionInheritedProperties,
        BorrowActionAllProperties,
    ]
):
    _type = deepcopy(BorrowActionAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of BorrowAction. Please see: https://schema.org/BorrowAction"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: BorrowActionAllProperties):
    pydantic_type = create_borrowaction_model(model=model)
    return pydantic_type(model).schema_json()
