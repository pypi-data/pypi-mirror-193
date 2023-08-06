"""
Researchers.

https://schema.org/Researcher
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ResearcherInheritedProperties(TypedDict):
    """Researchers.

    References:
        https://schema.org/Researcher
    Note:
        Model Depth 4
    Attributes:
        audienceType: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The target group associated with a given audience (e.g. veterans, car owners, musicians, etc.).
        geographicArea: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The geographic area associated with the audience.
    """

    audienceType: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    geographicArea: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]


class ResearcherProperties(TypedDict):
    """Researchers.

    References:
        https://schema.org/Researcher
    Note:
        Model Depth 4
    Attributes:
    """


class ResearcherAllProperties(
    ResearcherInheritedProperties, ResearcherProperties, TypedDict
):
    pass


class ResearcherBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Researcher", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"audienceType": {"exclude": True}}
        fields = {"geographicArea": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        ResearcherProperties, ResearcherInheritedProperties, ResearcherAllProperties
    ] = ResearcherAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Researcher"
    return model


Researcher = create_schema_org_model()


def create_researcher_model(
    model: Union[
        ResearcherProperties, ResearcherInheritedProperties, ResearcherAllProperties
    ]
):
    _type = deepcopy(ResearcherAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of Researcher. Please see: https://schema.org/Researcher"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: ResearcherAllProperties):
    pydantic_type = create_researcher_model(model=model)
    return pydantic_type(model).schema_json()
