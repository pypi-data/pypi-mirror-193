"""
A recipe. For dietary restrictions covered by the recipe, a few common restrictions are enumerated via [[suitableForDiet]]. The [[keywords]] property can also be used to add more detail.

https://schema.org/Recipe
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class RecipeInheritedProperties(TypedDict):
    """A recipe. For dietary restrictions covered by the recipe, a few common restrictions are enumerated via [[suitableForDiet]]. The [[keywords]] property can also be used to add more detail.

    References:
        https://schema.org/Recipe
    Note:
        Model Depth 4
    Attributes:
        prepTime: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The length of time it takes to prepare the items to be used in instructions or a direction, in [ISO 8601 duration format](http://en.wikipedia.org/wiki/ISO_8601).
        steps: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A single step item (as HowToStep, text, document, video, etc.) or a HowToSection (originally misnamed 'steps'; 'step' is preferred).
        estimatedCost: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The estimated cost of the supply or supplies consumed when performing instructions.
        yield_: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The quantity that results by performing instructions. For example, a paper airplane, 10 personalized candles.
        tool: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A sub property of instrument. An object used (but not consumed) when performing instructions or a direction.
        step: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A single step item (as HowToStep, text, document, video, etc.) or a HowToSection.
        performTime: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The length of time it takes to perform instructions or a direction (not including time to prepare the supplies), in [ISO 8601 duration format](http://en.wikipedia.org/wiki/ISO_8601).
        supply: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A sub-property of instrument. A supply consumed when performing instructions or a direction.
        totalTime: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The total time required to perform instructions or a direction (including time to prepare the supplies), in [ISO 8601 duration format](http://en.wikipedia.org/wiki/ISO_8601).
    """

    prepTime: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    steps: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    estimatedCost: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    yield_: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    tool: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    step: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    performTime: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    supply: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    totalTime: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    


class RecipeProperties(TypedDict):
    """A recipe. For dietary restrictions covered by the recipe, a few common restrictions are enumerated via [[suitableForDiet]]. The [[keywords]] property can also be used to add more detail.

    References:
        https://schema.org/Recipe
    Note:
        Model Depth 4
    Attributes:
        recipeYield: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The quantity produced by the recipe (for example, number of people served, number of servings, etc).
        nutrition: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Nutrition information about the recipe or menu item.
        cookingMethod: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The method of cooking, such as Frying, Steaming, ...
        suitableForDiet: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Indicates a dietary restriction or guideline for which this recipe or menu item is suitable, e.g. diabetic, halal etc.
        cookTime: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The time it takes to actually cook the dish, in [ISO 8601 duration format](http://en.wikipedia.org/wiki/ISO_8601).
        ingredients: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A single ingredient used in the recipe, e.g. sugar, flour or garlic.
        recipeCuisine: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The cuisine of the recipe (for example, French or Ethiopian).
        recipeInstructions: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A step in making the recipe, in the form of a single item (document, video, etc.) or an ordered list with HowToStep and/or HowToSection items.
        recipeIngredient: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A single ingredient used in the recipe, e.g. sugar, flour or garlic.
        recipeCategory: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The category of the recipe—for example, appetizer, entree, etc.
    """

    recipeYield: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    nutrition: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    cookingMethod: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    suitableForDiet: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    cookTime: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    ingredients: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    recipeCuisine: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    recipeInstructions: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    recipeIngredient: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    recipeCategory: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    


class AllProperties(RecipeInheritedProperties , RecipeProperties, TypedDict):
    pass


class RecipeBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="Recipe",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'prepTime': {'exclude': True}}
        fields = {'steps': {'exclude': True}}
        fields = {'estimatedCost': {'exclude': True}}
        fields = {'yield_': {'exclude': True}}
        fields = {'tool': {'exclude': True}}
        fields = {'step': {'exclude': True}}
        fields = {'performTime': {'exclude': True}}
        fields = {'supply': {'exclude': True}}
        fields = {'totalTime': {'exclude': True}}
        fields = {'recipeYield': {'exclude': True}}
        fields = {'nutrition': {'exclude': True}}
        fields = {'cookingMethod': {'exclude': True}}
        fields = {'suitableForDiet': {'exclude': True}}
        fields = {'cookTime': {'exclude': True}}
        fields = {'ingredients': {'exclude': True}}
        fields = {'recipeCuisine': {'exclude': True}}
        fields = {'recipeInstructions': {'exclude': True}}
        fields = {'recipeIngredient': {'exclude': True}}
        fields = {'recipeCategory': {'exclude': True}}
        


def create_schema_org_model(type_: Union[RecipeProperties, RecipeInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Recipe"
    return model
    

Recipe = create_schema_org_model()


def create_recipe_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_recipe_model(model=model)
    return pydantic_type(model).schema_json()


