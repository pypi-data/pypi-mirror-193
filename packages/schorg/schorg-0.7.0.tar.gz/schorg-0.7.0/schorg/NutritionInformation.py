"""
Nutritional information about the recipe.

https://schema.org/NutritionInformation
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


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
        sodiumContent: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The number of milligrams of sodium.
        carbohydrateContent: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The number of grams of carbohydrates.
        fatContent: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The number of grams of fat.
        cholesterolContent: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The number of milligrams of cholesterol.
        calories: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The number of calories.
        unsaturatedFatContent: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The number of grams of unsaturated fat.
        sugarContent: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The number of grams of sugar.
        transFatContent: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The number of grams of trans fat.
        proteinContent: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The number of grams of protein.
        saturatedFatContent: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The number of grams of saturated fat.
        servingSize: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The serving size, in terms of the number of volume or mass.
        fiberContent: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The number of grams of fiber.
    """

    sodiumContent: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    carbohydrateContent: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    fatContent: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    cholesterolContent: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    calories: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    unsaturatedFatContent: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    sugarContent: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    transFatContent: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    proteinContent: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    saturatedFatContent: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    servingSize: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    fiberContent: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    


class AllProperties(NutritionInformationInheritedProperties , NutritionInformationProperties, TypedDict):
    pass


class NutritionInformationBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="NutritionInformation",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'sodiumContent': {'exclude': True}}
        fields = {'carbohydrateContent': {'exclude': True}}
        fields = {'fatContent': {'exclude': True}}
        fields = {'cholesterolContent': {'exclude': True}}
        fields = {'calories': {'exclude': True}}
        fields = {'unsaturatedFatContent': {'exclude': True}}
        fields = {'sugarContent': {'exclude': True}}
        fields = {'transFatContent': {'exclude': True}}
        fields = {'proteinContent': {'exclude': True}}
        fields = {'saturatedFatContent': {'exclude': True}}
        fields = {'servingSize': {'exclude': True}}
        fields = {'fiberContent': {'exclude': True}}
        


def create_schema_org_model(type_: Union[NutritionInformationProperties, NutritionInformationInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "NutritionInformation"
    return model
    

NutritionInformation = create_schema_org_model()


def create_nutritioninformation_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_nutritioninformation_model(model=model)
    return pydantic_type(model).schema_json()


