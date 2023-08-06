"""
Size related properties of a product, typically a size code ([[name]]) and optionally a [[sizeSystem]], [[sizeGroup]], and product measurements ([[hasMeasurement]]). In addition, the intended audience can be defined through [[suggestedAge]], [[suggestedGender]], and suggested body measurements ([[suggestedMeasurement]]).

https://schema.org/SizeSpecification
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class SizeSpecificationInheritedProperties(TypedDict):
    """Size related properties of a product, typically a size code ([[name]]) and optionally a [[sizeSystem]], [[sizeGroup]], and product measurements ([[hasMeasurement]]). In addition, the intended audience can be defined through [[suggestedAge]], [[suggestedGender]], and suggested body measurements ([[suggestedMeasurement]]).

    References:
        https://schema.org/SizeSpecification
    Note:
        Model Depth 5
    Attributes:
        greater: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): This ordering relation for qualitative values indicates that the subject is greater than the object.
        additionalProperty: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A property-value pair representing an additional characteristic of the entity, e.g. a product feature or another characteristic for which there is no matching property in schema.org.Note: Publishers should be aware that applications designed to use specific schema.org properties (e.g. https://schema.org/width, https://schema.org/color, https://schema.org/gtin13, ...) will typically expect such data to be provided using those properties, rather than using the generic property/value mechanism.
        valueReference: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A secondary value that provides additional information on the original value, e.g. a reference temperature or a type of measurement.
        equal: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): This ordering relation for qualitative values indicates that the subject is equal to the object.
        lesser: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): This ordering relation for qualitative values indicates that the subject is lesser than the object.
        greaterOrEqual: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): This ordering relation for qualitative values indicates that the subject is greater than or equal to the object.
        lesserOrEqual: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): This ordering relation for qualitative values indicates that the subject is lesser than or equal to the object.
        nonEqual: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): This ordering relation for qualitative values indicates that the subject is not equal to the object.
    """

    greater: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    additionalProperty: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    valueReference: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    equal: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    lesser: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    greaterOrEqual: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    lesserOrEqual: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    nonEqual: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    


class SizeSpecificationProperties(TypedDict):
    """Size related properties of a product, typically a size code ([[name]]) and optionally a [[sizeSystem]], [[sizeGroup]], and product measurements ([[hasMeasurement]]). In addition, the intended audience can be defined through [[suggestedAge]], [[suggestedGender]], and suggested body measurements ([[suggestedMeasurement]]).

    References:
        https://schema.org/SizeSpecification
    Note:
        Model Depth 5
    Attributes:
        hasMeasurement: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A product measurement, for example the inseam of pants, the wheel size of a bicycle, or the gauge of a screw. Usually an exact measurement, but can also be a range of measurements for adjustable products, for example belts and ski bindings.
        suggestedMeasurement: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A suggested range of body measurements for the intended audience or person, for example inseam between 32 and 34 inches or height between 170 and 190 cm. Typically found on a size chart for wearable products.
        sizeSystem: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The size system used to identify a product's size. Typically either a standard (for example, "GS1" or "ISO-EN13402"), country code (for example "US" or "JP"), or a measuring system (for example "Metric" or "Imperial").
        sizeGroup: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The size group (also known as "size type") for a product's size. Size groups are common in the fashion industry to define size segments and suggested audiences for wearable products. Multiple values can be combined, for example "men's big and tall", "petite maternity" or "regular"
        suggestedGender: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The suggested gender of the intended person or audience, for example "male", "female", or "unisex".
        suggestedAge: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The age or age range for the intended audience or person, for example 3-12 months for infants, 1-5 years for toddlers.
    """

    hasMeasurement: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    suggestedMeasurement: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    sizeSystem: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    sizeGroup: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    suggestedGender: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    suggestedAge: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    


class AllProperties(SizeSpecificationInheritedProperties , SizeSpecificationProperties, TypedDict):
    pass


class SizeSpecificationBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="SizeSpecification",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'greater': {'exclude': True}}
        fields = {'additionalProperty': {'exclude': True}}
        fields = {'valueReference': {'exclude': True}}
        fields = {'equal': {'exclude': True}}
        fields = {'lesser': {'exclude': True}}
        fields = {'greaterOrEqual': {'exclude': True}}
        fields = {'lesserOrEqual': {'exclude': True}}
        fields = {'nonEqual': {'exclude': True}}
        fields = {'hasMeasurement': {'exclude': True}}
        fields = {'suggestedMeasurement': {'exclude': True}}
        fields = {'sizeSystem': {'exclude': True}}
        fields = {'sizeGroup': {'exclude': True}}
        fields = {'suggestedGender': {'exclude': True}}
        fields = {'suggestedAge': {'exclude': True}}
        


def create_schema_org_model(type_: Union[SizeSpecificationProperties, SizeSpecificationInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "SizeSpecification"
    return model
    

SizeSpecification = create_schema_org_model()


def create_sizespecification_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_sizespecification_model(model=model)
    return pydantic_type(model).schema_json()


