"""
The act of inserting at the beginning if an ordered collection.

https://schema.org/PrependAction
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class PrependActionInheritedProperties(TypedDict):
    """The act of inserting at the beginning if an ordered collection.

    References:
        https://schema.org/PrependAction
    Note:
        Model Depth 6
    Attributes:
        toLocation: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A sub property of location. The final location of the object or the agent after the action.
    """

    toLocation: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    


class PrependActionProperties(TypedDict):
    """The act of inserting at the beginning if an ordered collection.

    References:
        https://schema.org/PrependAction
    Note:
        Model Depth 6
    Attributes:
    """

    


class AllProperties(PrependActionInheritedProperties , PrependActionProperties, TypedDict):
    pass


class PrependActionBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="PrependAction",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'toLocation': {'exclude': True}}
        


def create_schema_org_model(type_: Union[PrependActionProperties, PrependActionInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "PrependAction"
    return model
    

PrependAction = create_schema_org_model()


def create_prependaction_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_prependaction_model(model=model)
    return pydantic_type(model).schema_json()


