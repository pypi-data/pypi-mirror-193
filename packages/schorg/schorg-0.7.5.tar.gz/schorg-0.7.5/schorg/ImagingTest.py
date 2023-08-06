"""
Any medical imaging modality typically used for diagnostic purposes.

https://schema.org/ImagingTest
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ImagingTestInheritedProperties(TypedDict):
    """Any medical imaging modality typically used for diagnostic purposes.

    References:
        https://schema.org/ImagingTest
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
    usedToDiagnose: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    usesDevice: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class ImagingTestProperties(TypedDict):
    """Any medical imaging modality typically used for diagnostic purposes.

    References:
        https://schema.org/ImagingTest
    Note:
        Model Depth 4
    Attributes:
        imagingTechnique: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Imaging technique used.
    """

    imagingTechnique: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]


class ImagingTestAllProperties(
    ImagingTestInheritedProperties, ImagingTestProperties, TypedDict
):
    pass


class ImagingTestBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="ImagingTest", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"affectedBy": {"exclude": True}}
        fields = {"normalRange": {"exclude": True}}
        fields = {"signDetected": {"exclude": True}}
        fields = {"usedToDiagnose": {"exclude": True}}
        fields = {"usesDevice": {"exclude": True}}
        fields = {"imagingTechnique": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        ImagingTestProperties, ImagingTestInheritedProperties, ImagingTestAllProperties
    ] = ImagingTestAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ImagingTest"
    return model


ImagingTest = create_schema_org_model()


def create_imagingtest_model(
    model: Union[
        ImagingTestProperties, ImagingTestInheritedProperties, ImagingTestAllProperties
    ]
):
    _type = deepcopy(ImagingTestAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of ImagingTest. Please see: https://schema.org/ImagingTest"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: ImagingTestAllProperties):
    pydantic_type = create_imagingtest_model(model=model)
    return pydantic_type(model).schema_json()
