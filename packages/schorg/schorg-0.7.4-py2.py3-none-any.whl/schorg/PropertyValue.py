"""
A property-value pair, e.g. representing a feature of a product or place. Use the 'name' property for the name of the property. If there is an additional human-readable version of the value, put that into the 'description' property. Always use specific schema.org properties when a) they exist and b) you can populate them. Using PropertyValue as a substitute will typically not trigger the same effect as using the original, specific property.    

https://schema.org/PropertyValue
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class PropertyValueInheritedProperties(TypedDict):
    """A property-value pair, e.g. representing a feature of a product or place. Use the 'name' property for the name of the property. If there is an additional human-readable version of the value, put that into the 'description' property. Always use specific schema.org properties when a) they exist and b) you can populate them. Using PropertyValue as a substitute will typically not trigger the same effect as using the original, specific property.

    References:
        https://schema.org/PropertyValue
    Note:
        Model Depth 4
    Attributes:
    """


class PropertyValueProperties(TypedDict):
    """A property-value pair, e.g. representing a feature of a product or place. Use the 'name' property for the name of the property. If there is an additional human-readable version of the value, put that into the 'description' property. Always use specific schema.org properties when a) they exist and b) you can populate them. Using PropertyValue as a substitute will typically not trigger the same effect as using the original, specific property.

    References:
        https://schema.org/PropertyValue
    Note:
        Model Depth 4
    Attributes:
        value: (Optional[Union[List[Union[StrictInt, StrictFloat, SchemaOrgObj, str, StrictBool]], StrictInt, StrictFloat, SchemaOrgObj, str, StrictBool]]): The value of the quantitative value or property value node.* For [[QuantitativeValue]] and [[MonetaryAmount]], the recommended type for values is 'Number'.* For [[PropertyValue]], it can be 'Text', 'Number', 'Boolean', or 'StructuredValue'.* Use values from 0123456789 (Unicode 'DIGIT ZERO' (U+0030) to 'DIGIT NINE' (U+0039)) rather than superficially similar Unicode symbols.* Use '.' (Unicode 'FULL STOP' (U+002E)) rather than ',' to indicate a decimal point. Avoid using these symbols as a readability separator.
        valueReference: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A secondary value that provides additional information on the original value, e.g. a reference temperature or a type of measurement.
        measurementTechnique: (Optional[Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]]): A technique or technology used in a [[Dataset]] (or [[DataDownload]], [[DataCatalog]]),corresponding to the method used for measuring the corresponding variable(s) (described using [[variableMeasured]]). This is oriented towards scientific and scholarly dataset publication but may have broader applicability; it is not intended as a full representation of measurement, but rather as a high level summary for dataset discovery.For example, if [[variableMeasured]] is: molecule concentration, [[measurementTechnique]] could be: "mass spectrometry" or "nmr spectroscopy" or "colorimetry" or "immunofluorescence".If the [[variableMeasured]] is "depression rating", the [[measurementTechnique]] could be "Zung Scale" or "HAM-D" or "Beck Depression Inventory".If there are several [[variableMeasured]] properties recorded for some given data object, use a [[PropertyValue]] for each [[variableMeasured]] and attach the corresponding [[measurementTechnique]].
        unitCode: (Optional[Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]]): The unit of measurement given using the UN/CEFACT Common Code (3 characters) or a URL. Other codes than the UN/CEFACT Common Code may be used with a prefix followed by a colon.
        maxValue: (Optional[Union[List[Union[StrictInt, StrictFloat, SchemaOrgObj, str]], StrictInt, StrictFloat, SchemaOrgObj, str]]): The upper value of some characteristic or property.
        unitText: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A string or text indicating the unit of measurement. Useful if you cannot provide a standard unit code for<a href='unitCode'>unitCode</a>.
        propertyID: (Optional[Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]]): A commonly used identifier for the characteristic represented by the property, e.g. a manufacturer or a standard code for a property. propertyID can be(1) a prefixed string, mainly meant to be used with standards for product properties; (2) a site-specific, non-prefixed string (e.g. the primary key of the property or the vendor-specific ID of the property), or (3)a URL indicating the type of the property, either pointing to an external vocabulary, or a Web resource that describes the property (e.g. a glossary entry).Standards bodies should promote a standard prefix for the identifiers of properties from their standards.
        minValue: (Optional[Union[List[Union[StrictInt, StrictFloat, SchemaOrgObj, str]], StrictInt, StrictFloat, SchemaOrgObj, str]]): The lower value of some characteristic or property.
    """

    value: NotRequired[
        Union[
            List[Union[StrictInt, StrictFloat, SchemaOrgObj, str, StrictBool]],
            StrictInt,
            StrictFloat,
            SchemaOrgObj,
            str,
            StrictBool,
        ]
    ]
    valueReference: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    measurementTechnique: NotRequired[
        Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]
    ]
    unitCode: NotRequired[
        Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]
    ]
    maxValue: NotRequired[
        Union[
            List[Union[StrictInt, StrictFloat, SchemaOrgObj, str]],
            StrictInt,
            StrictFloat,
            SchemaOrgObj,
            str,
        ]
    ]
    unitText: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    propertyID: NotRequired[
        Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]
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


class PropertyValueAllProperties(
    PropertyValueInheritedProperties, PropertyValueProperties, TypedDict
):
    pass


class PropertyValueBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="PropertyValue", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"value": {"exclude": True}}
        fields = {"valueReference": {"exclude": True}}
        fields = {"measurementTechnique": {"exclude": True}}
        fields = {"unitCode": {"exclude": True}}
        fields = {"maxValue": {"exclude": True}}
        fields = {"unitText": {"exclude": True}}
        fields = {"propertyID": {"exclude": True}}
        fields = {"minValue": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        PropertyValueProperties,
        PropertyValueInheritedProperties,
        PropertyValueAllProperties,
    ] = PropertyValueAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "PropertyValue"
    return model


PropertyValue = create_schema_org_model()


def create_propertyvalue_model(
    model: Union[
        PropertyValueProperties,
        PropertyValueInheritedProperties,
        PropertyValueAllProperties,
    ]
):
    _type = deepcopy(PropertyValueAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of PropertyValueAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: PropertyValueAllProperties):
    pydantic_type = create_propertyvalue_model(model=model)
    return pydantic_type(model).schema_json()
