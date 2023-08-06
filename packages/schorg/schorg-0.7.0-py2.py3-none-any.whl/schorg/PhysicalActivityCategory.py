"""
Categories of physical activity, organized by physiologic classification.

https://schema.org/PhysicalActivityCategory
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class PhysicalActivityCategoryInheritedProperties(TypedDict):
    """Categories of physical activity, organized by physiologic classification.

    References:
        https://schema.org/PhysicalActivityCategory
    Note:
        Model Depth 4
    Attributes:
        supersededBy: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Relates a term (i.e. a property, class or enumeration) to one that supersedes it.
    """

    supersededBy: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    


class PhysicalActivityCategoryProperties(TypedDict):
    """Categories of physical activity, organized by physiologic classification.

    References:
        https://schema.org/PhysicalActivityCategory
    Note:
        Model Depth 4
    Attributes:
    """

    


class AllProperties(PhysicalActivityCategoryInheritedProperties , PhysicalActivityCategoryProperties, TypedDict):
    pass


class PhysicalActivityCategoryBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="PhysicalActivityCategory",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'supersededBy': {'exclude': True}}
        


def create_schema_org_model(type_: Union[PhysicalActivityCategoryProperties, PhysicalActivityCategoryInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "PhysicalActivityCategory"
    return model
    

PhysicalActivityCategory = create_schema_org_model()


def create_physicalactivitycategory_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_physicalactivitycategory_model(model=model)
    return pydantic_type(model).schema_json()


