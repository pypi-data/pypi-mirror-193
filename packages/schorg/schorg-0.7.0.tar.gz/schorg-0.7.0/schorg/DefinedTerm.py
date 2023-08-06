"""
A word, name, acronym, phrase, etc. with a formal definition. Often used in the context of category or subject classification, glossaries or dictionaries, product or creative work types, etc. Use the name property for the term being defined, use termCode if the term has an alpha-numeric code allocated, use description to provide the definition of the term.

https://schema.org/DefinedTerm
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class DefinedTermInheritedProperties(TypedDict):
    """A word, name, acronym, phrase, etc. with a formal definition. Often used in the context of category or subject classification, glossaries or dictionaries, product or creative work types, etc. Use the name property for the term being defined, use termCode if the term has an alpha-numeric code allocated, use description to provide the definition of the term.

    References:
        https://schema.org/DefinedTerm
    Note:
        Model Depth 3
    Attributes:
    """

    


class DefinedTermProperties(TypedDict):
    """A word, name, acronym, phrase, etc. with a formal definition. Often used in the context of category or subject classification, glossaries or dictionaries, product or creative work types, etc. Use the name property for the term being defined, use termCode if the term has an alpha-numeric code allocated, use description to provide the definition of the term.

    References:
        https://schema.org/DefinedTerm
    Note:
        Model Depth 3
    Attributes:
        inDefinedTermSet: (Optional[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]): A [[DefinedTermSet]] that contains this term.
        termCode: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A code that identifies this [[DefinedTerm]] within a [[DefinedTermSet]]
    """

    inDefinedTermSet: NotRequired[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]
    termCode: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    


class AllProperties(DefinedTermInheritedProperties , DefinedTermProperties, TypedDict):
    pass


class DefinedTermBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="DefinedTerm",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'inDefinedTermSet': {'exclude': True}}
        fields = {'termCode': {'exclude': True}}
        


def create_schema_org_model(type_: Union[DefinedTermProperties, DefinedTermInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "DefinedTerm"
    return model
    

DefinedTerm = create_schema_org_model()


def create_definedterm_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_definedterm_model(model=model)
    return pydantic_type(model).schema_json()


