"""
A property, used to indicate attributes and relationships of some Thing; equivalent to rdf:Property.

https://schema.org/Property
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class PropertyInheritedProperties(TypedDict):
    """A property, used to indicate attributes and relationships of some Thing; equivalent to rdf:Property.

    References:
        https://schema.org/Property
    Note:
        Model Depth 3
    Attributes:
    """


class PropertyProperties(TypedDict):
    """A property, used to indicate attributes and relationships of some Thing; equivalent to rdf:Property.

    References:
        https://schema.org/Property
    Note:
        Model Depth 3
    Attributes:
        supersededBy: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Relates a term (i.e. a property, class or enumeration) to one that supersedes it.
        domainIncludes: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Relates a property to a class that is (one of) the type(s) the property is expected to be used on.
        inverseOf: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Relates a property to a property that is its inverse. Inverse properties relate the same pairs of items to each other, but in reversed direction. For example, the 'alumni' and 'alumniOf' properties are inverseOf each other. Some properties don't have explicit inverses; in these situations RDFa and JSON-LD syntax for reverse properties can be used.
        rangeIncludes: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Relates a property to a class that constitutes (one of) the expected type(s) for values of the property.
    """

    supersededBy: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    domainIncludes: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    inverseOf: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    rangeIncludes: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class PropertyAllProperties(PropertyInheritedProperties, PropertyProperties, TypedDict):
    pass


class PropertyBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Property", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"supersededBy": {"exclude": True}}
        fields = {"domainIncludes": {"exclude": True}}
        fields = {"inverseOf": {"exclude": True}}
        fields = {"rangeIncludes": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        PropertyProperties, PropertyInheritedProperties, PropertyAllProperties
    ] = PropertyAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Property"
    return model


Property = create_schema_org_model()


def create_property_model(
    model: Union[PropertyProperties, PropertyInheritedProperties, PropertyAllProperties]
):
    _type = deepcopy(PropertyAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: PropertyAllProperties):
    pydantic_type = create_property_model(model=model)
    return pydantic_type(model).schema_json()
