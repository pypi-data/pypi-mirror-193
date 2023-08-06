"""
Any medical imaging modality typically used for diagnostic purposes.

https://schema.org/ImagingTest
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ImagingTestInheritedProperties(TypedDict):
    """Any medical imaging modality typically used for diagnostic purposes.

    References:
        https://schema.org/ImagingTest
    Note:
        Model Depth 4
    Attributes:
        affectedBy: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Drugs that affect the test's results.
        normalRange: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Range of acceptable values for a typical patient, when applicable.
        signDetected: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A sign detected by the test.
        usedToDiagnose: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A condition the test is used to diagnose.
        usesDevice: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Device used to perform the test.
    """

    affectedBy: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    normalRange: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    signDetected: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    usedToDiagnose: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    usesDevice: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    


class ImagingTestProperties(TypedDict):
    """Any medical imaging modality typically used for diagnostic purposes.

    References:
        https://schema.org/ImagingTest
    Note:
        Model Depth 4
    Attributes:
        imagingTechnique: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Imaging technique used.
    """

    imagingTechnique: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    


class AllProperties(ImagingTestInheritedProperties , ImagingTestProperties, TypedDict):
    pass


class ImagingTestBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="ImagingTest",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'affectedBy': {'exclude': True}}
        fields = {'normalRange': {'exclude': True}}
        fields = {'signDetected': {'exclude': True}}
        fields = {'usedToDiagnose': {'exclude': True}}
        fields = {'usesDevice': {'exclude': True}}
        fields = {'imagingTechnique': {'exclude': True}}
        


def create_schema_org_model(type_: Union[ImagingTestProperties, ImagingTestInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ImagingTest"
    return model
    

ImagingTest = create_schema_org_model()


def create_imagingtest_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_imagingtest_model(model=model)
    return pydantic_type(model).schema_json()


