"""
The act of swallowing liquids.

https://schema.org/DrinkAction
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class DrinkActionInheritedProperties(TypedDict):
    """The act of swallowing liquids.

    References:
        https://schema.org/DrinkAction
    Note:
        Model Depth 4
    Attributes:
        actionAccessibilityRequirement: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A set of requirements that must be fulfilled in order to perform an Action. If more than one value is specified, fulfilling one set of requirements will allow the Action to be performed.
        expectsAcceptanceOf: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): An Offer which must be accepted before the user can perform the Action. For example, the user may need to buy a movie before being able to watch it.
    """

    actionAccessibilityRequirement: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    expectsAcceptanceOf: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]


class DrinkActionProperties(TypedDict):
    """The act of swallowing liquids.

    References:
        https://schema.org/DrinkAction
    Note:
        Model Depth 4
    Attributes:
    """


class DrinkActionAllProperties(
    DrinkActionInheritedProperties, DrinkActionProperties, TypedDict
):
    pass


class DrinkActionBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="DrinkAction", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"actionAccessibilityRequirement": {"exclude": True}}
        fields = {"expectsAcceptanceOf": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        DrinkActionProperties, DrinkActionInheritedProperties, DrinkActionAllProperties
    ] = DrinkActionAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "DrinkAction"
    return model


DrinkAction = create_schema_org_model()


def create_drinkaction_model(
    model: Union[
        DrinkActionProperties, DrinkActionInheritedProperties, DrinkActionAllProperties
    ]
):
    _type = deepcopy(DrinkActionAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of DrinkActionAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: DrinkActionAllProperties):
    pydantic_type = create_drinkaction_model(model=model)
    return pydantic_type(model).schema_json()
