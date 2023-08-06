"""
Specifies a location feature by providing a structured value representing a feature of an accommodation as a property-value pair of varying degrees of formality.

https://schema.org/LocationFeatureSpecification
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class LocationFeatureSpecificationInheritedProperties(TypedDict):
    """Specifies a location feature by providing a structured value representing a feature of an accommodation as a property-value pair of varying degrees of formality.

    References:
        https://schema.org/LocationFeatureSpecification
    Note:
        Model Depth 5
    Attributes:
        value: (Optional[Union[List[Union[SchemaOrgObj, str, StrictBool, StrictInt, StrictFloat]], SchemaOrgObj, str, StrictBool, StrictInt, StrictFloat]]): The value of the quantitative value or property value node.* For [[QuantitativeValue]] and [[MonetaryAmount]], the recommended type for values is 'Number'.* For [[PropertyValue]], it can be 'Text', 'Number', 'Boolean', or 'StructuredValue'.* Use values from 0123456789 (Unicode 'DIGIT ZERO' (U+0030) to 'DIGIT NINE' (U+0039)) rather than superficially similar Unicode symbols.* Use '.' (Unicode 'FULL STOP' (U+002E)) rather than ',' to indicate a decimal point. Avoid using these symbols as a readability separator.
        valueReference: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A secondary value that provides additional information on the original value, e.g. a reference temperature or a type of measurement.
        measurementTechnique: (Optional[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]): A technique or technology used in a [[Dataset]] (or [[DataDownload]], [[DataCatalog]]),corresponding to the method used for measuring the corresponding variable(s) (described using [[variableMeasured]]). This is oriented towards scientific and scholarly dataset publication but may have broader applicability; it is not intended as a full representation of measurement, but rather as a high level summary for dataset discovery.For example, if [[variableMeasured]] is: molecule concentration, [[measurementTechnique]] could be: "mass spectrometry" or "nmr spectroscopy" or "colorimetry" or "immunofluorescence".If the [[variableMeasured]] is "depression rating", the [[measurementTechnique]] could be "Zung Scale" or "HAM-D" or "Beck Depression Inventory".If there are several [[variableMeasured]] properties recorded for some given data object, use a [[PropertyValue]] for each [[variableMeasured]] and attach the corresponding [[measurementTechnique]].      
        unitCode: (Optional[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]): The unit of measurement given using the UN/CEFACT Common Code (3 characters) or a URL. Other codes than the UN/CEFACT Common Code may be used with a prefix followed by a colon.
        maxValue: (Optional[Union[List[Union[SchemaOrgObj, str, StrictInt, StrictFloat]], SchemaOrgObj, str, StrictInt, StrictFloat]]): The upper value of some characteristic or property.
        unitText: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A string or text indicating the unit of measurement. Useful if you cannot provide a standard unit code for<a href='unitCode'>unitCode</a>.
        propertyID: (Optional[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]): A commonly used identifier for the characteristic represented by the property, e.g. a manufacturer or a standard code for a property. propertyID can be(1) a prefixed string, mainly meant to be used with standards for product properties; (2) a site-specific, non-prefixed string (e.g. the primary key of the property or the vendor-specific ID of the property), or (3)a URL indicating the type of the property, either pointing to an external vocabulary, or a Web resource that describes the property (e.g. a glossary entry).Standards bodies should promote a standard prefix for the identifiers of properties from their standards.
        minValue: (Optional[Union[List[Union[SchemaOrgObj, str, StrictInt, StrictFloat]], SchemaOrgObj, str, StrictInt, StrictFloat]]): The lower value of some characteristic or property.
    """

    value: NotRequired[Union[List[Union[SchemaOrgObj, str, StrictBool, StrictInt, StrictFloat]], SchemaOrgObj, str, StrictBool, StrictInt, StrictFloat]]
    valueReference: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    measurementTechnique: NotRequired[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]
    unitCode: NotRequired[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]
    maxValue: NotRequired[Union[List[Union[SchemaOrgObj, str, StrictInt, StrictFloat]], SchemaOrgObj, str, StrictInt, StrictFloat]]
    unitText: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    propertyID: NotRequired[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]
    minValue: NotRequired[Union[List[Union[SchemaOrgObj, str, StrictInt, StrictFloat]], SchemaOrgObj, str, StrictInt, StrictFloat]]
    


class LocationFeatureSpecificationProperties(TypedDict):
    """Specifies a location feature by providing a structured value representing a feature of an accommodation as a property-value pair of varying degrees of formality.

    References:
        https://schema.org/LocationFeatureSpecification
    Note:
        Model Depth 5
    Attributes:
        validThrough: (Optional[Union[List[Union[datetime, SchemaOrgObj, str, date]], datetime, SchemaOrgObj, str, date]]): The date after when the item is not valid. For example the end of an offer, salary period, or a period of opening hours.
        hoursAvailable: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The hours during which this service or contact is available.
        validFrom: (Optional[Union[List[Union[datetime, SchemaOrgObj, str, date]], datetime, SchemaOrgObj, str, date]]): The date when the item becomes valid.
    """

    validThrough: NotRequired[Union[List[Union[datetime, SchemaOrgObj, str, date]], datetime, SchemaOrgObj, str, date]]
    hoursAvailable: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    validFrom: NotRequired[Union[List[Union[datetime, SchemaOrgObj, str, date]], datetime, SchemaOrgObj, str, date]]
    


class AllProperties(LocationFeatureSpecificationInheritedProperties , LocationFeatureSpecificationProperties, TypedDict):
    pass


class LocationFeatureSpecificationBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="LocationFeatureSpecification",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'value': {'exclude': True}}
        fields = {'valueReference': {'exclude': True}}
        fields = {'measurementTechnique': {'exclude': True}}
        fields = {'unitCode': {'exclude': True}}
        fields = {'maxValue': {'exclude': True}}
        fields = {'unitText': {'exclude': True}}
        fields = {'propertyID': {'exclude': True}}
        fields = {'minValue': {'exclude': True}}
        fields = {'validThrough': {'exclude': True}}
        fields = {'hoursAvailable': {'exclude': True}}
        fields = {'validFrom': {'exclude': True}}
        


def create_schema_org_model(type_: Union[LocationFeatureSpecificationProperties, LocationFeatureSpecificationInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "LocationFeatureSpecification"
    return model
    

LocationFeatureSpecification = create_schema_org_model()


def create_locationfeaturespecification_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_locationfeaturespecification_model(model=model)
    return pydantic_type(model).schema_json()


