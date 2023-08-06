"""
Indicates a range of postal codes, usually defined as the set of valid codes between [[postalCodeBegin]] and [[postalCodeEnd]], inclusively.

https://schema.org/PostalCodeRangeSpecification
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


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
        postalCodeBegin: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): First postal code in a range (included).
        postalCodeEnd: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Last postal code in the range (included). Needs to be after [[postalCodeBegin]].
    """

    postalCodeBegin: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    postalCodeEnd: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]


class PostalCodeRangeSpecificationAllProperties(
    PostalCodeRangeSpecificationInheritedProperties,
    PostalCodeRangeSpecificationProperties,
    TypedDict,
):
    pass


class PostalCodeRangeSpecificationBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="PostalCodeRangeSpecification", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"postalCodeBegin": {"exclude": True}}
        fields = {"postalCodeEnd": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        PostalCodeRangeSpecificationProperties,
        PostalCodeRangeSpecificationInheritedProperties,
        PostalCodeRangeSpecificationAllProperties,
    ] = PostalCodeRangeSpecificationAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "PostalCodeRangeSpecification"
    return model


PostalCodeRangeSpecification = create_schema_org_model()


def create_postalcoderangespecification_model(
    model: Union[
        PostalCodeRangeSpecificationProperties,
        PostalCodeRangeSpecificationInheritedProperties,
        PostalCodeRangeSpecificationAllProperties,
    ]
):
    _type = deepcopy(PostalCodeRangeSpecificationAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of PostalCodeRangeSpecificationAllProperties"
            )
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: PostalCodeRangeSpecificationAllProperties):
    pydantic_type = create_postalcoderangespecification_model(model=model)
    return pydantic_type(model).schema_json()
