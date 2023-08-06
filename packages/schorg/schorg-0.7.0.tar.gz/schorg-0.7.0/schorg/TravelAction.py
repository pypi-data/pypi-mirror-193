"""
The act of traveling from a fromLocation to a destination by a specified mode of transport, optionally with participants.

https://schema.org/TravelAction
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class TravelActionInheritedProperties(TypedDict):
    """The act of traveling from a fromLocation to a destination by a specified mode of transport, optionally with participants.

    References:
        https://schema.org/TravelAction
    Note:
        Model Depth 4
    Attributes:
        toLocation: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A sub property of location. The final location of the object or the agent after the action.
        fromLocation: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A sub property of location. The original location of the object or the agent before the action.
    """

    toLocation: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    fromLocation: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    


class TravelActionProperties(TypedDict):
    """The act of traveling from a fromLocation to a destination by a specified mode of transport, optionally with participants.

    References:
        https://schema.org/TravelAction
    Note:
        Model Depth 4
    Attributes:
        distance: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The distance travelled, e.g. exercising or travelling.
    """

    distance: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    


class AllProperties(TravelActionInheritedProperties , TravelActionProperties, TypedDict):
    pass


class TravelActionBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="TravelAction",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'toLocation': {'exclude': True}}
        fields = {'fromLocation': {'exclude': True}}
        fields = {'distance': {'exclude': True}}
        


def create_schema_org_model(type_: Union[TravelActionProperties, TravelActionInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "TravelAction"
    return model
    

TravelAction = create_schema_org_model()


def create_travelaction_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_travelaction_model(model=model)
    return pydantic_type(model).schema_json()


