"""
The act of downloading an object.

https://schema.org/DownloadAction
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class DownloadActionInheritedProperties(TypedDict):
    """The act of downloading an object.

    References:
        https://schema.org/DownloadAction
    Note:
        Model Depth 4
    Attributes:
        toLocation: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A sub property of location. The final location of the object or the agent after the action.
        fromLocation: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A sub property of location. The original location of the object or the agent before the action.
    """

    toLocation: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    fromLocation: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class DownloadActionProperties(TypedDict):
    """The act of downloading an object.

    References:
        https://schema.org/DownloadAction
    Note:
        Model Depth 4
    Attributes:
    """


class DownloadActionAllProperties(
    DownloadActionInheritedProperties, DownloadActionProperties, TypedDict
):
    pass


class DownloadActionBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="DownloadAction", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"toLocation": {"exclude": True}}
        fields = {"fromLocation": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        DownloadActionProperties,
        DownloadActionInheritedProperties,
        DownloadActionAllProperties,
    ] = DownloadActionAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "DownloadAction"
    return model


DownloadAction = create_schema_org_model()


def create_downloadaction_model(
    model: Union[
        DownloadActionProperties,
        DownloadActionInheritedProperties,
        DownloadActionAllProperties,
    ]
):
    _type = deepcopy(DownloadActionAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: DownloadActionAllProperties):
    pydantic_type = create_downloadaction_model(model=model)
    return pydantic_type(model).schema_json()
