"""
Nutritional information about the recipe.

https://schema.org/NutritionInformation
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class NutritionInformationInheritedProperties(TypedDict):
    """Nutritional information about the recipe.

    References:
        https://schema.org/NutritionInformation
    Note:
        Model Depth 4
    Attributes:
    """


class NutritionInformationProperties(TypedDict):
    """Nutritional information about the recipe.

    References:
        https://schema.org/NutritionInformation
    Note:
        Model Depth 4
    Attributes:
        sodiumContent: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The number of milligrams of sodium.
        carbohydrateContent: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The number of grams of carbohydrates.
        fatContent: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The number of grams of fat.
        cholesterolContent: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The number of milligrams of cholesterol.
        calories: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The number of calories.
        unsaturatedFatContent: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The number of grams of unsaturated fat.
        sugarContent: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The number of grams of sugar.
        transFatContent: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The number of grams of trans fat.
        proteinContent: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The number of grams of protein.
        saturatedFatContent: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The number of grams of saturated fat.
        servingSize: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The serving size, in terms of the number of volume or mass.
        fiberContent: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The number of grams of fiber.
    """

    sodiumContent: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    carbohydrateContent: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    fatContent: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    cholesterolContent: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    calories: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    unsaturatedFatContent: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    sugarContent: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    transFatContent: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    proteinContent: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    saturatedFatContent: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    servingSize: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    fiberContent: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class NutritionInformationAllProperties(
    NutritionInformationInheritedProperties, NutritionInformationProperties, TypedDict
):
    pass


class NutritionInformationBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="NutritionInformation", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"sodiumContent": {"exclude": True}}
        fields = {"carbohydrateContent": {"exclude": True}}
        fields = {"fatContent": {"exclude": True}}
        fields = {"cholesterolContent": {"exclude": True}}
        fields = {"calories": {"exclude": True}}
        fields = {"unsaturatedFatContent": {"exclude": True}}
        fields = {"sugarContent": {"exclude": True}}
        fields = {"transFatContent": {"exclude": True}}
        fields = {"proteinContent": {"exclude": True}}
        fields = {"saturatedFatContent": {"exclude": True}}
        fields = {"servingSize": {"exclude": True}}
        fields = {"fiberContent": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        NutritionInformationProperties,
        NutritionInformationInheritedProperties,
        NutritionInformationAllProperties,
    ] = NutritionInformationAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "NutritionInformation"
    return model


NutritionInformation = create_schema_org_model()


def create_nutritioninformation_model(
    model: Union[
        NutritionInformationProperties,
        NutritionInformationInheritedProperties,
        NutritionInformationAllProperties,
    ]
):
    _type = deepcopy(NutritionInformationAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of NutritionInformation. Please see: https://schema.org/NutritionInformation"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: NutritionInformationAllProperties):
    pydantic_type = create_nutritioninformation_model(model=model)
    return pydantic_type(model).schema_json()
