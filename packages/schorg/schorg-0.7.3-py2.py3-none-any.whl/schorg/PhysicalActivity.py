"""
Any bodily activity that enhances or maintains physical fitness and overall health and wellness. Includes activity that is part of daily living and routine, structured exercise, and exercise prescribed as part of a medical treatment or recovery plan.

https://schema.org/PhysicalActivity
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class PhysicalActivityInheritedProperties(TypedDict):
    """Any bodily activity that enhances or maintains physical fitness and overall health and wellness. Includes activity that is part of daily living and routine, structured exercise, and exercise prescribed as part of a medical treatment or recovery plan.

    References:
        https://schema.org/PhysicalActivity
    Note:
        Model Depth 4
    Attributes:
    """


class PhysicalActivityProperties(TypedDict):
    """Any bodily activity that enhances or maintains physical fitness and overall health and wellness. Includes activity that is part of daily living and routine, structured exercise, and exercise prescribed as part of a medical treatment or recovery plan.

    References:
        https://schema.org/PhysicalActivity
    Note:
        Model Depth 4
    Attributes:
        pathophysiology: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Changes in the normal mechanical, physical, and biochemical functions that are associated with this activity or condition.
        epidemiology: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The characteristics of associated patients, such as age, gender, race etc.
        category: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): A category for the item. Greater signs or slashes can be used to informally indicate a category hierarchy.
        associatedAnatomy: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The anatomy of the underlying organ system or structures associated with this entity.
    """

    pathophysiology: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    epidemiology: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    category: NotRequired[
        Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]
    ]
    associatedAnatomy: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]


class PhysicalActivityAllProperties(
    PhysicalActivityInheritedProperties, PhysicalActivityProperties, TypedDict
):
    pass


class PhysicalActivityBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="PhysicalActivity", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"pathophysiology": {"exclude": True}}
        fields = {"epidemiology": {"exclude": True}}
        fields = {"category": {"exclude": True}}
        fields = {"associatedAnatomy": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        PhysicalActivityProperties,
        PhysicalActivityInheritedProperties,
        PhysicalActivityAllProperties,
    ] = PhysicalActivityAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "PhysicalActivity"
    return model


PhysicalActivity = create_schema_org_model()


def create_physicalactivity_model(
    model: Union[
        PhysicalActivityProperties,
        PhysicalActivityInheritedProperties,
        PhysicalActivityAllProperties,
    ]
):
    _type = deepcopy(PhysicalActivityAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: PhysicalActivityAllProperties):
    pydantic_type = create_physicalactivity_model(model=model)
    return pydantic_type(model).schema_json()
