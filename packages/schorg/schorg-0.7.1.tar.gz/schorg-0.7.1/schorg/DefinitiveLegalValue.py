"""
Indicates a document for which the text is conclusively what the law says and is legally binding. (E.g. the digitally signed version of an Official Journal.)  Something "Definitive" is considered to be also [[AuthoritativeLegalValue]].

https://schema.org/DefinitiveLegalValue
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class DefinitiveLegalValueInheritedProperties(TypedDict):
    """Indicates a document for which the text is conclusively what the law says and is legally binding. (E.g. the digitally signed version of an Official Journal.)  Something "Definitive" is considered to be also [[AuthoritativeLegalValue]].

    References:
        https://schema.org/DefinitiveLegalValue
    Note:
        Model Depth 5
    Attributes:
    """

    


class DefinitiveLegalValueProperties(TypedDict):
    """Indicates a document for which the text is conclusively what the law says and is legally binding. (E.g. the digitally signed version of an Official Journal.)  Something "Definitive" is considered to be also [[AuthoritativeLegalValue]].

    References:
        https://schema.org/DefinitiveLegalValue
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(DefinitiveLegalValueInheritedProperties , DefinitiveLegalValueProperties, TypedDict):
    pass


class DefinitiveLegalValueBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="DefinitiveLegalValue",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[DefinitiveLegalValueProperties, DefinitiveLegalValueInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "DefinitiveLegalValue"
    return model
    

DefinitiveLegalValue = create_schema_org_model()


def create_definitivelegalvalue_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_definitivelegalvalue_model(model=model)
    return pydantic_type(model).schema_json()


