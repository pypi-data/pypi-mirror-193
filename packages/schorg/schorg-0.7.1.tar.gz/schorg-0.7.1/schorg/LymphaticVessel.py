"""
A type of blood vessel that specifically carries lymph fluid unidirectionally toward the heart.

https://schema.org/LymphaticVessel
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class LymphaticVesselInheritedProperties(TypedDict):
    """A type of blood vessel that specifically carries lymph fluid unidirectionally toward the heart.

    References:
        https://schema.org/LymphaticVessel
    Note:
        Model Depth 5
    Attributes:
    """

    


class LymphaticVesselProperties(TypedDict):
    """A type of blood vessel that specifically carries lymph fluid unidirectionally toward the heart.

    References:
        https://schema.org/LymphaticVessel
    Note:
        Model Depth 5
    Attributes:
        regionDrained: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The anatomical or organ system drained by this vessel; generally refers to a specific part of an organ.
        originatesFrom: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The vasculature the lymphatic structure originates, or afferents, from.
        runsTo: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The vasculature the lymphatic structure runs, or efferents, to.
    """

    regionDrained: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    originatesFrom: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    runsTo: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    


class AllProperties(LymphaticVesselInheritedProperties , LymphaticVesselProperties, TypedDict):
    pass


class LymphaticVesselBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="LymphaticVessel",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'regionDrained': {'exclude': True}}
        fields = {'originatesFrom': {'exclude': True}}
        fields = {'runsTo': {'exclude': True}}
        


def create_schema_org_model(type_: Union[LymphaticVesselProperties, LymphaticVesselInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "LymphaticVessel"
    return model
    

LymphaticVessel = create_schema_org_model()


def create_lymphaticvessel_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_lymphaticvessel_model(model=model)
    return pydantic_type(model).schema_json()


