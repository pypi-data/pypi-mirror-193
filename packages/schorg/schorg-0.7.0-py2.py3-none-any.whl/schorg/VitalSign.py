"""
Vital signs are measures of various physiological functions in order to assess the most basic body functions.

https://schema.org/VitalSign
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class VitalSignInheritedProperties(TypedDict):
    """Vital signs are measures of various physiological functions in order to assess the most basic body functions.

    References:
        https://schema.org/VitalSign
    Note:
        Model Depth 6
    Attributes:
        identifyingExam: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A physical examination that can identify this sign.
        identifyingTest: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A diagnostic test that can identify this sign.
    """

    identifyingExam: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    identifyingTest: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    


class VitalSignProperties(TypedDict):
    """Vital signs are measures of various physiological functions in order to assess the most basic body functions.

    References:
        https://schema.org/VitalSign
    Note:
        Model Depth 6
    Attributes:
    """

    


class AllProperties(VitalSignInheritedProperties , VitalSignProperties, TypedDict):
    pass


class VitalSignBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="VitalSign",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'identifyingExam': {'exclude': True}}
        fields = {'identifyingTest': {'exclude': True}}
        


def create_schema_org_model(type_: Union[VitalSignProperties, VitalSignInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "VitalSign"
    return model
    

VitalSign = create_schema_org_model()


def create_vitalsign_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_vitalsign_model(model=model)
    return pydantic_type(model).schema_json()


