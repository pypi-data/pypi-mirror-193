"""
A stage of a medical condition, such as 'Stage IIIa'.

https://schema.org/MedicalConditionStage
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MedicalConditionStageInheritedProperties(TypedDict):
    """A stage of a medical condition, such as 'Stage IIIa'.

    References:
        https://schema.org/MedicalConditionStage
    Note:
        Model Depth 4
    Attributes:
    """

    


class MedicalConditionStageProperties(TypedDict):
    """A stage of a medical condition, such as 'Stage IIIa'.

    References:
        https://schema.org/MedicalConditionStage
    Note:
        Model Depth 4
    Attributes:
        subStageSuffix: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The substage, e.g. 'a' for Stage IIIa.
        stageAsNumber: (Optional[Union[List[Union[SchemaOrgObj, str, StrictInt, StrictFloat]], SchemaOrgObj, str, StrictInt, StrictFloat]]): The stage represented as a number, e.g. 3.
    """

    subStageSuffix: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    stageAsNumber: NotRequired[Union[List[Union[SchemaOrgObj, str, StrictInt, StrictFloat]], SchemaOrgObj, str, StrictInt, StrictFloat]]
    


class AllProperties(MedicalConditionStageInheritedProperties , MedicalConditionStageProperties, TypedDict):
    pass


class MedicalConditionStageBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="MedicalConditionStage",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'subStageSuffix': {'exclude': True}}
        fields = {'stageAsNumber': {'exclude': True}}
        


def create_schema_org_model(type_: Union[MedicalConditionStageProperties, MedicalConditionStageInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MedicalConditionStage"
    return model
    

MedicalConditionStage = create_schema_org_model()


def create_medicalconditionstage_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_medicalconditionstage_model(model=model)
    return pydantic_type(model).schema_json()


