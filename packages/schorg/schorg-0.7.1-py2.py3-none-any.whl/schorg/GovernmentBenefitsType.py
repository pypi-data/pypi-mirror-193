"""
GovernmentBenefitsType enumerates several kinds of government benefits to support the COVID-19 situation. Note that this structure may not capture all benefits offered.

https://schema.org/GovernmentBenefitsType
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class GovernmentBenefitsTypeInheritedProperties(TypedDict):
    """GovernmentBenefitsType enumerates several kinds of government benefits to support the COVID-19 situation. Note that this structure may not capture all benefits offered.

    References:
        https://schema.org/GovernmentBenefitsType
    Note:
        Model Depth 4
    Attributes:
        supersededBy: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Relates a term (i.e. a property, class or enumeration) to one that supersedes it.
    """

    supersededBy: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    


class GovernmentBenefitsTypeProperties(TypedDict):
    """GovernmentBenefitsType enumerates several kinds of government benefits to support the COVID-19 situation. Note that this structure may not capture all benefits offered.

    References:
        https://schema.org/GovernmentBenefitsType
    Note:
        Model Depth 4
    Attributes:
    """

    


class AllProperties(GovernmentBenefitsTypeInheritedProperties , GovernmentBenefitsTypeProperties, TypedDict):
    pass


class GovernmentBenefitsTypeBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="GovernmentBenefitsType",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'supersededBy': {'exclude': True}}
        


def create_schema_org_model(type_: Union[GovernmentBenefitsTypeProperties, GovernmentBenefitsTypeInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "GovernmentBenefitsType"
    return model
    

GovernmentBenefitsType = create_schema_org_model()


def create_governmentbenefitstype_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_governmentbenefitstype_model(model=model)
    return pydantic_type(model).schema_json()


