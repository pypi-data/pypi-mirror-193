"""
Information about the engine of the vehicle. A vehicle can have multiple engines represented by multiple engine specification entities.

https://schema.org/EngineSpecification
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class EngineSpecificationInheritedProperties(TypedDict):
    """Information about the engine of the vehicle. A vehicle can have multiple engines represented by multiple engine specification entities.

    References:
        https://schema.org/EngineSpecification
    Note:
        Model Depth 4
    Attributes:
    """

    


class EngineSpecificationProperties(TypedDict):
    """Information about the engine of the vehicle. A vehicle can have multiple engines represented by multiple engine specification entities.

    References:
        https://schema.org/EngineSpecification
    Note:
        Model Depth 4
    Attributes:
        enginePower: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The power of the vehicle's engine.    Typical unit code(s): KWT for kilowatt, BHP for brake horsepower, N12 for metric horsepower (PS, with 1 PS = 735,49875 W)* Note 1: There are many different ways of measuring an engine's power. For an overview, see  [http://en.wikipedia.org/wiki/Horsepower#Engine\_power\_test\_codes](http://en.wikipedia.org/wiki/Horsepower#Engine_power_test_codes).* Note 2: You can link to information about how the given value has been determined using the [[valueReference]] property.* Note 3: You can use [[minValue]] and [[maxValue]] to indicate ranges.
        torque: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The torque (turning force) of the vehicle's engine.Typical unit code(s): NU for newton metre (N m), F17 for pound-force per foot, or F48 for pound-force per inch* Note 1: You can link to information about how the given value has been determined (e.g. reference RPM) using the [[valueReference]] property.* Note 2: You can use [[minValue]] and [[maxValue]] to indicate ranges.
        engineType: (Optional[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]): The type of engine or engines powering the vehicle.
        fuelType: (Optional[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]): The type of fuel suitable for the engine or engines of the vehicle. If the vehicle has only one engine, this property can be attached directly to the vehicle.
        engineDisplacement: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The volume swept by all of the pistons inside the cylinders of an internal combustion engine in a single movement. Typical unit code(s): CMQ for cubic centimeter, LTR for liters, INQ for cubic inches* Note 1: You can link to information about how the given value has been determined using the [[valueReference]] property.* Note 2: You can use [[minValue]] and [[maxValue]] to indicate ranges.
    """

    enginePower: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    torque: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    engineType: NotRequired[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]
    fuelType: NotRequired[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]
    engineDisplacement: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    


class AllProperties(EngineSpecificationInheritedProperties , EngineSpecificationProperties, TypedDict):
    pass


class EngineSpecificationBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="EngineSpecification",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'enginePower': {'exclude': True}}
        fields = {'torque': {'exclude': True}}
        fields = {'engineType': {'exclude': True}}
        fields = {'fuelType': {'exclude': True}}
        fields = {'engineDisplacement': {'exclude': True}}
        


def create_schema_org_model(type_: Union[EngineSpecificationProperties, EngineSpecificationInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "EngineSpecification"
    return model
    

EngineSpecification = create_schema_org_model()


def create_enginespecification_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_enginespecification_model(model=model)
    return pydantic_type(model).schema_json()


