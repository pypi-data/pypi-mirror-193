"""
The act of providing an object under an agreement that it will be returned at a later date. Reciprocal of BorrowAction.Related actions:* [[BorrowAction]]: Reciprocal of LendAction.

https://schema.org/LendAction
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


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
    


class AllProperties(LendActionInheritedProperties , LendActionProperties, TypedDict):
    pass


class LendActionBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="LendAction",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'toLocation': {'exclude': True}}
        fields = {'fromLocation': {'exclude': True}}
        fields = {'borrower': {'exclude': True}}
        


def create_schema_org_model(type_: Union[LendActionProperties, LendActionInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "LendAction"
    return model
    

LendAction = create_schema_org_model()


def create_lendaction_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_lendaction_model(model=model)
    return pydantic_type(model).schema_json()


