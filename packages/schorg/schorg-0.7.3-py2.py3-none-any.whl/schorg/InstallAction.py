"""
The act of installing an application.

https://schema.org/InstallAction
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class InstallActionInheritedProperties(TypedDict):
    """The act of installing an application.

    References:
        https://schema.org/InstallAction
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


class InstallActionProperties(TypedDict):
    """The act of installing an application.

    References:
        https://schema.org/InstallAction
    Note:
        Model Depth 4
    Attributes:
    """


class InstallActionAllProperties(
    InstallActionInheritedProperties, InstallActionProperties, TypedDict
):
    pass


class InstallActionBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="InstallAction", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"actionAccessibilityRequirement": {"exclude": True}}
        fields = {"expectsAcceptanceOf": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        InstallActionProperties,
        InstallActionInheritedProperties,
        InstallActionAllProperties,
    ] = InstallActionAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "InstallAction"
    return model


InstallAction = create_schema_org_model()


def create_installaction_model(
    model: Union[
        InstallActionProperties,
        InstallActionInheritedProperties,
        InstallActionAllProperties,
    ]
):
    _type = deepcopy(InstallActionAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: InstallActionAllProperties):
    pydantic_type = create_installaction_model(model=model)
    return pydantic_type(model).schema_json()
