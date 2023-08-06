"""
The act of inserting at the end if an ordered collection.

https://schema.org/AppendAction
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class AppendActionInheritedProperties(TypedDict):
    """The act of inserting at the end if an ordered collection.

    References:
        https://schema.org/AppendAction
    Note:
        Model Depth 6
    Attributes:
        toLocation: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A sub property of location. The final location of the object or the agent after the action.
    """

    toLocation: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    


class AppendActionProperties(TypedDict):
    """The act of inserting at the end if an ordered collection.

    References:
        https://schema.org/AppendAction
    Note:
        Model Depth 6
    Attributes:
    """

    


class AllProperties(AppendActionInheritedProperties , AppendActionProperties, TypedDict):
    pass


class AppendActionBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="AppendAction",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'toLocation': {'exclude': True}}
        


def create_schema_org_model(type_: Union[AppendActionProperties, AppendActionInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "AppendAction"
    return model
    

AppendAction = create_schema_org_model()


def create_appendaction_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_appendaction_model(model=model)
    return pydantic_type(model).schema_json()


