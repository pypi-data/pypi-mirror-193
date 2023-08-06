"""
An entry point, within some Web-based protocol.

https://schema.org/EntryPoint
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class EntryPointInheritedProperties(TypedDict):
    """An entry point, within some Web-based protocol.

    References:
        https://schema.org/EntryPoint
    Note:
        Model Depth 3
    Attributes:
    """


class EntryPointProperties(TypedDict):
    """An entry point, within some Web-based protocol.

    References:
        https://schema.org/EntryPoint
    Note:
        Model Depth 3
    Attributes:
        encodingType: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The supported encoding type(s) for an EntryPoint request.
        actionApplication: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): An application that can complete the request.
        actionPlatform: (Optional[Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]]): The high level platform(s) where the Action can be performed for the given URL. To specify a specific application or operating system instance, use actionApplication.
        contentType: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The supported content type(s) for an EntryPoint response.
        application: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): An application that can complete the request.
        httpMethod: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): An HTTP method that specifies the appropriate HTTP method for a request to an HTTP EntryPoint. Values are capitalized strings as used in HTTP.
        urlTemplate: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): An url template (RFC6570) that will be used to construct the target of the execution of the action.
    """

    encodingType: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    actionApplication: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    actionPlatform: NotRequired[
        Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]
    ]
    contentType: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    application: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    httpMethod: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    urlTemplate: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]


class EntryPointAllProperties(
    EntryPointInheritedProperties, EntryPointProperties, TypedDict
):
    pass


class EntryPointBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="EntryPoint", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"encodingType": {"exclude": True}}
        fields = {"actionApplication": {"exclude": True}}
        fields = {"actionPlatform": {"exclude": True}}
        fields = {"contentType": {"exclude": True}}
        fields = {"application": {"exclude": True}}
        fields = {"httpMethod": {"exclude": True}}
        fields = {"urlTemplate": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        EntryPointProperties, EntryPointInheritedProperties, EntryPointAllProperties
    ] = EntryPointAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "EntryPoint"
    return model


EntryPoint = create_schema_org_model()


def create_entrypoint_model(
    model: Union[
        EntryPointProperties, EntryPointInheritedProperties, EntryPointAllProperties
    ]
):
    _type = deepcopy(EntryPointAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of EntryPointAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: EntryPointAllProperties):
    pydantic_type = create_entrypoint_model(model=model)
    return pydantic_type(model).schema_json()
