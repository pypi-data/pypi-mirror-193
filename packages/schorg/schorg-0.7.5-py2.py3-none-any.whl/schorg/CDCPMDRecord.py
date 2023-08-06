"""
A CDCPMDRecord is a data structure representing a record in a CDC tabular data format      used for hospital data reporting. See [documentation](/docs/cdc-covid.html) for details, and the linked CDC materials for authoritative      definitions used as the source here.      

https://schema.org/CDCPMDRecord
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class CDCPMDRecordInheritedProperties(TypedDict):
    """A CDCPMDRecord is a data structure representing a record in a CDC tabular data format      used for hospital data reporting. See [documentation](/docs/cdc-covid.html) for details, and the linked CDC materials for authoritative      definitions used as the source here.

    References:
        https://schema.org/CDCPMDRecord
    Note:
        Model Depth 4
    Attributes:
    """


class CDCPMDRecordProperties(TypedDict):
    """A CDCPMDRecord is a data structure representing a record in a CDC tabular data format      used for hospital data reporting. See [documentation](/docs/cdc-covid.html) for details, and the linked CDC materials for authoritative      definitions used as the source here.

    References:
        https://schema.org/CDCPMDRecord
    Note:
        Model Depth 4
    Attributes:
        cvdNumC19MechVentPats: (Optional[Union[List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]], str, SchemaOrgObj, StrictInt, StrictFloat]]): numc19mechventpats - HOSPITALIZED and VENTILATED: Patients hospitalized in an NHSN inpatient care location who have suspected or confirmed COVID-19 and are on a mechanical ventilator.
        cvdNumBedsOcc: (Optional[Union[List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]], str, SchemaOrgObj, StrictInt, StrictFloat]]): numbedsocc - HOSPITAL INPATIENT BED OCCUPANCY: Total number of staffed inpatient beds that are occupied.
        cvdNumBeds: (Optional[Union[List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]], str, SchemaOrgObj, StrictInt, StrictFloat]]): numbeds - HOSPITAL INPATIENT BEDS: Inpatient beds, including all staffed, licensed, and overflow (surge) beds used for inpatients.
        cvdNumVentUse: (Optional[Union[List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]], str, SchemaOrgObj, StrictInt, StrictFloat]]): numventuse - MECHANICAL VENTILATORS IN USE: Total number of ventilators in use.
        cvdFacilityId: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Identifier of the NHSN facility that this data record applies to. Use [[cvdFacilityCounty]] to indicate the county. To provide other details, [[healthcareReportingData]] can be used on a [[Hospital]] entry.
        cvdNumC19HospPats: (Optional[Union[List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]], str, SchemaOrgObj, StrictInt, StrictFloat]]): numc19hosppats - HOSPITALIZED: Patients currently hospitalized in an inpatient care location who have suspected or confirmed COVID-19.
        cvdCollectionDate: (Optional[Union[List[Union[str, SchemaOrgObj, datetime]], str, SchemaOrgObj, datetime]]): collectiondate - Date for which patient counts are reported.
        cvdNumTotBeds: (Optional[Union[List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]], str, SchemaOrgObj, StrictInt, StrictFloat]]): numtotbeds - ALL HOSPITAL BEDS: Total number of all inpatient and outpatient beds, including all staffed, ICU, licensed, and overflow (surge) beds used for inpatients or outpatients.
        cvdFacilityCounty: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Name of the County of the NHSN facility that this data record applies to. Use [[cvdFacilityId]] to identify the facility. To provide other details, [[healthcareReportingData]] can be used on a [[Hospital]] entry.
        cvdNumC19Died: (Optional[Union[List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]], str, SchemaOrgObj, StrictInt, StrictFloat]]): numc19died - DEATHS: Patients with suspected or confirmed COVID-19 who died in the hospital, ED, or any overflow location.
        cvdNumVent: (Optional[Union[List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]], str, SchemaOrgObj, StrictInt, StrictFloat]]): numvent - MECHANICAL VENTILATORS: Total number of ventilators available.
        datePosted: (Optional[Union[List[Union[datetime, str, SchemaOrgObj, date]], datetime, str, SchemaOrgObj, date]]): Publication date of an online listing.
        cvdNumICUBeds: (Optional[Union[List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]], str, SchemaOrgObj, StrictInt, StrictFloat]]): numicubeds - ICU BEDS: Total number of staffed inpatient intensive care unit (ICU) beds.
        cvdNumC19OverflowPats: (Optional[Union[List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]], str, SchemaOrgObj, StrictInt, StrictFloat]]): numc19overflowpats - ED/OVERFLOW: Patients with suspected or confirmed COVID-19 who are in the ED or any overflow location awaiting an inpatient bed.
        cvdNumC19HOPats: (Optional[Union[List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]], str, SchemaOrgObj, StrictInt, StrictFloat]]): numc19hopats - HOSPITAL ONSET: Patients hospitalized in an NHSN inpatient care location with onset of suspected or confirmed COVID-19 14 or more days after hospitalization.
        cvdNumC19OFMechVentPats: (Optional[Union[List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]], str, SchemaOrgObj, StrictInt, StrictFloat]]): numc19ofmechventpats - ED/OVERFLOW and VENTILATED: Patients with suspected or confirmed COVID-19 who are in the ED or any overflow location awaiting an inpatient bed and on a mechanical ventilator.
        cvdNumICUBedsOcc: (Optional[Union[List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]], str, SchemaOrgObj, StrictInt, StrictFloat]]): numicubedsocc - ICU BED OCCUPANCY: Total number of staffed inpatient ICU beds that are occupied.
    """

    cvdNumC19MechVentPats: NotRequired[
        Union[
            List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]],
            str,
            SchemaOrgObj,
            StrictInt,
            StrictFloat,
        ]
    ]
    cvdNumBedsOcc: NotRequired[
        Union[
            List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]],
            str,
            SchemaOrgObj,
            StrictInt,
            StrictFloat,
        ]
    ]
    cvdNumBeds: NotRequired[
        Union[
            List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]],
            str,
            SchemaOrgObj,
            StrictInt,
            StrictFloat,
        ]
    ]
    cvdNumVentUse: NotRequired[
        Union[
            List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]],
            str,
            SchemaOrgObj,
            StrictInt,
            StrictFloat,
        ]
    ]
    cvdFacilityId: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    cvdNumC19HospPats: NotRequired[
        Union[
            List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]],
            str,
            SchemaOrgObj,
            StrictInt,
            StrictFloat,
        ]
    ]
    cvdCollectionDate: NotRequired[
        Union[List[Union[str, SchemaOrgObj, datetime]], str, SchemaOrgObj, datetime]
    ]
    cvdNumTotBeds: NotRequired[
        Union[
            List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]],
            str,
            SchemaOrgObj,
            StrictInt,
            StrictFloat,
        ]
    ]
    cvdFacilityCounty: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    cvdNumC19Died: NotRequired[
        Union[
            List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]],
            str,
            SchemaOrgObj,
            StrictInt,
            StrictFloat,
        ]
    ]
    cvdNumVent: NotRequired[
        Union[
            List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]],
            str,
            SchemaOrgObj,
            StrictInt,
            StrictFloat,
        ]
    ]
    datePosted: NotRequired[
        Union[
            List[Union[datetime, str, SchemaOrgObj, date]],
            datetime,
            str,
            SchemaOrgObj,
            date,
        ]
    ]
    cvdNumICUBeds: NotRequired[
        Union[
            List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]],
            str,
            SchemaOrgObj,
            StrictInt,
            StrictFloat,
        ]
    ]
    cvdNumC19OverflowPats: NotRequired[
        Union[
            List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]],
            str,
            SchemaOrgObj,
            StrictInt,
            StrictFloat,
        ]
    ]
    cvdNumC19HOPats: NotRequired[
        Union[
            List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]],
            str,
            SchemaOrgObj,
            StrictInt,
            StrictFloat,
        ]
    ]
    cvdNumC19OFMechVentPats: NotRequired[
        Union[
            List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]],
            str,
            SchemaOrgObj,
            StrictInt,
            StrictFloat,
        ]
    ]
    cvdNumICUBedsOcc: NotRequired[
        Union[
            List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]],
            str,
            SchemaOrgObj,
            StrictInt,
            StrictFloat,
        ]
    ]


class CDCPMDRecordAllProperties(
    CDCPMDRecordInheritedProperties, CDCPMDRecordProperties, TypedDict
):
    pass


class CDCPMDRecordBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="CDCPMDRecord", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"cvdNumC19MechVentPats": {"exclude": True}}
        fields = {"cvdNumBedsOcc": {"exclude": True}}
        fields = {"cvdNumBeds": {"exclude": True}}
        fields = {"cvdNumVentUse": {"exclude": True}}
        fields = {"cvdFacilityId": {"exclude": True}}
        fields = {"cvdNumC19HospPats": {"exclude": True}}
        fields = {"cvdCollectionDate": {"exclude": True}}
        fields = {"cvdNumTotBeds": {"exclude": True}}
        fields = {"cvdFacilityCounty": {"exclude": True}}
        fields = {"cvdNumC19Died": {"exclude": True}}
        fields = {"cvdNumVent": {"exclude": True}}
        fields = {"datePosted": {"exclude": True}}
        fields = {"cvdNumICUBeds": {"exclude": True}}
        fields = {"cvdNumC19OverflowPats": {"exclude": True}}
        fields = {"cvdNumC19HOPats": {"exclude": True}}
        fields = {"cvdNumC19OFMechVentPats": {"exclude": True}}
        fields = {"cvdNumICUBedsOcc": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        CDCPMDRecordProperties,
        CDCPMDRecordInheritedProperties,
        CDCPMDRecordAllProperties,
    ] = CDCPMDRecordAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "CDCPMDRecord"
    return model


CDCPMDRecord = create_schema_org_model()


def create_cdcpmdrecord_model(
    model: Union[
        CDCPMDRecordProperties,
        CDCPMDRecordInheritedProperties,
        CDCPMDRecordAllProperties,
    ]
):
    _type = deepcopy(CDCPMDRecordAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of CDCPMDRecord. Please see: https://schema.org/CDCPMDRecord"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: CDCPMDRecordAllProperties):
    pydantic_type = create_cdcpmdrecord_model(model=model)
    return pydantic_type(model).schema_json()
