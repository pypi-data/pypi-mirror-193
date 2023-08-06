"""
The act of expressing a preference from a set of options or a large or unbounded set of choices/options.

https://schema.org/ChooseAction
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ChooseActionInheritedProperties(TypedDict):
    """The act of expressing a preference from a set of options or a large or unbounded set of choices/options.

    References:
        https://schema.org/ChooseAction
    Note:
        Model Depth 4
    Attributes:
    """


class ChooseActionProperties(TypedDict):
    """The act of expressing a preference from a set of options or a large or unbounded set of choices/options.

    References:
        https://schema.org/ChooseAction
    Note:
        Model Depth 4
    Attributes:
        option: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A sub property of object. The options subject to this action.
        actionOption: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A sub property of object. The options subject to this action.
    """

    option: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    actionOption: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class ChooseActionAllProperties(
    ChooseActionInheritedProperties, ChooseActionProperties, TypedDict
):
    pass


class ChooseActionBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="ChooseAction", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"option": {"exclude": True}}
        fields = {"actionOption": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        ChooseActionProperties,
        ChooseActionInheritedProperties,
        ChooseActionAllProperties,
    ] = ChooseActionAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ChooseAction"
    return model


ChooseAction = create_schema_org_model()


def create_chooseaction_model(
    model: Union[
        ChooseActionProperties,
        ChooseActionInheritedProperties,
        ChooseActionAllProperties,
    ]
):
    _type = deepcopy(ChooseActionAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: ChooseActionAllProperties):
    pydantic_type = create_chooseaction_model(model=model)
    return pydantic_type(model).schema_json()
