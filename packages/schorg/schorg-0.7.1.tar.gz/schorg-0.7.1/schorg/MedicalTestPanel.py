"""
Any collection of tests commonly ordered together.

https://schema.org/MedicalTestPanel
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MedicalTestPanelInheritedProperties(TypedDict):
    """Any collection of tests commonly ordered together.

    References:
        https://schema.org/MedicalTestPanel
    Note:
        Model Depth 4
    Attributes:
        affectedBy: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Drugs that affect the test's results.
        normalRange: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Range of acceptable values for a typical patient, when applicable.
        signDetected: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A sign detected by the test.
        usedToDiagnose: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A condition the test is used to diagnose.
        usesDevice: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Device used to perform the test.
    """

    affectedBy: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    normalRange: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    signDetected: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    usedToDiagnose: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    usesDevice: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    


class MedicalTestPanelProperties(TypedDict):
    """Any collection of tests commonly ordered together.

    References:
        https://schema.org/MedicalTestPanel
    Note:
        Model Depth 4
    Attributes:
        subTest: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A component test of the panel.
    """

    subTest: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    


class AllProperties(MedicalTestPanelInheritedProperties , MedicalTestPanelProperties, TypedDict):
    pass


class MedicalTestPanelBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="MedicalTestPanel",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'affectedBy': {'exclude': True}}
        fields = {'normalRange': {'exclude': True}}
        fields = {'signDetected': {'exclude': True}}
        fields = {'usedToDiagnose': {'exclude': True}}
        fields = {'usesDevice': {'exclude': True}}
        fields = {'subTest': {'exclude': True}}
        


def create_schema_org_model(type_: Union[MedicalTestPanelProperties, MedicalTestPanelInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MedicalTestPanel"
    return model
    

MedicalTestPanel = create_schema_org_model()


def create_medicaltestpanel_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_medicaltestpanel_model(model=model)
    return pydantic_type(model).schema_json()


