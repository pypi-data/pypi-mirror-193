"""
The act of producing/preparing food.

https://schema.org/CookAction
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class CookActionInheritedProperties(TypedDict):
    """The act of producing/preparing food.

    References:
        https://schema.org/CookAction
    Note:
        Model Depth 4
    Attributes:
    """

    


class CookActionProperties(TypedDict):
    """The act of producing/preparing food.

    References:
        https://schema.org/CookAction
    Note:
        Model Depth 4
    Attributes:
        foodEvent: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A sub property of location. The specific food event where the action occurred.
        recipe: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A sub property of instrument. The recipe/instructions used to perform the action.
        foodEstablishment: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A sub property of location. The specific food establishment where the action occurred.
    """

    foodEvent: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    recipe: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    foodEstablishment: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    


class AllProperties(CookActionInheritedProperties , CookActionProperties, TypedDict):
    pass


class CookActionBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="CookAction",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'foodEvent': {'exclude': True}}
        fields = {'recipe': {'exclude': True}}
        fields = {'foodEstablishment': {'exclude': True}}
        


def create_schema_org_model(type_: Union[CookActionProperties, CookActionInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "CookAction"
    return model
    

CookAction = create_schema_org_model()


def create_cookaction_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_cookaction_model(model=model)
    return pydantic_type(model).schema_json()


