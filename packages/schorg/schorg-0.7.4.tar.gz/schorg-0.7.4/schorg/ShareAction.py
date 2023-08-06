"""
The act of distributing content to people for their amusement or edification.

https://schema.org/ShareAction
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ShareActionInheritedProperties(TypedDict):
    """The act of distributing content to people for their amusement or edification.

    References:
        https://schema.org/ShareAction
    Note:
        Model Depth 5
    Attributes:
        about: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The subject matter of the content.
        recipient: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A sub property of participant. The participant who is at the receiving end of the action.
        language: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A sub property of instrument. The language used on this action.
        inLanguage: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The language of the content or performance or used in an action. Please use one of the language codes from the [IETF BCP 47 standard](http://tools.ietf.org/html/bcp47). See also [[availableLanguage]].
    """

    about: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    recipient: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    language: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    inLanguage: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]


class ShareActionProperties(TypedDict):
    """The act of distributing content to people for their amusement or edification.

    References:
        https://schema.org/ShareAction
    Note:
        Model Depth 5
    Attributes:
    """


class ShareActionAllProperties(
    ShareActionInheritedProperties, ShareActionProperties, TypedDict
):
    pass


class ShareActionBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="ShareAction", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"about": {"exclude": True}}
        fields = {"recipient": {"exclude": True}}
        fields = {"language": {"exclude": True}}
        fields = {"inLanguage": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        ShareActionProperties, ShareActionInheritedProperties, ShareActionAllProperties
    ] = ShareActionAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ShareAction"
    return model


ShareAction = create_schema_org_model()


def create_shareaction_model(
    model: Union[
        ShareActionProperties, ShareActionInheritedProperties, ShareActionAllProperties
    ]
):
    _type = deepcopy(ShareActionAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of ShareActionAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: ShareActionAllProperties):
    pydantic_type = create_shareaction_model(model=model)
    return pydantic_type(model).schema_json()
