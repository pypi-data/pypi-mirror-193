"""
The act of applying an object to its intended purpose.

https://schema.org/UseAction
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class UseActionInheritedProperties(TypedDict):
    """The act of applying an object to its intended purpose.

    References:
        https://schema.org/UseAction
    Note:
        Model Depth 4
    Attributes:
        actionAccessibilityRequirement: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A set of requirements that must be fulfilled in order to perform an Action. If more than one value is specified, fulfilling one set of requirements will allow the Action to be performed.
        expectsAcceptanceOf: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): An Offer which must be accepted before the user can perform the Action. For example, the user may need to buy a movie before being able to watch it.
    """

    actionAccessibilityRequirement: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    expectsAcceptanceOf: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    


class UseActionProperties(TypedDict):
    """The act of applying an object to its intended purpose.

    References:
        https://schema.org/UseAction
    Note:
        Model Depth 4
    Attributes:
    """

    


class AllProperties(UseActionInheritedProperties , UseActionProperties, TypedDict):
    pass


class UseActionBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="UseAction",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'actionAccessibilityRequirement': {'exclude': True}}
        fields = {'expectsAcceptanceOf': {'exclude': True}}
        


def create_schema_org_model(type_: Union[UseActionProperties, UseActionInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "UseAction"
    return model
    

UseAction = create_schema_org_model()


def create_useaction_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_useaction_model(model=model)
    return pydantic_type(model).schema_json()


