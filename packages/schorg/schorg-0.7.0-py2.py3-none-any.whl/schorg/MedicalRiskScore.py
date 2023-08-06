"""
A simple system that adds up the number of risk factors to yield a score that is associated with prognosis, e.g. CHAD score, TIMI risk score.

https://schema.org/MedicalRiskScore
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MedicalRiskScoreInheritedProperties(TypedDict):
    """A simple system that adds up the number of risk factors to yield a score that is associated with prognosis, e.g. CHAD score, TIMI risk score.

    References:
        https://schema.org/MedicalRiskScore
    Note:
        Model Depth 4
    Attributes:
        estimatesRiskOf: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The condition, complication, or symptom whose risk is being estimated.
        includedRiskFactor: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A modifiable or non-modifiable risk factor included in the calculation, e.g. age, coexisting condition.
    """

    estimatesRiskOf: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    includedRiskFactor: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    


class MedicalRiskScoreProperties(TypedDict):
    """A simple system that adds up the number of risk factors to yield a score that is associated with prognosis, e.g. CHAD score, TIMI risk score.

    References:
        https://schema.org/MedicalRiskScore
    Note:
        Model Depth 4
    Attributes:
        algorithm: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The algorithm or rules to follow to compute the score.
    """

    algorithm: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    


class AllProperties(MedicalRiskScoreInheritedProperties , MedicalRiskScoreProperties, TypedDict):
    pass


class MedicalRiskScoreBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="MedicalRiskScore",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'estimatesRiskOf': {'exclude': True}}
        fields = {'includedRiskFactor': {'exclude': True}}
        fields = {'algorithm': {'exclude': True}}
        


def create_schema_org_model(type_: Union[MedicalRiskScoreProperties, MedicalRiskScoreInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MedicalRiskScore"
    return model
    

MedicalRiskScore = create_schema_org_model()


def create_medicalriskscore_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_medicalriskscore_model(model=model)
    return pydantic_type(model).schema_json()


