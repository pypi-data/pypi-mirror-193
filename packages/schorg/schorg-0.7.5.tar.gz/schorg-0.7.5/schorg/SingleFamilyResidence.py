"""
Residence type: Single-family home.

https://schema.org/SingleFamilyResidence
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class SingleFamilyResidenceInheritedProperties(TypedDict):
    """Residence type: Single-family home.

    References:
        https://schema.org/SingleFamilyResidence
    Note:
        Model Depth 5
    Attributes:
        numberOfRooms: (Optional[Union[List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]], str, SchemaOrgObj, StrictInt, StrictFloat]]): The number of rooms (excluding bathrooms and closets) of the accommodation or lodging business.Typical unit code(s): ROM for room or C62 for no unit. The type of room can be put in the unitText property of the QuantitativeValue.
    """

    numberOfRooms: NotRequired[
        Union[
            List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]],
            str,
            SchemaOrgObj,
            StrictInt,
            StrictFloat,
        ]
    ]


class SingleFamilyResidenceProperties(TypedDict):
    """Residence type: Single-family home.

    References:
        https://schema.org/SingleFamilyResidence
    Note:
        Model Depth 5
    Attributes:
        numberOfRooms: (Optional[Union[List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]], str, SchemaOrgObj, StrictInt, StrictFloat]]): The number of rooms (excluding bathrooms and closets) of the accommodation or lodging business.Typical unit code(s): ROM for room or C62 for no unit. The type of room can be put in the unitText property of the QuantitativeValue.
        occupancy: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The allowed total occupancy for the accommodation in persons (including infants etc). For individual accommodations, this is not necessarily the legal maximum but defines the permitted usage as per the contractual agreement (e.g. a double room used by a single person).Typical unit code(s): C62 for person
    """

    numberOfRooms: NotRequired[
        Union[
            List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]],
            str,
            SchemaOrgObj,
            StrictInt,
            StrictFloat,
        ]
    ]
    occupancy: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class SingleFamilyResidenceAllProperties(
    SingleFamilyResidenceInheritedProperties, SingleFamilyResidenceProperties, TypedDict
):
    pass


class SingleFamilyResidenceBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="SingleFamilyResidence", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"numberOfRooms": {"exclude": True}}
        fields = {"numberOfRooms": {"exclude": True}}
        fields = {"occupancy": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        SingleFamilyResidenceProperties,
        SingleFamilyResidenceInheritedProperties,
        SingleFamilyResidenceAllProperties,
    ] = SingleFamilyResidenceAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "SingleFamilyResidence"
    return model


SingleFamilyResidence = create_schema_org_model()


def create_singlefamilyresidence_model(
    model: Union[
        SingleFamilyResidenceProperties,
        SingleFamilyResidenceInheritedProperties,
        SingleFamilyResidenceAllProperties,
    ]
):
    _type = deepcopy(SingleFamilyResidenceAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of SingleFamilyResidence. Please see: https://schema.org/SingleFamilyResidence"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: SingleFamilyResidenceAllProperties):
    pydantic_type = create_singlefamilyresidence_model(model=model)
    return pydantic_type(model).schema_json()
