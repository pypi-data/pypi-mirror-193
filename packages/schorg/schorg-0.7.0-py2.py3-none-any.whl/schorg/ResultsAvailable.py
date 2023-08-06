"""
Results are available.

https://schema.org/ResultsAvailable
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ResultsAvailableInheritedProperties(TypedDict):
    """Results are available.

    References:
        https://schema.org/ResultsAvailable
    Note:
        Model Depth 6
    Attributes:
    """

    


class ResultsAvailableProperties(TypedDict):
    """Results are available.

    References:
        https://schema.org/ResultsAvailable
    Note:
        Model Depth 6
    Attributes:
    """

    


class AllProperties(ResultsAvailableInheritedProperties , ResultsAvailableProperties, TypedDict):
    pass


class ResultsAvailableBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="ResultsAvailable",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[ResultsAvailableProperties, ResultsAvailableInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ResultsAvailable"
    return model
    

ResultsAvailable = create_schema_org_model()


def create_resultsavailable_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_resultsavailable_model(model=model)
    return pydantic_type(model).schema_json()


