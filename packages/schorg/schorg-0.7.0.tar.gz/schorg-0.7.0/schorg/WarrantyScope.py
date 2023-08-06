"""
A range of services that will be provided to a customer free of charge in case of a defect or malfunction of a product.Commonly used values:* http://purl.org/goodrelations/v1#Labor-BringIn* http://purl.org/goodrelations/v1#PartsAndLabor-BringIn* http://purl.org/goodrelations/v1#PartsAndLabor-PickUp      

https://schema.org/WarrantyScope
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class WarrantyScopeInheritedProperties(TypedDict):
    """A range of services that will be provided to a customer free of charge in case of a defect or malfunction of a product.Commonly used values:* http://purl.org/goodrelations/v1#Labor-BringIn* http://purl.org/goodrelations/v1#PartsAndLabor-BringIn* http://purl.org/goodrelations/v1#PartsAndLabor-PickUp      

    References:
        https://schema.org/WarrantyScope
    Note:
        Model Depth 4
    Attributes:
        supersededBy: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Relates a term (i.e. a property, class or enumeration) to one that supersedes it.
    """

    supersededBy: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    


class WarrantyScopeProperties(TypedDict):
    """A range of services that will be provided to a customer free of charge in case of a defect or malfunction of a product.Commonly used values:* http://purl.org/goodrelations/v1#Labor-BringIn* http://purl.org/goodrelations/v1#PartsAndLabor-BringIn* http://purl.org/goodrelations/v1#PartsAndLabor-PickUp      

    References:
        https://schema.org/WarrantyScope
    Note:
        Model Depth 4
    Attributes:
    """

    


class AllProperties(WarrantyScopeInheritedProperties , WarrantyScopeProperties, TypedDict):
    pass


class WarrantyScopeBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="WarrantyScope",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'supersededBy': {'exclude': True}}
        


def create_schema_org_model(type_: Union[WarrantyScopeProperties, WarrantyScopeInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "WarrantyScope"
    return model
    

WarrantyScope = create_schema_org_model()


def create_warrantyscope_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_warrantyscope_model(model=model)
    return pydantic_type(model).schema_json()


