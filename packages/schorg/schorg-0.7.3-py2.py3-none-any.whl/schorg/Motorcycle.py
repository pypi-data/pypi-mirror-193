"""
A motorcycle or motorbike is a single-track, two-wheeled motor vehicle.

https://schema.org/Motorcycle
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MotorcycleInheritedProperties(TypedDict):
    """A motorcycle or motorbike is a single-track, two-wheeled motor vehicle.

    References:
        https://schema.org/Motorcycle
    Note:
        Model Depth 4
    Attributes:
        vehicleSpecialUsage: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Indicates whether the vehicle has been used for special purposes, like commercial rental, driving school, or as a taxi. The legislation in many countries requires this information to be revealed when offering a car for sale.
        trailerWeight: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The permitted weight of a trailer attached to the vehicle.Typical unit code(s): KGM for kilogram, LBR for pound* Note 1: You can indicate additional information in the [[name]] of the [[QuantitativeValue]] node.* Note 2: You may also link to a [[QualitativeValue]] node that provides additional information using [[valueReference]].* Note 3: Note that you can use [[minValue]] and [[maxValue]] to indicate ranges.
        cargoVolume: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The available volume for cargo or luggage. For automobiles, this is usually the trunk volume.Typical unit code(s): LTR for liters, FTQ for cubic foot/feetNote: You can use [[minValue]] and [[maxValue]] to indicate ranges.
        steeringPosition: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The position of the steering wheel or similar device (mostly for cars).
        fuelConsumption: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The amount of fuel consumed for traveling a particular distance or temporal duration with the given vehicle (e.g. liters per 100 km).* Note 1: There are unfortunately no standard unit codes for liters per 100 km.  Use [[unitText]] to indicate the unit of measurement, e.g. L/100 km.* Note 2: There are two ways of indicating the fuel consumption, [[fuelConsumption]] (e.g. 8 liters per 100 km) and [[fuelEfficiency]] (e.g. 30 miles per gallon). They are reciprocal.* Note 3: Often, the absolute value is useful only when related to driving speed ("at 80 km/h") or usage pattern ("city traffic"). You can use [[valueReference]] to link the value for the fuel consumption to another value.
        modelDate: (Optional[Union[List[Union[str, date, SchemaOrgObj]], str, date, SchemaOrgObj]]): The release date of a vehicle model (often used to differentiate versions of the same make and model).
        vehicleTransmission: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): The type of component used for transmitting the power from a rotating power source to the wheels or other relevant component(s) ("gearbox" for cars).
        emissionsCO2: (Optional[Union[List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]], str, StrictInt, StrictFloat, SchemaOrgObj]]): The CO2 emissions in g/km. When used in combination with a QuantitativeValue, put "g/km" into the unitText property of that value, since there is no UN/CEFACT Common Code for "g/km".
        meetsEmissionStandard: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): Indicates that the vehicle meets the respective emission standard.
        payload: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The permitted weight of passengers and cargo, EXCLUDING the weight of the empty vehicle.Typical unit code(s): KGM for kilogram, LBR for pound* Note 1: Many databases specify the permitted TOTAL weight instead, which is the sum of [[weight]] and [[payload]]* Note 2: You can indicate additional information in the [[name]] of the [[QuantitativeValue]] node.* Note 3: You may also link to a [[QualitativeValue]] node that provides additional information using [[valueReference]].* Note 4: Note that you can use [[minValue]] and [[maxValue]] to indicate ranges.
        fuelCapacity: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The capacity of the fuel tank or in the case of electric cars, the battery. If there are multiple components for storage, this should indicate the total of all storage of the same type.Typical unit code(s): LTR for liters, GLL of US gallons, GLI for UK / imperial gallons, AMH for ampere-hours (for electrical vehicles).
        wheelbase: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The distance between the centers of the front and rear wheels.Typical unit code(s): CMT for centimeters, MTR for meters, INH for inches, FOT for foot/feet
        vehicleIdentificationNumber: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The Vehicle Identification Number (VIN) is a unique serial number used by the automotive industry to identify individual motor vehicles.
        vehicleInteriorType: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The type or material of the interior of the vehicle (e.g. synthetic fabric, leather, wood, etc.). While most interior types are characterized by the material used, an interior type can also be based on vehicle usage or target audience.
        vehicleEngine: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Information about the engine or engines of the vehicle.
        numberOfDoors: (Optional[Union[List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]], str, StrictInt, StrictFloat, SchemaOrgObj]]): The number of doors.Typical unit code(s): C62
        vehicleInteriorColor: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The color or color combination of the interior of the vehicle.
        driveWheelConfiguration: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The drive wheel configuration, i.e. which roadwheels will receive torque from the vehicle's engine via the drivetrain.
        numberOfAxles: (Optional[Union[List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]], str, StrictInt, StrictFloat, SchemaOrgObj]]): The number of axles.Typical unit code(s): C62
        vehicleSeatingCapacity: (Optional[Union[List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]], str, StrictInt, StrictFloat, SchemaOrgObj]]): The number of passengers that can be seated in the vehicle, both in terms of the physical space available, and in terms of limitations set by law.Typical unit code(s): C62 for persons.
        numberOfPreviousOwners: (Optional[Union[List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]], str, StrictInt, StrictFloat, SchemaOrgObj]]): The number of owners of the vehicle, including the current one.Typical unit code(s): C62
        purchaseDate: (Optional[Union[List[Union[str, date, SchemaOrgObj]], str, date, SchemaOrgObj]]): The date the item, e.g. vehicle, was purchased by the current owner.
        bodyType: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): Indicates the design and body style of the vehicle (e.g. station wagon, hatchback, etc.).
        fuelType: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): The type of fuel suitable for the engine or engines of the vehicle. If the vehicle has only one engine, this property can be attached directly to the vehicle.
        speed: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The speed range of the vehicle. If the vehicle is powered by an engine, the upper limit of the speed range (indicated by [[maxValue]]) should be the maximum speed achievable under regular conditions.Typical unit code(s): KMH for km/h, HM for mile per hour (0.447 04 m/s), KNT for knot*Note 1: Use [[minValue]] and [[maxValue]] to indicate the range. Typically, the minimal value is zero.* Note 2: There are many different ways of measuring the speed range. You can link to information about how the given value has been determined using the [[valueReference]] property.
        mileageFromOdometer: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The total distance travelled by the particular vehicle since its initial production, as read from its odometer.Typical unit code(s): KMT for kilometers, SMI for statute miles
        productionDate: (Optional[Union[List[Union[str, date, SchemaOrgObj]], str, date, SchemaOrgObj]]): The date of production of the item, e.g. vehicle.
        knownVehicleDamages: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A textual description of known damages, both repaired and unrepaired.
        dateVehicleFirstRegistered: (Optional[Union[List[Union[str, date, SchemaOrgObj]], str, date, SchemaOrgObj]]): The date of the first registration of the vehicle with the respective public authorities.
        weightTotal: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The permitted total weight of the loaded vehicle, including passengers and cargo and the weight of the empty vehicle.Typical unit code(s): KGM for kilogram, LBR for pound* Note 1: You can indicate additional information in the [[name]] of the [[QuantitativeValue]] node.* Note 2: You may also link to a [[QualitativeValue]] node that provides additional information using [[valueReference]].* Note 3: Note that you can use [[minValue]] and [[maxValue]] to indicate ranges.
        numberOfAirbags: (Optional[Union[List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]], str, StrictInt, StrictFloat, SchemaOrgObj]]): The number or type of airbags in the vehicle.
        fuelEfficiency: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The distance traveled per unit of fuel used; most commonly miles per gallon (mpg) or kilometers per liter (km/L).* Note 1: There are unfortunately no standard unit codes for miles per gallon or kilometers per liter. Use [[unitText]] to indicate the unit of measurement, e.g. mpg or km/L.* Note 2: There are two ways of indicating the fuel consumption, [[fuelConsumption]] (e.g. 8 liters per 100 km) and [[fuelEfficiency]] (e.g. 30 miles per gallon). They are reciprocal.* Note 3: Often, the absolute value is useful only when related to driving speed ("at 80 km/h") or usage pattern ("city traffic"). You can use [[valueReference]] to link the value for the fuel economy to another value.
        vehicleModelDate: (Optional[Union[List[Union[str, date, SchemaOrgObj]], str, date, SchemaOrgObj]]): The release date of a vehicle model (often used to differentiate versions of the same make and model).
        numberOfForwardGears: (Optional[Union[List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]], str, StrictInt, StrictFloat, SchemaOrgObj]]): The total number of forward gears available for the transmission system of the vehicle.Typical unit code(s): C62
        callSign: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A [callsign](https://en.wikipedia.org/wiki/Call_sign), as used in broadcasting and radio communications to identify people, radio and TV stations, or vehicles.
        vehicleConfiguration: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A short text indicating the configuration of the vehicle, e.g. '5dr hatchback ST 2.5 MT 225 hp' or 'limited edition'.
        tongueWeight: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The permitted vertical load (TWR) of a trailer attached to the vehicle. Also referred to as Tongue Load Rating (TLR) or Vertical Load Rating (VLR).Typical unit code(s): KGM for kilogram, LBR for pound* Note 1: You can indicate additional information in the [[name]] of the [[QuantitativeValue]] node.* Note 2: You may also link to a [[QualitativeValue]] node that provides additional information using [[valueReference]].* Note 3: Note that you can use [[minValue]] and [[maxValue]] to indicate ranges.
        accelerationTime: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The time needed to accelerate the vehicle from a given start velocity to a given target velocity.Typical unit code(s): SEC for seconds* Note: There are unfortunately no standard unit codes for seconds/0..100 km/h or seconds/0..60 mph. Simply use "SEC" for seconds and indicate the velocities in the [[name]] of the [[QuantitativeValue]], or use [[valueReference]] with a [[QuantitativeValue]] of 0..60 mph or 0..100 km/h to specify the reference speeds.
        seatingCapacity: (Optional[Union[List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]], str, StrictInt, StrictFloat, SchemaOrgObj]]): The number of persons that can be seated (e.g. in a vehicle), both in terms of the physical space available, and in terms of limitations set by law.Typical unit code(s): C62 for persons
    """

    vehicleSpecialUsage: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    trailerWeight: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    cargoVolume: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    steeringPosition: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    fuelConsumption: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    modelDate: NotRequired[
        Union[List[Union[str, date, SchemaOrgObj]], str, date, SchemaOrgObj]
    ]
    vehicleTransmission: NotRequired[
        Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]
    ]
    emissionsCO2: NotRequired[
        Union[
            List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]],
            str,
            StrictInt,
            StrictFloat,
            SchemaOrgObj,
        ]
    ]
    meetsEmissionStandard: NotRequired[
        Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]
    ]
    payload: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    fuelCapacity: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    wheelbase: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    vehicleIdentificationNumber: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    vehicleInteriorType: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    vehicleEngine: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    numberOfDoors: NotRequired[
        Union[
            List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]],
            str,
            StrictInt,
            StrictFloat,
            SchemaOrgObj,
        ]
    ]
    vehicleInteriorColor: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    driveWheelConfiguration: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    numberOfAxles: NotRequired[
        Union[
            List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]],
            str,
            StrictInt,
            StrictFloat,
            SchemaOrgObj,
        ]
    ]
    vehicleSeatingCapacity: NotRequired[
        Union[
            List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]],
            str,
            StrictInt,
            StrictFloat,
            SchemaOrgObj,
        ]
    ]
    numberOfPreviousOwners: NotRequired[
        Union[
            List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]],
            str,
            StrictInt,
            StrictFloat,
            SchemaOrgObj,
        ]
    ]
    purchaseDate: NotRequired[
        Union[List[Union[str, date, SchemaOrgObj]], str, date, SchemaOrgObj]
    ]
    bodyType: NotRequired[
        Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]
    ]
    fuelType: NotRequired[
        Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]
    ]
    speed: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    mileageFromOdometer: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    productionDate: NotRequired[
        Union[List[Union[str, date, SchemaOrgObj]], str, date, SchemaOrgObj]
    ]
    knownVehicleDamages: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    dateVehicleFirstRegistered: NotRequired[
        Union[List[Union[str, date, SchemaOrgObj]], str, date, SchemaOrgObj]
    ]
    weightTotal: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    numberOfAirbags: NotRequired[
        Union[
            List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]],
            str,
            StrictInt,
            StrictFloat,
            SchemaOrgObj,
        ]
    ]
    fuelEfficiency: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    vehicleModelDate: NotRequired[
        Union[List[Union[str, date, SchemaOrgObj]], str, date, SchemaOrgObj]
    ]
    numberOfForwardGears: NotRequired[
        Union[
            List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]],
            str,
            StrictInt,
            StrictFloat,
            SchemaOrgObj,
        ]
    ]
    callSign: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    vehicleConfiguration: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    tongueWeight: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    accelerationTime: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    seatingCapacity: NotRequired[
        Union[
            List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]],
            str,
            StrictInt,
            StrictFloat,
            SchemaOrgObj,
        ]
    ]


class MotorcycleProperties(TypedDict):
    """A motorcycle or motorbike is a single-track, two-wheeled motor vehicle.

    References:
        https://schema.org/Motorcycle
    Note:
        Model Depth 4
    Attributes:
    """


class MotorcycleAllProperties(
    MotorcycleInheritedProperties, MotorcycleProperties, TypedDict
):
    pass


class MotorcycleBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Motorcycle", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"vehicleSpecialUsage": {"exclude": True}}
        fields = {"trailerWeight": {"exclude": True}}
        fields = {"cargoVolume": {"exclude": True}}
        fields = {"steeringPosition": {"exclude": True}}
        fields = {"fuelConsumption": {"exclude": True}}
        fields = {"modelDate": {"exclude": True}}
        fields = {"vehicleTransmission": {"exclude": True}}
        fields = {"emissionsCO2": {"exclude": True}}
        fields = {"meetsEmissionStandard": {"exclude": True}}
        fields = {"payload": {"exclude": True}}
        fields = {"fuelCapacity": {"exclude": True}}
        fields = {"wheelbase": {"exclude": True}}
        fields = {"vehicleIdentificationNumber": {"exclude": True}}
        fields = {"vehicleInteriorType": {"exclude": True}}
        fields = {"vehicleEngine": {"exclude": True}}
        fields = {"numberOfDoors": {"exclude": True}}
        fields = {"vehicleInteriorColor": {"exclude": True}}
        fields = {"driveWheelConfiguration": {"exclude": True}}
        fields = {"numberOfAxles": {"exclude": True}}
        fields = {"vehicleSeatingCapacity": {"exclude": True}}
        fields = {"numberOfPreviousOwners": {"exclude": True}}
        fields = {"purchaseDate": {"exclude": True}}
        fields = {"bodyType": {"exclude": True}}
        fields = {"fuelType": {"exclude": True}}
        fields = {"speed": {"exclude": True}}
        fields = {"mileageFromOdometer": {"exclude": True}}
        fields = {"productionDate": {"exclude": True}}
        fields = {"knownVehicleDamages": {"exclude": True}}
        fields = {"dateVehicleFirstRegistered": {"exclude": True}}
        fields = {"weightTotal": {"exclude": True}}
        fields = {"numberOfAirbags": {"exclude": True}}
        fields = {"fuelEfficiency": {"exclude": True}}
        fields = {"vehicleModelDate": {"exclude": True}}
        fields = {"numberOfForwardGears": {"exclude": True}}
        fields = {"callSign": {"exclude": True}}
        fields = {"vehicleConfiguration": {"exclude": True}}
        fields = {"tongueWeight": {"exclude": True}}
        fields = {"accelerationTime": {"exclude": True}}
        fields = {"seatingCapacity": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        MotorcycleProperties, MotorcycleInheritedProperties, MotorcycleAllProperties
    ] = MotorcycleAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Motorcycle"
    return model


Motorcycle = create_schema_org_model()


def create_motorcycle_model(
    model: Union[
        MotorcycleProperties, MotorcycleInheritedProperties, MotorcycleAllProperties
    ]
):
    _type = deepcopy(MotorcycleAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: MotorcycleAllProperties):
    pydantic_type = create_motorcycle_model(model=model)
    return pydantic_type(model).schema_json()
