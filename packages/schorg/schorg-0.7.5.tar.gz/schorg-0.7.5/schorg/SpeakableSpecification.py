"""
A SpeakableSpecification indicates (typically via [[xpath]] or [[cssSelector]]) sections of a document that are highlighted as particularly [[speakable]]. Instances of this type are expected to be used primarily as values of the [[speakable]] property.

https://schema.org/SpeakableSpecification
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class SpeakableSpecificationInheritedProperties(TypedDict):
    """A SpeakableSpecification indicates (typically via [[xpath]] or [[cssSelector]]) sections of a document that are highlighted as particularly [[speakable]]. Instances of this type are expected to be used primarily as values of the [[speakable]] property.

    References:
        https://schema.org/SpeakableSpecification
    Note:
        Model Depth 3
    Attributes:
    """


class SpeakableSpecificationProperties(TypedDict):
    """A SpeakableSpecification indicates (typically via [[xpath]] or [[cssSelector]]) sections of a document that are highlighted as particularly [[speakable]]. Instances of this type are expected to be used primarily as values of the [[speakable]] property.

    References:
        https://schema.org/SpeakableSpecification
    Note:
        Model Depth 3
    Attributes:
        xpath: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): An XPath, e.g. of a [[SpeakableSpecification]] or [[WebPageElement]]. In the latter case, multiple matches within a page can constitute a single conceptual "Web page element".
        cssSelector: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A CSS selector, e.g. of a [[SpeakableSpecification]] or [[WebPageElement]]. In the latter case, multiple matches within a page can constitute a single conceptual "Web page element".
    """

    xpath: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    cssSelector: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class SpeakableSpecificationAllProperties(
    SpeakableSpecificationInheritedProperties,
    SpeakableSpecificationProperties,
    TypedDict,
):
    pass


class SpeakableSpecificationBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="SpeakableSpecification", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"xpath": {"exclude": True}}
        fields = {"cssSelector": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        SpeakableSpecificationProperties,
        SpeakableSpecificationInheritedProperties,
        SpeakableSpecificationAllProperties,
    ] = SpeakableSpecificationAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "SpeakableSpecification"
    return model


SpeakableSpecification = create_schema_org_model()


def create_speakablespecification_model(
    model: Union[
        SpeakableSpecificationProperties,
        SpeakableSpecificationInheritedProperties,
        SpeakableSpecificationAllProperties,
    ]
):
    _type = deepcopy(SpeakableSpecificationAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of SpeakableSpecification. Please see: https://schema.org/SpeakableSpecification"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: SpeakableSpecificationAllProperties):
    pydantic_type = create_speakablespecification_model(model=model)
    return pydantic_type(model).schema_json()
