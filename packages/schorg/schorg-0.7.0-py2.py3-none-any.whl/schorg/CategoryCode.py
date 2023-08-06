"""
A Category Code.

https://schema.org/CategoryCode
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class CategoryCodeInheritedProperties(TypedDict):
    """A Category Code.

    References:
        https://schema.org/CategoryCode
    Note:
        Model Depth 4
    Attributes:
        inDefinedTermSet: (Optional[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]): A [[DefinedTermSet]] that contains this term.
        termCode: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A code that identifies this [[DefinedTerm]] within a [[DefinedTermSet]]
    """

    inDefinedTermSet: NotRequired[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]
    termCode: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    


class CategoryCodeProperties(TypedDict):
    """A Category Code.

    References:
        https://schema.org/CategoryCode
    Note:
        Model Depth 4
    Attributes:
        codeValue: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A short textual code that uniquely identifies the value.
        inCodeSet: (Optional[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]): A [[CategoryCodeSet]] that contains this category code.
    """

    codeValue: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    inCodeSet: NotRequired[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]
    


class AllProperties(CategoryCodeInheritedProperties , CategoryCodeProperties, TypedDict):
    pass


class CategoryCodeBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="CategoryCode",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'inDefinedTermSet': {'exclude': True}}
        fields = {'termCode': {'exclude': True}}
        fields = {'codeValue': {'exclude': True}}
        fields = {'inCodeSet': {'exclude': True}}
        


def create_schema_org_model(type_: Union[CategoryCodeProperties, CategoryCodeInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "CategoryCode"
    return model
    

CategoryCode = create_schema_org_model()


def create_categorycode_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_categorycode_model(model=model)
    return pydantic_type(model).schema_json()


