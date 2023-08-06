"""
A publication event, e.g. catch-up TV or radio podcast, during which a program is available on-demand.

https://schema.org/OnDemandEvent
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class OnDemandEventInheritedProperties(TypedDict):
    """A publication event, e.g. catch-up TV or radio podcast, during which a program is available on-demand.

    References:
        https://schema.org/OnDemandEvent
    Note:
        Model Depth 4
    Attributes:
        publishedBy: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): An agent associated with the publication event.
        free: (Optional[Union[List[Union[SchemaOrgObj, str, StrictBool]], SchemaOrgObj, str, StrictBool]]): A flag to signal that the item, event, or place is accessible for free.
        publishedOn: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A broadcast service associated with the publication event.
    """

    publishedBy: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    free: NotRequired[Union[List[Union[SchemaOrgObj, str, StrictBool]], SchemaOrgObj, str, StrictBool]]
    publishedOn: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    


class OnDemandEventProperties(TypedDict):
    """A publication event, e.g. catch-up TV or radio podcast, during which a program is available on-demand.

    References:
        https://schema.org/OnDemandEvent
    Note:
        Model Depth 4
    Attributes:
    """

    


class AllProperties(OnDemandEventInheritedProperties , OnDemandEventProperties, TypedDict):
    pass


class OnDemandEventBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="OnDemandEvent",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'publishedBy': {'exclude': True}}
        fields = {'free': {'exclude': True}}
        fields = {'publishedOn': {'exclude': True}}
        


def create_schema_org_model(type_: Union[OnDemandEventProperties, OnDemandEventInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "OnDemandEvent"
    return model
    

OnDemandEvent = create_schema_org_model()


def create_ondemandevent_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_ondemandevent_model(model=model)
    return pydantic_type(model).schema_json()


