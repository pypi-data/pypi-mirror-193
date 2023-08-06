"""
The act of providing an object under an agreement that it will be returned at a later date. Reciprocal of BorrowAction.Related actions:* [[BorrowAction]]: Reciprocal of LendAction.

https://schema.org/LendAction
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class LendActionInheritedProperties(TypedDict):
    """The act of providing an object under an agreement that it will be returned at a later date. Reciprocal of BorrowAction.Related actions:* [[BorrowAction]]: Reciprocal of LendAction.

    References:
        https://schema.org/LendAction
    Note:
        Model Depth 4
    Attributes:
        toLocation: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A sub property of location. The final location of the object or the agent after the action.
        fromLocation: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A sub property of location. The original location of the object or the agent before the action.
    """

    toLocation: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    fromLocation: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]


class LendActionProperties(TypedDict):
    """The act of providing an object under an agreement that it will be returned at a later date. Reciprocal of BorrowAction.Related actions:* [[BorrowAction]]: Reciprocal of LendAction.

    References:
        https://schema.org/LendAction
    Note:
        Model Depth 4
    Attributes:
        borrower: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A sub property of participant. The person that borrows the object being lent.
    """

    borrower: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]


class LendActionAllProperties(
    LendActionInheritedProperties, LendActionProperties, TypedDict
):
    pass


class LendActionBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="LendAction", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"toLocation": {"exclude": True}}
        fields = {"fromLocation": {"exclude": True}}
        fields = {"borrower": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        LendActionProperties, LendActionInheritedProperties, LendActionAllProperties
    ] = LendActionAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "LendAction"
    return model


LendAction = create_schema_org_model()


def create_lendaction_model(
    model: Union[
        LendActionProperties, LendActionInheritedProperties, LendActionAllProperties
    ]
):
    _type = deepcopy(LendActionAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of LendActionAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: LendActionAllProperties):
    pydantic_type = create_lendaction_model(model=model)
    return pydantic_type(model).schema_json()
