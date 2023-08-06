"""
The act of authoring written creative content.

https://schema.org/WriteAction
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class WriteActionInheritedProperties(TypedDict):
    """The act of authoring written creative content.

    References:
        https://schema.org/WriteAction
    Note:
        Model Depth 4
    Attributes:
    """

    


class WriteActionProperties(TypedDict):
    """The act of authoring written creative content.

    References:
        https://schema.org/WriteAction
    Note:
        Model Depth 4
    Attributes:
        language: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A sub property of instrument. The language used on this action.
        inLanguage: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The language of the content or performance or used in an action. Please use one of the language codes from the [IETF BCP 47 standard](http://tools.ietf.org/html/bcp47). See also [[availableLanguage]].
    """

    language: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    inLanguage: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    


class AllProperties(WriteActionInheritedProperties , WriteActionProperties, TypedDict):
    pass


class WriteActionBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="WriteAction",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'language': {'exclude': True}}
        fields = {'inLanguage': {'exclude': True}}
        


def create_schema_org_model(type_: Union[WriteActionProperties, WriteActionInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "WriteAction"
    return model
    

WriteAction = create_schema_org_model()


def create_writeaction_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_writeaction_model(model=model)
    return pydantic_type(model).schema_json()


