"""
The legal availability status of a medical drug.

https://schema.org/DrugLegalStatus
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class DrugLegalStatusInheritedProperties(TypedDict):
    """The legal availability status of a medical drug.

    References:
        https://schema.org/DrugLegalStatus
    Note:
        Model Depth 4
    Attributes:
    """


class DrugLegalStatusProperties(TypedDict):
    """The legal availability status of a medical drug.

    References:
        https://schema.org/DrugLegalStatus
    Note:
        Model Depth 4
    Attributes:
        applicableLocation: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The location in which the status applies.
    """

    applicableLocation: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]


class DrugLegalStatusAllProperties(
    DrugLegalStatusInheritedProperties, DrugLegalStatusProperties, TypedDict
):
    pass


class DrugLegalStatusBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="DrugLegalStatus", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"applicableLocation": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        DrugLegalStatusProperties,
        DrugLegalStatusInheritedProperties,
        DrugLegalStatusAllProperties,
    ] = DrugLegalStatusAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "DrugLegalStatus"
    return model


DrugLegalStatus = create_schema_org_model()


def create_druglegalstatus_model(
    model: Union[
        DrugLegalStatusProperties,
        DrugLegalStatusInheritedProperties,
        DrugLegalStatusAllProperties,
    ]
):
    _type = deepcopy(DrugLegalStatusAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of DrugLegalStatus. Please see: https://schema.org/DrugLegalStatus"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: DrugLegalStatusAllProperties):
    pydantic_type = create_druglegalstatus_model(model=model)
    return pydantic_type(model).schema_json()
