"""
A specific strength in which a medical drug is available in a specific country.

https://schema.org/DrugStrength
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class DrugStrengthInheritedProperties(TypedDict):
    """A specific strength in which a medical drug is available in a specific country.

    References:
        https://schema.org/DrugStrength
    Note:
        Model Depth 4
    Attributes:
    """


class DrugStrengthProperties(TypedDict):
    """A specific strength in which a medical drug is available in a specific country.

    References:
        https://schema.org/DrugStrength
    Note:
        Model Depth 4
    Attributes:
        activeIngredient: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): An active ingredient, typically chemical compounds and/or biologic substances.
        availableIn: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The location in which the strength is available.
        strengthValue: (Optional[Union[List[Union[StrictInt, StrictFloat, SchemaOrgObj, str]], StrictInt, StrictFloat, SchemaOrgObj, str]]): The value of an active ingredient's strength, e.g. 325.
        strengthUnit: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The units of an active ingredient's strength, e.g. mg.
        maximumIntake: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Recommended intake of this supplement for a given population as defined by a specific recommending authority.
    """

    activeIngredient: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    availableIn: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    strengthValue: NotRequired[
        Union[
            List[Union[StrictInt, StrictFloat, SchemaOrgObj, str]],
            StrictInt,
            StrictFloat,
            SchemaOrgObj,
            str,
        ]
    ]
    strengthUnit: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    maximumIntake: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]


class DrugStrengthAllProperties(
    DrugStrengthInheritedProperties, DrugStrengthProperties, TypedDict
):
    pass


class DrugStrengthBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="DrugStrength", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"activeIngredient": {"exclude": True}}
        fields = {"availableIn": {"exclude": True}}
        fields = {"strengthValue": {"exclude": True}}
        fields = {"strengthUnit": {"exclude": True}}
        fields = {"maximumIntake": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        DrugStrengthProperties,
        DrugStrengthInheritedProperties,
        DrugStrengthAllProperties,
    ] = DrugStrengthAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "DrugStrength"
    return model


DrugStrength = create_schema_org_model()


def create_drugstrength_model(
    model: Union[
        DrugStrengthProperties,
        DrugStrengthInheritedProperties,
        DrugStrengthAllProperties,
    ]
):
    _type = deepcopy(DrugStrengthAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of DrugStrengthAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: DrugStrengthAllProperties):
    pydantic_type = create_drugstrength_model(model=model)
    return pydantic_type(model).schema_json()
