"""
An alternative, closely-related condition typically considered later in the differential diagnosis process along with the signs that are used to distinguish it.

https://schema.org/DDxElement
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class DDxElementInheritedProperties(TypedDict):
    """An alternative, closely-related condition typically considered later in the differential diagnosis process along with the signs that are used to distinguish it.

    References:
        https://schema.org/DDxElement
    Note:
        Model Depth 4
    Attributes:
    """

    


class DDxElementProperties(TypedDict):
    """An alternative, closely-related condition typically considered later in the differential diagnosis process along with the signs that are used to distinguish it.

    References:
        https://schema.org/DDxElement
    Note:
        Model Depth 4
    Attributes:
        distinguishingSign: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): One of a set of signs and symptoms that can be used to distinguish this diagnosis from others in the differential diagnosis.
        diagnosis: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): One or more alternative conditions considered in the differential diagnosis process as output of a diagnosis process.
    """

    distinguishingSign: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    diagnosis: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    


class AllProperties(DDxElementInheritedProperties , DDxElementProperties, TypedDict):
    pass


class DDxElementBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="DDxElement",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'distinguishingSign': {'exclude': True}}
        fields = {'diagnosis': {'exclude': True}}
        


def create_schema_org_model(type_: Union[DDxElementProperties, DDxElementInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "DDxElement"
    return model
    

DDxElement = create_schema_org_model()


def create_ddxelement_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_ddxelement_model(model=model)
    return pydantic_type(model).schema_json()


