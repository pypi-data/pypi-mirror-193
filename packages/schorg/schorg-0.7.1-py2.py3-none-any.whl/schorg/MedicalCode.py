"""
A code for a medical entity.

https://schema.org/MedicalCode
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MedicalCodeInheritedProperties(TypedDict):
    """A code for a medical entity.

    References:
        https://schema.org/MedicalCode
    Note:
        Model Depth 4
    Attributes:
        codeValue: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A short textual code that uniquely identifies the value.
        inCodeSet: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): A [[CategoryCodeSet]] that contains this category code.
    """

    codeValue: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    inCodeSet: NotRequired[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]
    


class MedicalCodeProperties(TypedDict):
    """A code for a medical entity.

    References:
        https://schema.org/MedicalCode
    Note:
        Model Depth 4
    Attributes:
        codeValue: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A short textual code that uniquely identifies the value.
        codingSystem: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The coding system, e.g. 'ICD-10'.
    """

    codeValue: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    codingSystem: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    


class AllProperties(MedicalCodeInheritedProperties , MedicalCodeProperties, TypedDict):
    pass


class MedicalCodeBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="MedicalCode",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'codeValue': {'exclude': True}}
        fields = {'inCodeSet': {'exclude': True}}
        fields = {'codeValue': {'exclude': True}}
        fields = {'codingSystem': {'exclude': True}}
        


def create_schema_org_model(type_: Union[MedicalCodeProperties, MedicalCodeInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MedicalCode"
    return model
    

MedicalCode = create_schema_org_model()


def create_medicalcode_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_medicalcode_model(model=model)
    return pydantic_type(model).schema_json()


