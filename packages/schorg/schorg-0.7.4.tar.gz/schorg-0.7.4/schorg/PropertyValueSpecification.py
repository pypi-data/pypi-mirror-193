"""
A Property value specification.

https://schema.org/PropertyValueSpecification
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


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
        valuePattern: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Specifies a regular expression for testing literal values according to the HTML spec.
        readonlyValue: (Optional[Union[List[Union[SchemaOrgObj, str, StrictBool]], SchemaOrgObj, str, StrictBool]]): Whether or not a property is mutable.  Default is false. Specifying this for a property that also has a value makes it act similar to a "hidden" input in an HTML form.
        valueMinLength: (Optional[Union[List[Union[StrictInt, StrictFloat, SchemaOrgObj, str]], StrictInt, StrictFloat, SchemaOrgObj, str]]): Specifies the minimum allowed range for number of characters in a literal value.
        valueName: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Indicates the name of the PropertyValueSpecification to be used in URL templates and form encoding in a manner analogous to HTML's input@name.
        maxValue: (Optional[Union[List[Union[StrictInt, StrictFloat, SchemaOrgObj, str]], StrictInt, StrictFloat, SchemaOrgObj, str]]): The upper value of some characteristic or property.
        valueMaxLength: (Optional[Union[List[Union[StrictInt, StrictFloat, SchemaOrgObj, str]], StrictInt, StrictFloat, SchemaOrgObj, str]]): Specifies the allowed range for number of characters in a literal value.
        valueRequired: (Optional[Union[List[Union[SchemaOrgObj, str, StrictBool]], SchemaOrgObj, str, StrictBool]]): Whether the property must be filled in to complete the action.  Default is false.
        stepValue: (Optional[Union[List[Union[StrictInt, StrictFloat, SchemaOrgObj, str]], StrictInt, StrictFloat, SchemaOrgObj, str]]): The stepValue attribute indicates the granularity that is expected (and required) of the value in a PropertyValueSpecification.
        defaultValue: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The default value of the input.  For properties that expect a literal, the default is a literal value, for properties that expect an object, it's an ID reference to one of the current values.
        multipleValues: (Optional[Union[List[Union[SchemaOrgObj, str, StrictBool]], SchemaOrgObj, str, StrictBool]]): Whether multiple values are allowed for the property.  Default is false.
        minValue: (Optional[Union[List[Union[StrictInt, StrictFloat, SchemaOrgObj, str]], StrictInt, StrictFloat, SchemaOrgObj, str]]): The lower value of some characteristic or property.
    """

    valuePattern: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    readonlyValue: NotRequired[
        Union[List[Union[SchemaOrgObj, str, StrictBool]], SchemaOrgObj, str, StrictBool]
    ]
    valueMinLength: NotRequired[
        Union[
            List[Union[StrictInt, StrictFloat, SchemaOrgObj, str]],
            StrictInt,
            StrictFloat,
            SchemaOrgObj,
            str,
        ]
    ]
    valueName: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    maxValue: NotRequired[
        Union[
            List[Union[StrictInt, StrictFloat, SchemaOrgObj, str]],
            StrictInt,
            StrictFloat,
            SchemaOrgObj,
            str,
        ]
    ]
    valueMaxLength: NotRequired[
        Union[
            List[Union[StrictInt, StrictFloat, SchemaOrgObj, str]],
            StrictInt,
            StrictFloat,
            SchemaOrgObj,
            str,
        ]
    ]
    valueRequired: NotRequired[
        Union[List[Union[SchemaOrgObj, str, StrictBool]], SchemaOrgObj, str, StrictBool]
    ]
    stepValue: NotRequired[
        Union[
            List[Union[StrictInt, StrictFloat, SchemaOrgObj, str]],
            StrictInt,
            StrictFloat,
            SchemaOrgObj,
            str,
        ]
    ]
    defaultValue: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    multipleValues: NotRequired[
        Union[List[Union[SchemaOrgObj, str, StrictBool]], SchemaOrgObj, str, StrictBool]
    ]
    minValue: NotRequired[
        Union[
            List[Union[StrictInt, StrictFloat, SchemaOrgObj, str]],
            StrictInt,
            StrictFloat,
            SchemaOrgObj,
            str,
        ]
    ]


class PropertyValueSpecificationAllProperties(
    PropertyValueSpecificationInheritedProperties,
    PropertyValueSpecificationProperties,
    TypedDict,
):
    pass


class PropertyValueSpecificationBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="PropertyValueSpecification", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"valuePattern": {"exclude": True}}
        fields = {"readonlyValue": {"exclude": True}}
        fields = {"valueMinLength": {"exclude": True}}
        fields = {"valueName": {"exclude": True}}
        fields = {"maxValue": {"exclude": True}}
        fields = {"valueMaxLength": {"exclude": True}}
        fields = {"valueRequired": {"exclude": True}}
        fields = {"stepValue": {"exclude": True}}
        fields = {"defaultValue": {"exclude": True}}
        fields = {"multipleValues": {"exclude": True}}
        fields = {"minValue": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        PropertyValueSpecificationProperties,
        PropertyValueSpecificationInheritedProperties,
        PropertyValueSpecificationAllProperties,
    ] = PropertyValueSpecificationAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "PropertyValueSpecification"
    return model


PropertyValueSpecification = create_schema_org_model()


def create_propertyvaluespecification_model(
    model: Union[
        PropertyValueSpecificationProperties,
        PropertyValueSpecificationInheritedProperties,
        PropertyValueSpecificationAllProperties,
    ]
):
    _type = deepcopy(PropertyValueSpecificationAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of PropertyValueSpecificationAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: PropertyValueSpecificationAllProperties):
    pydantic_type = create_propertyvaluespecification_model(model=model)
    return pydantic_type(model).schema_json()
