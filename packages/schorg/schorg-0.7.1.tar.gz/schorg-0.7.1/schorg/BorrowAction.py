"""
The act of obtaining an object under an agreement to return it at a later date. Reciprocal of LendAction.Related actions:* [[LendAction]]: Reciprocal of BorrowAction.

https://schema.org/BorrowAction
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


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
    


class AllProperties(BorrowActionInheritedProperties , BorrowActionProperties, TypedDict):
    pass


class BorrowActionBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="BorrowAction",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'toLocation': {'exclude': True}}
        fields = {'fromLocation': {'exclude': True}}
        fields = {'lender': {'exclude': True}}
        


def create_schema_org_model(type_: Union[BorrowActionProperties, BorrowActionInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "BorrowAction"
    return model
    

BorrowAction = create_schema_org_model()


def create_borrowaction_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_borrowaction_model(model=model)
    return pydantic_type(model).schema_json()


