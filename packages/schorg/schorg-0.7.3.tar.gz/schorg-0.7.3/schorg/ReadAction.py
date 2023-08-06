"""
The act of consuming written content.

https://schema.org/ReadAction
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ReadActionInheritedProperties(TypedDict):
    """The act of consuming written content.

    References:
        https://schema.org/ReadAction
    Note:
        Model Depth 4
    Attributes:
        actionAccessibilityRequirement: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A set of requirements that must be fulfilled in order to perform an Action. If more than one value is specified, fulfilling one set of requirements will allow the Action to be performed.
        expectsAcceptanceOf: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): An Offer which must be accepted before the user can perform the Action. For example, the user may need to buy a movie before being able to watch it.
    """

    actionAccessibilityRequirement: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    expectsAcceptanceOf: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]


class ReadActionProperties(TypedDict):
    """The act of consuming written content.

    References:
        https://schema.org/ReadAction
    Note:
        Model Depth 4
    Attributes:
    """


class ReadActionAllProperties(
    ReadActionInheritedProperties, ReadActionProperties, TypedDict
):
    pass


class ReadActionBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="ReadAction", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"actionAccessibilityRequirement": {"exclude": True}}
        fields = {"expectsAcceptanceOf": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        ReadActionProperties, ReadActionInheritedProperties, ReadActionAllProperties
    ] = ReadActionAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ReadAction"
    return model


ReadAction = create_schema_org_model()


def create_readaction_model(
    model: Union[
        ReadActionProperties, ReadActionInheritedProperties, ReadActionAllProperties
    ]
):
    _type = deepcopy(ReadActionAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: ReadActionAllProperties):
    pydantic_type = create_readaction_model(model=model)
    return pydantic_type(model).schema_json()
