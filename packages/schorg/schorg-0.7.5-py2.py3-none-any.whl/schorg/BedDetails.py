"""
An entity holding detailed information about the available bed types, e.g. the quantity of twin beds for a hotel room. For the single case of just one bed of a certain type, you can use bed directly with a text. See also [[BedType]] (under development).

https://schema.org/BedDetails
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class BedDetailsInheritedProperties(TypedDict):
    """An entity holding detailed information about the available bed types, e.g. the quantity of twin beds for a hotel room. For the single case of just one bed of a certain type, you can use bed directly with a text. See also [[BedType]] (under development).

    References:
        https://schema.org/BedDetails
    Note:
        Model Depth 3
    Attributes:
    """


class BedDetailsProperties(TypedDict):
    """An entity holding detailed information about the available bed types, e.g. the quantity of twin beds for a hotel room. For the single case of just one bed of a certain type, you can use bed directly with a text. See also [[BedType]] (under development).

    References:
        https://schema.org/BedDetails
    Note:
        Model Depth 3
    Attributes:
        typeOfBed: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The type of bed to which the BedDetail refers, i.e. the type of bed available in the quantity indicated by quantity.
        numberOfBeds: (Optional[Union[List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]], str, SchemaOrgObj, StrictInt, StrictFloat]]): The quantity of the given bed type available in the HotelRoom, Suite, House, or Apartment.
    """

    typeOfBed: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    numberOfBeds: NotRequired[
        Union[
            List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]],
            str,
            SchemaOrgObj,
            StrictInt,
            StrictFloat,
        ]
    ]


class BedDetailsAllProperties(
    BedDetailsInheritedProperties, BedDetailsProperties, TypedDict
):
    pass


class BedDetailsBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="BedDetails", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"typeOfBed": {"exclude": True}}
        fields = {"numberOfBeds": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        BedDetailsProperties, BedDetailsInheritedProperties, BedDetailsAllProperties
    ] = BedDetailsAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "BedDetails"
    return model


BedDetails = create_schema_org_model()


def create_beddetails_model(
    model: Union[
        BedDetailsProperties, BedDetailsInheritedProperties, BedDetailsAllProperties
    ]
):
    _type = deepcopy(BedDetailsAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of BedDetails. Please see: https://schema.org/BedDetails"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: BedDetailsAllProperties):
    pydantic_type = create_beddetails_model(model=model)
    return pydantic_type(model).schema_json()
