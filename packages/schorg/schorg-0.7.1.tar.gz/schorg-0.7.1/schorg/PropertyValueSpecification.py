"""
A Property value specification.

https://schema.org/PropertyValueSpecification
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class PropertyValueSpecificationInheritedProperties(TypedDict):
    """A Property value specification.

    References:
        https://schema.org/PropertyValueSpecification
    Note:
        Model Depth 3
    Attributes:
    """

    


class PropertyValueSpecificationProperties(TypedDict):
    """A Property value specification.

    References:
        https://schema.org/PropertyValueSpecification
    Note:
        Model Depth 3
    Attributes:
        valuePattern: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Specifies a regular expression for testing literal values according to the HTML spec.
        readonlyValue: (Optional[Union[List[Union[str, SchemaOrgObj, StrictBool]], str, SchemaOrgObj, StrictBool]]): Whether or not a property is mutable.  Default is false. Specifying this for a property that also has a value makes it act similar to a "hidden" input in an HTML form.
        valueMinLength: (Optional[Union[List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]], str, StrictInt, StrictFloat, SchemaOrgObj]]): Specifies the minimum allowed range for number of characters in a literal value.
        valueName: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Indicates the name of the PropertyValueSpecification to be used in URL templates and form encoding in a manner analogous to HTML's input@name.
        maxValue: (Optional[Union[List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]], str, StrictInt, StrictFloat, SchemaOrgObj]]): The upper value of some characteristic or property.
        valueMaxLength: (Optional[Union[List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]], str, StrictInt, StrictFloat, SchemaOrgObj]]): Specifies the allowed range for number of characters in a literal value.
        valueRequired: (Optional[Union[List[Union[str, SchemaOrgObj, StrictBool]], str, SchemaOrgObj, StrictBool]]): Whether the property must be filled in to complete the action.  Default is false.
        stepValue: (Optional[Union[List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]], str, StrictInt, StrictFloat, SchemaOrgObj]]): The stepValue attribute indicates the granularity that is expected (and required) of the value in a PropertyValueSpecification.
        defaultValue: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The default value of the input.  For properties that expect a literal, the default is a literal value, for properties that expect an object, it's an ID reference to one of the current values.
        multipleValues: (Optional[Union[List[Union[str, SchemaOrgObj, StrictBool]], str, SchemaOrgObj, StrictBool]]): Whether multiple values are allowed for the property.  Default is false.
        minValue: (Optional[Union[List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]], str, StrictInt, StrictFloat, SchemaOrgObj]]): The lower value of some characteristic or property.
    """

    valuePattern: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    readonlyValue: NotRequired[Union[List[Union[str, SchemaOrgObj, StrictBool]], str, SchemaOrgObj, StrictBool]]
    valueMinLength: NotRequired[Union[List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]], str, StrictInt, StrictFloat, SchemaOrgObj]]
    valueName: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    maxValue: NotRequired[Union[List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]], str, StrictInt, StrictFloat, SchemaOrgObj]]
    valueMaxLength: NotRequired[Union[List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]], str, StrictInt, StrictFloat, SchemaOrgObj]]
    valueRequired: NotRequired[Union[List[Union[str, SchemaOrgObj, StrictBool]], str, SchemaOrgObj, StrictBool]]
    stepValue: NotRequired[Union[List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]], str, StrictInt, StrictFloat, SchemaOrgObj]]
    defaultValue: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    multipleValues: NotRequired[Union[List[Union[str, SchemaOrgObj, StrictBool]], str, SchemaOrgObj, StrictBool]]
    minValue: NotRequired[Union[List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]], str, StrictInt, StrictFloat, SchemaOrgObj]]
    


class AllProperties(PropertyValueSpecificationInheritedProperties , PropertyValueSpecificationProperties, TypedDict):
    pass


class PropertyValueSpecificationBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="PropertyValueSpecification",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'valuePattern': {'exclude': True}}
        fields = {'readonlyValue': {'exclude': True}}
        fields = {'valueMinLength': {'exclude': True}}
        fields = {'valueName': {'exclude': True}}
        fields = {'maxValue': {'exclude': True}}
        fields = {'valueMaxLength': {'exclude': True}}
        fields = {'valueRequired': {'exclude': True}}
        fields = {'stepValue': {'exclude': True}}
        fields = {'defaultValue': {'exclude': True}}
        fields = {'multipleValues': {'exclude': True}}
        fields = {'minValue': {'exclude': True}}
        


def create_schema_org_model(type_: Union[PropertyValueSpecificationProperties, PropertyValueSpecificationInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "PropertyValueSpecification"
    return model
    

PropertyValueSpecification = create_schema_org_model()


def create_propertyvaluespecification_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_propertyvaluespecification_model(model=model)
    return pydantic_type(model).schema_json()


