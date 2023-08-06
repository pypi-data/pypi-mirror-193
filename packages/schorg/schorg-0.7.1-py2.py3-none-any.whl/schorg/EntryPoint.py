"""
An entry point, within some Web-based protocol.

https://schema.org/EntryPoint
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


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
        encodingType: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The supported encoding type(s) for an EntryPoint request.
        actionApplication: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): An application that can complete the request.
        actionPlatform: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): The high level platform(s) where the Action can be performed for the given URL. To specify a specific application or operating system instance, use actionApplication.
        contentType: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The supported content type(s) for an EntryPoint response.
        application: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): An application that can complete the request.
        httpMethod: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): An HTTP method that specifies the appropriate HTTP method for a request to an HTTP EntryPoint. Values are capitalized strings as used in HTTP.
        urlTemplate: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): An url template (RFC6570) that will be used to construct the target of the execution of the action.
    """

    encodingType: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    actionApplication: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    actionPlatform: NotRequired[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]
    contentType: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    application: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    httpMethod: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    urlTemplate: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    


class AllProperties(EntryPointInheritedProperties , EntryPointProperties, TypedDict):
    pass


class EntryPointBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="EntryPoint",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'encodingType': {'exclude': True}}
        fields = {'actionApplication': {'exclude': True}}
        fields = {'actionPlatform': {'exclude': True}}
        fields = {'contentType': {'exclude': True}}
        fields = {'application': {'exclude': True}}
        fields = {'httpMethod': {'exclude': True}}
        fields = {'urlTemplate': {'exclude': True}}
        


def create_schema_org_model(type_: Union[EntryPointProperties, EntryPointInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "EntryPoint"
    return model
    

EntryPoint = create_schema_org_model()


def create_entrypoint_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_entrypoint_model(model=model)
    return pydantic_type(model).schema_json()


