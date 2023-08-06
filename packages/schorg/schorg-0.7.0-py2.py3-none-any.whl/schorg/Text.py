"""
Data type: Text.

https://schema.org/Text
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class TextInheritedProperties(TypedDict):
    """Data type: Text.

    References:
        https://schema.org/Text
    Note:
        Model Depth 5
    Attributes:
    """

    


class TextProperties(TypedDict):
    """Data type: Text.

    References:
        https://schema.org/Text
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(TextInheritedProperties , TextProperties, TypedDict):
    pass


class TextBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="Text",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[TextProperties, TextInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Text"
    return model
    

Text = create_schema_org_model()


def create_text_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_text_model(model=model)
    return pydantic_type(model).schema_json()


