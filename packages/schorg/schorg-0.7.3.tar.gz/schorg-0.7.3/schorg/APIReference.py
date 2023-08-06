"""
Reference documentation for application programming interfaces (APIs).

https://schema.org/APIReference
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class APIReferenceInheritedProperties(TypedDict):
    """Reference documentation for application programming interfaces (APIs).

    References:
        https://schema.org/APIReference
    Note:
        Model Depth 5
    Attributes:
        proficiencyLevel: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Proficiency needed for this content; expected values: 'Beginner', 'Expert'.
        dependencies: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Prerequisites needed to fulfill steps in article.
    """

    proficiencyLevel: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    dependencies: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class APIReferenceProperties(TypedDict):
    """Reference documentation for application programming interfaces (APIs).

    References:
        https://schema.org/APIReference
    Note:
        Model Depth 5
    Attributes:
        programmingModel: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Indicates whether API is managed or unmanaged.
        targetPlatform: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Type of app development: phone, Metro style, desktop, XBox, etc.
        assembly: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Library file name, e.g., mscorlib.dll, system.web.dll.
        assemblyVersion: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Associated product/technology version. E.g., .NET Framework 4.5.
        executableLibraryName: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Library file name, e.g., mscorlib.dll, system.web.dll.
    """

    programmingModel: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    targetPlatform: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    assembly: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    assemblyVersion: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    executableLibraryName: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]


class APIReferenceAllProperties(
    APIReferenceInheritedProperties, APIReferenceProperties, TypedDict
):
    pass


class APIReferenceBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="APIReference", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"proficiencyLevel": {"exclude": True}}
        fields = {"dependencies": {"exclude": True}}
        fields = {"programmingModel": {"exclude": True}}
        fields = {"targetPlatform": {"exclude": True}}
        fields = {"assembly": {"exclude": True}}
        fields = {"assemblyVersion": {"exclude": True}}
        fields = {"executableLibraryName": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        APIReferenceProperties,
        APIReferenceInheritedProperties,
        APIReferenceAllProperties,
    ] = APIReferenceAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "APIReference"
    return model


APIReference = create_schema_org_model()


def create_apireference_model(
    model: Union[
        APIReferenceProperties,
        APIReferenceInheritedProperties,
        APIReferenceAllProperties,
    ]
):
    _type = deepcopy(APIReferenceAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: APIReferenceAllProperties):
    pydantic_type = create_apireference_model(model=model)
    return pydantic_type(model).schema_json()
