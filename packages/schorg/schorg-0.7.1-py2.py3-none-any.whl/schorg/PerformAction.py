"""
The act of participating in performance arts.

https://schema.org/PerformAction
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class PerformActionInheritedProperties(TypedDict):
    """The act of participating in performance arts.

    References:
        https://schema.org/PerformAction
    Note:
        Model Depth 4
    Attributes:
        event: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Upcoming or past event associated with this place, organization, or action.
        audience: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): An intended audience, i.e. a group for whom something was created.
    """

    event: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    audience: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    


class PerformActionProperties(TypedDict):
    """The act of participating in performance arts.

    References:
        https://schema.org/PerformAction
    Note:
        Model Depth 4
    Attributes:
        entertainmentBusiness: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A sub property of location. The entertainment business where the action occurred.
    """

    entertainmentBusiness: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    


class AllProperties(PerformActionInheritedProperties , PerformActionProperties, TypedDict):
    pass


class PerformActionBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="PerformAction",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'event': {'exclude': True}}
        fields = {'audience': {'exclude': True}}
        fields = {'entertainmentBusiness': {'exclude': True}}
        


def create_schema_org_model(type_: Union[PerformActionProperties, PerformActionInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "PerformAction"
    return model
    

PerformAction = create_schema_org_model()


def create_performaction_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_performaction_model(model=model)
    return pydantic_type(model).schema_json()


