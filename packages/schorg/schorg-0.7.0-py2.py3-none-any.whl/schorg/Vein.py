"""
A type of blood vessel that specifically carries blood to the heart.

https://schema.org/Vein
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class VeinInheritedProperties(TypedDict):
    """A type of blood vessel that specifically carries blood to the heart.

    References:
        https://schema.org/Vein
    Note:
        Model Depth 5
    Attributes:
    """

    


class VeinProperties(TypedDict):
    """A type of blood vessel that specifically carries blood to the heart.

    References:
        https://schema.org/Vein
    Note:
        Model Depth 5
    Attributes:
        tributary: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The anatomical or organ system that the vein flows into; a larger structure that the vein connects to.
        regionDrained: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The anatomical or organ system drained by this vessel; generally refers to a specific part of an organ.
        drainsTo: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The vasculature that the vein drains into.
    """

    tributary: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    regionDrained: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    drainsTo: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    


class AllProperties(VeinInheritedProperties , VeinProperties, TypedDict):
    pass


class VeinBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="Vein",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'tributary': {'exclude': True}}
        fields = {'regionDrained': {'exclude': True}}
        fields = {'drainsTo': {'exclude': True}}
        


def create_schema_org_model(type_: Union[VeinProperties, VeinInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Vein"
    return model
    

Vein = create_schema_org_model()


def create_vein_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_vein_model(model=model)
    return pydantic_type(model).schema_json()


