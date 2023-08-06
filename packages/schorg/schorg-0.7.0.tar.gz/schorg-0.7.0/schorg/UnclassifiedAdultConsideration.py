"""
The item is suitable only for adults, without indicating why. Due to widespread use of "adult" as a euphemism for "sexual", many such items are likely suited also for the SexualContentConsideration code.

https://schema.org/UnclassifiedAdultConsideration
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class UnclassifiedAdultConsiderationInheritedProperties(TypedDict):
    """The item is suitable only for adults, without indicating why. Due to widespread use of "adult" as a euphemism for "sexual", many such items are likely suited also for the SexualContentConsideration code.

    References:
        https://schema.org/UnclassifiedAdultConsideration
    Note:
        Model Depth 5
    Attributes:
    """

    


class UnclassifiedAdultConsiderationProperties(TypedDict):
    """The item is suitable only for adults, without indicating why. Due to widespread use of "adult" as a euphemism for "sexual", many such items are likely suited also for the SexualContentConsideration code.

    References:
        https://schema.org/UnclassifiedAdultConsideration
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(UnclassifiedAdultConsiderationInheritedProperties , UnclassifiedAdultConsiderationProperties, TypedDict):
    pass


class UnclassifiedAdultConsiderationBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="UnclassifiedAdultConsideration",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[UnclassifiedAdultConsiderationProperties, UnclassifiedAdultConsiderationInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "UnclassifiedAdultConsideration"
    return model
    

UnclassifiedAdultConsideration = create_schema_org_model()


def create_unclassifiedadultconsideration_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_unclassifiedadultconsideration_model(model=model)
    return pydantic_type(model).schema_json()


