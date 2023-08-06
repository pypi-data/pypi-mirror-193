"""
A word, name, acronym, phrase, etc. with a formal definition. Often used in the context of category or subject classification, glossaries or dictionaries, product or creative work types, etc. Use the name property for the term being defined, use termCode if the term has an alpha-numeric code allocated, use description to provide the definition of the term.

https://schema.org/DefinedTerm
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


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
        inDefinedTermSet: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): A [[DefinedTermSet]] that contains this term.
        termCode: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A code that identifies this [[DefinedTerm]] within a [[DefinedTermSet]]
    """

    inDefinedTermSet: NotRequired[
        Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]
    ]
    termCode: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class DefinedTermAllProperties(
    DefinedTermInheritedProperties, DefinedTermProperties, TypedDict
):
    pass


class DefinedTermBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="DefinedTerm", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"inDefinedTermSet": {"exclude": True}}
        fields = {"termCode": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        DefinedTermProperties, DefinedTermInheritedProperties, DefinedTermAllProperties
    ] = DefinedTermAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "DefinedTerm"
    return model


DefinedTerm = create_schema_org_model()


def create_definedterm_model(
    model: Union[
        DefinedTermProperties, DefinedTermInheritedProperties, DefinedTermAllProperties
    ]
):
    _type = deepcopy(DefinedTermAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of DefinedTerm. Please see: https://schema.org/DefinedTerm"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: DefinedTermAllProperties):
    pydantic_type = create_definedterm_model(model=model)
    return pydantic_type(model).schema_json()
