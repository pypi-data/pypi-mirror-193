"""
The act of expressing a preference from a fixed/finite/structured set of choices/options.

https://schema.org/VoteAction
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class VoteActionInheritedProperties(TypedDict):
    """The act of expressing a preference from a fixed/finite/structured set of choices/options.

    References:
        https://schema.org/VoteAction
    Note:
        Model Depth 5
    Attributes:
        option: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A sub property of object. The options subject to this action.
        actionOption: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A sub property of object. The options subject to this action.
    """

    option: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    actionOption: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    


class VoteActionProperties(TypedDict):
    """The act of expressing a preference from a fixed/finite/structured set of choices/options.

    References:
        https://schema.org/VoteAction
    Note:
        Model Depth 5
    Attributes:
        candidate: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A sub property of object. The candidate subject of this action.
    """

    candidate: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    


class AllProperties(VoteActionInheritedProperties , VoteActionProperties, TypedDict):
    pass


class VoteActionBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="VoteAction",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'option': {'exclude': True}}
        fields = {'actionOption': {'exclude': True}}
        fields = {'candidate': {'exclude': True}}
        


def create_schema_org_model(type_: Union[VoteActionProperties, VoteActionInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "VoteAction"
    return model
    

VoteAction = create_schema_org_model()


def create_voteaction_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_voteaction_model(model=model)
    return pydantic_type(model).schema_json()


