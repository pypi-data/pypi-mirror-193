"""
The act of swallowing solid objects.

https://schema.org/EatAction
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class EatActionInheritedProperties(TypedDict):
    """The act of swallowing solid objects.

    References:
        https://schema.org/EatAction
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


class EatActionProperties(TypedDict):
    """The act of swallowing solid objects.

    References:
        https://schema.org/EatAction
    Note:
        Model Depth 4
    Attributes:
    """


class EatActionAllProperties(
    EatActionInheritedProperties, EatActionProperties, TypedDict
):
    pass


class EatActionBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="EatAction", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"actionAccessibilityRequirement": {"exclude": True}}
        fields = {"expectsAcceptanceOf": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        EatActionProperties, EatActionInheritedProperties, EatActionAllProperties
    ] = EatActionAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "EatAction"
    return model


EatAction = create_schema_org_model()


def create_eataction_model(
    model: Union[
        EatActionProperties, EatActionInheritedProperties, EatActionAllProperties
    ]
):
    _type = deepcopy(EatActionAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of EatActionAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: EatActionAllProperties):
    pydantic_type = create_eataction_model(model=model)
    return pydantic_type(model).schema_json()
