"""
All the documents published by an official publisher should have at least the legal value level "OfficialLegalValue". This indicates that the document was published by an organisation with the public task of making it available (e.g. a consolidated version of an EU directive published by the EU Office of Publications).

https://schema.org/OfficialLegalValue
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class OfficialLegalValueInheritedProperties(TypedDict):
    """All the documents published by an official publisher should have at least the legal value level "OfficialLegalValue". This indicates that the document was published by an organisation with the public task of making it available (e.g. a consolidated version of an EU directive published by the EU Office of Publications).

    References:
        https://schema.org/OfficialLegalValue
    Note:
        Model Depth 5
    Attributes:
    """

    


class OfficialLegalValueProperties(TypedDict):
    """All the documents published by an official publisher should have at least the legal value level "OfficialLegalValue". This indicates that the document was published by an organisation with the public task of making it available (e.g. a consolidated version of an EU directive published by the EU Office of Publications).

    References:
        https://schema.org/OfficialLegalValue
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(OfficialLegalValueInheritedProperties , OfficialLegalValueProperties, TypedDict):
    pass


class OfficialLegalValueBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="OfficialLegalValue",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[OfficialLegalValueProperties, OfficialLegalValueInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "OfficialLegalValue"
    return model
    

OfficialLegalValue = create_schema_org_model()


def create_officiallegalvalue_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_officiallegalvalue_model(model=model)
    return pydantic_type(model).schema_json()


