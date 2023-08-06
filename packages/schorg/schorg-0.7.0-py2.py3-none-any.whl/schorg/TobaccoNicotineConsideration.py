"""
Item contains tobacco and/or nicotine, for example cigars, cigarettes, chewing tobacco, e-cigarettes, or hookahs.

https://schema.org/TobaccoNicotineConsideration
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class TobaccoNicotineConsiderationInheritedProperties(TypedDict):
    """Item contains tobacco and/or nicotine, for example cigars, cigarettes, chewing tobacco, e-cigarettes, or hookahs.

    References:
        https://schema.org/TobaccoNicotineConsideration
    Note:
        Model Depth 5
    Attributes:
    """

    


class TobaccoNicotineConsiderationProperties(TypedDict):
    """Item contains tobacco and/or nicotine, for example cigars, cigarettes, chewing tobacco, e-cigarettes, or hookahs.

    References:
        https://schema.org/TobaccoNicotineConsideration
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(TobaccoNicotineConsiderationInheritedProperties , TobaccoNicotineConsiderationProperties, TypedDict):
    pass


class TobaccoNicotineConsiderationBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="TobaccoNicotineConsideration",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[TobaccoNicotineConsiderationProperties, TobaccoNicotineConsiderationInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "TobaccoNicotineConsideration"
    return model
    

TobaccoNicotineConsideration = create_schema_org_model()


def create_tobacconicotineconsideration_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_tobacconicotineconsideration_model(model=model)
    return pydantic_type(model).schema_json()


