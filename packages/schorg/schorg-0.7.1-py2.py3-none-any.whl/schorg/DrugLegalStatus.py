"""
The legal availability status of a medical drug.

https://schema.org/DrugLegalStatus
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class DrugLegalStatusInheritedProperties(TypedDict):
    """The legal availability status of a medical drug.

    References:
        https://schema.org/DrugLegalStatus
    Note:
        Model Depth 4
    Attributes:
    """

    


class DrugLegalStatusProperties(TypedDict):
    """The legal availability status of a medical drug.

    References:
        https://schema.org/DrugLegalStatus
    Note:
        Model Depth 4
    Attributes:
        applicableLocation: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The location in which the status applies.
    """

    applicableLocation: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    


class AllProperties(DrugLegalStatusInheritedProperties , DrugLegalStatusProperties, TypedDict):
    pass


class DrugLegalStatusBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="DrugLegalStatus",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'applicableLocation': {'exclude': True}}
        


def create_schema_org_model(type_: Union[DrugLegalStatusProperties, DrugLegalStatusInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "DrugLegalStatus"
    return model
    

DrugLegalStatus = create_schema_org_model()


def create_druglegalstatus_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_druglegalstatus_model(model=model)
    return pydantic_type(model).schema_json()


