"""
A facility, often associated with a hospital or medical school, that is devoted to the specific diagnosis and/or healthcare. Previously limited to outpatients but with evolution it may be open to inpatients as well.

https://schema.org/MedicalClinic
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MedicalClinicInheritedProperties(TypedDict):
    """A facility, often associated with a hospital or medical school, that is devoted to the specific diagnosis and/or healthcare. Previously limited to outpatients but with evolution it may be open to inpatients as well.

    References:
        https://schema.org/MedicalClinic
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
    


class MedicalClinicProperties(TypedDict):
    """A facility, often associated with a hospital or medical school, that is devoted to the specific diagnosis and/or healthcare. Previously limited to outpatients but with evolution it may be open to inpatients as well.

    References:
        https://schema.org/MedicalClinic
    Note:
        Model Depth 4
    Attributes:
        medicalSpecialty: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A medical specialty of the provider.
        availableService: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A medical service available from this provider.
    """

    medicalSpecialty: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    availableService: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    


class AllProperties(MedicalClinicInheritedProperties , MedicalClinicProperties, TypedDict):
    pass


class MedicalClinicBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="MedicalClinic",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'healthPlanNetworkId': {'exclude': True}}
        fields = {'medicalSpecialty': {'exclude': True}}
        fields = {'isAcceptingNewPatients': {'exclude': True}}
        fields = {'medicalSpecialty': {'exclude': True}}
        fields = {'availableService': {'exclude': True}}
        


def create_schema_org_model(type_: Union[MedicalClinicProperties, MedicalClinicInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MedicalClinic"
    return model
    

MedicalClinic = create_schema_org_model()


def create_medicalclinic_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_medicalclinic_model(model=model)
    return pydantic_type(model).schema_json()


