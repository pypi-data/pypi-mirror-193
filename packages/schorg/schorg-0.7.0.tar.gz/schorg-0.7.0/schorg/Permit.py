"""
A permit issued by an organization, e.g. a parking pass.

https://schema.org/Permit
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class PermitInheritedProperties(TypedDict):
    """A permit issued by an organization, e.g. a parking pass.

    References:
        https://schema.org/Permit
    Note:
        Model Depth 3
    Attributes:
    """

    


class PermitProperties(TypedDict):
    """A permit issued by an organization, e.g. a parking pass.

    References:
        https://schema.org/Permit
    Note:
        Model Depth 3
    Attributes:
        permitAudience: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The target audience for this permit.
        issuedBy: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The organization issuing the ticket or permit.
        validUntil: (Optional[Union[List[Union[SchemaOrgObj, str, date]], SchemaOrgObj, str, date]]): The date when the item is no longer valid.
        validFor: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The duration of validity of a permit or similar thing.
        validIn: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The geographic area where a permit or similar thing is valid.
        validFrom: (Optional[Union[List[Union[datetime, SchemaOrgObj, str, date]], datetime, SchemaOrgObj, str, date]]): The date when the item becomes valid.
        issuedThrough: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The service through which the permit was granted.
    """

    permitAudience: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    issuedBy: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    validUntil: NotRequired[Union[List[Union[SchemaOrgObj, str, date]], SchemaOrgObj, str, date]]
    validFor: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    validIn: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    validFrom: NotRequired[Union[List[Union[datetime, SchemaOrgObj, str, date]], datetime, SchemaOrgObj, str, date]]
    issuedThrough: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    


class AllProperties(PermitInheritedProperties , PermitProperties, TypedDict):
    pass


class PermitBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="Permit",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'permitAudience': {'exclude': True}}
        fields = {'issuedBy': {'exclude': True}}
        fields = {'validUntil': {'exclude': True}}
        fields = {'validFor': {'exclude': True}}
        fields = {'validIn': {'exclude': True}}
        fields = {'validFrom': {'exclude': True}}
        fields = {'issuedThrough': {'exclude': True}}
        


def create_schema_org_model(type_: Union[PermitProperties, PermitInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Permit"
    return model
    

Permit = create_schema_org_model()


def create_permit_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_permit_model(model=model)
    return pydantic_type(model).schema_json()


