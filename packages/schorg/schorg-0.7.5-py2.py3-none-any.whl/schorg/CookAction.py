"""
The act of producing/preparing food.

https://schema.org/CookAction
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class CookActionInheritedProperties(TypedDict):
    """The act of producing/preparing food.

    References:
        https://schema.org/CookAction
    Note:
        Model Depth 4
    Attributes:
    """


class CookActionProperties(TypedDict):
    """The act of producing/preparing food.

    References:
        https://schema.org/CookAction
    Note:
        Model Depth 4
    Attributes:
        foodEvent: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A sub property of location. The specific food event where the action occurred.
        recipe: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A sub property of instrument. The recipe/instructions used to perform the action.
        foodEstablishment: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A sub property of location. The specific food establishment where the action occurred.
    """

    foodEvent: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    recipe: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    foodEstablishment: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]


class CookActionAllProperties(
    CookActionInheritedProperties, CookActionProperties, TypedDict
):
    pass


class CookActionBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="CookAction", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"foodEvent": {"exclude": True}}
        fields = {"recipe": {"exclude": True}}
        fields = {"foodEstablishment": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        CookActionProperties, CookActionInheritedProperties, CookActionAllProperties
    ] = CookActionAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "CookAction"
    return model


CookAction = create_schema_org_model()


def create_cookaction_model(
    model: Union[
        CookActionProperties, CookActionInheritedProperties, CookActionAllProperties
    ]
):
    _type = deepcopy(CookActionAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of CookAction. Please see: https://schema.org/CookAction"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: CookActionAllProperties):
    pydantic_type = create_cookaction_model(model=model)
    return pydantic_type(model).schema_json()
