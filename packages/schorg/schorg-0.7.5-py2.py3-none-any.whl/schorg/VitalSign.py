"""
Vital signs are measures of various physiological functions in order to assess the most basic body functions.

https://schema.org/VitalSign
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class VitalSignInheritedProperties(TypedDict):
    """Vital signs are measures of various physiological functions in order to assess the most basic body functions.

    References:
        https://schema.org/VitalSign
    Note:
        Model Depth 6
    Attributes:
        identifyingExam: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A physical examination that can identify this sign.
        identifyingTest: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A diagnostic test that can identify this sign.
    """

    identifyingExam: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    identifyingTest: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]


class VitalSignProperties(TypedDict):
    """Vital signs are measures of various physiological functions in order to assess the most basic body functions.

    References:
        https://schema.org/VitalSign
    Note:
        Model Depth 6
    Attributes:
    """


class VitalSignAllProperties(
    VitalSignInheritedProperties, VitalSignProperties, TypedDict
):
    pass


class VitalSignBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="VitalSign", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"identifyingExam": {"exclude": True}}
        fields = {"identifyingTest": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        VitalSignProperties, VitalSignInheritedProperties, VitalSignAllProperties
    ] = VitalSignAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "VitalSign"
    return model


VitalSign = create_schema_org_model()


def create_vitalsign_model(
    model: Union[
        VitalSignProperties, VitalSignInheritedProperties, VitalSignAllProperties
    ]
):
    _type = deepcopy(VitalSignAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of VitalSign. Please see: https://schema.org/VitalSign"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: VitalSignAllProperties):
    pydantic_type = create_vitalsign_model(model=model)
    return pydantic_type(model).schema_json()
