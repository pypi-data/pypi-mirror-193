"""
This type covers computer programming languages such as Scheme and Lisp, as well as other language-like computer representations. Natural languages are best represented with the [[Language]] type.

https://schema.org/ComputerLanguage
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ComputerLanguageInheritedProperties(TypedDict):
    """This type covers computer programming languages such as Scheme and Lisp, as well as other language-like computer representations. Natural languages are best represented with the [[Language]] type.

    References:
        https://schema.org/ComputerLanguage
    Note:
        Model Depth 3
    Attributes:
    """

    


class ComputerLanguageProperties(TypedDict):
    """This type covers computer programming languages such as Scheme and Lisp, as well as other language-like computer representations. Natural languages are best represented with the [[Language]] type.

    References:
        https://schema.org/ComputerLanguage
    Note:
        Model Depth 3
    Attributes:
    """

    


class AllProperties(ComputerLanguageInheritedProperties , ComputerLanguageProperties, TypedDict):
    pass


class ComputerLanguageBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="ComputerLanguage",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[ComputerLanguageProperties, ComputerLanguageInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ComputerLanguage"
    return model
    

ComputerLanguage = create_schema_org_model()


def create_computerlanguage_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_computerlanguage_model(model=model)
    return pydantic_type(model).schema_json()


