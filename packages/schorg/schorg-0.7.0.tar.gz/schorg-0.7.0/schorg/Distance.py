"""
Properties that take Distances as values are of the form '&lt;Number&gt; &lt;Length unit of measure&gt;'. E.g., '7 ft'.

https://schema.org/Distance
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class DistanceInheritedProperties(TypedDict):
    """Properties that take Distances as values are of the form '&lt;Number&gt; &lt;Length unit of measure&gt;'. E.g., '7 ft'.

    References:
        https://schema.org/Distance
    Note:
        Model Depth 4
    Attributes:
    """

    


class DistanceProperties(TypedDict):
    """Properties that take Distances as values are of the form '&lt;Number&gt; &lt;Length unit of measure&gt;'. E.g., '7 ft'.

    References:
        https://schema.org/Distance
    Note:
        Model Depth 4
    Attributes:
    """

    


class AllProperties(DistanceInheritedProperties , DistanceProperties, TypedDict):
    pass


class DistanceBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="Distance",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[DistanceProperties, DistanceInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Distance"
    return model
    

Distance = create_schema_org_model()


def create_distance_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_distance_model(model=model)
    return pydantic_type(model).schema_json()


