"""
The act of swallowing solid objects.

https://schema.org/EatAction
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class EatActionInheritedProperties(TypedDict):
    """The act of swallowing solid objects.

    References:
        https://schema.org/EatAction
    Note:
        Model Depth 4
    Attributes:
        actionAccessibilityRequirement: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A set of requirements that must be fulfilled in order to perform an Action. If more than one value is specified, fulfilling one set of requirements will allow the Action to be performed.
        expectsAcceptanceOf: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): An Offer which must be accepted before the user can perform the Action. For example, the user may need to buy a movie before being able to watch it.
    """

    actionAccessibilityRequirement: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    expectsAcceptanceOf: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    


class EatActionProperties(TypedDict):
    """The act of swallowing solid objects.

    References:
        https://schema.org/EatAction
    Note:
        Model Depth 4
    Attributes:
    """

    


class AllProperties(EatActionInheritedProperties , EatActionProperties, TypedDict):
    pass


class EatActionBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="EatAction",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'actionAccessibilityRequirement': {'exclude': True}}
        fields = {'expectsAcceptanceOf': {'exclude': True}}
        


def create_schema_org_model(type_: Union[EatActionProperties, EatActionInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "EatAction"
    return model
    

EatAction = create_schema_org_model()


def create_eataction_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_eataction_model(model=model)
    return pydantic_type(model).schema_json()


