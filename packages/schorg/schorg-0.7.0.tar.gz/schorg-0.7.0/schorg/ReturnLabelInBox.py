"""
Specifies that a return label will be provided by the seller in the shipping box.

https://schema.org/ReturnLabelInBox
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ReturnLabelInBoxInheritedProperties(TypedDict):
    """Specifies that a return label will be provided by the seller in the shipping box.

    References:
        https://schema.org/ReturnLabelInBox
    Note:
        Model Depth 5
    Attributes:
    """

    


class ReturnLabelInBoxProperties(TypedDict):
    """Specifies that a return label will be provided by the seller in the shipping box.

    References:
        https://schema.org/ReturnLabelInBox
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(ReturnLabelInBoxInheritedProperties , ReturnLabelInBoxProperties, TypedDict):
    pass


class ReturnLabelInBoxBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="ReturnLabelInBox",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[ReturnLabelInBoxProperties, ReturnLabelInBoxInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ReturnLabelInBox"
    return model
    

ReturnLabelInBox = create_schema_org_model()


def create_returnlabelinbox_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_returnlabelinbox_model(model=model)
    return pydantic_type(model).schema_json()


