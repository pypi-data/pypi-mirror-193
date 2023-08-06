"""
A pharmacy or drugstore.

https://schema.org/Pharmacy
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class PharmacyInheritedProperties(TypedDict):
    """A pharmacy or drugstore.

    References:
        https://schema.org/Pharmacy
    Note:
        Model Depth 4
    Attributes:
        healthPlanNetworkId: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Name or unique ID of network. (Networks are often reused across different insurance plans.)
        medicalSpecialty: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A medical specialty of the provider.
        isAcceptingNewPatients: (Optional[Union[List[Union[SchemaOrgObj, str, StrictBool]], SchemaOrgObj, str, StrictBool]]): Whether the provider is accepting new patients.
    """

    healthPlanNetworkId: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    medicalSpecialty: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    isAcceptingNewPatients: NotRequired[Union[List[Union[SchemaOrgObj, str, StrictBool]], SchemaOrgObj, str, StrictBool]]
    


class PharmacyProperties(TypedDict):
    """A pharmacy or drugstore.

    References:
        https://schema.org/Pharmacy
    Note:
        Model Depth 4
    Attributes:
    """

    


class AllProperties(PharmacyInheritedProperties , PharmacyProperties, TypedDict):
    pass


class PharmacyBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="Pharmacy",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'healthPlanNetworkId': {'exclude': True}}
        fields = {'medicalSpecialty': {'exclude': True}}
        fields = {'isAcceptingNewPatients': {'exclude': True}}
        


def create_schema_org_model(type_: Union[PharmacyProperties, PharmacyInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Pharmacy"
    return model
    

Pharmacy = create_schema_org_model()


def create_pharmacy_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_pharmacy_model(model=model)
    return pydantic_type(model).schema_json()


