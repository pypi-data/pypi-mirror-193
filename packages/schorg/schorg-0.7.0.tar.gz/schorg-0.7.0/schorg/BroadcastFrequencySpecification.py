"""
The frequency in MHz and the modulation used for a particular BroadcastService.

https://schema.org/BroadcastFrequencySpecification
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class BroadcastFrequencySpecificationInheritedProperties(TypedDict):
    """The frequency in MHz and the modulation used for a particular BroadcastService.

    References:
        https://schema.org/BroadcastFrequencySpecification
    Note:
        Model Depth 3
    Attributes:
    """

    


class BroadcastFrequencySpecificationProperties(TypedDict):
    """The frequency in MHz and the modulation used for a particular BroadcastService.

    References:
        https://schema.org/BroadcastFrequencySpecification
    Note:
        Model Depth 3
    Attributes:
        broadcastSignalModulation: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The modulation (e.g. FM, AM, etc) used by a particular broadcast service.
        broadcastSubChannel: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The subchannel used for the broadcast.
        broadcastFrequencyValue: (Optional[Union[List[Union[SchemaOrgObj, str, StrictInt, StrictFloat]], SchemaOrgObj, str, StrictInt, StrictFloat]]): The frequency in MHz for a particular broadcast.
    """

    broadcastSignalModulation: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    broadcastSubChannel: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    broadcastFrequencyValue: NotRequired[Union[List[Union[SchemaOrgObj, str, StrictInt, StrictFloat]], SchemaOrgObj, str, StrictInt, StrictFloat]]
    


class AllProperties(BroadcastFrequencySpecificationInheritedProperties , BroadcastFrequencySpecificationProperties, TypedDict):
    pass


class BroadcastFrequencySpecificationBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="BroadcastFrequencySpecification",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'broadcastSignalModulation': {'exclude': True}}
        fields = {'broadcastSubChannel': {'exclude': True}}
        fields = {'broadcastFrequencyValue': {'exclude': True}}
        


def create_schema_org_model(type_: Union[BroadcastFrequencySpecificationProperties, BroadcastFrequencySpecificationInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "BroadcastFrequencySpecification"
    return model
    

BroadcastFrequencySpecification = create_schema_org_model()


def create_broadcastfrequencyspecification_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_broadcastfrequencyspecification_model(model=model)
    return pydantic_type(model).schema_json()


