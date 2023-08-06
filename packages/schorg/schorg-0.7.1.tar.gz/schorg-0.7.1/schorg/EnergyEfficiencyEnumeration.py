"""
Enumerates energy efficiency levels (also known as "classes" or "ratings") and certifications that are part of several international energy efficiency standards.

https://schema.org/EnergyEfficiencyEnumeration
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class EnergyEfficiencyEnumerationInheritedProperties(TypedDict):
    """Enumerates energy efficiency levels (also known as "classes" or "ratings") and certifications that are part of several international energy efficiency standards.

    References:
        https://schema.org/EnergyEfficiencyEnumeration
    Note:
        Model Depth 4
    Attributes:
        supersededBy: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Relates a term (i.e. a property, class or enumeration) to one that supersedes it.
    """

    supersededBy: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    


class EnergyEfficiencyEnumerationProperties(TypedDict):
    """Enumerates energy efficiency levels (also known as "classes" or "ratings") and certifications that are part of several international energy efficiency standards.

    References:
        https://schema.org/EnergyEfficiencyEnumeration
    Note:
        Model Depth 4
    Attributes:
    """

    


class AllProperties(EnergyEfficiencyEnumerationInheritedProperties , EnergyEfficiencyEnumerationProperties, TypedDict):
    pass


class EnergyEfficiencyEnumerationBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="EnergyEfficiencyEnumeration",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'supersededBy': {'exclude': True}}
        


def create_schema_org_model(type_: Union[EnergyEfficiencyEnumerationProperties, EnergyEfficiencyEnumerationInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "EnergyEfficiencyEnumeration"
    return model
    

EnergyEfficiencyEnumeration = create_schema_org_model()


def create_energyefficiencyenumeration_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_energyefficiencyenumeration_model(model=model)
    return pydantic_type(model).schema_json()


