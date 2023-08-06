"""
A bus (also omnibus or autobus) is a road vehicle designed to carry passengers. Coaches are luxury busses, usually in service for long distance travel.

https://schema.org/BusOrCoach
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class BusOrCoachInheritedProperties(TypedDict):
    """A bus (also omnibus or autobus) is a road vehicle designed to carry passengers. Coaches are luxury busses, usually in service for long distance travel.

    References:
        https://schema.org/BusOrCoach
    Note:
        Model Depth 4
    Attributes:
        vehicleSpecialUsage: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Indicates whether the vehicle has been used for special purposes, like commercial rental, driving school, or as a taxi. The legislation in many countries requires this information to be revealed when offering a car for sale.
        trailerWeight: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The permitted weight of a trailer attached to the vehicle.Typical unit code(s): KGM for kilogram, LBR for pound* Note 1: You can indicate additional information in the [[name]] of the [[QuantitativeValue]] node.* Note 2: You may also link to a [[QualitativeValue]] node that provides additional information using [[valueReference]].* Note 3: Note that you can use [[minValue]] and [[maxValue]] to indicate ranges.
        cargoVolume: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The available volume for cargo or luggage. For automobiles, this is usually the trunk volume.Typical unit code(s): LTR for liters, FTQ for cubic foot/feetNote: You can use [[minValue]] and [[maxValue]] to indicate ranges.
        steeringPosition: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The position of the steering wheel or similar device (mostly for cars).
        fuelConsumption: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The amount of fuel consumed for traveling a particular distance or temporal duration with the given vehicle (e.g. liters per 100 km).* Note 1: There are unfortunately no standard unit codes for liters per 100 km.  Use [[unitText]] to indicate the unit of measurement, e.g. L/100 km.* Note 2: There are two ways of indicating the fuel consumption, [[fuelConsumption]] (e.g. 8 liters per 100 km) and [[fuelEfficiency]] (e.g. 30 miles per gallon). They are reciprocal.* Note 3: Often, the absolute value is useful only when related to driving speed ("at 80 km/h") or usage pattern ("city traffic"). You can use [[valueReference]] to link the value for the fuel consumption to another value.
        modelDate: (Optional[Union[List[Union[SchemaOrgObj, str, date]], SchemaOrgObj, str, date]]): The release date of a vehicle model (often used to differentiate versions of the same make and model).
        vehicleTransmission: (Optional[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]): The type of component used for transmitting the power from a rotating power source to the wheels or other relevant component(s) ("gearbox" for cars).
        emissionsCO2: (Optional[Union[List[Union[SchemaOrgObj, str, StrictInt, StrictFloat]], SchemaOrgObj, str, StrictInt, StrictFloat]]): The CO2 emissions in g/km. When used in combination with a QuantitativeValue, put "g/km" into the unitText property of that value, since there is no UN/CEFACT Common Code for "g/km".
        meetsEmissionStandard: (Optional[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]): Indicates that the vehicle meets the respective emission standard.
        payload: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The permitted weight of passengers and cargo, EXCLUDING the weight of the empty vehicle.Typical unit code(s): KGM for kilogram, LBR for pound* Note 1: Many databases specify the permitted TOTAL weight instead, which is the sum of [[weight]] and [[payload]]* Note 2: You can indicate additional information in the [[name]] of the [[QuantitativeValue]] node.* Note 3: You may also link to a [[QualitativeValue]] node that provides additional information using [[valueReference]].* Note 4: Note that you can use [[minValue]] and [[maxValue]] to indicate ranges.
        fuelCapacity: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The capacity of the fuel tank or in the case of electric cars, the battery. If there are multiple components for storage, this should indicate the total of all storage of the same type.Typical unit code(s): LTR for liters, GLL of US gallons, GLI for UK / imperial gallons, AMH for ampere-hours (for electrical vehicles).
        wheelbase: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The distance between the centers of the front and rear wheels.Typical unit code(s): CMT for centimeters, MTR for meters, INH for inches, FOT for foot/feet
        vehicleIdentificationNumber: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The Vehicle Identification Number (VIN) is a unique serial number used by the automotive industry to identify individual motor vehicles.
        vehicleInteriorType: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The type or material of the interior of the vehicle (e.g. synthetic fabric, leather, wood, etc.). While most interior types are characterized by the material used, an interior type can also be based on vehicle usage or target audience.
        vehicleEngine: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Information about the engine or engines of the vehicle.
        numberOfDoors: (Optional[Union[List[Union[SchemaOrgObj, str, StrictInt, StrictFloat]], SchemaOrgObj, str, StrictInt, StrictFloat]]): The number of doors.Typical unit code(s): C62
        vehicleInteriorColor: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The color or color combination of the interior of the vehicle.
        driveWheelConfiguration: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The drive wheel configuration, i.e. which roadwheels will receive torque from the vehicle's engine via the drivetrain.
        numberOfAxles: (Optional[Union[List[Union[SchemaOrgObj, str, StrictInt, StrictFloat]], SchemaOrgObj, str, StrictInt, StrictFloat]]): The number of axles.Typical unit code(s): C62
        vehicleSeatingCapacity: (Optional[Union[List[Union[SchemaOrgObj, str, StrictInt, StrictFloat]], SchemaOrgObj, str, StrictInt, StrictFloat]]): The number of passengers that can be seated in the vehicle, both in terms of the physical space available, and in terms of limitations set by law.Typical unit code(s): C62 for persons.
        numberOfPreviousOwners: (Optional[Union[List[Union[SchemaOrgObj, str, StrictInt, StrictFloat]], SchemaOrgObj, str, StrictInt, StrictFloat]]): The number of owners of the vehicle, including the current one.Typical unit code(s): C62
        purchaseDate: (Optional[Union[List[Union[SchemaOrgObj, str, date]], SchemaOrgObj, str, date]]): The date the item, e.g. vehicle, was purchased by the current owner.
        bodyType: (Optional[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]): Indicates the design and body style of the vehicle (e.g. station wagon, hatchback, etc.).
        fuelType: (Optional[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]): The type of fuel suitable for the engine or engines of the vehicle. If the vehicle has only one engine, this property can be attached directly to the vehicle.
        speed: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The speed range of the vehicle. If the vehicle is powered by an engine, the upper limit of the speed range (indicated by [[maxValue]]) should be the maximum speed achievable under regular conditions.Typical unit code(s): KMH for km/h, HM for mile per hour (0.447 04 m/s), KNT for knot*Note 1: Use [[minValue]] and [[maxValue]] to indicate the range. Typically, the minimal value is zero.* Note 2: There are many different ways of measuring the speed range. You can link to information about how the given value has been determined using the [[valueReference]] property.
        mileageFromOdometer: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The total distance travelled by the particular vehicle since its initial production, as read from its odometer.Typical unit code(s): KMT for kilometers, SMI for statute miles
        productionDate: (Optional[Union[List[Union[SchemaOrgObj, str, date]], SchemaOrgObj, str, date]]): The date of production of the item, e.g. vehicle.
        knownVehicleDamages: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A textual description of known damages, both repaired and unrepaired.
        dateVehicleFirstRegistered: (Optional[Union[List[Union[SchemaOrgObj, str, date]], SchemaOrgObj, str, date]]): The date of the first registration of the vehicle with the respective public authorities.
        weightTotal: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The permitted total weight of the loaded vehicle, including passengers and cargo and the weight of the empty vehicle.Typical unit code(s): KGM for kilogram, LBR for pound* Note 1: You can indicate additional information in the [[name]] of the [[QuantitativeValue]] node.* Note 2: You may also link to a [[QualitativeValue]] node that provides additional information using [[valueReference]].* Note 3: Note that you can use [[minValue]] and [[maxValue]] to indicate ranges.
        numberOfAirbags: (Optional[Union[List[Union[SchemaOrgObj, str, StrictInt, StrictFloat]], SchemaOrgObj, str, StrictInt, StrictFloat]]): The number or type of airbags in the vehicle.
        fuelEfficiency: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The distance traveled per unit of fuel used; most commonly miles per gallon (mpg) or kilometers per liter (km/L).* Note 1: There are unfortunately no standard unit codes for miles per gallon or kilometers per liter. Use [[unitText]] to indicate the unit of measurement, e.g. mpg or km/L.* Note 2: There are two ways of indicating the fuel consumption, [[fuelConsumption]] (e.g. 8 liters per 100 km) and [[fuelEfficiency]] (e.g. 30 miles per gallon). They are reciprocal.* Note 3: Often, the absolute value is useful only when related to driving speed ("at 80 km/h") or usage pattern ("city traffic"). You can use [[valueReference]] to link the value for the fuel economy to another value.
        vehicleModelDate: (Optional[Union[List[Union[SchemaOrgObj, str, date]], SchemaOrgObj, str, date]]): The release date of a vehicle model (often used to differentiate versions of the same make and model).
        numberOfForwardGears: (Optional[Union[List[Union[SchemaOrgObj, str, StrictInt, StrictFloat]], SchemaOrgObj, str, StrictInt, StrictFloat]]): The total number of forward gears available for the transmission system of the vehicle.Typical unit code(s): C62
        callSign: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A [callsign](https://en.wikipedia.org/wiki/Call_sign), as used in broadcasting and radio communications to identify people, radio and TV stations, or vehicles.
        vehicleConfiguration: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A short text indicating the configuration of the vehicle, e.g. '5dr hatchback ST 2.5 MT 225 hp' or 'limited edition'.
        tongueWeight: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The permitted vertical load (TWR) of a trailer attached to the vehicle. Also referred to as Tongue Load Rating (TLR) or Vertical Load Rating (VLR).Typical unit code(s): KGM for kilogram, LBR for pound* Note 1: You can indicate additional information in the [[name]] of the [[QuantitativeValue]] node.* Note 2: You may also link to a [[QualitativeValue]] node that provides additional information using [[valueReference]].* Note 3: Note that you can use [[minValue]] and [[maxValue]] to indicate ranges.
        accelerationTime: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The time needed to accelerate the vehicle from a given start velocity to a given target velocity.Typical unit code(s): SEC for seconds* Note: There are unfortunately no standard unit codes for seconds/0..100 km/h or seconds/0..60 mph. Simply use "SEC" for seconds and indicate the velocities in the [[name]] of the [[QuantitativeValue]], or use [[valueReference]] with a [[QuantitativeValue]] of 0..60 mph or 0..100 km/h to specify the reference speeds.
        seatingCapacity: (Optional[Union[List[Union[SchemaOrgObj, str, StrictInt, StrictFloat]], SchemaOrgObj, str, StrictInt, StrictFloat]]): The number of persons that can be seated (e.g. in a vehicle), both in terms of the physical space available, and in terms of limitations set by law.Typical unit code(s): C62 for persons 
    """

    vehicleSpecialUsage: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    trailerWeight: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    cargoVolume: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    steeringPosition: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    fuelConsumption: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    modelDate: NotRequired[Union[List[Union[SchemaOrgObj, str, date]], SchemaOrgObj, str, date]]
    vehicleTransmission: NotRequired[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]
    emissionsCO2: NotRequired[Union[List[Union[SchemaOrgObj, str, StrictInt, StrictFloat]], SchemaOrgObj, str, StrictInt, StrictFloat]]
    meetsEmissionStandard: NotRequired[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]
    payload: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    fuelCapacity: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    wheelbase: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    vehicleIdentificationNumber: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    vehicleInteriorType: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    vehicleEngine: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    numberOfDoors: NotRequired[Union[List[Union[SchemaOrgObj, str, StrictInt, StrictFloat]], SchemaOrgObj, str, StrictInt, StrictFloat]]
    vehicleInteriorColor: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    driveWheelConfiguration: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    numberOfAxles: NotRequired[Union[List[Union[SchemaOrgObj, str, StrictInt, StrictFloat]], SchemaOrgObj, str, StrictInt, StrictFloat]]
    vehicleSeatingCapacity: NotRequired[Union[List[Union[SchemaOrgObj, str, StrictInt, StrictFloat]], SchemaOrgObj, str, StrictInt, StrictFloat]]
    numberOfPreviousOwners: NotRequired[Union[List[Union[SchemaOrgObj, str, StrictInt, StrictFloat]], SchemaOrgObj, str, StrictInt, StrictFloat]]
    purchaseDate: NotRequired[Union[List[Union[SchemaOrgObj, str, date]], SchemaOrgObj, str, date]]
    bodyType: NotRequired[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]
    fuelType: NotRequired[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]
    speed: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    mileageFromOdometer: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    productionDate: NotRequired[Union[List[Union[SchemaOrgObj, str, date]], SchemaOrgObj, str, date]]
    knownVehicleDamages: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    dateVehicleFirstRegistered: NotRequired[Union[List[Union[SchemaOrgObj, str, date]], SchemaOrgObj, str, date]]
    weightTotal: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    numberOfAirbags: NotRequired[Union[List[Union[SchemaOrgObj, str, StrictInt, StrictFloat]], SchemaOrgObj, str, StrictInt, StrictFloat]]
    fuelEfficiency: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    vehicleModelDate: NotRequired[Union[List[Union[SchemaOrgObj, str, date]], SchemaOrgObj, str, date]]
    numberOfForwardGears: NotRequired[Union[List[Union[SchemaOrgObj, str, StrictInt, StrictFloat]], SchemaOrgObj, str, StrictInt, StrictFloat]]
    callSign: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    vehicleConfiguration: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    tongueWeight: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    accelerationTime: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    seatingCapacity: NotRequired[Union[List[Union[SchemaOrgObj, str, StrictInt, StrictFloat]], SchemaOrgObj, str, StrictInt, StrictFloat]]
    


class BusOrCoachProperties(TypedDict):
    """A bus (also omnibus or autobus) is a road vehicle designed to carry passengers. Coaches are luxury busses, usually in service for long distance travel.

    References:
        https://schema.org/BusOrCoach
    Note:
        Model Depth 4
    Attributes:
        roofLoad: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The permitted total weight of cargo and installations (e.g. a roof rack) on top of the vehicle.Typical unit code(s): KGM for kilogram, LBR for pound* Note 1: You can indicate additional information in the [[name]] of the [[QuantitativeValue]] node.* Note 2: You may also link to a [[QualitativeValue]] node that provides additional information using [[valueReference]]* Note 3: Note that you can use [[minValue]] and [[maxValue]] to indicate ranges.
        acrissCode: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The ACRISS Car Classification Code is a code used by many car rental companies, for classifying vehicles. ACRISS stands for Association of Car Rental Industry Systems and Standards.
    """

    roofLoad: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    acrissCode: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    


class AllProperties(BusOrCoachInheritedProperties , BusOrCoachProperties, TypedDict):
    pass


class BusOrCoachBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="BusOrCoach",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'vehicleSpecialUsage': {'exclude': True}}
        fields = {'trailerWeight': {'exclude': True}}
        fields = {'cargoVolume': {'exclude': True}}
        fields = {'steeringPosition': {'exclude': True}}
        fields = {'fuelConsumption': {'exclude': True}}
        fields = {'modelDate': {'exclude': True}}
        fields = {'vehicleTransmission': {'exclude': True}}
        fields = {'emissionsCO2': {'exclude': True}}
        fields = {'meetsEmissionStandard': {'exclude': True}}
        fields = {'payload': {'exclude': True}}
        fields = {'fuelCapacity': {'exclude': True}}
        fields = {'wheelbase': {'exclude': True}}
        fields = {'vehicleIdentificationNumber': {'exclude': True}}
        fields = {'vehicleInteriorType': {'exclude': True}}
        fields = {'vehicleEngine': {'exclude': True}}
        fields = {'numberOfDoors': {'exclude': True}}
        fields = {'vehicleInteriorColor': {'exclude': True}}
        fields = {'driveWheelConfiguration': {'exclude': True}}
        fields = {'numberOfAxles': {'exclude': True}}
        fields = {'vehicleSeatingCapacity': {'exclude': True}}
        fields = {'numberOfPreviousOwners': {'exclude': True}}
        fields = {'purchaseDate': {'exclude': True}}
        fields = {'bodyType': {'exclude': True}}
        fields = {'fuelType': {'exclude': True}}
        fields = {'speed': {'exclude': True}}
        fields = {'mileageFromOdometer': {'exclude': True}}
        fields = {'productionDate': {'exclude': True}}
        fields = {'knownVehicleDamages': {'exclude': True}}
        fields = {'dateVehicleFirstRegistered': {'exclude': True}}
        fields = {'weightTotal': {'exclude': True}}
        fields = {'numberOfAirbags': {'exclude': True}}
        fields = {'fuelEfficiency': {'exclude': True}}
        fields = {'vehicleModelDate': {'exclude': True}}
        fields = {'numberOfForwardGears': {'exclude': True}}
        fields = {'callSign': {'exclude': True}}
        fields = {'vehicleConfiguration': {'exclude': True}}
        fields = {'tongueWeight': {'exclude': True}}
        fields = {'accelerationTime': {'exclude': True}}
        fields = {'seatingCapacity': {'exclude': True}}
        fields = {'roofLoad': {'exclude': True}}
        fields = {'acrissCode': {'exclude': True}}
        


def create_schema_org_model(type_: Union[BusOrCoachProperties, BusOrCoachInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "BusOrCoach"
    return model
    

BusOrCoach = create_schema_org_model()


def create_busorcoach_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_busorcoach_model(model=model)
    return pydantic_type(model).schema_json()


