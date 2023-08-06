"""
A supply consumed when performing the instructions for how to achieve a result.

https://schema.org/HowToSupply
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class HowToSupplyInheritedProperties(TypedDict):
    """A supply consumed when performing the instructions for how to achieve a result.

    References:
        https://schema.org/HowToSupply
    Note:
        Model Depth 5
    Attributes:
        requiredQuantity: (Optional[Union[List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]], str, StrictInt, StrictFloat, SchemaOrgObj]]): The required quantity of the item(s).
    """

    requiredQuantity: NotRequired[Union[List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]], str, StrictInt, StrictFloat, SchemaOrgObj]]
    


class HowToSupplyProperties(TypedDict):
    """A supply consumed when performing the instructions for how to achieve a result.

    References:
        https://schema.org/HowToSupply
    Note:
        Model Depth 5
    Attributes:
        estimatedCost: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The estimated cost of the supply or supplies consumed when performing instructions.
    """

    estimatedCost: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    


class AllProperties(HowToSupplyInheritedProperties , HowToSupplyProperties, TypedDict):
    pass


class HowToSupplyBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="HowToSupply",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'requiredQuantity': {'exclude': True}}
        fields = {'estimatedCost': {'exclude': True}}
        


def create_schema_org_model(type_: Union[HowToSupplyProperties, HowToSupplyInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "HowToSupply"
    return model
    

HowToSupply = create_schema_org_model()


def create_howtosupply_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_howtosupply_model(model=model)
    return pydantic_type(model).schema_json()


