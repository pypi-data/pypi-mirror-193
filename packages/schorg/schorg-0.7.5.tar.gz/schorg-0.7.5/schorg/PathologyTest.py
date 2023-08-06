"""
A medical test performed by a laboratory that typically involves examination of a tissue sample by a pathologist.

https://schema.org/PathologyTest
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class PathologyTestInheritedProperties(TypedDict):
    """A medical test performed by a laboratory that typically involves examination of a tissue sample by a pathologist.

    References:
        https://schema.org/PathologyTest
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


class PathologyTestProperties(TypedDict):
    """A medical test performed by a laboratory that typically involves examination of a tissue sample by a pathologist.

    References:
        https://schema.org/PathologyTest
    Note:
        Model Depth 4
    Attributes:
        tissueSample: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The type of tissue sample required for the test.
    """

    tissueSample: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class PathologyTestAllProperties(
    PathologyTestInheritedProperties, PathologyTestProperties, TypedDict
):
    pass


class PathologyTestBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="PathologyTest", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"affectedBy": {"exclude": True}}
        fields = {"normalRange": {"exclude": True}}
        fields = {"signDetected": {"exclude": True}}
        fields = {"usedToDiagnose": {"exclude": True}}
        fields = {"usesDevice": {"exclude": True}}
        fields = {"tissueSample": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        PathologyTestProperties,
        PathologyTestInheritedProperties,
        PathologyTestAllProperties,
    ] = PathologyTestAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "PathologyTest"
    return model


PathologyTest = create_schema_org_model()


def create_pathologytest_model(
    model: Union[
        PathologyTestProperties,
        PathologyTestInheritedProperties,
        PathologyTestAllProperties,
    ]
):
    _type = deepcopy(PathologyTestAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of PathologyTest. Please see: https://schema.org/PathologyTest"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: PathologyTestAllProperties):
    pydantic_type = create_pathologytest_model(model=model)
    return pydantic_type(model).schema_json()
