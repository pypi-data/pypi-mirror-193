"""
A tool used (but not consumed) when performing instructions for how to achieve a result.

https://schema.org/HowToTool
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class HowToToolInheritedProperties(TypedDict):
    """A tool used (but not consumed) when performing instructions for how to achieve a result.

    References:
        https://schema.org/HowToTool
    Note:
        Model Depth 5
    Attributes:
        requiredQuantity: (Optional[Union[List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]], str, StrictInt, StrictFloat, SchemaOrgObj]]): The required quantity of the item(s).
    """

    requiredQuantity: NotRequired[Union[List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]], str, StrictInt, StrictFloat, SchemaOrgObj]]
    


class HowToToolProperties(TypedDict):
    """A tool used (but not consumed) when performing instructions for how to achieve a result.

    References:
        https://schema.org/HowToTool
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(HowToToolInheritedProperties , HowToToolProperties, TypedDict):
    pass


class HowToToolBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="HowToTool",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'requiredQuantity': {'exclude': True}}
        


def create_schema_org_model(type_: Union[HowToToolProperties, HowToToolInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "HowToTool"
    return model
    

HowToTool = create_schema_org_model()


def create_howtotool_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_howtotool_model(model=model)
    return pydantic_type(model).schema_json()


