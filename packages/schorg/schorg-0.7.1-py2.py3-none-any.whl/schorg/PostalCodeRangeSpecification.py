"""
Indicates a range of postal codes, usually defined as the set of valid codes between [[postalCodeBegin]] and [[postalCodeEnd]], inclusively.

https://schema.org/PostalCodeRangeSpecification
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class PostalCodeRangeSpecificationInheritedProperties(TypedDict):
    """Indicates a range of postal codes, usually defined as the set of valid codes between [[postalCodeBegin]] and [[postalCodeEnd]], inclusively.

    References:
        https://schema.org/PostalCodeRangeSpecification
    Note:
        Model Depth 4
    Attributes:
    """

    


class PostalCodeRangeSpecificationProperties(TypedDict):
    """Indicates a range of postal codes, usually defined as the set of valid codes between [[postalCodeBegin]] and [[postalCodeEnd]], inclusively.

    References:
        https://schema.org/PostalCodeRangeSpecification
    Note:
        Model Depth 4
    Attributes:
        postalCodeBegin: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): First postal code in a range (included).
        postalCodeEnd: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Last postal code in the range (included). Needs to be after [[postalCodeBegin]].
    """

    postalCodeBegin: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    postalCodeEnd: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    


class AllProperties(PostalCodeRangeSpecificationInheritedProperties , PostalCodeRangeSpecificationProperties, TypedDict):
    pass


class PostalCodeRangeSpecificationBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="PostalCodeRangeSpecification",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'postalCodeBegin': {'exclude': True}}
        fields = {'postalCodeEnd': {'exclude': True}}
        


def create_schema_org_model(type_: Union[PostalCodeRangeSpecificationProperties, PostalCodeRangeSpecificationInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "PostalCodeRangeSpecification"
    return model
    

PostalCodeRangeSpecification = create_schema_org_model()


def create_postalcoderangespecification_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_postalcoderangespecification_model(model=model)
    return pydantic_type(model).schema_json()


