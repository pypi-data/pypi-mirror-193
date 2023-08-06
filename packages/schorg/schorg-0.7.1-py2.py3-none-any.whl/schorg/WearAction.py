"""
The act of dressing oneself in clothing.

https://schema.org/WearAction
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class WearActionInheritedProperties(TypedDict):
    """The act of dressing oneself in clothing.

    References:
        https://schema.org/WearAction
    Note:
        Model Depth 5
    Attributes:
    """

    


class WearActionProperties(TypedDict):
    """The act of dressing oneself in clothing.

    References:
        https://schema.org/WearAction
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(WearActionInheritedProperties , WearActionProperties, TypedDict):
    pass


class WearActionBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="WearAction",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[WearActionProperties, WearActionInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "WearAction"
    return model
    

WearAction = create_schema_org_model()


def create_wearaction_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_wearaction_model(model=model)
    return pydantic_type(model).schema_json()


