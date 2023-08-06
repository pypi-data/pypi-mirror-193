"""
A vet's office.

https://schema.org/VeterinaryCare
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class VeterinaryCareInheritedProperties(TypedDict):
    """A vet's office.

    References:
        https://schema.org/VeterinaryCare
    Note:
        Model Depth 4
    Attributes:
        healthPlanNetworkId: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Name or unique ID of network. (Networks are often reused across different insurance plans.)
        medicalSpecialty: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A medical specialty of the provider.
        isAcceptingNewPatients: (Optional[Union[List[Union[str, SchemaOrgObj, StrictBool]], str, SchemaOrgObj, StrictBool]]): Whether the provider is accepting new patients.
    """

    healthPlanNetworkId: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    medicalSpecialty: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    isAcceptingNewPatients: NotRequired[Union[List[Union[str, SchemaOrgObj, StrictBool]], str, SchemaOrgObj, StrictBool]]
    


class VeterinaryCareProperties(TypedDict):
    """A vet's office.

    References:
        https://schema.org/VeterinaryCare
    Note:
        Model Depth 4
    Attributes:
    """

    


class AllProperties(VeterinaryCareInheritedProperties , VeterinaryCareProperties, TypedDict):
    pass


class VeterinaryCareBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="VeterinaryCare",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'healthPlanNetworkId': {'exclude': True}}
        fields = {'medicalSpecialty': {'exclude': True}}
        fields = {'isAcceptingNewPatients': {'exclude': True}}
        


def create_schema_org_model(type_: Union[VeterinaryCareProperties, VeterinaryCareInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "VeterinaryCare"
    return model
    

VeterinaryCare = create_schema_org_model()


def create_veterinarycare_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_veterinarycare_model(model=model)
    return pydantic_type(model).schema_json()


