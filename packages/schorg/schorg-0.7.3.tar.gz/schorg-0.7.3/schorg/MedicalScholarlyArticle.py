"""
A scholarly article in the medical domain.

https://schema.org/MedicalScholarlyArticle
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MedicalScholarlyArticleInheritedProperties(TypedDict):
    """A scholarly article in the medical domain.

    References:
        https://schema.org/MedicalScholarlyArticle
    Note:
        Model Depth 5
    Attributes:
    """


class MedicalScholarlyArticleProperties(TypedDict):
    """A scholarly article in the medical domain.

    References:
        https://schema.org/MedicalScholarlyArticle
    Note:
        Model Depth 5
    Attributes:
        publicationType: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The type of the medical article, taken from the US NLM MeSH publication type catalog. See also [MeSH documentation](http://www.nlm.nih.gov/mesh/pubtypes.html).
    """

    publicationType: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]


class MedicalScholarlyArticleAllProperties(
    MedicalScholarlyArticleInheritedProperties,
    MedicalScholarlyArticleProperties,
    TypedDict,
):
    pass


class MedicalScholarlyArticleBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="MedicalScholarlyArticle", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"publicationType": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        MedicalScholarlyArticleProperties,
        MedicalScholarlyArticleInheritedProperties,
        MedicalScholarlyArticleAllProperties,
    ] = MedicalScholarlyArticleAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MedicalScholarlyArticle"
    return model


MedicalScholarlyArticle = create_schema_org_model()


def create_medicalscholarlyarticle_model(
    model: Union[
        MedicalScholarlyArticleProperties,
        MedicalScholarlyArticleInheritedProperties,
        MedicalScholarlyArticleAllProperties,
    ]
):
    _type = deepcopy(MedicalScholarlyArticleAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: MedicalScholarlyArticleAllProperties):
    pydantic_type = create_medicalscholarlyarticle_model(model=model)
    return pydantic_type(model).schema_json()
