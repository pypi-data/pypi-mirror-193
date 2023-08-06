
def Thing_test():
    from schorg.Thing import ThingInheritedProperties
    from schorg.Thing import ThingProperties
    from schorg.Thing import AllProperties
    from schorg.Thing import create_schema_org_model
    from schorg.Thing import Thing

    a = create_schema_org_model(type_=ThingInheritedProperties)
    b = create_schema_org_model(type_=ThingProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Thing.schema()


def Intangible_test():
    from schorg.Intangible import IntangibleInheritedProperties
    from schorg.Intangible import IntangibleProperties
    from schorg.Intangible import AllProperties
    from schorg.Intangible import create_schema_org_model
    from schorg.Intangible import Intangible

    a = create_schema_org_model(type_=IntangibleInheritedProperties)
    b = create_schema_org_model(type_=IntangibleProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Intangible.schema()


def StructuredValue_test():
    from schorg.StructuredValue import StructuredValueInheritedProperties
    from schorg.StructuredValue import StructuredValueProperties
    from schorg.StructuredValue import AllProperties
    from schorg.StructuredValue import create_schema_org_model
    from schorg.StructuredValue import StructuredValue

    a = create_schema_org_model(type_=StructuredValueInheritedProperties)
    b = create_schema_org_model(type_=StructuredValueProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    StructuredValue.schema()


def GeoShape_test():
    from schorg.GeoShape import GeoShapeInheritedProperties
    from schorg.GeoShape import GeoShapeProperties
    from schorg.GeoShape import AllProperties
    from schorg.GeoShape import create_schema_org_model
    from schorg.GeoShape import GeoShape

    a = create_schema_org_model(type_=GeoShapeInheritedProperties)
    b = create_schema_org_model(type_=GeoShapeProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    GeoShape.schema()


def Enumeration_test():
    from schorg.Enumeration import EnumerationInheritedProperties
    from schorg.Enumeration import EnumerationProperties
    from schorg.Enumeration import AllProperties
    from schorg.Enumeration import create_schema_org_model
    from schorg.Enumeration import Enumeration

    a = create_schema_org_model(type_=EnumerationInheritedProperties)
    b = create_schema_org_model(type_=EnumerationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Enumeration.schema()


def SizeGroupEnumeration_test():
    from schorg.SizeGroupEnumeration import SizeGroupEnumerationInheritedProperties
    from schorg.SizeGroupEnumeration import SizeGroupEnumerationProperties
    from schorg.SizeGroupEnumeration import AllProperties
    from schorg.SizeGroupEnumeration import create_schema_org_model
    from schorg.SizeGroupEnumeration import SizeGroupEnumeration

    a = create_schema_org_model(type_=SizeGroupEnumerationInheritedProperties)
    b = create_schema_org_model(type_=SizeGroupEnumerationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    SizeGroupEnumeration.schema()


def WearableSizeGroupEnumeration_test():
    from schorg.WearableSizeGroupEnumeration import WearableSizeGroupEnumerationInheritedProperties
    from schorg.WearableSizeGroupEnumeration import WearableSizeGroupEnumerationProperties
    from schorg.WearableSizeGroupEnumeration import AllProperties
    from schorg.WearableSizeGroupEnumeration import create_schema_org_model
    from schorg.WearableSizeGroupEnumeration import WearableSizeGroupEnumeration

    a = create_schema_org_model(type_=WearableSizeGroupEnumerationInheritedProperties)
    b = create_schema_org_model(type_=WearableSizeGroupEnumerationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    WearableSizeGroupEnumeration.schema()


def WearableSizeGroupMens_test():
    from schorg.WearableSizeGroupMens import WearableSizeGroupMensInheritedProperties
    from schorg.WearableSizeGroupMens import WearableSizeGroupMensProperties
    from schorg.WearableSizeGroupMens import AllProperties
    from schorg.WearableSizeGroupMens import create_schema_org_model
    from schorg.WearableSizeGroupMens import WearableSizeGroupMens

    a = create_schema_org_model(type_=WearableSizeGroupMensInheritedProperties)
    b = create_schema_org_model(type_=WearableSizeGroupMensProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    WearableSizeGroupMens.schema()


def QualitativeValue_test():
    from schorg.QualitativeValue import QualitativeValueInheritedProperties
    from schorg.QualitativeValue import QualitativeValueProperties
    from schorg.QualitativeValue import AllProperties
    from schorg.QualitativeValue import create_schema_org_model
    from schorg.QualitativeValue import QualitativeValue

    a = create_schema_org_model(type_=QualitativeValueInheritedProperties)
    b = create_schema_org_model(type_=QualitativeValueProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    QualitativeValue.schema()


def DriveWheelConfigurationValue_test():
    from schorg.DriveWheelConfigurationValue import DriveWheelConfigurationValueInheritedProperties
    from schorg.DriveWheelConfigurationValue import DriveWheelConfigurationValueProperties
    from schorg.DriveWheelConfigurationValue import AllProperties
    from schorg.DriveWheelConfigurationValue import create_schema_org_model
    from schorg.DriveWheelConfigurationValue import DriveWheelConfigurationValue

    a = create_schema_org_model(type_=DriveWheelConfigurationValueInheritedProperties)
    b = create_schema_org_model(type_=DriveWheelConfigurationValueProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    DriveWheelConfigurationValue.schema()


def FrontWheelDriveConfiguration_test():
    from schorg.FrontWheelDriveConfiguration import FrontWheelDriveConfigurationInheritedProperties
    from schorg.FrontWheelDriveConfiguration import FrontWheelDriveConfigurationProperties
    from schorg.FrontWheelDriveConfiguration import AllProperties
    from schorg.FrontWheelDriveConfiguration import create_schema_org_model
    from schorg.FrontWheelDriveConfiguration import FrontWheelDriveConfiguration

    a = create_schema_org_model(type_=FrontWheelDriveConfigurationInheritedProperties)
    b = create_schema_org_model(type_=FrontWheelDriveConfigurationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    FrontWheelDriveConfiguration.schema()


def QuantitativeValueDistribution_test():
    from schorg.QuantitativeValueDistribution import QuantitativeValueDistributionInheritedProperties
    from schorg.QuantitativeValueDistribution import QuantitativeValueDistributionProperties
    from schorg.QuantitativeValueDistribution import AllProperties
    from schorg.QuantitativeValueDistribution import create_schema_org_model
    from schorg.QuantitativeValueDistribution import QuantitativeValueDistribution

    a = create_schema_org_model(type_=QuantitativeValueDistributionInheritedProperties)
    b = create_schema_org_model(type_=QuantitativeValueDistributionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    QuantitativeValueDistribution.schema()


def MonetaryAmountDistribution_test():
    from schorg.MonetaryAmountDistribution import MonetaryAmountDistributionInheritedProperties
    from schorg.MonetaryAmountDistribution import MonetaryAmountDistributionProperties
    from schorg.MonetaryAmountDistribution import AllProperties
    from schorg.MonetaryAmountDistribution import create_schema_org_model
    from schorg.MonetaryAmountDistribution import MonetaryAmountDistribution

    a = create_schema_org_model(type_=MonetaryAmountDistributionInheritedProperties)
    b = create_schema_org_model(type_=MonetaryAmountDistributionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MonetaryAmountDistribution.schema()


def Organization_test():
    from schorg.Organization import OrganizationInheritedProperties
    from schorg.Organization import OrganizationProperties
    from schorg.Organization import AllProperties
    from schorg.Organization import create_schema_org_model
    from schorg.Organization import Organization

    a = create_schema_org_model(type_=OrganizationInheritedProperties)
    b = create_schema_org_model(type_=OrganizationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Organization.schema()


def WorkersUnion_test():
    from schorg.WorkersUnion import WorkersUnionInheritedProperties
    from schorg.WorkersUnion import WorkersUnionProperties
    from schorg.WorkersUnion import AllProperties
    from schorg.WorkersUnion import create_schema_org_model
    from schorg.WorkersUnion import WorkersUnion

    a = create_schema_org_model(type_=WorkersUnionInheritedProperties)
    b = create_schema_org_model(type_=WorkersUnionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    WorkersUnion.schema()


def Place_test():
    from schorg.Place import PlaceInheritedProperties
    from schorg.Place import PlaceProperties
    from schorg.Place import AllProperties
    from schorg.Place import create_schema_org_model
    from schorg.Place import Place

    a = create_schema_org_model(type_=PlaceInheritedProperties)
    b = create_schema_org_model(type_=PlaceProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Place.schema()


def CivicStructure_test():
    from schorg.CivicStructure import CivicStructureInheritedProperties
    from schorg.CivicStructure import CivicStructureProperties
    from schorg.CivicStructure import AllProperties
    from schorg.CivicStructure import create_schema_org_model
    from schorg.CivicStructure import CivicStructure

    a = create_schema_org_model(type_=CivicStructureInheritedProperties)
    b = create_schema_org_model(type_=CivicStructureProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    CivicStructure.schema()


def Park_test():
    from schorg.Park import ParkInheritedProperties
    from schorg.Park import ParkProperties
    from schorg.Park import AllProperties
    from schorg.Park import create_schema_org_model
    from schorg.Park import Park

    a = create_schema_org_model(type_=ParkInheritedProperties)
    b = create_schema_org_model(type_=ParkProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Park.schema()


def LocalBusiness_test():
    from schorg.LocalBusiness import LocalBusinessInheritedProperties
    from schorg.LocalBusiness import LocalBusinessProperties
    from schorg.LocalBusiness import AllProperties
    from schorg.LocalBusiness import create_schema_org_model
    from schorg.LocalBusiness import LocalBusiness

    a = create_schema_org_model(type_=LocalBusinessInheritedProperties)
    b = create_schema_org_model(type_=LocalBusinessProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    LocalBusiness.schema()


def Store_test():
    from schorg.Store import StoreInheritedProperties
    from schorg.Store import StoreProperties
    from schorg.Store import AllProperties
    from schorg.Store import create_schema_org_model
    from schorg.Store import Store

    a = create_schema_org_model(type_=StoreInheritedProperties)
    b = create_schema_org_model(type_=StoreProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Store.schema()


def PetStore_test():
    from schorg.PetStore import PetStoreInheritedProperties
    from schorg.PetStore import PetStoreProperties
    from schorg.PetStore import AllProperties
    from schorg.PetStore import create_schema_org_model
    from schorg.PetStore import PetStore

    a = create_schema_org_model(type_=PetStoreInheritedProperties)
    b = create_schema_org_model(type_=PetStoreProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    PetStore.schema()


def MedicalEntity_test():
    from schorg.MedicalEntity import MedicalEntityInheritedProperties
    from schorg.MedicalEntity import MedicalEntityProperties
    from schorg.MedicalEntity import AllProperties
    from schorg.MedicalEntity import create_schema_org_model
    from schorg.MedicalEntity import MedicalEntity

    a = create_schema_org_model(type_=MedicalEntityInheritedProperties)
    b = create_schema_org_model(type_=MedicalEntityProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MedicalEntity.schema()


def MedicalIntangible_test():
    from schorg.MedicalIntangible import MedicalIntangibleInheritedProperties
    from schorg.MedicalIntangible import MedicalIntangibleProperties
    from schorg.MedicalIntangible import AllProperties
    from schorg.MedicalIntangible import create_schema_org_model
    from schorg.MedicalIntangible import MedicalIntangible

    a = create_schema_org_model(type_=MedicalIntangibleInheritedProperties)
    b = create_schema_org_model(type_=MedicalIntangibleProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MedicalIntangible.schema()


def DDxElement_test():
    from schorg.DDxElement import DDxElementInheritedProperties
    from schorg.DDxElement import DDxElementProperties
    from schorg.DDxElement import AllProperties
    from schorg.DDxElement import create_schema_org_model
    from schorg.DDxElement import DDxElement

    a = create_schema_org_model(type_=DDxElementInheritedProperties)
    b = create_schema_org_model(type_=DDxElementProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    DDxElement.schema()


def ReturnFeesEnumeration_test():
    from schorg.ReturnFeesEnumeration import ReturnFeesEnumerationInheritedProperties
    from schorg.ReturnFeesEnumeration import ReturnFeesEnumerationProperties
    from schorg.ReturnFeesEnumeration import AllProperties
    from schorg.ReturnFeesEnumeration import create_schema_org_model
    from schorg.ReturnFeesEnumeration import ReturnFeesEnumeration

    a = create_schema_org_model(type_=ReturnFeesEnumerationInheritedProperties)
    b = create_schema_org_model(type_=ReturnFeesEnumerationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ReturnFeesEnumeration.schema()


def ReturnShippingFees_test():
    from schorg.ReturnShippingFees import ReturnShippingFeesInheritedProperties
    from schorg.ReturnShippingFees import ReturnShippingFeesProperties
    from schorg.ReturnShippingFees import AllProperties
    from schorg.ReturnShippingFees import create_schema_org_model
    from schorg.ReturnShippingFees import ReturnShippingFees

    a = create_schema_org_model(type_=ReturnShippingFeesInheritedProperties)
    b = create_schema_org_model(type_=ReturnShippingFeesProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ReturnShippingFees.schema()


def Florist_test():
    from schorg.Florist import FloristInheritedProperties
    from schorg.Florist import FloristProperties
    from schorg.Florist import AllProperties
    from schorg.Florist import create_schema_org_model
    from schorg.Florist import Florist

    a = create_schema_org_model(type_=FloristInheritedProperties)
    b = create_schema_org_model(type_=FloristProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Florist.schema()


def AnatomicalStructure_test():
    from schorg.AnatomicalStructure import AnatomicalStructureInheritedProperties
    from schorg.AnatomicalStructure import AnatomicalStructureProperties
    from schorg.AnatomicalStructure import AllProperties
    from schorg.AnatomicalStructure import create_schema_org_model
    from schorg.AnatomicalStructure import AnatomicalStructure

    a = create_schema_org_model(type_=AnatomicalStructureInheritedProperties)
    b = create_schema_org_model(type_=AnatomicalStructureProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    AnatomicalStructure.schema()


def SizeSystemEnumeration_test():
    from schorg.SizeSystemEnumeration import SizeSystemEnumerationInheritedProperties
    from schorg.SizeSystemEnumeration import SizeSystemEnumerationProperties
    from schorg.SizeSystemEnumeration import AllProperties
    from schorg.SizeSystemEnumeration import create_schema_org_model
    from schorg.SizeSystemEnumeration import SizeSystemEnumeration

    a = create_schema_org_model(type_=SizeSystemEnumerationInheritedProperties)
    b = create_schema_org_model(type_=SizeSystemEnumerationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    SizeSystemEnumeration.schema()


def WearableSizeSystemEnumeration_test():
    from schorg.WearableSizeSystemEnumeration import WearableSizeSystemEnumerationInheritedProperties
    from schorg.WearableSizeSystemEnumeration import WearableSizeSystemEnumerationProperties
    from schorg.WearableSizeSystemEnumeration import AllProperties
    from schorg.WearableSizeSystemEnumeration import create_schema_org_model
    from schorg.WearableSizeSystemEnumeration import WearableSizeSystemEnumeration

    a = create_schema_org_model(type_=WearableSizeSystemEnumerationInheritedProperties)
    b = create_schema_org_model(type_=WearableSizeSystemEnumerationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    WearableSizeSystemEnumeration.schema()


def WearableSizeSystemBR_test():
    from schorg.WearableSizeSystemBR import WearableSizeSystemBRInheritedProperties
    from schorg.WearableSizeSystemBR import WearableSizeSystemBRProperties
    from schorg.WearableSizeSystemBR import AllProperties
    from schorg.WearableSizeSystemBR import create_schema_org_model
    from schorg.WearableSizeSystemBR import WearableSizeSystemBR

    a = create_schema_org_model(type_=WearableSizeSystemBRInheritedProperties)
    b = create_schema_org_model(type_=WearableSizeSystemBRProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    WearableSizeSystemBR.schema()


def NonprofitType_test():
    from schorg.NonprofitType import NonprofitTypeInheritedProperties
    from schorg.NonprofitType import NonprofitTypeProperties
    from schorg.NonprofitType import AllProperties
    from schorg.NonprofitType import create_schema_org_model
    from schorg.NonprofitType import NonprofitType

    a = create_schema_org_model(type_=NonprofitTypeInheritedProperties)
    b = create_schema_org_model(type_=NonprofitTypeProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    NonprofitType.schema()


def NLNonprofitType_test():
    from schorg.NLNonprofitType import NLNonprofitTypeInheritedProperties
    from schorg.NLNonprofitType import NLNonprofitTypeProperties
    from schorg.NLNonprofitType import AllProperties
    from schorg.NLNonprofitType import create_schema_org_model
    from schorg.NLNonprofitType import NLNonprofitType

    a = create_schema_org_model(type_=NLNonprofitTypeInheritedProperties)
    b = create_schema_org_model(type_=NLNonprofitTypeProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    NLNonprofitType.schema()


def NonprofitSBBI_test():
    from schorg.NonprofitSBBI import NonprofitSBBIInheritedProperties
    from schorg.NonprofitSBBI import NonprofitSBBIProperties
    from schorg.NonprofitSBBI import AllProperties
    from schorg.NonprofitSBBI import create_schema_org_model
    from schorg.NonprofitSBBI import NonprofitSBBI

    a = create_schema_org_model(type_=NonprofitSBBIInheritedProperties)
    b = create_schema_org_model(type_=NonprofitSBBIProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    NonprofitSBBI.schema()


def CreativeWork_test():
    from schorg.CreativeWork import CreativeWorkInheritedProperties
    from schorg.CreativeWork import CreativeWorkProperties
    from schorg.CreativeWork import AllProperties
    from schorg.CreativeWork import create_schema_org_model
    from schorg.CreativeWork import CreativeWork

    a = create_schema_org_model(type_=CreativeWorkInheritedProperties)
    b = create_schema_org_model(type_=CreativeWorkProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    CreativeWork.schema()


def DataCatalog_test():
    from schorg.DataCatalog import DataCatalogInheritedProperties
    from schorg.DataCatalog import DataCatalogProperties
    from schorg.DataCatalog import AllProperties
    from schorg.DataCatalog import create_schema_org_model
    from schorg.DataCatalog import DataCatalog

    a = create_schema_org_model(type_=DataCatalogInheritedProperties)
    b = create_schema_org_model(type_=DataCatalogProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    DataCatalog.schema()


def WebPageElement_test():
    from schorg.WebPageElement import WebPageElementInheritedProperties
    from schorg.WebPageElement import WebPageElementProperties
    from schorg.WebPageElement import AllProperties
    from schorg.WebPageElement import create_schema_org_model
    from schorg.WebPageElement import WebPageElement

    a = create_schema_org_model(type_=WebPageElementInheritedProperties)
    b = create_schema_org_model(type_=WebPageElementProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    WebPageElement.schema()


def Accommodation_test():
    from schorg.Accommodation import AccommodationInheritedProperties
    from schorg.Accommodation import AccommodationProperties
    from schorg.Accommodation import AllProperties
    from schorg.Accommodation import create_schema_org_model
    from schorg.Accommodation import Accommodation

    a = create_schema_org_model(type_=AccommodationInheritedProperties)
    b = create_schema_org_model(type_=AccommodationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Accommodation.schema()


def Apartment_test():
    from schorg.Apartment import ApartmentInheritedProperties
    from schorg.Apartment import ApartmentProperties
    from schorg.Apartment import AllProperties
    from schorg.Apartment import create_schema_org_model
    from schorg.Apartment import Apartment

    a = create_schema_org_model(type_=ApartmentInheritedProperties)
    b = create_schema_org_model(type_=ApartmentProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Apartment.schema()


def Event_test():
    from schorg.Event import EventInheritedProperties
    from schorg.Event import EventProperties
    from schorg.Event import AllProperties
    from schorg.Event import create_schema_org_model
    from schorg.Event import Event

    a = create_schema_org_model(type_=EventInheritedProperties)
    b = create_schema_org_model(type_=EventProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Event.schema()


def LiteraryEvent_test():
    from schorg.LiteraryEvent import LiteraryEventInheritedProperties
    from schorg.LiteraryEvent import LiteraryEventProperties
    from schorg.LiteraryEvent import AllProperties
    from schorg.LiteraryEvent import create_schema_org_model
    from schorg.LiteraryEvent import LiteraryEvent

    a = create_schema_org_model(type_=LiteraryEventInheritedProperties)
    b = create_schema_org_model(type_=LiteraryEventProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    LiteraryEvent.schema()


def Clip_test():
    from schorg.Clip import ClipInheritedProperties
    from schorg.Clip import ClipProperties
    from schorg.Clip import AllProperties
    from schorg.Clip import create_schema_org_model
    from schorg.Clip import Clip

    a = create_schema_org_model(type_=ClipInheritedProperties)
    b = create_schema_org_model(type_=ClipProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Clip.schema()


def MovieClip_test():
    from schorg.MovieClip import MovieClipInheritedProperties
    from schorg.MovieClip import MovieClipProperties
    from schorg.MovieClip import AllProperties
    from schorg.MovieClip import create_schema_org_model
    from schorg.MovieClip import MovieClip

    a = create_schema_org_model(type_=MovieClipInheritedProperties)
    b = create_schema_org_model(type_=MovieClipProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MovieClip.schema()


def EducationEvent_test():
    from schorg.EducationEvent import EducationEventInheritedProperties
    from schorg.EducationEvent import EducationEventProperties
    from schorg.EducationEvent import AllProperties
    from schorg.EducationEvent import create_schema_org_model
    from schorg.EducationEvent import EducationEvent

    a = create_schema_org_model(type_=EducationEventInheritedProperties)
    b = create_schema_org_model(type_=EducationEventProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    EducationEvent.schema()


def MedicalProcedure_test():
    from schorg.MedicalProcedure import MedicalProcedureInheritedProperties
    from schorg.MedicalProcedure import MedicalProcedureProperties
    from schorg.MedicalProcedure import AllProperties
    from schorg.MedicalProcedure import create_schema_org_model
    from schorg.MedicalProcedure import MedicalProcedure

    a = create_schema_org_model(type_=MedicalProcedureInheritedProperties)
    b = create_schema_org_model(type_=MedicalProcedureProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MedicalProcedure.schema()


def MedicalEnumeration_test():
    from schorg.MedicalEnumeration import MedicalEnumerationInheritedProperties
    from schorg.MedicalEnumeration import MedicalEnumerationProperties
    from schorg.MedicalEnumeration import AllProperties
    from schorg.MedicalEnumeration import create_schema_org_model
    from schorg.MedicalEnumeration import MedicalEnumeration

    a = create_schema_org_model(type_=MedicalEnumerationInheritedProperties)
    b = create_schema_org_model(type_=MedicalEnumerationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MedicalEnumeration.schema()


def PhysicalExam_test():
    from schorg.PhysicalExam import PhysicalExamInheritedProperties
    from schorg.PhysicalExam import PhysicalExamProperties
    from schorg.PhysicalExam import AllProperties
    from schorg.PhysicalExam import create_schema_org_model
    from schorg.PhysicalExam import PhysicalExam

    a = create_schema_org_model(type_=PhysicalExamInheritedProperties)
    b = create_schema_org_model(type_=PhysicalExamProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    PhysicalExam.schema()


def Abdomen_test():
    from schorg.Abdomen import AbdomenInheritedProperties
    from schorg.Abdomen import AbdomenProperties
    from schorg.Abdomen import AllProperties
    from schorg.Abdomen import create_schema_org_model
    from schorg.Abdomen import Abdomen

    a = create_schema_org_model(type_=AbdomenInheritedProperties)
    b = create_schema_org_model(type_=AbdomenProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Abdomen.schema()


def SocialEvent_test():
    from schorg.SocialEvent import SocialEventInheritedProperties
    from schorg.SocialEvent import SocialEventProperties
    from schorg.SocialEvent import AllProperties
    from schorg.SocialEvent import create_schema_org_model
    from schorg.SocialEvent import SocialEvent

    a = create_schema_org_model(type_=SocialEventInheritedProperties)
    b = create_schema_org_model(type_=SocialEventProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    SocialEvent.schema()


def MedicalTest_test():
    from schorg.MedicalTest import MedicalTestInheritedProperties
    from schorg.MedicalTest import MedicalTestProperties
    from schorg.MedicalTest import AllProperties
    from schorg.MedicalTest import create_schema_org_model
    from schorg.MedicalTest import MedicalTest

    a = create_schema_org_model(type_=MedicalTestInheritedProperties)
    b = create_schema_org_model(type_=MedicalTestProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MedicalTest.schema()


def ImagingTest_test():
    from schorg.ImagingTest import ImagingTestInheritedProperties
    from schorg.ImagingTest import ImagingTestProperties
    from schorg.ImagingTest import AllProperties
    from schorg.ImagingTest import create_schema_org_model
    from schorg.ImagingTest import ImagingTest

    a = create_schema_org_model(type_=ImagingTestInheritedProperties)
    b = create_schema_org_model(type_=ImagingTestProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ImagingTest.schema()


def InteractionCounter_test():
    from schorg.InteractionCounter import InteractionCounterInheritedProperties
    from schorg.InteractionCounter import InteractionCounterProperties
    from schorg.InteractionCounter import AllProperties
    from schorg.InteractionCounter import create_schema_org_model
    from schorg.InteractionCounter import InteractionCounter

    a = create_schema_org_model(type_=InteractionCounterInheritedProperties)
    b = create_schema_org_model(type_=InteractionCounterProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    InteractionCounter.schema()


def Audience_test():
    from schorg.Audience import AudienceInheritedProperties
    from schorg.Audience import AudienceProperties
    from schorg.Audience import AllProperties
    from schorg.Audience import create_schema_org_model
    from schorg.Audience import Audience

    a = create_schema_org_model(type_=AudienceInheritedProperties)
    b = create_schema_org_model(type_=AudienceProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Audience.schema()


def PeopleAudience_test():
    from schorg.PeopleAudience import PeopleAudienceInheritedProperties
    from schorg.PeopleAudience import PeopleAudienceProperties
    from schorg.PeopleAudience import AllProperties
    from schorg.PeopleAudience import create_schema_org_model
    from schorg.PeopleAudience import PeopleAudience

    a = create_schema_org_model(type_=PeopleAudienceInheritedProperties)
    b = create_schema_org_model(type_=PeopleAudienceProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    PeopleAudience.schema()


def ParentAudience_test():
    from schorg.ParentAudience import ParentAudienceInheritedProperties
    from schorg.ParentAudience import ParentAudienceProperties
    from schorg.ParentAudience import AllProperties
    from schorg.ParentAudience import create_schema_org_model
    from schorg.ParentAudience import ParentAudience

    a = create_schema_org_model(type_=ParentAudienceInheritedProperties)
    b = create_schema_org_model(type_=ParentAudienceProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ParentAudience.schema()


def Product_test():
    from schorg.Product import ProductInheritedProperties
    from schorg.Product import ProductProperties
    from schorg.Product import AllProperties
    from schorg.Product import create_schema_org_model
    from schorg.Product import Product

    a = create_schema_org_model(type_=ProductInheritedProperties)
    b = create_schema_org_model(type_=ProductProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Product.schema()


def ProductModel_test():
    from schorg.ProductModel import ProductModelInheritedProperties
    from schorg.ProductModel import ProductModelProperties
    from schorg.ProductModel import AllProperties
    from schorg.ProductModel import create_schema_org_model
    from schorg.ProductModel import ProductModel

    a = create_schema_org_model(type_=ProductModelInheritedProperties)
    b = create_schema_org_model(type_=ProductModelProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ProductModel.schema()


def MedicalTrialDesign_test():
    from schorg.MedicalTrialDesign import MedicalTrialDesignInheritedProperties
    from schorg.MedicalTrialDesign import MedicalTrialDesignProperties
    from schorg.MedicalTrialDesign import AllProperties
    from schorg.MedicalTrialDesign import create_schema_org_model
    from schorg.MedicalTrialDesign import MedicalTrialDesign

    a = create_schema_org_model(type_=MedicalTrialDesignInheritedProperties)
    b = create_schema_org_model(type_=MedicalTrialDesignProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MedicalTrialDesign.schema()


def PlaceboControlledTrial_test():
    from schorg.PlaceboControlledTrial import PlaceboControlledTrialInheritedProperties
    from schorg.PlaceboControlledTrial import PlaceboControlledTrialProperties
    from schorg.PlaceboControlledTrial import AllProperties
    from schorg.PlaceboControlledTrial import create_schema_org_model
    from schorg.PlaceboControlledTrial import PlaceboControlledTrial

    a = create_schema_org_model(type_=PlaceboControlledTrialInheritedProperties)
    b = create_schema_org_model(type_=PlaceboControlledTrialProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    PlaceboControlledTrial.schema()


def Action_test():
    from schorg.Action import ActionInheritedProperties
    from schorg.Action import ActionProperties
    from schorg.Action import AllProperties
    from schorg.Action import create_schema_org_model
    from schorg.Action import Action

    a = create_schema_org_model(type_=ActionInheritedProperties)
    b = create_schema_org_model(type_=ActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Action.schema()


def CreateAction_test():
    from schorg.CreateAction import CreateActionInheritedProperties
    from schorg.CreateAction import CreateActionProperties
    from schorg.CreateAction import AllProperties
    from schorg.CreateAction import create_schema_org_model
    from schorg.CreateAction import CreateAction

    a = create_schema_org_model(type_=CreateActionInheritedProperties)
    b = create_schema_org_model(type_=CreateActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    CreateAction.schema()


def PhotographAction_test():
    from schorg.PhotographAction import PhotographActionInheritedProperties
    from schorg.PhotographAction import PhotographActionProperties
    from schorg.PhotographAction import AllProperties
    from schorg.PhotographAction import create_schema_org_model
    from schorg.PhotographAction import PhotographAction

    a = create_schema_org_model(type_=PhotographActionInheritedProperties)
    b = create_schema_org_model(type_=PhotographActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    PhotographAction.schema()


def USNonprofitType_test():
    from schorg.USNonprofitType import USNonprofitTypeInheritedProperties
    from schorg.USNonprofitType import USNonprofitTypeProperties
    from schorg.USNonprofitType import AllProperties
    from schorg.USNonprofitType import create_schema_org_model
    from schorg.USNonprofitType import USNonprofitType

    a = create_schema_org_model(type_=USNonprofitTypeInheritedProperties)
    b = create_schema_org_model(type_=USNonprofitTypeProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    USNonprofitType.schema()


def Nonprofit501c4_test():
    from schorg.Nonprofit501c4 import Nonprofit501c4InheritedProperties
    from schorg.Nonprofit501c4 import Nonprofit501c4Properties
    from schorg.Nonprofit501c4 import AllProperties
    from schorg.Nonprofit501c4 import create_schema_org_model
    from schorg.Nonprofit501c4 import Nonprofit501c4

    a = create_schema_org_model(type_=Nonprofit501c4InheritedProperties)
    b = create_schema_org_model(type_=Nonprofit501c4Properties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Nonprofit501c4.schema()


def MeasurementTypeEnumeration_test():
    from schorg.MeasurementTypeEnumeration import MeasurementTypeEnumerationInheritedProperties
    from schorg.MeasurementTypeEnumeration import MeasurementTypeEnumerationProperties
    from schorg.MeasurementTypeEnumeration import AllProperties
    from schorg.MeasurementTypeEnumeration import create_schema_org_model
    from schorg.MeasurementTypeEnumeration import MeasurementTypeEnumeration

    a = create_schema_org_model(type_=MeasurementTypeEnumerationInheritedProperties)
    b = create_schema_org_model(type_=MeasurementTypeEnumerationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MeasurementTypeEnumeration.schema()


def BodyMeasurementTypeEnumeration_test():
    from schorg.BodyMeasurementTypeEnumeration import BodyMeasurementTypeEnumerationInheritedProperties
    from schorg.BodyMeasurementTypeEnumeration import BodyMeasurementTypeEnumerationProperties
    from schorg.BodyMeasurementTypeEnumeration import AllProperties
    from schorg.BodyMeasurementTypeEnumeration import create_schema_org_model
    from schorg.BodyMeasurementTypeEnumeration import BodyMeasurementTypeEnumeration

    a = create_schema_org_model(type_=BodyMeasurementTypeEnumerationInheritedProperties)
    b = create_schema_org_model(type_=BodyMeasurementTypeEnumerationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    BodyMeasurementTypeEnumeration.schema()


def BodyMeasurementWeight_test():
    from schorg.BodyMeasurementWeight import BodyMeasurementWeightInheritedProperties
    from schorg.BodyMeasurementWeight import BodyMeasurementWeightProperties
    from schorg.BodyMeasurementWeight import AllProperties
    from schorg.BodyMeasurementWeight import create_schema_org_model
    from schorg.BodyMeasurementWeight import BodyMeasurementWeight

    a = create_schema_org_model(type_=BodyMeasurementWeightInheritedProperties)
    b = create_schema_org_model(type_=BodyMeasurementWeightProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    BodyMeasurementWeight.schema()


def Reservation_test():
    from schorg.Reservation import ReservationInheritedProperties
    from schorg.Reservation import ReservationProperties
    from schorg.Reservation import AllProperties
    from schorg.Reservation import create_schema_org_model
    from schorg.Reservation import Reservation

    a = create_schema_org_model(type_=ReservationInheritedProperties)
    b = create_schema_org_model(type_=ReservationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Reservation.schema()


def FlightReservation_test():
    from schorg.FlightReservation import FlightReservationInheritedProperties
    from schorg.FlightReservation import FlightReservationProperties
    from schorg.FlightReservation import AllProperties
    from schorg.FlightReservation import create_schema_org_model
    from schorg.FlightReservation import FlightReservation

    a = create_schema_org_model(type_=FlightReservationInheritedProperties)
    b = create_schema_org_model(type_=FlightReservationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    FlightReservation.schema()


def Grant_test():
    from schorg.Grant import GrantInheritedProperties
    from schorg.Grant import GrantProperties
    from schorg.Grant import AllProperties
    from schorg.Grant import create_schema_org_model
    from schorg.Grant import Grant

    a = create_schema_org_model(type_=GrantInheritedProperties)
    b = create_schema_org_model(type_=GrantProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Grant.schema()


def MonetaryGrant_test():
    from schorg.MonetaryGrant import MonetaryGrantInheritedProperties
    from schorg.MonetaryGrant import MonetaryGrantProperties
    from schorg.MonetaryGrant import AllProperties
    from schorg.MonetaryGrant import create_schema_org_model
    from schorg.MonetaryGrant import MonetaryGrant

    a = create_schema_org_model(type_=MonetaryGrantInheritedProperties)
    b = create_schema_org_model(type_=MonetaryGrantProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MonetaryGrant.schema()


def MedicalIndication_test():
    from schorg.MedicalIndication import MedicalIndicationInheritedProperties
    from schorg.MedicalIndication import MedicalIndicationProperties
    from schorg.MedicalIndication import AllProperties
    from schorg.MedicalIndication import create_schema_org_model
    from schorg.MedicalIndication import MedicalIndication

    a = create_schema_org_model(type_=MedicalIndicationInheritedProperties)
    b = create_schema_org_model(type_=MedicalIndicationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MedicalIndication.schema()


def TreatmentIndication_test():
    from schorg.TreatmentIndication import TreatmentIndicationInheritedProperties
    from schorg.TreatmentIndication import TreatmentIndicationProperties
    from schorg.TreatmentIndication import AllProperties
    from schorg.TreatmentIndication import create_schema_org_model
    from schorg.TreatmentIndication import TreatmentIndication

    a = create_schema_org_model(type_=TreatmentIndicationInheritedProperties)
    b = create_schema_org_model(type_=TreatmentIndicationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    TreatmentIndication.schema()


def Cemetery_test():
    from schorg.Cemetery import CemeteryInheritedProperties
    from schorg.Cemetery import CemeteryProperties
    from schorg.Cemetery import AllProperties
    from schorg.Cemetery import create_schema_org_model
    from schorg.Cemetery import Cemetery

    a = create_schema_org_model(type_=CemeteryInheritedProperties)
    b = create_schema_org_model(type_=CemeteryProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Cemetery.schema()


def EnergyEfficiencyEnumeration_test():
    from schorg.EnergyEfficiencyEnumeration import EnergyEfficiencyEnumerationInheritedProperties
    from schorg.EnergyEfficiencyEnumeration import EnergyEfficiencyEnumerationProperties
    from schorg.EnergyEfficiencyEnumeration import AllProperties
    from schorg.EnergyEfficiencyEnumeration import create_schema_org_model
    from schorg.EnergyEfficiencyEnumeration import EnergyEfficiencyEnumeration

    a = create_schema_org_model(type_=EnergyEfficiencyEnumerationInheritedProperties)
    b = create_schema_org_model(type_=EnergyEfficiencyEnumerationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    EnergyEfficiencyEnumeration.schema()


def EUEnergyEfficiencyEnumeration_test():
    from schorg.EUEnergyEfficiencyEnumeration import EUEnergyEfficiencyEnumerationInheritedProperties
    from schorg.EUEnergyEfficiencyEnumeration import EUEnergyEfficiencyEnumerationProperties
    from schorg.EUEnergyEfficiencyEnumeration import AllProperties
    from schorg.EUEnergyEfficiencyEnumeration import create_schema_org_model
    from schorg.EUEnergyEfficiencyEnumeration import EUEnergyEfficiencyEnumeration

    a = create_schema_org_model(type_=EUEnergyEfficiencyEnumerationInheritedProperties)
    b = create_schema_org_model(type_=EUEnergyEfficiencyEnumerationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    EUEnergyEfficiencyEnumeration.schema()


def EUEnergyEfficiencyCategoryA3Plus_test():
    from schorg.EUEnergyEfficiencyCategoryA3Plus import EUEnergyEfficiencyCategoryA3PlusInheritedProperties
    from schorg.EUEnergyEfficiencyCategoryA3Plus import EUEnergyEfficiencyCategoryA3PlusProperties
    from schorg.EUEnergyEfficiencyCategoryA3Plus import AllProperties
    from schorg.EUEnergyEfficiencyCategoryA3Plus import create_schema_org_model
    from schorg.EUEnergyEfficiencyCategoryA3Plus import EUEnergyEfficiencyCategoryA3Plus

    a = create_schema_org_model(type_=EUEnergyEfficiencyCategoryA3PlusInheritedProperties)
    b = create_schema_org_model(type_=EUEnergyEfficiencyCategoryA3PlusProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    EUEnergyEfficiencyCategoryA3Plus.schema()


def DigitalPlatformEnumeration_test():
    from schorg.DigitalPlatformEnumeration import DigitalPlatformEnumerationInheritedProperties
    from schorg.DigitalPlatformEnumeration import DigitalPlatformEnumerationProperties
    from schorg.DigitalPlatformEnumeration import AllProperties
    from schorg.DigitalPlatformEnumeration import create_schema_org_model
    from schorg.DigitalPlatformEnumeration import DigitalPlatformEnumeration

    a = create_schema_org_model(type_=DigitalPlatformEnumerationInheritedProperties)
    b = create_schema_org_model(type_=DigitalPlatformEnumerationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    DigitalPlatformEnumeration.schema()


def MedicalBusiness_test():
    from schorg.MedicalBusiness import MedicalBusinessInheritedProperties
    from schorg.MedicalBusiness import MedicalBusinessProperties
    from schorg.MedicalBusiness import AllProperties
    from schorg.MedicalBusiness import create_schema_org_model
    from schorg.MedicalBusiness import MedicalBusiness

    a = create_schema_org_model(type_=MedicalBusinessInheritedProperties)
    b = create_schema_org_model(type_=MedicalBusinessProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MedicalBusiness.schema()


def Specialty_test():
    from schorg.Specialty import SpecialtyInheritedProperties
    from schorg.Specialty import SpecialtyProperties
    from schorg.Specialty import AllProperties
    from schorg.Specialty import create_schema_org_model
    from schorg.Specialty import Specialty

    a = create_schema_org_model(type_=SpecialtyInheritedProperties)
    b = create_schema_org_model(type_=SpecialtyProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Specialty.schema()


def MedicalSpecialty_test():
    from schorg.MedicalSpecialty import MedicalSpecialtyInheritedProperties
    from schorg.MedicalSpecialty import MedicalSpecialtyProperties
    from schorg.MedicalSpecialty import AllProperties
    from schorg.MedicalSpecialty import create_schema_org_model
    from schorg.MedicalSpecialty import MedicalSpecialty

    a = create_schema_org_model(type_=MedicalSpecialtyInheritedProperties)
    b = create_schema_org_model(type_=MedicalSpecialtyProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MedicalSpecialty.schema()


def PublicHealth_test():
    from schorg.PublicHealth import PublicHealthInheritedProperties
    from schorg.PublicHealth import PublicHealthProperties
    from schorg.PublicHealth import AllProperties
    from schorg.PublicHealth import create_schema_org_model
    from schorg.PublicHealth import PublicHealth

    a = create_schema_org_model(type_=PublicHealthInheritedProperties)
    b = create_schema_org_model(type_=PublicHealthProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    PublicHealth.schema()


def WearableSizeSystemEN13402_test():
    from schorg.WearableSizeSystemEN13402 import WearableSizeSystemEN13402InheritedProperties
    from schorg.WearableSizeSystemEN13402 import WearableSizeSystemEN13402Properties
    from schorg.WearableSizeSystemEN13402 import AllProperties
    from schorg.WearableSizeSystemEN13402 import create_schema_org_model
    from schorg.WearableSizeSystemEN13402 import WearableSizeSystemEN13402

    a = create_schema_org_model(type_=WearableSizeSystemEN13402InheritedProperties)
    b = create_schema_org_model(type_=WearableSizeSystemEN13402Properties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    WearableSizeSystemEN13402.schema()


def InteractAction_test():
    from schorg.InteractAction import InteractActionInheritedProperties
    from schorg.InteractAction import InteractActionProperties
    from schorg.InteractAction import AllProperties
    from schorg.InteractAction import create_schema_org_model
    from schorg.InteractAction import InteractAction

    a = create_schema_org_model(type_=InteractActionInheritedProperties)
    b = create_schema_org_model(type_=InteractActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    InteractAction.schema()


def CommunicateAction_test():
    from schorg.CommunicateAction import CommunicateActionInheritedProperties
    from schorg.CommunicateAction import CommunicateActionProperties
    from schorg.CommunicateAction import AllProperties
    from schorg.CommunicateAction import create_schema_org_model
    from schorg.CommunicateAction import CommunicateAction

    a = create_schema_org_model(type_=CommunicateActionInheritedProperties)
    b = create_schema_org_model(type_=CommunicateActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    CommunicateAction.schema()


def CheckInAction_test():
    from schorg.CheckInAction import CheckInActionInheritedProperties
    from schorg.CheckInAction import CheckInActionProperties
    from schorg.CheckInAction import AllProperties
    from schorg.CheckInAction import create_schema_org_model
    from schorg.CheckInAction import CheckInAction

    a = create_schema_org_model(type_=CheckInActionInheritedProperties)
    b = create_schema_org_model(type_=CheckInActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    CheckInAction.schema()


def PriceComponentTypeEnumeration_test():
    from schorg.PriceComponentTypeEnumeration import PriceComponentTypeEnumerationInheritedProperties
    from schorg.PriceComponentTypeEnumeration import PriceComponentTypeEnumerationProperties
    from schorg.PriceComponentTypeEnumeration import AllProperties
    from schorg.PriceComponentTypeEnumeration import create_schema_org_model
    from schorg.PriceComponentTypeEnumeration import PriceComponentTypeEnumeration

    a = create_schema_org_model(type_=PriceComponentTypeEnumerationInheritedProperties)
    b = create_schema_org_model(type_=PriceComponentTypeEnumerationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    PriceComponentTypeEnumeration.schema()


def DistanceFee_test():
    from schorg.DistanceFee import DistanceFeeInheritedProperties
    from schorg.DistanceFee import DistanceFeeProperties
    from schorg.DistanceFee import AllProperties
    from schorg.DistanceFee import create_schema_org_model
    from schorg.DistanceFee import DistanceFee

    a = create_schema_org_model(type_=DistanceFeeInheritedProperties)
    b = create_schema_org_model(type_=DistanceFeeProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    DistanceFee.schema()


def WearableSizeGroupExtraShort_test():
    from schorg.WearableSizeGroupExtraShort import WearableSizeGroupExtraShortInheritedProperties
    from schorg.WearableSizeGroupExtraShort import WearableSizeGroupExtraShortProperties
    from schorg.WearableSizeGroupExtraShort import AllProperties
    from schorg.WearableSizeGroupExtraShort import create_schema_org_model
    from schorg.WearableSizeGroupExtraShort import WearableSizeGroupExtraShort

    a = create_schema_org_model(type_=WearableSizeGroupExtraShortInheritedProperties)
    b = create_schema_org_model(type_=WearableSizeGroupExtraShortProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    WearableSizeGroupExtraShort.schema()


def EventAttendanceModeEnumeration_test():
    from schorg.EventAttendanceModeEnumeration import EventAttendanceModeEnumerationInheritedProperties
    from schorg.EventAttendanceModeEnumeration import EventAttendanceModeEnumerationProperties
    from schorg.EventAttendanceModeEnumeration import AllProperties
    from schorg.EventAttendanceModeEnumeration import create_schema_org_model
    from schorg.EventAttendanceModeEnumeration import EventAttendanceModeEnumeration

    a = create_schema_org_model(type_=EventAttendanceModeEnumerationInheritedProperties)
    b = create_schema_org_model(type_=EventAttendanceModeEnumerationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    EventAttendanceModeEnumeration.schema()


def WearableSizeSystemJP_test():
    from schorg.WearableSizeSystemJP import WearableSizeSystemJPInheritedProperties
    from schorg.WearableSizeSystemJP import WearableSizeSystemJPProperties
    from schorg.WearableSizeSystemJP import AllProperties
    from schorg.WearableSizeSystemJP import create_schema_org_model
    from schorg.WearableSizeSystemJP import WearableSizeSystemJP

    a = create_schema_org_model(type_=WearableSizeSystemJPInheritedProperties)
    b = create_schema_org_model(type_=WearableSizeSystemJPProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    WearableSizeSystemJP.schema()


def StatusEnumeration_test():
    from schorg.StatusEnumeration import StatusEnumerationInheritedProperties
    from schorg.StatusEnumeration import StatusEnumerationProperties
    from schorg.StatusEnumeration import AllProperties
    from schorg.StatusEnumeration import create_schema_org_model
    from schorg.StatusEnumeration import StatusEnumeration

    a = create_schema_org_model(type_=StatusEnumerationInheritedProperties)
    b = create_schema_org_model(type_=StatusEnumerationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    StatusEnumeration.schema()


def OrderStatus_test():
    from schorg.OrderStatus import OrderStatusInheritedProperties
    from schorg.OrderStatus import OrderStatusProperties
    from schorg.OrderStatus import AllProperties
    from schorg.OrderStatus import create_schema_org_model
    from schorg.OrderStatus import OrderStatus

    a = create_schema_org_model(type_=OrderStatusInheritedProperties)
    b = create_schema_org_model(type_=OrderStatusProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    OrderStatus.schema()


def OrderCancelled_test():
    from schorg.OrderCancelled import OrderCancelledInheritedProperties
    from schorg.OrderCancelled import OrderCancelledProperties
    from schorg.OrderCancelled import AllProperties
    from schorg.OrderCancelled import create_schema_org_model
    from schorg.OrderCancelled import OrderCancelled

    a = create_schema_org_model(type_=OrderCancelledInheritedProperties)
    b = create_schema_org_model(type_=OrderCancelledProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    OrderCancelled.schema()


def PhysicalActivityCategory_test():
    from schorg.PhysicalActivityCategory import PhysicalActivityCategoryInheritedProperties
    from schorg.PhysicalActivityCategory import PhysicalActivityCategoryProperties
    from schorg.PhysicalActivityCategory import AllProperties
    from schorg.PhysicalActivityCategory import create_schema_org_model
    from schorg.PhysicalActivityCategory import PhysicalActivityCategory

    a = create_schema_org_model(type_=PhysicalActivityCategoryInheritedProperties)
    b = create_schema_org_model(type_=PhysicalActivityCategoryProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    PhysicalActivityCategory.schema()


def StrengthTraining_test():
    from schorg.StrengthTraining import StrengthTrainingInheritedProperties
    from schorg.StrengthTraining import StrengthTrainingProperties
    from schorg.StrengthTraining import AllProperties
    from schorg.StrengthTraining import create_schema_org_model
    from schorg.StrengthTraining import StrengthTraining

    a = create_schema_org_model(type_=StrengthTrainingInheritedProperties)
    b = create_schema_org_model(type_=StrengthTrainingProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    StrengthTraining.schema()


def FoodEstablishmentReservation_test():
    from schorg.FoodEstablishmentReservation import FoodEstablishmentReservationInheritedProperties
    from schorg.FoodEstablishmentReservation import FoodEstablishmentReservationProperties
    from schorg.FoodEstablishmentReservation import AllProperties
    from schorg.FoodEstablishmentReservation import create_schema_org_model
    from schorg.FoodEstablishmentReservation import FoodEstablishmentReservation

    a = create_schema_org_model(type_=FoodEstablishmentReservationInheritedProperties)
    b = create_schema_org_model(type_=FoodEstablishmentReservationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    FoodEstablishmentReservation.schema()


def VisualArtwork_test():
    from schorg.VisualArtwork import VisualArtworkInheritedProperties
    from schorg.VisualArtwork import VisualArtworkProperties
    from schorg.VisualArtwork import AllProperties
    from schorg.VisualArtwork import create_schema_org_model
    from schorg.VisualArtwork import VisualArtwork

    a = create_schema_org_model(type_=VisualArtworkInheritedProperties)
    b = create_schema_org_model(type_=VisualArtworkProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    VisualArtwork.schema()


def CoverArt_test():
    from schorg.CoverArt import CoverArtInheritedProperties
    from schorg.CoverArt import CoverArtProperties
    from schorg.CoverArt import AllProperties
    from schorg.CoverArt import create_schema_org_model
    from schorg.CoverArt import CoverArt

    a = create_schema_org_model(type_=CoverArtInheritedProperties)
    b = create_schema_org_model(type_=CoverArtProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    CoverArt.schema()


def MedicineSystem_test():
    from schorg.MedicineSystem import MedicineSystemInheritedProperties
    from schorg.MedicineSystem import MedicineSystemProperties
    from schorg.MedicineSystem import AllProperties
    from schorg.MedicineSystem import create_schema_org_model
    from schorg.MedicineSystem import MedicineSystem

    a = create_schema_org_model(type_=MedicineSystemInheritedProperties)
    b = create_schema_org_model(type_=MedicineSystemProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MedicineSystem.schema()


def Osteopathic_test():
    from schorg.Osteopathic import OsteopathicInheritedProperties
    from schorg.Osteopathic import OsteopathicProperties
    from schorg.Osteopathic import AllProperties
    from schorg.Osteopathic import create_schema_org_model
    from schorg.Osteopathic import Osteopathic

    a = create_schema_org_model(type_=OsteopathicInheritedProperties)
    b = create_schema_org_model(type_=OsteopathicProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Osteopathic.schema()


def MusicReleaseFormatType_test():
    from schorg.MusicReleaseFormatType import MusicReleaseFormatTypeInheritedProperties
    from schorg.MusicReleaseFormatType import MusicReleaseFormatTypeProperties
    from schorg.MusicReleaseFormatType import AllProperties
    from schorg.MusicReleaseFormatType import create_schema_org_model
    from schorg.MusicReleaseFormatType import MusicReleaseFormatType

    a = create_schema_org_model(type_=MusicReleaseFormatTypeInheritedProperties)
    b = create_schema_org_model(type_=MusicReleaseFormatTypeProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MusicReleaseFormatType.schema()


def DigitalAudioTapeFormat_test():
    from schorg.DigitalAudioTapeFormat import DigitalAudioTapeFormatInheritedProperties
    from schorg.DigitalAudioTapeFormat import DigitalAudioTapeFormatProperties
    from schorg.DigitalAudioTapeFormat import AllProperties
    from schorg.DigitalAudioTapeFormat import create_schema_org_model
    from schorg.DigitalAudioTapeFormat import DigitalAudioTapeFormat

    a = create_schema_org_model(type_=DigitalAudioTapeFormatInheritedProperties)
    b = create_schema_org_model(type_=DigitalAudioTapeFormatProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    DigitalAudioTapeFormat.schema()


def HealthInsurancePlan_test():
    from schorg.HealthInsurancePlan import HealthInsurancePlanInheritedProperties
    from schorg.HealthInsurancePlan import HealthInsurancePlanProperties
    from schorg.HealthInsurancePlan import AllProperties
    from schorg.HealthInsurancePlan import create_schema_org_model
    from schorg.HealthInsurancePlan import HealthInsurancePlan

    a = create_schema_org_model(type_=HealthInsurancePlanInheritedProperties)
    b = create_schema_org_model(type_=HealthInsurancePlanProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    HealthInsurancePlan.schema()


def SportsOrganization_test():
    from schorg.SportsOrganization import SportsOrganizationInheritedProperties
    from schorg.SportsOrganization import SportsOrganizationProperties
    from schorg.SportsOrganization import AllProperties
    from schorg.SportsOrganization import create_schema_org_model
    from schorg.SportsOrganization import SportsOrganization

    a = create_schema_org_model(type_=SportsOrganizationInheritedProperties)
    b = create_schema_org_model(type_=SportsOrganizationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    SportsOrganization.schema()


def AutomotiveBusiness_test():
    from schorg.AutomotiveBusiness import AutomotiveBusinessInheritedProperties
    from schorg.AutomotiveBusiness import AutomotiveBusinessProperties
    from schorg.AutomotiveBusiness import AllProperties
    from schorg.AutomotiveBusiness import create_schema_org_model
    from schorg.AutomotiveBusiness import AutomotiveBusiness

    a = create_schema_org_model(type_=AutomotiveBusinessInheritedProperties)
    b = create_schema_org_model(type_=AutomotiveBusinessProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    AutomotiveBusiness.schema()


def AutoRepair_test():
    from schorg.AutoRepair import AutoRepairInheritedProperties
    from schorg.AutoRepair import AutoRepairProperties
    from schorg.AutoRepair import AllProperties
    from schorg.AutoRepair import create_schema_org_model
    from schorg.AutoRepair import AutoRepair

    a = create_schema_org_model(type_=AutoRepairInheritedProperties)
    b = create_schema_org_model(type_=AutoRepairProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    AutoRepair.schema()


def OnlineBusiness_test():
    from schorg.OnlineBusiness import OnlineBusinessInheritedProperties
    from schorg.OnlineBusiness import OnlineBusinessProperties
    from schorg.OnlineBusiness import AllProperties
    from schorg.OnlineBusiness import create_schema_org_model
    from schorg.OnlineBusiness import OnlineBusiness

    a = create_schema_org_model(type_=OnlineBusinessInheritedProperties)
    b = create_schema_org_model(type_=OnlineBusinessProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    OnlineBusiness.schema()


def MedicalStudyStatus_test():
    from schorg.MedicalStudyStatus import MedicalStudyStatusInheritedProperties
    from schorg.MedicalStudyStatus import MedicalStudyStatusProperties
    from schorg.MedicalStudyStatus import AllProperties
    from schorg.MedicalStudyStatus import create_schema_org_model
    from schorg.MedicalStudyStatus import MedicalStudyStatus

    a = create_schema_org_model(type_=MedicalStudyStatusInheritedProperties)
    b = create_schema_org_model(type_=MedicalStudyStatusProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MedicalStudyStatus.schema()


def ResultsAvailable_test():
    from schorg.ResultsAvailable import ResultsAvailableInheritedProperties
    from schorg.ResultsAvailable import ResultsAvailableProperties
    from schorg.ResultsAvailable import AllProperties
    from schorg.ResultsAvailable import create_schema_org_model
    from schorg.ResultsAvailable import ResultsAvailable

    a = create_schema_org_model(type_=ResultsAvailableInheritedProperties)
    b = create_schema_org_model(type_=ResultsAvailableProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ResultsAvailable.schema()


def Suite_test():
    from schorg.Suite import SuiteInheritedProperties
    from schorg.Suite import SuiteProperties
    from schorg.Suite import AllProperties
    from schorg.Suite import create_schema_org_model
    from schorg.Suite import Suite

    a = create_schema_org_model(type_=SuiteInheritedProperties)
    b = create_schema_org_model(type_=SuiteProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Suite.schema()


def EUEnergyEfficiencyCategoryG_test():
    from schorg.EUEnergyEfficiencyCategoryG import EUEnergyEfficiencyCategoryGInheritedProperties
    from schorg.EUEnergyEfficiencyCategoryG import EUEnergyEfficiencyCategoryGProperties
    from schorg.EUEnergyEfficiencyCategoryG import AllProperties
    from schorg.EUEnergyEfficiencyCategoryG import create_schema_org_model
    from schorg.EUEnergyEfficiencyCategoryG import EUEnergyEfficiencyCategoryG

    a = create_schema_org_model(type_=EUEnergyEfficiencyCategoryGInheritedProperties)
    b = create_schema_org_model(type_=EUEnergyEfficiencyCategoryGProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    EUEnergyEfficiencyCategoryG.schema()


def DeliveryMethod_test():
    from schorg.DeliveryMethod import DeliveryMethodInheritedProperties
    from schorg.DeliveryMethod import DeliveryMethodProperties
    from schorg.DeliveryMethod import AllProperties
    from schorg.DeliveryMethod import create_schema_org_model
    from schorg.DeliveryMethod import DeliveryMethod

    a = create_schema_org_model(type_=DeliveryMethodInheritedProperties)
    b = create_schema_org_model(type_=DeliveryMethodProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    DeliveryMethod.schema()


def ParcelService_test():
    from schorg.ParcelService import ParcelServiceInheritedProperties
    from schorg.ParcelService import ParcelServiceProperties
    from schorg.ParcelService import AllProperties
    from schorg.ParcelService import create_schema_org_model
    from schorg.ParcelService import ParcelService

    a = create_schema_org_model(type_=ParcelServiceInheritedProperties)
    b = create_schema_org_model(type_=ParcelServiceProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ParcelService.schema()


def TradeAction_test():
    from schorg.TradeAction import TradeActionInheritedProperties
    from schorg.TradeAction import TradeActionProperties
    from schorg.TradeAction import AllProperties
    from schorg.TradeAction import create_schema_org_model
    from schorg.TradeAction import TradeAction

    a = create_schema_org_model(type_=TradeActionInheritedProperties)
    b = create_schema_org_model(type_=TradeActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    TradeAction.schema()


def TipAction_test():
    from schorg.TipAction import TipActionInheritedProperties
    from schorg.TipAction import TipActionProperties
    from schorg.TipAction import AllProperties
    from schorg.TipAction import create_schema_org_model
    from schorg.TipAction import TipAction

    a = create_schema_org_model(type_=TipActionInheritedProperties)
    b = create_schema_org_model(type_=TipActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    TipAction.schema()


def LearningResource_test():
    from schorg.LearningResource import LearningResourceInheritedProperties
    from schorg.LearningResource import LearningResourceProperties
    from schorg.LearningResource import AllProperties
    from schorg.LearningResource import create_schema_org_model
    from schorg.LearningResource import LearningResource

    a = create_schema_org_model(type_=LearningResourceInheritedProperties)
    b = create_schema_org_model(type_=LearningResourceProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    LearningResource.schema()


def MedicalAudienceType_test():
    from schorg.MedicalAudienceType import MedicalAudienceTypeInheritedProperties
    from schorg.MedicalAudienceType import MedicalAudienceTypeProperties
    from schorg.MedicalAudienceType import AllProperties
    from schorg.MedicalAudienceType import create_schema_org_model
    from schorg.MedicalAudienceType import MedicalAudienceType

    a = create_schema_org_model(type_=MedicalAudienceTypeInheritedProperties)
    b = create_schema_org_model(type_=MedicalAudienceTypeProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MedicalAudienceType.schema()


def LodgingBusiness_test():
    from schorg.LodgingBusiness import LodgingBusinessInheritedProperties
    from schorg.LodgingBusiness import LodgingBusinessProperties
    from schorg.LodgingBusiness import AllProperties
    from schorg.LodgingBusiness import create_schema_org_model
    from schorg.LodgingBusiness import LodgingBusiness

    a = create_schema_org_model(type_=LodgingBusinessInheritedProperties)
    b = create_schema_org_model(type_=LodgingBusinessProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    LodgingBusiness.schema()


def BedAndBreakfast_test():
    from schorg.BedAndBreakfast import BedAndBreakfastInheritedProperties
    from schorg.BedAndBreakfast import BedAndBreakfastProperties
    from schorg.BedAndBreakfast import AllProperties
    from schorg.BedAndBreakfast import create_schema_org_model
    from schorg.BedAndBreakfast import BedAndBreakfast

    a = create_schema_org_model(type_=BedAndBreakfastInheritedProperties)
    b = create_schema_org_model(type_=BedAndBreakfastProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    BedAndBreakfast.schema()


def EngineSpecification_test():
    from schorg.EngineSpecification import EngineSpecificationInheritedProperties
    from schorg.EngineSpecification import EngineSpecificationProperties
    from schorg.EngineSpecification import AllProperties
    from schorg.EngineSpecification import create_schema_org_model
    from schorg.EngineSpecification import EngineSpecification

    a = create_schema_org_model(type_=EngineSpecificationInheritedProperties)
    b = create_schema_org_model(type_=EngineSpecificationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    EngineSpecification.schema()


def Bridge_test():
    from schorg.Bridge import BridgeInheritedProperties
    from schorg.Bridge import BridgeProperties
    from schorg.Bridge import AllProperties
    from schorg.Bridge import create_schema_org_model
    from schorg.Bridge import Bridge

    a = create_schema_org_model(type_=BridgeInheritedProperties)
    b = create_schema_org_model(type_=BridgeProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Bridge.schema()


def OnlineStore_test():
    from schorg.OnlineStore import OnlineStoreInheritedProperties
    from schorg.OnlineStore import OnlineStoreProperties
    from schorg.OnlineStore import AllProperties
    from schorg.OnlineStore import create_schema_org_model
    from schorg.OnlineStore import OnlineStore

    a = create_schema_org_model(type_=OnlineStoreInheritedProperties)
    b = create_schema_org_model(type_=OnlineStoreProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    OnlineStore.schema()


def ReservationStatusType_test():
    from schorg.ReservationStatusType import ReservationStatusTypeInheritedProperties
    from schorg.ReservationStatusType import ReservationStatusTypeProperties
    from schorg.ReservationStatusType import AllProperties
    from schorg.ReservationStatusType import create_schema_org_model
    from schorg.ReservationStatusType import ReservationStatusType

    a = create_schema_org_model(type_=ReservationStatusTypeInheritedProperties)
    b = create_schema_org_model(type_=ReservationStatusTypeProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ReservationStatusType.schema()


def ReservationCancelled_test():
    from schorg.ReservationCancelled import ReservationCancelledInheritedProperties
    from schorg.ReservationCancelled import ReservationCancelledProperties
    from schorg.ReservationCancelled import AllProperties
    from schorg.ReservationCancelled import create_schema_org_model
    from schorg.ReservationCancelled import ReservationCancelled

    a = create_schema_org_model(type_=ReservationCancelledInheritedProperties)
    b = create_schema_org_model(type_=ReservationCancelledProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ReservationCancelled.schema()


def Thesis_test():
    from schorg.Thesis import ThesisInheritedProperties
    from schorg.Thesis import ThesisProperties
    from schorg.Thesis import AllProperties
    from schorg.Thesis import create_schema_org_model
    from schorg.Thesis import Thesis

    a = create_schema_org_model(type_=ThesisInheritedProperties)
    b = create_schema_org_model(type_=ThesisProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Thesis.schema()


def BusinessAudience_test():
    from schorg.BusinessAudience import BusinessAudienceInheritedProperties
    from schorg.BusinessAudience import BusinessAudienceProperties
    from schorg.BusinessAudience import AllProperties
    from schorg.BusinessAudience import create_schema_org_model
    from schorg.BusinessAudience import BusinessAudience

    a = create_schema_org_model(type_=BusinessAudienceInheritedProperties)
    b = create_schema_org_model(type_=BusinessAudienceProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    BusinessAudience.schema()


def Service_test():
    from schorg.Service import ServiceInheritedProperties
    from schorg.Service import ServiceProperties
    from schorg.Service import AllProperties
    from schorg.Service import create_schema_org_model
    from schorg.Service import Service

    a = create_schema_org_model(type_=ServiceInheritedProperties)
    b = create_schema_org_model(type_=ServiceProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Service.schema()


def FinancialProduct_test():
    from schorg.FinancialProduct import FinancialProductInheritedProperties
    from schorg.FinancialProduct import FinancialProductProperties
    from schorg.FinancialProduct import AllProperties
    from schorg.FinancialProduct import create_schema_org_model
    from schorg.FinancialProduct import FinancialProduct

    a = create_schema_org_model(type_=FinancialProductInheritedProperties)
    b = create_schema_org_model(type_=FinancialProductProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    FinancialProduct.schema()


def InvestmentOrDeposit_test():
    from schorg.InvestmentOrDeposit import InvestmentOrDepositInheritedProperties
    from schorg.InvestmentOrDeposit import InvestmentOrDepositProperties
    from schorg.InvestmentOrDeposit import AllProperties
    from schorg.InvestmentOrDeposit import create_schema_org_model
    from schorg.InvestmentOrDeposit import InvestmentOrDeposit

    a = create_schema_org_model(type_=InvestmentOrDepositInheritedProperties)
    b = create_schema_org_model(type_=InvestmentOrDepositProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    InvestmentOrDeposit.schema()


def BrokerageAccount_test():
    from schorg.BrokerageAccount import BrokerageAccountInheritedProperties
    from schorg.BrokerageAccount import BrokerageAccountProperties
    from schorg.BrokerageAccount import AllProperties
    from schorg.BrokerageAccount import create_schema_org_model
    from schorg.BrokerageAccount import BrokerageAccount

    a = create_schema_org_model(type_=BrokerageAccountInheritedProperties)
    b = create_schema_org_model(type_=BrokerageAccountProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    BrokerageAccount.schema()


def FinancialService_test():
    from schorg.FinancialService import FinancialServiceInheritedProperties
    from schorg.FinancialService import FinancialServiceProperties
    from schorg.FinancialService import AllProperties
    from schorg.FinancialService import create_schema_org_model
    from schorg.FinancialService import FinancialService

    a = create_schema_org_model(type_=FinancialServiceInheritedProperties)
    b = create_schema_org_model(type_=FinancialServiceProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    FinancialService.schema()


def AutomatedTeller_test():
    from schorg.AutomatedTeller import AutomatedTellerInheritedProperties
    from schorg.AutomatedTeller import AutomatedTellerProperties
    from schorg.AutomatedTeller import AllProperties
    from schorg.AutomatedTeller import create_schema_org_model
    from schorg.AutomatedTeller import AutomatedTeller

    a = create_schema_org_model(type_=AutomatedTellerInheritedProperties)
    b = create_schema_org_model(type_=AutomatedTellerProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    AutomatedTeller.schema()


def DayOfWeek_test():
    from schorg.DayOfWeek import DayOfWeekInheritedProperties
    from schorg.DayOfWeek import DayOfWeekProperties
    from schorg.DayOfWeek import AllProperties
    from schorg.DayOfWeek import create_schema_org_model
    from schorg.DayOfWeek import DayOfWeek

    a = create_schema_org_model(type_=DayOfWeekInheritedProperties)
    b = create_schema_org_model(type_=DayOfWeekProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    DayOfWeek.schema()


def Thursday_test():
    from schorg.Thursday import ThursdayInheritedProperties
    from schorg.Thursday import ThursdayProperties
    from schorg.Thursday import AllProperties
    from schorg.Thursday import create_schema_org_model
    from schorg.Thursday import Thursday

    a = create_schema_org_model(type_=ThursdayInheritedProperties)
    b = create_schema_org_model(type_=ThursdayProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Thursday.schema()


def Crematorium_test():
    from schorg.Crematorium import CrematoriumInheritedProperties
    from schorg.Crematorium import CrematoriumProperties
    from schorg.Crematorium import AllProperties
    from schorg.Crematorium import create_schema_org_model
    from schorg.Crematorium import Crematorium

    a = create_schema_org_model(type_=CrematoriumInheritedProperties)
    b = create_schema_org_model(type_=CrematoriumProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Crematorium.schema()


def MedicalConditionStage_test():
    from schorg.MedicalConditionStage import MedicalConditionStageInheritedProperties
    from schorg.MedicalConditionStage import MedicalConditionStageProperties
    from schorg.MedicalConditionStage import AllProperties
    from schorg.MedicalConditionStage import create_schema_org_model
    from schorg.MedicalConditionStage import MedicalConditionStage

    a = create_schema_org_model(type_=MedicalConditionStageInheritedProperties)
    b = create_schema_org_model(type_=MedicalConditionStageProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MedicalConditionStage.schema()


def DietNutrition_test():
    from schorg.DietNutrition import DietNutritionInheritedProperties
    from schorg.DietNutrition import DietNutritionProperties
    from schorg.DietNutrition import AllProperties
    from schorg.DietNutrition import create_schema_org_model
    from schorg.DietNutrition import DietNutrition

    a = create_schema_org_model(type_=DietNutritionInheritedProperties)
    b = create_schema_org_model(type_=DietNutritionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    DietNutrition.schema()


def Rheumatologic_test():
    from schorg.Rheumatologic import RheumatologicInheritedProperties
    from schorg.Rheumatologic import RheumatologicProperties
    from schorg.Rheumatologic import AllProperties
    from schorg.Rheumatologic import create_schema_org_model
    from schorg.Rheumatologic import Rheumatologic

    a = create_schema_org_model(type_=RheumatologicInheritedProperties)
    b = create_schema_org_model(type_=RheumatologicProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Rheumatologic.schema()


def AssessAction_test():
    from schorg.AssessAction import AssessActionInheritedProperties
    from schorg.AssessAction import AssessActionProperties
    from schorg.AssessAction import AllProperties
    from schorg.AssessAction import create_schema_org_model
    from schorg.AssessAction import AssessAction

    a = create_schema_org_model(type_=AssessActionInheritedProperties)
    b = create_schema_org_model(type_=AssessActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    AssessAction.schema()


def EmergencyService_test():
    from schorg.EmergencyService import EmergencyServiceInheritedProperties
    from schorg.EmergencyService import EmergencyServiceProperties
    from schorg.EmergencyService import AllProperties
    from schorg.EmergencyService import create_schema_org_model
    from schorg.EmergencyService import EmergencyService

    a = create_schema_org_model(type_=EmergencyServiceInheritedProperties)
    b = create_schema_org_model(type_=EmergencyServiceProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    EmergencyService.schema()


def FireStation_test():
    from schorg.FireStation import FireStationInheritedProperties
    from schorg.FireStation import FireStationProperties
    from schorg.FireStation import AllProperties
    from schorg.FireStation import create_schema_org_model
    from schorg.FireStation import FireStation

    a = create_schema_org_model(type_=FireStationInheritedProperties)
    b = create_schema_org_model(type_=FireStationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    FireStation.schema()


def Class_test():
    from schorg.Class import ClassInheritedProperties
    from schorg.Class import ClassProperties
    from schorg.Class import AllProperties
    from schorg.Class import create_schema_org_model
    from schorg.Class import Class

    a = create_schema_org_model(type_=ClassInheritedProperties)
    b = create_schema_org_model(type_=ClassProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Class.schema()


def DataType_test():
    from schorg.DataType import DataTypeInheritedProperties
    from schorg.DataType import DataTypeProperties
    from schorg.DataType import AllProperties
    from schorg.DataType import create_schema_org_model
    from schorg.DataType import DataType

    a = create_schema_org_model(type_=DataTypeInheritedProperties)
    b = create_schema_org_model(type_=DataTypeProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    DataType.schema()


def Text_test():
    from schorg.Text import TextInheritedProperties
    from schorg.Text import TextProperties
    from schorg.Text import AllProperties
    from schorg.Text import create_schema_org_model
    from schorg.Text import Text

    a = create_schema_org_model(type_=TextInheritedProperties)
    b = create_schema_org_model(type_=TextProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Text.schema()


def CssSelectorType_test():
    from schorg.CssSelectorType import CssSelectorTypeInheritedProperties
    from schorg.CssSelectorType import CssSelectorTypeProperties
    from schorg.CssSelectorType import AllProperties
    from schorg.CssSelectorType import create_schema_org_model
    from schorg.CssSelectorType import CssSelectorType

    a = create_schema_org_model(type_=CssSelectorTypeInheritedProperties)
    b = create_schema_org_model(type_=CssSelectorTypeProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    CssSelectorType.schema()


def LaserDiscFormat_test():
    from schorg.LaserDiscFormat import LaserDiscFormatInheritedProperties
    from schorg.LaserDiscFormat import LaserDiscFormatProperties
    from schorg.LaserDiscFormat import AllProperties
    from schorg.LaserDiscFormat import create_schema_org_model
    from schorg.LaserDiscFormat import LaserDiscFormat

    a = create_schema_org_model(type_=LaserDiscFormatInheritedProperties)
    b = create_schema_org_model(type_=LaserDiscFormatProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    LaserDiscFormat.schema()


def Ticket_test():
    from schorg.Ticket import TicketInheritedProperties
    from schorg.Ticket import TicketProperties
    from schorg.Ticket import AllProperties
    from schorg.Ticket import create_schema_org_model
    from schorg.Ticket import Ticket

    a = create_schema_org_model(type_=TicketInheritedProperties)
    b = create_schema_org_model(type_=TicketProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Ticket.schema()


def OfferItemCondition_test():
    from schorg.OfferItemCondition import OfferItemConditionInheritedProperties
    from schorg.OfferItemCondition import OfferItemConditionProperties
    from schorg.OfferItemCondition import AllProperties
    from schorg.OfferItemCondition import create_schema_org_model
    from schorg.OfferItemCondition import OfferItemCondition

    a = create_schema_org_model(type_=OfferItemConditionInheritedProperties)
    b = create_schema_org_model(type_=OfferItemConditionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    OfferItemCondition.schema()


def UsedCondition_test():
    from schorg.UsedCondition import UsedConditionInheritedProperties
    from schorg.UsedCondition import UsedConditionProperties
    from schorg.UsedCondition import AllProperties
    from schorg.UsedCondition import create_schema_org_model
    from schorg.UsedCondition import UsedCondition

    a = create_schema_org_model(type_=UsedConditionInheritedProperties)
    b = create_schema_org_model(type_=UsedConditionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    UsedCondition.schema()


def WebPage_test():
    from schorg.WebPage import WebPageInheritedProperties
    from schorg.WebPage import WebPageProperties
    from schorg.WebPage import AllProperties
    from schorg.WebPage import create_schema_org_model
    from schorg.WebPage import WebPage

    a = create_schema_org_model(type_=WebPageInheritedProperties)
    b = create_schema_org_model(type_=WebPageProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    WebPage.schema()


def CollectionPage_test():
    from schorg.CollectionPage import CollectionPageInheritedProperties
    from schorg.CollectionPage import CollectionPageProperties
    from schorg.CollectionPage import AllProperties
    from schorg.CollectionPage import create_schema_org_model
    from schorg.CollectionPage import CollectionPage

    a = create_schema_org_model(type_=CollectionPageInheritedProperties)
    b = create_schema_org_model(type_=CollectionPageProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    CollectionPage.schema()


def LifestyleModification_test():
    from schorg.LifestyleModification import LifestyleModificationInheritedProperties
    from schorg.LifestyleModification import LifestyleModificationProperties
    from schorg.LifestyleModification import AllProperties
    from schorg.LifestyleModification import create_schema_org_model
    from schorg.LifestyleModification import LifestyleModification

    a = create_schema_org_model(type_=LifestyleModificationInheritedProperties)
    b = create_schema_org_model(type_=LifestyleModificationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    LifestyleModification.schema()


def PhysicalActivity_test():
    from schorg.PhysicalActivity import PhysicalActivityInheritedProperties
    from schorg.PhysicalActivity import PhysicalActivityProperties
    from schorg.PhysicalActivity import AllProperties
    from schorg.PhysicalActivity import create_schema_org_model
    from schorg.PhysicalActivity import PhysicalActivity

    a = create_schema_org_model(type_=PhysicalActivityInheritedProperties)
    b = create_schema_org_model(type_=PhysicalActivityProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    PhysicalActivity.schema()


def LiquorStore_test():
    from schorg.LiquorStore import LiquorStoreInheritedProperties
    from schorg.LiquorStore import LiquorStoreProperties
    from schorg.LiquorStore import AllProperties
    from schorg.LiquorStore import create_schema_org_model
    from schorg.LiquorStore import LiquorStore

    a = create_schema_org_model(type_=LiquorStoreInheritedProperties)
    b = create_schema_org_model(type_=LiquorStoreProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    LiquorStore.schema()


def DrugPregnancyCategory_test():
    from schorg.DrugPregnancyCategory import DrugPregnancyCategoryInheritedProperties
    from schorg.DrugPregnancyCategory import DrugPregnancyCategoryProperties
    from schorg.DrugPregnancyCategory import AllProperties
    from schorg.DrugPregnancyCategory import create_schema_org_model
    from schorg.DrugPregnancyCategory import DrugPregnancyCategory

    a = create_schema_org_model(type_=DrugPregnancyCategoryInheritedProperties)
    b = create_schema_org_model(type_=DrugPregnancyCategoryProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    DrugPregnancyCategory.schema()


def FDAcategoryX_test():
    from schorg.FDAcategoryX import FDAcategoryXInheritedProperties
    from schorg.FDAcategoryX import FDAcategoryXProperties
    from schorg.FDAcategoryX import AllProperties
    from schorg.FDAcategoryX import create_schema_org_model
    from schorg.FDAcategoryX import FDAcategoryX

    a = create_schema_org_model(type_=FDAcategoryXInheritedProperties)
    b = create_schema_org_model(type_=FDAcategoryXProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    FDAcategoryX.schema()


def EducationalOrganization_test():
    from schorg.EducationalOrganization import EducationalOrganizationInheritedProperties
    from schorg.EducationalOrganization import EducationalOrganizationProperties
    from schorg.EducationalOrganization import AllProperties
    from schorg.EducationalOrganization import create_schema_org_model
    from schorg.EducationalOrganization import EducationalOrganization

    a = create_schema_org_model(type_=EducationalOrganizationInheritedProperties)
    b = create_schema_org_model(type_=EducationalOrganizationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    EducationalOrganization.schema()


def Series_test():
    from schorg.Series import SeriesInheritedProperties
    from schorg.Series import SeriesProperties
    from schorg.Series import AllProperties
    from schorg.Series import create_schema_org_model
    from schorg.Series import Series

    a = create_schema_org_model(type_=SeriesInheritedProperties)
    b = create_schema_org_model(type_=SeriesProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Series.schema()


def EventSeries_test():
    from schorg.EventSeries import EventSeriesInheritedProperties
    from schorg.EventSeries import EventSeriesProperties
    from schorg.EventSeries import AllProperties
    from schorg.EventSeries import create_schema_org_model
    from schorg.EventSeries import EventSeries

    a = create_schema_org_model(type_=EventSeriesInheritedProperties)
    b = create_schema_org_model(type_=EventSeriesProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    EventSeries.schema()


def WearableSizeGroupPetite_test():
    from schorg.WearableSizeGroupPetite import WearableSizeGroupPetiteInheritedProperties
    from schorg.WearableSizeGroupPetite import WearableSizeGroupPetiteProperties
    from schorg.WearableSizeGroupPetite import AllProperties
    from schorg.WearableSizeGroupPetite import create_schema_org_model
    from schorg.WearableSizeGroupPetite import WearableSizeGroupPetite

    a = create_schema_org_model(type_=WearableSizeGroupPetiteInheritedProperties)
    b = create_schema_org_model(type_=WearableSizeGroupPetiteProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    WearableSizeGroupPetite.schema()


def HealthAspectEnumeration_test():
    from schorg.HealthAspectEnumeration import HealthAspectEnumerationInheritedProperties
    from schorg.HealthAspectEnumeration import HealthAspectEnumerationProperties
    from schorg.HealthAspectEnumeration import AllProperties
    from schorg.HealthAspectEnumeration import create_schema_org_model
    from schorg.HealthAspectEnumeration import HealthAspectEnumeration

    a = create_schema_org_model(type_=HealthAspectEnumerationInheritedProperties)
    b = create_schema_org_model(type_=HealthAspectEnumerationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    HealthAspectEnumeration.schema()


def PrognosisHealthAspect_test():
    from schorg.PrognosisHealthAspect import PrognosisHealthAspectInheritedProperties
    from schorg.PrognosisHealthAspect import PrognosisHealthAspectProperties
    from schorg.PrognosisHealthAspect import AllProperties
    from schorg.PrognosisHealthAspect import create_schema_org_model
    from schorg.PrognosisHealthAspect import PrognosisHealthAspect

    a = create_schema_org_model(type_=PrognosisHealthAspectInheritedProperties)
    b = create_schema_org_model(type_=PrognosisHealthAspectProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    PrognosisHealthAspect.schema()


def LegalForceStatus_test():
    from schorg.LegalForceStatus import LegalForceStatusInheritedProperties
    from schorg.LegalForceStatus import LegalForceStatusProperties
    from schorg.LegalForceStatus import AllProperties
    from schorg.LegalForceStatus import create_schema_org_model
    from schorg.LegalForceStatus import LegalForceStatus

    a = create_schema_org_model(type_=LegalForceStatusInheritedProperties)
    b = create_schema_org_model(type_=LegalForceStatusProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    LegalForceStatus.schema()


def PartiallyInForce_test():
    from schorg.PartiallyInForce import PartiallyInForceInheritedProperties
    from schorg.PartiallyInForce import PartiallyInForceProperties
    from schorg.PartiallyInForce import AllProperties
    from schorg.PartiallyInForce import create_schema_org_model
    from schorg.PartiallyInForce import PartiallyInForce

    a = create_schema_org_model(type_=PartiallyInForceInheritedProperties)
    b = create_schema_org_model(type_=PartiallyInForceProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    PartiallyInForce.schema()


def RestockingFees_test():
    from schorg.RestockingFees import RestockingFeesInheritedProperties
    from schorg.RestockingFees import RestockingFeesProperties
    from schorg.RestockingFees import AllProperties
    from schorg.RestockingFees import create_schema_org_model
    from schorg.RestockingFees import RestockingFees

    a = create_schema_org_model(type_=RestockingFeesInheritedProperties)
    b = create_schema_org_model(type_=RestockingFeesProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    RestockingFees.schema()


def WearableMeasurementTypeEnumeration_test():
    from schorg.WearableMeasurementTypeEnumeration import WearableMeasurementTypeEnumerationInheritedProperties
    from schorg.WearableMeasurementTypeEnumeration import WearableMeasurementTypeEnumerationProperties
    from schorg.WearableMeasurementTypeEnumeration import AllProperties
    from schorg.WearableMeasurementTypeEnumeration import create_schema_org_model
    from schorg.WearableMeasurementTypeEnumeration import WearableMeasurementTypeEnumeration

    a = create_schema_org_model(type_=WearableMeasurementTypeEnumerationInheritedProperties)
    b = create_schema_org_model(type_=WearableMeasurementTypeEnumerationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    WearableMeasurementTypeEnumeration.schema()


def WearableMeasurementHips_test():
    from schorg.WearableMeasurementHips import WearableMeasurementHipsInheritedProperties
    from schorg.WearableMeasurementHips import WearableMeasurementHipsProperties
    from schorg.WearableMeasurementHips import AllProperties
    from schorg.WearableMeasurementHips import create_schema_org_model
    from schorg.WearableMeasurementHips import WearableMeasurementHips

    a = create_schema_org_model(type_=WearableMeasurementHipsInheritedProperties)
    b = create_schema_org_model(type_=WearableMeasurementHipsProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    WearableMeasurementHips.schema()


def UserInteraction_test():
    from schorg.UserInteraction import UserInteractionInheritedProperties
    from schorg.UserInteraction import UserInteractionProperties
    from schorg.UserInteraction import AllProperties
    from schorg.UserInteraction import create_schema_org_model
    from schorg.UserInteraction import UserInteraction

    a = create_schema_org_model(type_=UserInteractionInheritedProperties)
    b = create_schema_org_model(type_=UserInteractionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    UserInteraction.schema()


def UserPageVisits_test():
    from schorg.UserPageVisits import UserPageVisitsInheritedProperties
    from schorg.UserPageVisits import UserPageVisitsProperties
    from schorg.UserPageVisits import AllProperties
    from schorg.UserPageVisits import create_schema_org_model
    from schorg.UserPageVisits import UserPageVisits

    a = create_schema_org_model(type_=UserPageVisitsInheritedProperties)
    b = create_schema_org_model(type_=UserPageVisitsProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    UserPageVisits.schema()


def DigitalDocumentPermissionType_test():
    from schorg.DigitalDocumentPermissionType import DigitalDocumentPermissionTypeInheritedProperties
    from schorg.DigitalDocumentPermissionType import DigitalDocumentPermissionTypeProperties
    from schorg.DigitalDocumentPermissionType import AllProperties
    from schorg.DigitalDocumentPermissionType import create_schema_org_model
    from schorg.DigitalDocumentPermissionType import DigitalDocumentPermissionType

    a = create_schema_org_model(type_=DigitalDocumentPermissionTypeInheritedProperties)
    b = create_schema_org_model(type_=DigitalDocumentPermissionTypeProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    DigitalDocumentPermissionType.schema()


def CommentPermission_test():
    from schorg.CommentPermission import CommentPermissionInheritedProperties
    from schorg.CommentPermission import CommentPermissionProperties
    from schorg.CommentPermission import AllProperties
    from schorg.CommentPermission import create_schema_org_model
    from schorg.CommentPermission import CommentPermission

    a = create_schema_org_model(type_=CommentPermissionInheritedProperties)
    b = create_schema_org_model(type_=CommentPermissionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    CommentPermission.schema()


def MediaManipulationRatingEnumeration_test():
    from schorg.MediaManipulationRatingEnumeration import MediaManipulationRatingEnumerationInheritedProperties
    from schorg.MediaManipulationRatingEnumeration import MediaManipulationRatingEnumerationProperties
    from schorg.MediaManipulationRatingEnumeration import AllProperties
    from schorg.MediaManipulationRatingEnumeration import create_schema_org_model
    from schorg.MediaManipulationRatingEnumeration import MediaManipulationRatingEnumeration

    a = create_schema_org_model(type_=MediaManipulationRatingEnumerationInheritedProperties)
    b = create_schema_org_model(type_=MediaManipulationRatingEnumerationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MediaManipulationRatingEnumeration.schema()


def OriginalMediaContent_test():
    from schorg.OriginalMediaContent import OriginalMediaContentInheritedProperties
    from schorg.OriginalMediaContent import OriginalMediaContentProperties
    from schorg.OriginalMediaContent import AllProperties
    from schorg.OriginalMediaContent import create_schema_org_model
    from schorg.OriginalMediaContent import OriginalMediaContent

    a = create_schema_org_model(type_=OriginalMediaContentInheritedProperties)
    b = create_schema_org_model(type_=OriginalMediaContentProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    OriginalMediaContent.schema()


def DVDFormat_test():
    from schorg.DVDFormat import DVDFormatInheritedProperties
    from schorg.DVDFormat import DVDFormatProperties
    from schorg.DVDFormat import AllProperties
    from schorg.DVDFormat import create_schema_org_model
    from schorg.DVDFormat import DVDFormat

    a = create_schema_org_model(type_=DVDFormatInheritedProperties)
    b = create_schema_org_model(type_=DVDFormatProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    DVDFormat.schema()


def UserDownloads_test():
    from schorg.UserDownloads import UserDownloadsInheritedProperties
    from schorg.UserDownloads import UserDownloadsProperties
    from schorg.UserDownloads import AllProperties
    from schorg.UserDownloads import create_schema_org_model
    from schorg.UserDownloads import UserDownloads

    a = create_schema_org_model(type_=UserDownloadsInheritedProperties)
    b = create_schema_org_model(type_=UserDownloadsProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    UserDownloads.schema()


def TrainReservation_test():
    from schorg.TrainReservation import TrainReservationInheritedProperties
    from schorg.TrainReservation import TrainReservationProperties
    from schorg.TrainReservation import AllProperties
    from schorg.TrainReservation import create_schema_org_model
    from schorg.TrainReservation import TrainReservation

    a = create_schema_org_model(type_=TrainReservationInheritedProperties)
    b = create_schema_org_model(type_=TrainReservationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    TrainReservation.schema()


def MusicPlaylist_test():
    from schorg.MusicPlaylist import MusicPlaylistInheritedProperties
    from schorg.MusicPlaylist import MusicPlaylistProperties
    from schorg.MusicPlaylist import AllProperties
    from schorg.MusicPlaylist import create_schema_org_model
    from schorg.MusicPlaylist import MusicPlaylist

    a = create_schema_org_model(type_=MusicPlaylistInheritedProperties)
    b = create_schema_org_model(type_=MusicPlaylistProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MusicPlaylist.schema()


def VirtualLocation_test():
    from schorg.VirtualLocation import VirtualLocationInheritedProperties
    from schorg.VirtualLocation import VirtualLocationProperties
    from schorg.VirtualLocation import AllProperties
    from schorg.VirtualLocation import create_schema_org_model
    from schorg.VirtualLocation import VirtualLocation

    a = create_schema_org_model(type_=VirtualLocationInheritedProperties)
    b = create_schema_org_model(type_=VirtualLocationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    VirtualLocation.schema()


def EntertainmentBusiness_test():
    from schorg.EntertainmentBusiness import EntertainmentBusinessInheritedProperties
    from schorg.EntertainmentBusiness import EntertainmentBusinessProperties
    from schorg.EntertainmentBusiness import AllProperties
    from schorg.EntertainmentBusiness import create_schema_org_model
    from schorg.EntertainmentBusiness import EntertainmentBusiness

    a = create_schema_org_model(type_=EntertainmentBusinessInheritedProperties)
    b = create_schema_org_model(type_=EntertainmentBusinessProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    EntertainmentBusiness.schema()


def AdultEntertainment_test():
    from schorg.AdultEntertainment import AdultEntertainmentInheritedProperties
    from schorg.AdultEntertainment import AdultEntertainmentProperties
    from schorg.AdultEntertainment import AllProperties
    from schorg.AdultEntertainment import create_schema_org_model
    from schorg.AdultEntertainment import AdultEntertainment

    a = create_schema_org_model(type_=AdultEntertainmentInheritedProperties)
    b = create_schema_org_model(type_=AdultEntertainmentProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    AdultEntertainment.schema()


def Review_test():
    from schorg.Review import ReviewInheritedProperties
    from schorg.Review import ReviewProperties
    from schorg.Review import AllProperties
    from schorg.Review import create_schema_org_model
    from schorg.Review import Review

    a = create_schema_org_model(type_=ReviewInheritedProperties)
    b = create_schema_org_model(type_=ReviewProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Review.schema()


def Recommendation_test():
    from schorg.Recommendation import RecommendationInheritedProperties
    from schorg.Recommendation import RecommendationProperties
    from schorg.Recommendation import AllProperties
    from schorg.Recommendation import create_schema_org_model
    from schorg.Recommendation import Recommendation

    a = create_schema_org_model(type_=RecommendationInheritedProperties)
    b = create_schema_org_model(type_=RecommendationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Recommendation.schema()


def MediaObject_test():
    from schorg.MediaObject import MediaObjectInheritedProperties
    from schorg.MediaObject import MediaObjectProperties
    from schorg.MediaObject import AllProperties
    from schorg.MediaObject import create_schema_org_model
    from schorg.MediaObject import MediaObject

    a = create_schema_org_model(type_=MediaObjectInheritedProperties)
    b = create_schema_org_model(type_=MediaObjectProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MediaObject.schema()


def AudioObject_test():
    from schorg.AudioObject import AudioObjectInheritedProperties
    from schorg.AudioObject import AudioObjectProperties
    from schorg.AudioObject import AllProperties
    from schorg.AudioObject import create_schema_org_model
    from schorg.AudioObject import AudioObject

    a = create_schema_org_model(type_=AudioObjectInheritedProperties)
    b = create_schema_org_model(type_=AudioObjectProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    AudioObject.schema()


def Book_test():
    from schorg.Book import BookInheritedProperties
    from schorg.Book import BookProperties
    from schorg.Book import AllProperties
    from schorg.Book import create_schema_org_model
    from schorg.Book import Book

    a = create_schema_org_model(type_=BookInheritedProperties)
    b = create_schema_org_model(type_=BookProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Book.schema()


def Audiobook_test():
    from schorg.Audiobook import AudiobookInheritedProperties
    from schorg.Audiobook import AudiobookProperties
    from schorg.Audiobook import AllProperties
    from schorg.Audiobook import create_schema_org_model
    from schorg.Audiobook import Audiobook

    a = create_schema_org_model(type_=AudiobookInheritedProperties)
    b = create_schema_org_model(type_=AudiobookProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Audiobook.schema()


def Person_test():
    from schorg.Person import PersonInheritedProperties
    from schorg.Person import PersonProperties
    from schorg.Person import AllProperties
    from schorg.Person import create_schema_org_model
    from schorg.Person import Person

    a = create_schema_org_model(type_=PersonInheritedProperties)
    b = create_schema_org_model(type_=PersonProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Person.schema()


def MedicalAudience_test():
    from schorg.MedicalAudience import MedicalAudienceInheritedProperties
    from schorg.MedicalAudience import MedicalAudienceProperties
    from schorg.MedicalAudience import AllProperties
    from schorg.MedicalAudience import create_schema_org_model
    from schorg.MedicalAudience import MedicalAudience

    a = create_schema_org_model(type_=MedicalAudienceInheritedProperties)
    b = create_schema_org_model(type_=MedicalAudienceProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MedicalAudience.schema()


def Patient_test():
    from schorg.Patient import PatientInheritedProperties
    from schorg.Patient import PatientProperties
    from schorg.Patient import AllProperties
    from schorg.Patient import create_schema_org_model
    from schorg.Patient import Patient

    a = create_schema_org_model(type_=PatientInheritedProperties)
    b = create_schema_org_model(type_=PatientProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Patient.schema()


def GovernmentBenefitsType_test():
    from schorg.GovernmentBenefitsType import GovernmentBenefitsTypeInheritedProperties
    from schorg.GovernmentBenefitsType import GovernmentBenefitsTypeProperties
    from schorg.GovernmentBenefitsType import AllProperties
    from schorg.GovernmentBenefitsType import create_schema_org_model
    from schorg.GovernmentBenefitsType import GovernmentBenefitsType

    a = create_schema_org_model(type_=GovernmentBenefitsTypeInheritedProperties)
    b = create_schema_org_model(type_=GovernmentBenefitsTypeProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    GovernmentBenefitsType.schema()


def BusinessSupport_test():
    from schorg.BusinessSupport import BusinessSupportInheritedProperties
    from schorg.BusinessSupport import BusinessSupportProperties
    from schorg.BusinessSupport import AllProperties
    from schorg.BusinessSupport import create_schema_org_model
    from schorg.BusinessSupport import BusinessSupport

    a = create_schema_org_model(type_=BusinessSupportInheritedProperties)
    b = create_schema_org_model(type_=BusinessSupportProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    BusinessSupport.schema()


def SatireOrParodyContent_test():
    from schorg.SatireOrParodyContent import SatireOrParodyContentInheritedProperties
    from schorg.SatireOrParodyContent import SatireOrParodyContentProperties
    from schorg.SatireOrParodyContent import AllProperties
    from schorg.SatireOrParodyContent import create_schema_org_model
    from schorg.SatireOrParodyContent import SatireOrParodyContent

    a = create_schema_org_model(type_=SatireOrParodyContentInheritedProperties)
    b = create_schema_org_model(type_=SatireOrParodyContentProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    SatireOrParodyContent.schema()


def Genitourinary_test():
    from schorg.Genitourinary import GenitourinaryInheritedProperties
    from schorg.Genitourinary import GenitourinaryProperties
    from schorg.Genitourinary import AllProperties
    from schorg.Genitourinary import create_schema_org_model
    from schorg.Genitourinary import Genitourinary

    a = create_schema_org_model(type_=GenitourinaryInheritedProperties)
    b = create_schema_org_model(type_=GenitourinaryProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Genitourinary.schema()


def Collection_test():
    from schorg.Collection import CollectionInheritedProperties
    from schorg.Collection import CollectionProperties
    from schorg.Collection import AllProperties
    from schorg.Collection import create_schema_org_model
    from schorg.Collection import Collection

    a = create_schema_org_model(type_=CollectionInheritedProperties)
    b = create_schema_org_model(type_=CollectionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Collection.schema()


def ProductCollection_test():
    from schorg.ProductCollection import ProductCollectionInheritedProperties
    from schorg.ProductCollection import ProductCollectionProperties
    from schorg.ProductCollection import AllProperties
    from schorg.ProductCollection import create_schema_org_model
    from schorg.ProductCollection import ProductCollection

    a = create_schema_org_model(type_=ProductCollectionInheritedProperties)
    b = create_schema_org_model(type_=ProductCollectionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ProductCollection.schema()


def Role_test():
    from schorg.Role import RoleInheritedProperties
    from schorg.Role import RoleProperties
    from schorg.Role import AllProperties
    from schorg.Role import create_schema_org_model
    from schorg.Role import Role

    a = create_schema_org_model(type_=RoleInheritedProperties)
    b = create_schema_org_model(type_=RoleProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Role.schema()


def OrganizationRole_test():
    from schorg.OrganizationRole import OrganizationRoleInheritedProperties
    from schorg.OrganizationRole import OrganizationRoleProperties
    from schorg.OrganizationRole import AllProperties
    from schorg.OrganizationRole import create_schema_org_model
    from schorg.OrganizationRole import OrganizationRole

    a = create_schema_org_model(type_=OrganizationRoleInheritedProperties)
    b = create_schema_org_model(type_=OrganizationRoleProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    OrganizationRole.schema()


def FindAction_test():
    from schorg.FindAction import FindActionInheritedProperties
    from schorg.FindAction import FindActionProperties
    from schorg.FindAction import AllProperties
    from schorg.FindAction import create_schema_org_model
    from schorg.FindAction import FindAction

    a = create_schema_org_model(type_=FindActionInheritedProperties)
    b = create_schema_org_model(type_=FindActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    FindAction.schema()


def GeoCircle_test():
    from schorg.GeoCircle import GeoCircleInheritedProperties
    from schorg.GeoCircle import GeoCircleProperties
    from schorg.GeoCircle import AllProperties
    from schorg.GeoCircle import create_schema_org_model
    from schorg.GeoCircle import GeoCircle

    a = create_schema_org_model(type_=GeoCircleInheritedProperties)
    b = create_schema_org_model(type_=GeoCircleProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    GeoCircle.schema()


def SportsActivityLocation_test():
    from schorg.SportsActivityLocation import SportsActivityLocationInheritedProperties
    from schorg.SportsActivityLocation import SportsActivityLocationProperties
    from schorg.SportsActivityLocation import AllProperties
    from schorg.SportsActivityLocation import create_schema_org_model
    from schorg.SportsActivityLocation import SportsActivityLocation

    a = create_schema_org_model(type_=SportsActivityLocationInheritedProperties)
    b = create_schema_org_model(type_=SportsActivityLocationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    SportsActivityLocation.schema()


def Room_test():
    from schorg.Room import RoomInheritedProperties
    from schorg.Room import RoomProperties
    from schorg.Room import AllProperties
    from schorg.Room import create_schema_org_model
    from schorg.Room import Room

    a = create_schema_org_model(type_=RoomInheritedProperties)
    b = create_schema_org_model(type_=RoomProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Room.schema()


def MeetingRoom_test():
    from schorg.MeetingRoom import MeetingRoomInheritedProperties
    from schorg.MeetingRoom import MeetingRoomProperties
    from schorg.MeetingRoom import AllProperties
    from schorg.MeetingRoom import create_schema_org_model
    from schorg.MeetingRoom import MeetingRoom

    a = create_schema_org_model(type_=MeetingRoomInheritedProperties)
    b = create_schema_org_model(type_=MeetingRoomProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MeetingRoom.schema()


def UKNonprofitType_test():
    from schorg.UKNonprofitType import UKNonprofitTypeInheritedProperties
    from schorg.UKNonprofitType import UKNonprofitTypeProperties
    from schorg.UKNonprofitType import AllProperties
    from schorg.UKNonprofitType import create_schema_org_model
    from schorg.UKNonprofitType import UKNonprofitType

    a = create_schema_org_model(type_=UKNonprofitTypeInheritedProperties)
    b = create_schema_org_model(type_=UKNonprofitTypeProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    UKNonprofitType.schema()


def Trip_test():
    from schorg.Trip import TripInheritedProperties
    from schorg.Trip import TripProperties
    from schorg.Trip import AllProperties
    from schorg.Trip import create_schema_org_model
    from schorg.Trip import Trip

    a = create_schema_org_model(type_=TripInheritedProperties)
    b = create_schema_org_model(type_=TripProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Trip.schema()


def BoatTrip_test():
    from schorg.BoatTrip import BoatTripInheritedProperties
    from schorg.BoatTrip import BoatTripProperties
    from schorg.BoatTrip import AllProperties
    from schorg.BoatTrip import create_schema_org_model
    from schorg.BoatTrip import BoatTrip

    a = create_schema_org_model(type_=BoatTripInheritedProperties)
    b = create_schema_org_model(type_=BoatTripProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    BoatTrip.schema()


def EmployeeRole_test():
    from schorg.EmployeeRole import EmployeeRoleInheritedProperties
    from schorg.EmployeeRole import EmployeeRoleProperties
    from schorg.EmployeeRole import AllProperties
    from schorg.EmployeeRole import create_schema_org_model
    from schorg.EmployeeRole import EmployeeRole

    a = create_schema_org_model(type_=EmployeeRoleInheritedProperties)
    b = create_schema_org_model(type_=EmployeeRoleProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    EmployeeRole.schema()


def BookStore_test():
    from schorg.BookStore import BookStoreInheritedProperties
    from schorg.BookStore import BookStoreProperties
    from schorg.BookStore import AllProperties
    from schorg.BookStore import create_schema_org_model
    from schorg.BookStore import BookStore

    a = create_schema_org_model(type_=BookStoreInheritedProperties)
    b = create_schema_org_model(type_=BookStoreProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    BookStore.schema()


def Gastroenterologic_test():
    from schorg.Gastroenterologic import GastroenterologicInheritedProperties
    from schorg.Gastroenterologic import GastroenterologicProperties
    from schorg.Gastroenterologic import AllProperties
    from schorg.Gastroenterologic import create_schema_org_model
    from schorg.Gastroenterologic import Gastroenterologic

    a = create_schema_org_model(type_=GastroenterologicInheritedProperties)
    b = create_schema_org_model(type_=GastroenterologicProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Gastroenterologic.schema()


def UpdateAction_test():
    from schorg.UpdateAction import UpdateActionInheritedProperties
    from schorg.UpdateAction import UpdateActionProperties
    from schorg.UpdateAction import AllProperties
    from schorg.UpdateAction import create_schema_org_model
    from schorg.UpdateAction import UpdateAction

    a = create_schema_org_model(type_=UpdateActionInheritedProperties)
    b = create_schema_org_model(type_=UpdateActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    UpdateAction.schema()


def SoftwareApplication_test():
    from schorg.SoftwareApplication import SoftwareApplicationInheritedProperties
    from schorg.SoftwareApplication import SoftwareApplicationProperties
    from schorg.SoftwareApplication import AllProperties
    from schorg.SoftwareApplication import create_schema_org_model
    from schorg.SoftwareApplication import SoftwareApplication

    a = create_schema_org_model(type_=SoftwareApplicationInheritedProperties)
    b = create_schema_org_model(type_=SoftwareApplicationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    SoftwareApplication.schema()


def MobileApplication_test():
    from schorg.MobileApplication import MobileApplicationInheritedProperties
    from schorg.MobileApplication import MobileApplicationProperties
    from schorg.MobileApplication import AllProperties
    from schorg.MobileApplication import create_schema_org_model
    from schorg.MobileApplication import MobileApplication

    a = create_schema_org_model(type_=MobileApplicationInheritedProperties)
    b = create_schema_org_model(type_=MobileApplicationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MobileApplication.schema()


def DiagnosticProcedure_test():
    from schorg.DiagnosticProcedure import DiagnosticProcedureInheritedProperties
    from schorg.DiagnosticProcedure import DiagnosticProcedureProperties
    from schorg.DiagnosticProcedure import AllProperties
    from schorg.DiagnosticProcedure import create_schema_org_model
    from schorg.DiagnosticProcedure import DiagnosticProcedure

    a = create_schema_org_model(type_=DiagnosticProcedureInheritedProperties)
    b = create_schema_org_model(type_=DiagnosticProcedureProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    DiagnosticProcedure.schema()


def LegalService_test():
    from schorg.LegalService import LegalServiceInheritedProperties
    from schorg.LegalService import LegalServiceProperties
    from schorg.LegalService import AllProperties
    from schorg.LegalService import create_schema_org_model
    from schorg.LegalService import LegalService

    a = create_schema_org_model(type_=LegalServiceInheritedProperties)
    b = create_schema_org_model(type_=LegalServiceProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    LegalService.schema()


def Attorney_test():
    from schorg.Attorney import AttorneyInheritedProperties
    from schorg.Attorney import AttorneyProperties
    from schorg.Attorney import AllProperties
    from schorg.Attorney import create_schema_org_model
    from schorg.Attorney import Attorney

    a = create_schema_org_model(type_=AttorneyInheritedProperties)
    b = create_schema_org_model(type_=AttorneyProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Attorney.schema()


def EUEnergyEfficiencyCategoryA_test():
    from schorg.EUEnergyEfficiencyCategoryA import EUEnergyEfficiencyCategoryAInheritedProperties
    from schorg.EUEnergyEfficiencyCategoryA import EUEnergyEfficiencyCategoryAProperties
    from schorg.EUEnergyEfficiencyCategoryA import AllProperties
    from schorg.EUEnergyEfficiencyCategoryA import create_schema_org_model
    from schorg.EUEnergyEfficiencyCategoryA import EUEnergyEfficiencyCategoryA

    a = create_schema_org_model(type_=EUEnergyEfficiencyCategoryAInheritedProperties)
    b = create_schema_org_model(type_=EUEnergyEfficiencyCategoryAProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    EUEnergyEfficiencyCategoryA.schema()


def BloodTest_test():
    from schorg.BloodTest import BloodTestInheritedProperties
    from schorg.BloodTest import BloodTestProperties
    from schorg.BloodTest import AllProperties
    from schorg.BloodTest import create_schema_org_model
    from schorg.BloodTest import BloodTest

    a = create_schema_org_model(type_=BloodTestInheritedProperties)
    b = create_schema_org_model(type_=BloodTestProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    BloodTest.schema()


def RadioStation_test():
    from schorg.RadioStation import RadioStationInheritedProperties
    from schorg.RadioStation import RadioStationProperties
    from schorg.RadioStation import AllProperties
    from schorg.RadioStation import create_schema_org_model
    from schorg.RadioStation import RadioStation

    a = create_schema_org_model(type_=RadioStationInheritedProperties)
    b = create_schema_org_model(type_=RadioStationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    RadioStation.schema()


def ComputerStore_test():
    from schorg.ComputerStore import ComputerStoreInheritedProperties
    from schorg.ComputerStore import ComputerStoreProperties
    from schorg.ComputerStore import AllProperties
    from schorg.ComputerStore import create_schema_org_model
    from schorg.ComputerStore import ComputerStore

    a = create_schema_org_model(type_=ComputerStoreInheritedProperties)
    b = create_schema_org_model(type_=ComputerStoreProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ComputerStore.schema()


def RentalCarReservation_test():
    from schorg.RentalCarReservation import RentalCarReservationInheritedProperties
    from schorg.RentalCarReservation import RentalCarReservationProperties
    from schorg.RentalCarReservation import AllProperties
    from schorg.RentalCarReservation import create_schema_org_model
    from schorg.RentalCarReservation import RentalCarReservation

    a = create_schema_org_model(type_=RentalCarReservationInheritedProperties)
    b = create_schema_org_model(type_=RentalCarReservationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    RentalCarReservation.schema()


def ItemList_test():
    from schorg.ItemList import ItemListInheritedProperties
    from schorg.ItemList import ItemListProperties
    from schorg.ItemList import AllProperties
    from schorg.ItemList import create_schema_org_model
    from schorg.ItemList import ItemList

    a = create_schema_org_model(type_=ItemListInheritedProperties)
    b = create_schema_org_model(type_=ItemListProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ItemList.schema()


def CausesHealthAspect_test():
    from schorg.CausesHealthAspect import CausesHealthAspectInheritedProperties
    from schorg.CausesHealthAspect import CausesHealthAspectProperties
    from schorg.CausesHealthAspect import AllProperties
    from schorg.CausesHealthAspect import create_schema_org_model
    from schorg.CausesHealthAspect import CausesHealthAspect

    a = create_schema_org_model(type_=CausesHealthAspectInheritedProperties)
    b = create_schema_org_model(type_=CausesHealthAspectProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    CausesHealthAspect.schema()


def RestrictedDiet_test():
    from schorg.RestrictedDiet import RestrictedDietInheritedProperties
    from schorg.RestrictedDiet import RestrictedDietProperties
    from schorg.RestrictedDiet import AllProperties
    from schorg.RestrictedDiet import create_schema_org_model
    from schorg.RestrictedDiet import RestrictedDiet

    a = create_schema_org_model(type_=RestrictedDietInheritedProperties)
    b = create_schema_org_model(type_=RestrictedDietProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    RestrictedDiet.schema()


def VegetarianDiet_test():
    from schorg.VegetarianDiet import VegetarianDietInheritedProperties
    from schorg.VegetarianDiet import VegetarianDietProperties
    from schorg.VegetarianDiet import AllProperties
    from schorg.VegetarianDiet import create_schema_org_model
    from schorg.VegetarianDiet import VegetarianDiet

    a = create_schema_org_model(type_=VegetarianDietInheritedProperties)
    b = create_schema_org_model(type_=VegetarianDietProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    VegetarianDiet.schema()


def MerchantReturnPolicySeasonalOverride_test():
    from schorg.MerchantReturnPolicySeasonalOverride import MerchantReturnPolicySeasonalOverrideInheritedProperties
    from schorg.MerchantReturnPolicySeasonalOverride import MerchantReturnPolicySeasonalOverrideProperties
    from schorg.MerchantReturnPolicySeasonalOverride import AllProperties
    from schorg.MerchantReturnPolicySeasonalOverride import create_schema_org_model
    from schorg.MerchantReturnPolicySeasonalOverride import MerchantReturnPolicySeasonalOverride

    a = create_schema_org_model(type_=MerchantReturnPolicySeasonalOverrideInheritedProperties)
    b = create_schema_org_model(type_=MerchantReturnPolicySeasonalOverrideProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MerchantReturnPolicySeasonalOverride.schema()


def RearWheelDriveConfiguration_test():
    from schorg.RearWheelDriveConfiguration import RearWheelDriveConfigurationInheritedProperties
    from schorg.RearWheelDriveConfiguration import RearWheelDriveConfigurationProperties
    from schorg.RearWheelDriveConfiguration import AllProperties
    from schorg.RearWheelDriveConfiguration import create_schema_org_model
    from schorg.RearWheelDriveConfiguration import RearWheelDriveConfiguration

    a = create_schema_org_model(type_=RearWheelDriveConfigurationInheritedProperties)
    b = create_schema_org_model(type_=RearWheelDriveConfigurationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    RearWheelDriveConfiguration.schema()


def ContactPointOption_test():
    from schorg.ContactPointOption import ContactPointOptionInheritedProperties
    from schorg.ContactPointOption import ContactPointOptionProperties
    from schorg.ContactPointOption import AllProperties
    from schorg.ContactPointOption import create_schema_org_model
    from schorg.ContactPointOption import ContactPointOption

    a = create_schema_org_model(type_=ContactPointOptionInheritedProperties)
    b = create_schema_org_model(type_=ContactPointOptionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ContactPointOption.schema()


def IgnoreAction_test():
    from schorg.IgnoreAction import IgnoreActionInheritedProperties
    from schorg.IgnoreAction import IgnoreActionProperties
    from schorg.IgnoreAction import AllProperties
    from schorg.IgnoreAction import create_schema_org_model
    from schorg.IgnoreAction import IgnoreAction

    a = create_schema_org_model(type_=IgnoreActionInheritedProperties)
    b = create_schema_org_model(type_=IgnoreActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    IgnoreAction.schema()


def UserCheckins_test():
    from schorg.UserCheckins import UserCheckinsInheritedProperties
    from schorg.UserCheckins import UserCheckinsProperties
    from schorg.UserCheckins import AllProperties
    from schorg.UserCheckins import create_schema_org_model
    from schorg.UserCheckins import UserCheckins

    a = create_schema_org_model(type_=UserCheckinsInheritedProperties)
    b = create_schema_org_model(type_=UserCheckinsProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    UserCheckins.schema()


def MoveAction_test():
    from schorg.MoveAction import MoveActionInheritedProperties
    from schorg.MoveAction import MoveActionProperties
    from schorg.MoveAction import AllProperties
    from schorg.MoveAction import create_schema_org_model
    from schorg.MoveAction import MoveAction

    a = create_schema_org_model(type_=MoveActionInheritedProperties)
    b = create_schema_org_model(type_=MoveActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MoveAction.schema()


def ArriveAction_test():
    from schorg.ArriveAction import ArriveActionInheritedProperties
    from schorg.ArriveAction import ArriveActionProperties
    from schorg.ArriveAction import AllProperties
    from schorg.ArriveAction import create_schema_org_model
    from schorg.ArriveAction import ArriveAction

    a = create_schema_org_model(type_=ArriveActionInheritedProperties)
    b = create_schema_org_model(type_=ArriveActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ArriveAction.schema()


def RecyclingCenter_test():
    from schorg.RecyclingCenter import RecyclingCenterInheritedProperties
    from schorg.RecyclingCenter import RecyclingCenterProperties
    from schorg.RecyclingCenter import AllProperties
    from schorg.RecyclingCenter import create_schema_org_model
    from schorg.RecyclingCenter import RecyclingCenter

    a = create_schema_org_model(type_=RecyclingCenterInheritedProperties)
    b = create_schema_org_model(type_=RecyclingCenterProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    RecyclingCenter.schema()


def HomeAndConstructionBusiness_test():
    from schorg.HomeAndConstructionBusiness import HomeAndConstructionBusinessInheritedProperties
    from schorg.HomeAndConstructionBusiness import HomeAndConstructionBusinessProperties
    from schorg.HomeAndConstructionBusiness import AllProperties
    from schorg.HomeAndConstructionBusiness import create_schema_org_model
    from schorg.HomeAndConstructionBusiness import HomeAndConstructionBusiness

    a = create_schema_org_model(type_=HomeAndConstructionBusinessInheritedProperties)
    b = create_schema_org_model(type_=HomeAndConstructionBusinessProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    HomeAndConstructionBusiness.schema()


def RoofingContractor_test():
    from schorg.RoofingContractor import RoofingContractorInheritedProperties
    from schorg.RoofingContractor import RoofingContractorProperties
    from schorg.RoofingContractor import AllProperties
    from schorg.RoofingContractor import create_schema_org_model
    from schorg.RoofingContractor import RoofingContractor

    a = create_schema_org_model(type_=RoofingContractorInheritedProperties)
    b = create_schema_org_model(type_=RoofingContractorProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    RoofingContractor.schema()


def WearableMeasurementLength_test():
    from schorg.WearableMeasurementLength import WearableMeasurementLengthInheritedProperties
    from schorg.WearableMeasurementLength import WearableMeasurementLengthProperties
    from schorg.WearableMeasurementLength import AllProperties
    from schorg.WearableMeasurementLength import create_schema_org_model
    from schorg.WearableMeasurementLength import WearableMeasurementLength

    a = create_schema_org_model(type_=WearableMeasurementLengthInheritedProperties)
    b = create_schema_org_model(type_=WearableMeasurementLengthProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    WearableMeasurementLength.schema()


def ReservationConfirmed_test():
    from schorg.ReservationConfirmed import ReservationConfirmedInheritedProperties
    from schorg.ReservationConfirmed import ReservationConfirmedProperties
    from schorg.ReservationConfirmed import AllProperties
    from schorg.ReservationConfirmed import create_schema_org_model
    from schorg.ReservationConfirmed import ReservationConfirmed

    a = create_schema_org_model(type_=ReservationConfirmedInheritedProperties)
    b = create_schema_org_model(type_=ReservationConfirmedProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ReservationConfirmed.schema()


def EUEnergyEfficiencyCategoryC_test():
    from schorg.EUEnergyEfficiencyCategoryC import EUEnergyEfficiencyCategoryCInheritedProperties
    from schorg.EUEnergyEfficiencyCategoryC import EUEnergyEfficiencyCategoryCProperties
    from schorg.EUEnergyEfficiencyCategoryC import AllProperties
    from schorg.EUEnergyEfficiencyCategoryC import create_schema_org_model
    from schorg.EUEnergyEfficiencyCategoryC import EUEnergyEfficiencyCategoryC

    a = create_schema_org_model(type_=EUEnergyEfficiencyCategoryCInheritedProperties)
    b = create_schema_org_model(type_=EUEnergyEfficiencyCategoryCProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    EUEnergyEfficiencyCategoryC.schema()


def GeoCoordinates_test():
    from schorg.GeoCoordinates import GeoCoordinatesInheritedProperties
    from schorg.GeoCoordinates import GeoCoordinatesProperties
    from schorg.GeoCoordinates import AllProperties
    from schorg.GeoCoordinates import create_schema_org_model
    from schorg.GeoCoordinates import GeoCoordinates

    a = create_schema_org_model(type_=GeoCoordinatesInheritedProperties)
    b = create_schema_org_model(type_=GeoCoordinatesProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    GeoCoordinates.schema()


def PriceTypeEnumeration_test():
    from schorg.PriceTypeEnumeration import PriceTypeEnumerationInheritedProperties
    from schorg.PriceTypeEnumeration import PriceTypeEnumerationProperties
    from schorg.PriceTypeEnumeration import AllProperties
    from schorg.PriceTypeEnumeration import create_schema_org_model
    from schorg.PriceTypeEnumeration import PriceTypeEnumeration

    a = create_schema_org_model(type_=PriceTypeEnumerationInheritedProperties)
    b = create_schema_org_model(type_=PriceTypeEnumerationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    PriceTypeEnumeration.schema()


def SRP_test():
    from schorg.SRP import SRPInheritedProperties
    from schorg.SRP import SRPProperties
    from schorg.SRP import AllProperties
    from schorg.SRP import create_schema_org_model
    from schorg.SRP import SRP

    a = create_schema_org_model(type_=SRPInheritedProperties)
    b = create_schema_org_model(type_=SRPProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    SRP.schema()


def TaxiStand_test():
    from schorg.TaxiStand import TaxiStandInheritedProperties
    from schorg.TaxiStand import TaxiStandProperties
    from schorg.TaxiStand import AllProperties
    from schorg.TaxiStand import create_schema_org_model
    from schorg.TaxiStand import TaxiStand

    a = create_schema_org_model(type_=TaxiStandInheritedProperties)
    b = create_schema_org_model(type_=TaxiStandProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    TaxiStand.schema()


def Nonprofit501c2_test():
    from schorg.Nonprofit501c2 import Nonprofit501c2InheritedProperties
    from schorg.Nonprofit501c2 import Nonprofit501c2Properties
    from schorg.Nonprofit501c2 import AllProperties
    from schorg.Nonprofit501c2 import create_schema_org_model
    from schorg.Nonprofit501c2 import Nonprofit501c2

    a = create_schema_org_model(type_=Nonprofit501c2InheritedProperties)
    b = create_schema_org_model(type_=Nonprofit501c2Properties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Nonprofit501c2.schema()


def ClothingStore_test():
    from schorg.ClothingStore import ClothingStoreInheritedProperties
    from schorg.ClothingStore import ClothingStoreProperties
    from schorg.ClothingStore import AllProperties
    from schorg.ClothingStore import create_schema_org_model
    from schorg.ClothingStore import ClothingStore

    a = create_schema_org_model(type_=ClothingStoreInheritedProperties)
    b = create_schema_org_model(type_=ClothingStoreProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ClothingStore.schema()


def VideoObject_test():
    from schorg.VideoObject import VideoObjectInheritedProperties
    from schorg.VideoObject import VideoObjectProperties
    from schorg.VideoObject import AllProperties
    from schorg.VideoObject import create_schema_org_model
    from schorg.VideoObject import VideoObject

    a = create_schema_org_model(type_=VideoObjectInheritedProperties)
    b = create_schema_org_model(type_=VideoObjectProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    VideoObject.schema()


def VideoObjectSnapshot_test():
    from schorg.VideoObjectSnapshot import VideoObjectSnapshotInheritedProperties
    from schorg.VideoObjectSnapshot import VideoObjectSnapshotProperties
    from schorg.VideoObjectSnapshot import AllProperties
    from schorg.VideoObjectSnapshot import create_schema_org_model
    from schorg.VideoObjectSnapshot import VideoObjectSnapshot

    a = create_schema_org_model(type_=VideoObjectSnapshotInheritedProperties)
    b = create_schema_org_model(type_=VideoObjectSnapshotProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    VideoObjectSnapshot.schema()


def OverviewHealthAspect_test():
    from schorg.OverviewHealthAspect import OverviewHealthAspectInheritedProperties
    from schorg.OverviewHealthAspect import OverviewHealthAspectProperties
    from schorg.OverviewHealthAspect import AllProperties
    from schorg.OverviewHealthAspect import create_schema_org_model
    from schorg.OverviewHealthAspect import OverviewHealthAspect

    a = create_schema_org_model(type_=OverviewHealthAspectInheritedProperties)
    b = create_schema_org_model(type_=OverviewHealthAspectProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    OverviewHealthAspect.schema()


def Guide_test():
    from schorg.Guide import GuideInheritedProperties
    from schorg.Guide import GuideProperties
    from schorg.Guide import AllProperties
    from schorg.Guide import create_schema_org_model
    from schorg.Guide import Guide

    a = create_schema_org_model(type_=GuideInheritedProperties)
    b = create_schema_org_model(type_=GuideProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Guide.schema()


def TransferAction_test():
    from schorg.TransferAction import TransferActionInheritedProperties
    from schorg.TransferAction import TransferActionProperties
    from schorg.TransferAction import AllProperties
    from schorg.TransferAction import create_schema_org_model
    from schorg.TransferAction import TransferAction

    a = create_schema_org_model(type_=TransferActionInheritedProperties)
    b = create_schema_org_model(type_=TransferActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    TransferAction.schema()


def MoneyTransfer_test():
    from schorg.MoneyTransfer import MoneyTransferInheritedProperties
    from schorg.MoneyTransfer import MoneyTransferProperties
    from schorg.MoneyTransfer import AllProperties
    from schorg.MoneyTransfer import create_schema_org_model
    from schorg.MoneyTransfer import MoneyTransfer

    a = create_schema_org_model(type_=MoneyTransferInheritedProperties)
    b = create_schema_org_model(type_=MoneyTransferProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MoneyTransfer.schema()


def Festival_test():
    from schorg.Festival import FestivalInheritedProperties
    from schorg.Festival import FestivalProperties
    from schorg.Festival import AllProperties
    from schorg.Festival import create_schema_org_model
    from schorg.Festival import Festival

    a = create_schema_org_model(type_=FestivalInheritedProperties)
    b = create_schema_org_model(type_=FestivalProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Festival.schema()


def Endocrine_test():
    from schorg.Endocrine import EndocrineInheritedProperties
    from schorg.Endocrine import EndocrineProperties
    from schorg.Endocrine import AllProperties
    from schorg.Endocrine import create_schema_org_model
    from schorg.Endocrine import Endocrine

    a = create_schema_org_model(type_=EndocrineInheritedProperties)
    b = create_schema_org_model(type_=EndocrineProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Endocrine.schema()


def WearableMeasurementOutsideLeg_test():
    from schorg.WearableMeasurementOutsideLeg import WearableMeasurementOutsideLegInheritedProperties
    from schorg.WearableMeasurementOutsideLeg import WearableMeasurementOutsideLegProperties
    from schorg.WearableMeasurementOutsideLeg import AllProperties
    from schorg.WearableMeasurementOutsideLeg import create_schema_org_model
    from schorg.WearableMeasurementOutsideLeg import WearableMeasurementOutsideLeg

    a = create_schema_org_model(type_=WearableMeasurementOutsideLegInheritedProperties)
    b = create_schema_org_model(type_=WearableMeasurementOutsideLegProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    WearableMeasurementOutsideLeg.schema()


def MusicAlbum_test():
    from schorg.MusicAlbum import MusicAlbumInheritedProperties
    from schorg.MusicAlbum import MusicAlbumProperties
    from schorg.MusicAlbum import AllProperties
    from schorg.MusicAlbum import create_schema_org_model
    from schorg.MusicAlbum import MusicAlbum

    a = create_schema_org_model(type_=MusicAlbumInheritedProperties)
    b = create_schema_org_model(type_=MusicAlbumProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MusicAlbum.schema()


def Article_test():
    from schorg.Article import ArticleInheritedProperties
    from schorg.Article import ArticleProperties
    from schorg.Article import AllProperties
    from schorg.Article import create_schema_org_model
    from schorg.Article import Article

    a = create_schema_org_model(type_=ArticleInheritedProperties)
    b = create_schema_org_model(type_=ArticleProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Article.schema()


def NewsArticle_test():
    from schorg.NewsArticle import NewsArticleInheritedProperties
    from schorg.NewsArticle import NewsArticleProperties
    from schorg.NewsArticle import AllProperties
    from schorg.NewsArticle import create_schema_org_model
    from schorg.NewsArticle import NewsArticle

    a = create_schema_org_model(type_=NewsArticleInheritedProperties)
    b = create_schema_org_model(type_=NewsArticleProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    NewsArticle.schema()


def AskPublicNewsArticle_test():
    from schorg.AskPublicNewsArticle import AskPublicNewsArticleInheritedProperties
    from schorg.AskPublicNewsArticle import AskPublicNewsArticleProperties
    from schorg.AskPublicNewsArticle import AllProperties
    from schorg.AskPublicNewsArticle import create_schema_org_model
    from schorg.AskPublicNewsArticle import AskPublicNewsArticle

    a = create_schema_org_model(type_=AskPublicNewsArticleInheritedProperties)
    b = create_schema_org_model(type_=AskPublicNewsArticleProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    AskPublicNewsArticle.schema()


def ServiceChannel_test():
    from schorg.ServiceChannel import ServiceChannelInheritedProperties
    from schorg.ServiceChannel import ServiceChannelProperties
    from schorg.ServiceChannel import AllProperties
    from schorg.ServiceChannel import create_schema_org_model
    from schorg.ServiceChannel import ServiceChannel

    a = create_schema_org_model(type_=ServiceChannelInheritedProperties)
    b = create_schema_org_model(type_=ServiceChannelProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ServiceChannel.schema()


def Saturday_test():
    from schorg.Saturday import SaturdayInheritedProperties
    from schorg.Saturday import SaturdayProperties
    from schorg.Saturday import AllProperties
    from schorg.Saturday import create_schema_org_model
    from schorg.Saturday import Saturday

    a = create_schema_org_model(type_=SaturdayInheritedProperties)
    b = create_schema_org_model(type_=SaturdayProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Saturday.schema()


def OccupationalExperienceRequirements_test():
    from schorg.OccupationalExperienceRequirements import OccupationalExperienceRequirementsInheritedProperties
    from schorg.OccupationalExperienceRequirements import OccupationalExperienceRequirementsProperties
    from schorg.OccupationalExperienceRequirements import AllProperties
    from schorg.OccupationalExperienceRequirements import create_schema_org_model
    from schorg.OccupationalExperienceRequirements import OccupationalExperienceRequirements

    a = create_schema_org_model(type_=OccupationalExperienceRequirementsInheritedProperties)
    b = create_schema_org_model(type_=OccupationalExperienceRequirementsProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    OccupationalExperienceRequirements.schema()


def HealthPlanNetwork_test():
    from schorg.HealthPlanNetwork import HealthPlanNetworkInheritedProperties
    from schorg.HealthPlanNetwork import HealthPlanNetworkProperties
    from schorg.HealthPlanNetwork import AllProperties
    from schorg.HealthPlanNetwork import create_schema_org_model
    from schorg.HealthPlanNetwork import HealthPlanNetwork

    a = create_schema_org_model(type_=HealthPlanNetworkInheritedProperties)
    b = create_schema_org_model(type_=HealthPlanNetworkProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    HealthPlanNetwork.schema()


def TouristTrip_test():
    from schorg.TouristTrip import TouristTripInheritedProperties
    from schorg.TouristTrip import TouristTripProperties
    from schorg.TouristTrip import AllProperties
    from schorg.TouristTrip import create_schema_org_model
    from schorg.TouristTrip import TouristTrip

    a = create_schema_org_model(type_=TouristTripInheritedProperties)
    b = create_schema_org_model(type_=TouristTripProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    TouristTrip.schema()


def SymptomsHealthAspect_test():
    from schorg.SymptomsHealthAspect import SymptomsHealthAspectInheritedProperties
    from schorg.SymptomsHealthAspect import SymptomsHealthAspectProperties
    from schorg.SymptomsHealthAspect import AllProperties
    from schorg.SymptomsHealthAspect import create_schema_org_model
    from schorg.SymptomsHealthAspect import SymptomsHealthAspect

    a = create_schema_org_model(type_=SymptomsHealthAspectInheritedProperties)
    b = create_schema_org_model(type_=SymptomsHealthAspectProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    SymptomsHealthAspect.schema()


def Neuro_test():
    from schorg.Neuro import NeuroInheritedProperties
    from schorg.Neuro import NeuroProperties
    from schorg.Neuro import AllProperties
    from schorg.Neuro import create_schema_org_model
    from schorg.Neuro import Neuro

    a = create_schema_org_model(type_=NeuroInheritedProperties)
    b = create_schema_org_model(type_=NeuroProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Neuro.schema()


def HobbyShop_test():
    from schorg.HobbyShop import HobbyShopInheritedProperties
    from schorg.HobbyShop import HobbyShopProperties
    from schorg.HobbyShop import AllProperties
    from schorg.HobbyShop import create_schema_org_model
    from schorg.HobbyShop import HobbyShop

    a = create_schema_org_model(type_=HobbyShopInheritedProperties)
    b = create_schema_org_model(type_=HobbyShopProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    HobbyShop.schema()


def BodyMeasurementFoot_test():
    from schorg.BodyMeasurementFoot import BodyMeasurementFootInheritedProperties
    from schorg.BodyMeasurementFoot import BodyMeasurementFootProperties
    from schorg.BodyMeasurementFoot import AllProperties
    from schorg.BodyMeasurementFoot import create_schema_org_model
    from schorg.BodyMeasurementFoot import BodyMeasurementFoot

    a = create_schema_org_model(type_=BodyMeasurementFootInheritedProperties)
    b = create_schema_org_model(type_=BodyMeasurementFootProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    BodyMeasurementFoot.schema()


def Casino_test():
    from schorg.Casino import CasinoInheritedProperties
    from schorg.Casino import CasinoProperties
    from schorg.Casino import AllProperties
    from schorg.Casino import create_schema_org_model
    from schorg.Casino import Casino

    a = create_schema_org_model(type_=CasinoInheritedProperties)
    b = create_schema_org_model(type_=CasinoProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Casino.schema()


def SoftwareSourceCode_test():
    from schorg.SoftwareSourceCode import SoftwareSourceCodeInheritedProperties
    from schorg.SoftwareSourceCode import SoftwareSourceCodeProperties
    from schorg.SoftwareSourceCode import AllProperties
    from schorg.SoftwareSourceCode import create_schema_org_model
    from schorg.SoftwareSourceCode import SoftwareSourceCode

    a = create_schema_org_model(type_=SoftwareSourceCodeInheritedProperties)
    b = create_schema_org_model(type_=SoftwareSourceCodeProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    SoftwareSourceCode.schema()


def MultiCenterTrial_test():
    from schorg.MultiCenterTrial import MultiCenterTrialInheritedProperties
    from schorg.MultiCenterTrial import MultiCenterTrialProperties
    from schorg.MultiCenterTrial import AllProperties
    from schorg.MultiCenterTrial import create_schema_org_model
    from schorg.MultiCenterTrial import MultiCenterTrial

    a = create_schema_org_model(type_=MultiCenterTrialInheritedProperties)
    b = create_schema_org_model(type_=MultiCenterTrialProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MultiCenterTrial.schema()


def ItemAvailability_test():
    from schorg.ItemAvailability import ItemAvailabilityInheritedProperties
    from schorg.ItemAvailability import ItemAvailabilityProperties
    from schorg.ItemAvailability import AllProperties
    from schorg.ItemAvailability import create_schema_org_model
    from schorg.ItemAvailability import ItemAvailability

    a = create_schema_org_model(type_=ItemAvailabilityInheritedProperties)
    b = create_schema_org_model(type_=ItemAvailabilityProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ItemAvailability.schema()


def BackOrder_test():
    from schorg.BackOrder import BackOrderInheritedProperties
    from schorg.BackOrder import BackOrderProperties
    from schorg.BackOrder import AllProperties
    from schorg.BackOrder import create_schema_org_model
    from schorg.BackOrder import BackOrder

    a = create_schema_org_model(type_=BackOrderInheritedProperties)
    b = create_schema_org_model(type_=BackOrderProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    BackOrder.schema()


def CreativeWorkSeason_test():
    from schorg.CreativeWorkSeason import CreativeWorkSeasonInheritedProperties
    from schorg.CreativeWorkSeason import CreativeWorkSeasonProperties
    from schorg.CreativeWorkSeason import AllProperties
    from schorg.CreativeWorkSeason import create_schema_org_model
    from schorg.CreativeWorkSeason import CreativeWorkSeason

    a = create_schema_org_model(type_=CreativeWorkSeasonInheritedProperties)
    b = create_schema_org_model(type_=CreativeWorkSeasonProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    CreativeWorkSeason.schema()


def PodcastSeason_test():
    from schorg.PodcastSeason import PodcastSeasonInheritedProperties
    from schorg.PodcastSeason import PodcastSeasonProperties
    from schorg.PodcastSeason import AllProperties
    from schorg.PodcastSeason import create_schema_org_model
    from schorg.PodcastSeason import PodcastSeason

    a = create_schema_org_model(type_=PodcastSeasonInheritedProperties)
    b = create_schema_org_model(type_=PodcastSeasonProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    PodcastSeason.schema()


def EventReservation_test():
    from schorg.EventReservation import EventReservationInheritedProperties
    from schorg.EventReservation import EventReservationProperties
    from schorg.EventReservation import AllProperties
    from schorg.EventReservation import create_schema_org_model
    from schorg.EventReservation import EventReservation

    a = create_schema_org_model(type_=EventReservationInheritedProperties)
    b = create_schema_org_model(type_=EventReservationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    EventReservation.schema()


def MedicalProcedureType_test():
    from schorg.MedicalProcedureType import MedicalProcedureTypeInheritedProperties
    from schorg.MedicalProcedureType import MedicalProcedureTypeProperties
    from schorg.MedicalProcedureType import AllProperties
    from schorg.MedicalProcedureType import create_schema_org_model
    from schorg.MedicalProcedureType import MedicalProcedureType

    a = create_schema_org_model(type_=MedicalProcedureTypeInheritedProperties)
    b = create_schema_org_model(type_=MedicalProcedureTypeProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MedicalProcedureType.schema()


def Rating_test():
    from schorg.Rating import RatingInheritedProperties
    from schorg.Rating import RatingProperties
    from schorg.Rating import AllProperties
    from schorg.Rating import create_schema_org_model
    from schorg.Rating import Rating

    a = create_schema_org_model(type_=RatingInheritedProperties)
    b = create_schema_org_model(type_=RatingProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Rating.schema()


def AggregateRating_test():
    from schorg.AggregateRating import AggregateRatingInheritedProperties
    from schorg.AggregateRating import AggregateRatingProperties
    from schorg.AggregateRating import AllProperties
    from schorg.AggregateRating import create_schema_org_model
    from schorg.AggregateRating import AggregateRating

    a = create_schema_org_model(type_=AggregateRatingInheritedProperties)
    b = create_schema_org_model(type_=AggregateRatingProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    AggregateRating.schema()


def DataDownload_test():
    from schorg.DataDownload import DataDownloadInheritedProperties
    from schorg.DataDownload import DataDownloadProperties
    from schorg.DataDownload import AllProperties
    from schorg.DataDownload import create_schema_org_model
    from schorg.DataDownload import DataDownload

    a = create_schema_org_model(type_=DataDownloadInheritedProperties)
    b = create_schema_org_model(type_=DataDownloadProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    DataDownload.schema()


def MerchantReturnEnumeration_test():
    from schorg.MerchantReturnEnumeration import MerchantReturnEnumerationInheritedProperties
    from schorg.MerchantReturnEnumeration import MerchantReturnEnumerationProperties
    from schorg.MerchantReturnEnumeration import AllProperties
    from schorg.MerchantReturnEnumeration import create_schema_org_model
    from schorg.MerchantReturnEnumeration import MerchantReturnEnumeration

    a = create_schema_org_model(type_=MerchantReturnEnumerationInheritedProperties)
    b = create_schema_org_model(type_=MerchantReturnEnumerationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MerchantReturnEnumeration.schema()


def MerchantReturnUnlimitedWindow_test():
    from schorg.MerchantReturnUnlimitedWindow import MerchantReturnUnlimitedWindowInheritedProperties
    from schorg.MerchantReturnUnlimitedWindow import MerchantReturnUnlimitedWindowProperties
    from schorg.MerchantReturnUnlimitedWindow import AllProperties
    from schorg.MerchantReturnUnlimitedWindow import create_schema_org_model
    from schorg.MerchantReturnUnlimitedWindow import MerchantReturnUnlimitedWindow

    a = create_schema_org_model(type_=MerchantReturnUnlimitedWindowInheritedProperties)
    b = create_schema_org_model(type_=MerchantReturnUnlimitedWindowProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MerchantReturnUnlimitedWindow.schema()


def CreativeWorkSeries_test():
    from schorg.CreativeWorkSeries import CreativeWorkSeriesInheritedProperties
    from schorg.CreativeWorkSeries import CreativeWorkSeriesProperties
    from schorg.CreativeWorkSeries import AllProperties
    from schorg.CreativeWorkSeries import create_schema_org_model
    from schorg.CreativeWorkSeries import CreativeWorkSeries

    a = create_schema_org_model(type_=CreativeWorkSeriesInheritedProperties)
    b = create_schema_org_model(type_=CreativeWorkSeriesProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    CreativeWorkSeries.schema()


def Periodical_test():
    from schorg.Periodical import PeriodicalInheritedProperties
    from schorg.Periodical import PeriodicalProperties
    from schorg.Periodical import AllProperties
    from schorg.Periodical import create_schema_org_model
    from schorg.Periodical import Periodical

    a = create_schema_org_model(type_=PeriodicalInheritedProperties)
    b = create_schema_org_model(type_=PeriodicalProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Periodical.schema()


def ComicSeries_test():
    from schorg.ComicSeries import ComicSeriesInheritedProperties
    from schorg.ComicSeries import ComicSeriesProperties
    from schorg.ComicSeries import AllProperties
    from schorg.ComicSeries import create_schema_org_model
    from schorg.ComicSeries import ComicSeries

    a = create_schema_org_model(type_=ComicSeriesInheritedProperties)
    b = create_schema_org_model(type_=ComicSeriesProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ComicSeries.schema()


def AdultOrientedEnumeration_test():
    from schorg.AdultOrientedEnumeration import AdultOrientedEnumerationInheritedProperties
    from schorg.AdultOrientedEnumeration import AdultOrientedEnumerationProperties
    from schorg.AdultOrientedEnumeration import AllProperties
    from schorg.AdultOrientedEnumeration import create_schema_org_model
    from schorg.AdultOrientedEnumeration import AdultOrientedEnumeration

    a = create_schema_org_model(type_=AdultOrientedEnumerationInheritedProperties)
    b = create_schema_org_model(type_=AdultOrientedEnumerationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    AdultOrientedEnumeration.schema()


def SexualContentConsideration_test():
    from schorg.SexualContentConsideration import SexualContentConsiderationInheritedProperties
    from schorg.SexualContentConsideration import SexualContentConsiderationProperties
    from schorg.SexualContentConsideration import AllProperties
    from schorg.SexualContentConsideration import create_schema_org_model
    from schorg.SexualContentConsideration import SexualContentConsideration

    a = create_schema_org_model(type_=SexualContentConsiderationInheritedProperties)
    b = create_schema_org_model(type_=SexualContentConsiderationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    SexualContentConsideration.schema()


def GovernmentService_test():
    from schorg.GovernmentService import GovernmentServiceInheritedProperties
    from schorg.GovernmentService import GovernmentServiceProperties
    from schorg.GovernmentService import AllProperties
    from schorg.GovernmentService import create_schema_org_model
    from schorg.GovernmentService import GovernmentService

    a = create_schema_org_model(type_=GovernmentServiceInheritedProperties)
    b = create_schema_org_model(type_=GovernmentServiceProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    GovernmentService.schema()


def Landform_test():
    from schorg.Landform import LandformInheritedProperties
    from schorg.Landform import LandformProperties
    from schorg.Landform import AllProperties
    from schorg.Landform import create_schema_org_model
    from schorg.Landform import Landform

    a = create_schema_org_model(type_=LandformInheritedProperties)
    b = create_schema_org_model(type_=LandformProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Landform.schema()


def Continent_test():
    from schorg.Continent import ContinentInheritedProperties
    from schorg.Continent import ContinentProperties
    from schorg.Continent import AllProperties
    from schorg.Continent import create_schema_org_model
    from schorg.Continent import Continent

    a = create_schema_org_model(type_=ContinentInheritedProperties)
    b = create_schema_org_model(type_=ContinentProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Continent.schema()


def EducationalOccupationalCredential_test():
    from schorg.EducationalOccupationalCredential import EducationalOccupationalCredentialInheritedProperties
    from schorg.EducationalOccupationalCredential import EducationalOccupationalCredentialProperties
    from schorg.EducationalOccupationalCredential import AllProperties
    from schorg.EducationalOccupationalCredential import create_schema_org_model
    from schorg.EducationalOccupationalCredential import EducationalOccupationalCredential

    a = create_schema_org_model(type_=EducationalOccupationalCredentialInheritedProperties)
    b = create_schema_org_model(type_=EducationalOccupationalCredentialProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    EducationalOccupationalCredential.schema()


def MedicalCondition_test():
    from schorg.MedicalCondition import MedicalConditionInheritedProperties
    from schorg.MedicalCondition import MedicalConditionProperties
    from schorg.MedicalCondition import AllProperties
    from schorg.MedicalCondition import create_schema_org_model
    from schorg.MedicalCondition import MedicalCondition

    a = create_schema_org_model(type_=MedicalConditionInheritedProperties)
    b = create_schema_org_model(type_=MedicalConditionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MedicalCondition.schema()


def InfectiousDisease_test():
    from schorg.InfectiousDisease import InfectiousDiseaseInheritedProperties
    from schorg.InfectiousDisease import InfectiousDiseaseProperties
    from schorg.InfectiousDisease import AllProperties
    from schorg.InfectiousDisease import create_schema_org_model
    from schorg.InfectiousDisease import InfectiousDisease

    a = create_schema_org_model(type_=InfectiousDiseaseInheritedProperties)
    b = create_schema_org_model(type_=InfectiousDiseaseProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    InfectiousDisease.schema()


def ReturnMethodEnumeration_test():
    from schorg.ReturnMethodEnumeration import ReturnMethodEnumerationInheritedProperties
    from schorg.ReturnMethodEnumeration import ReturnMethodEnumerationProperties
    from schorg.ReturnMethodEnumeration import AllProperties
    from schorg.ReturnMethodEnumeration import create_schema_org_model
    from schorg.ReturnMethodEnumeration import ReturnMethodEnumeration

    a = create_schema_org_model(type_=ReturnMethodEnumerationInheritedProperties)
    b = create_schema_org_model(type_=ReturnMethodEnumerationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ReturnMethodEnumeration.schema()


def ReturnByMail_test():
    from schorg.ReturnByMail import ReturnByMailInheritedProperties
    from schorg.ReturnByMail import ReturnByMailProperties
    from schorg.ReturnByMail import AllProperties
    from schorg.ReturnByMail import create_schema_org_model
    from schorg.ReturnByMail import ReturnByMail

    a = create_schema_org_model(type_=ReturnByMailInheritedProperties)
    b = create_schema_org_model(type_=ReturnByMailProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ReturnByMail.schema()


def InfectiousAgentClass_test():
    from schorg.InfectiousAgentClass import InfectiousAgentClassInheritedProperties
    from schorg.InfectiousAgentClass import InfectiousAgentClassProperties
    from schorg.InfectiousAgentClass import AllProperties
    from schorg.InfectiousAgentClass import create_schema_org_model
    from schorg.InfectiousAgentClass import InfectiousAgentClass

    a = create_schema_org_model(type_=InfectiousAgentClassInheritedProperties)
    b = create_schema_org_model(type_=InfectiousAgentClassProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    InfectiousAgentClass.schema()


def Prion_test():
    from schorg.Prion import PrionInheritedProperties
    from schorg.Prion import PrionProperties
    from schorg.Prion import AllProperties
    from schorg.Prion import create_schema_org_model
    from schorg.Prion import Prion

    a = create_schema_org_model(type_=PrionInheritedProperties)
    b = create_schema_org_model(type_=PrionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Prion.schema()


def PerformingGroup_test():
    from schorg.PerformingGroup import PerformingGroupInheritedProperties
    from schorg.PerformingGroup import PerformingGroupProperties
    from schorg.PerformingGroup import AllProperties
    from schorg.PerformingGroup import create_schema_org_model
    from schorg.PerformingGroup import PerformingGroup

    a = create_schema_org_model(type_=PerformingGroupInheritedProperties)
    b = create_schema_org_model(type_=PerformingGroupProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    PerformingGroup.schema()


def MusicGroup_test():
    from schorg.MusicGroup import MusicGroupInheritedProperties
    from schorg.MusicGroup import MusicGroupProperties
    from schorg.MusicGroup import AllProperties
    from schorg.MusicGroup import create_schema_org_model
    from schorg.MusicGroup import MusicGroup

    a = create_schema_org_model(type_=MusicGroupInheritedProperties)
    b = create_schema_org_model(type_=MusicGroupProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MusicGroup.schema()


def SingleCenterTrial_test():
    from schorg.SingleCenterTrial import SingleCenterTrialInheritedProperties
    from schorg.SingleCenterTrial import SingleCenterTrialProperties
    from schorg.SingleCenterTrial import AllProperties
    from schorg.SingleCenterTrial import create_schema_org_model
    from schorg.SingleCenterTrial import SingleCenterTrial

    a = create_schema_org_model(type_=SingleCenterTrialInheritedProperties)
    b = create_schema_org_model(type_=SingleCenterTrialProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    SingleCenterTrial.schema()


def Nonprofit501c10_test():
    from schorg.Nonprofit501c10 import Nonprofit501c10InheritedProperties
    from schorg.Nonprofit501c10 import Nonprofit501c10Properties
    from schorg.Nonprofit501c10 import AllProperties
    from schorg.Nonprofit501c10 import create_schema_org_model
    from schorg.Nonprofit501c10 import Nonprofit501c10

    a = create_schema_org_model(type_=Nonprofit501c10InheritedProperties)
    b = create_schema_org_model(type_=Nonprofit501c10Properties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Nonprofit501c10.schema()


def MedicalTestPanel_test():
    from schorg.MedicalTestPanel import MedicalTestPanelInheritedProperties
    from schorg.MedicalTestPanel import MedicalTestPanelProperties
    from schorg.MedicalTestPanel import AllProperties
    from schorg.MedicalTestPanel import create_schema_org_model
    from schorg.MedicalTestPanel import MedicalTestPanel

    a = create_schema_org_model(type_=MedicalTestPanelInheritedProperties)
    b = create_schema_org_model(type_=MedicalTestPanelProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MedicalTestPanel.schema()


def DrugStrength_test():
    from schorg.DrugStrength import DrugStrengthInheritedProperties
    from schorg.DrugStrength import DrugStrengthProperties
    from schorg.DrugStrength import AllProperties
    from schorg.DrugStrength import create_schema_org_model
    from schorg.DrugStrength import DrugStrength

    a = create_schema_org_model(type_=DrugStrengthInheritedProperties)
    b = create_schema_org_model(type_=DrugStrengthProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    DrugStrength.schema()


def TypeAndQuantityNode_test():
    from schorg.TypeAndQuantityNode import TypeAndQuantityNodeInheritedProperties
    from schorg.TypeAndQuantityNode import TypeAndQuantityNodeProperties
    from schorg.TypeAndQuantityNode import AllProperties
    from schorg.TypeAndQuantityNode import create_schema_org_model
    from schorg.TypeAndQuantityNode import TypeAndQuantityNode

    a = create_schema_org_model(type_=TypeAndQuantityNodeInheritedProperties)
    b = create_schema_org_model(type_=TypeAndQuantityNodeProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    TypeAndQuantityNode.schema()


def MediaSubscription_test():
    from schorg.MediaSubscription import MediaSubscriptionInheritedProperties
    from schorg.MediaSubscription import MediaSubscriptionProperties
    from schorg.MediaSubscription import AllProperties
    from schorg.MediaSubscription import create_schema_org_model
    from schorg.MediaSubscription import MediaSubscription

    a = create_schema_org_model(type_=MediaSubscriptionInheritedProperties)
    b = create_schema_org_model(type_=MediaSubscriptionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MediaSubscription.schema()


def DrugCostCategory_test():
    from schorg.DrugCostCategory import DrugCostCategoryInheritedProperties
    from schorg.DrugCostCategory import DrugCostCategoryProperties
    from schorg.DrugCostCategory import AllProperties
    from schorg.DrugCostCategory import create_schema_org_model
    from schorg.DrugCostCategory import DrugCostCategory

    a = create_schema_org_model(type_=DrugCostCategoryInheritedProperties)
    b = create_schema_org_model(type_=DrugCostCategoryProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    DrugCostCategory.schema()


def Retail_test():
    from schorg.Retail import RetailInheritedProperties
    from schorg.Retail import RetailProperties
    from schorg.Retail import AllProperties
    from schorg.Retail import create_schema_org_model
    from schorg.Retail import Retail

    a = create_schema_org_model(type_=RetailInheritedProperties)
    b = create_schema_org_model(type_=RetailProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Retail.schema()


def WearableSizeGroupHusky_test():
    from schorg.WearableSizeGroupHusky import WearableSizeGroupHuskyInheritedProperties
    from schorg.WearableSizeGroupHusky import WearableSizeGroupHuskyProperties
    from schorg.WearableSizeGroupHusky import AllProperties
    from schorg.WearableSizeGroupHusky import create_schema_org_model
    from schorg.WearableSizeGroupHusky import WearableSizeGroupHusky

    a = create_schema_org_model(type_=WearableSizeGroupHuskyInheritedProperties)
    b = create_schema_org_model(type_=WearableSizeGroupHuskyProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    WearableSizeGroupHusky.schema()


def DiabeticDiet_test():
    from schorg.DiabeticDiet import DiabeticDietInheritedProperties
    from schorg.DiabeticDiet import DiabeticDietProperties
    from schorg.DiabeticDiet import AllProperties
    from schorg.DiabeticDiet import create_schema_org_model
    from schorg.DiabeticDiet import DiabeticDiet

    a = create_schema_org_model(type_=DiabeticDietInheritedProperties)
    b = create_schema_org_model(type_=DiabeticDietProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    DiabeticDiet.schema()


def MedicalImagingTechnique_test():
    from schorg.MedicalImagingTechnique import MedicalImagingTechniqueInheritedProperties
    from schorg.MedicalImagingTechnique import MedicalImagingTechniqueProperties
    from schorg.MedicalImagingTechnique import AllProperties
    from schorg.MedicalImagingTechnique import create_schema_org_model
    from schorg.MedicalImagingTechnique import MedicalImagingTechnique

    a = create_schema_org_model(type_=MedicalImagingTechniqueInheritedProperties)
    b = create_schema_org_model(type_=MedicalImagingTechniqueProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MedicalImagingTechnique.schema()


def XRay_test():
    from schorg.XRay import XRayInheritedProperties
    from schorg.XRay import XRayProperties
    from schorg.XRay import AllProperties
    from schorg.XRay import create_schema_org_model
    from schorg.XRay import XRay

    a = create_schema_org_model(type_=XRayInheritedProperties)
    b = create_schema_org_model(type_=XRayProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    XRay.schema()


def WearableMeasurementInseam_test():
    from schorg.WearableMeasurementInseam import WearableMeasurementInseamInheritedProperties
    from schorg.WearableMeasurementInseam import WearableMeasurementInseamProperties
    from schorg.WearableMeasurementInseam import AllProperties
    from schorg.WearableMeasurementInseam import create_schema_org_model
    from schorg.WearableMeasurementInseam import WearableMeasurementInseam

    a = create_schema_org_model(type_=WearableMeasurementInseamInheritedProperties)
    b = create_schema_org_model(type_=WearableMeasurementInseamProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    WearableMeasurementInseam.schema()


def SeeDoctorHealthAspect_test():
    from schorg.SeeDoctorHealthAspect import SeeDoctorHealthAspectInheritedProperties
    from schorg.SeeDoctorHealthAspect import SeeDoctorHealthAspectProperties
    from schorg.SeeDoctorHealthAspect import AllProperties
    from schorg.SeeDoctorHealthAspect import create_schema_org_model
    from schorg.SeeDoctorHealthAspect import SeeDoctorHealthAspect

    a = create_schema_org_model(type_=SeeDoctorHealthAspectInheritedProperties)
    b = create_schema_org_model(type_=SeeDoctorHealthAspectProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    SeeDoctorHealthAspect.schema()


def MusicEvent_test():
    from schorg.MusicEvent import MusicEventInheritedProperties
    from schorg.MusicEvent import MusicEventProperties
    from schorg.MusicEvent import AllProperties
    from schorg.MusicEvent import create_schema_org_model
    from schorg.MusicEvent import MusicEvent

    a = create_schema_org_model(type_=MusicEventInheritedProperties)
    b = create_schema_org_model(type_=MusicEventProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MusicEvent.schema()


def MixedEventAttendanceMode_test():
    from schorg.MixedEventAttendanceMode import MixedEventAttendanceModeInheritedProperties
    from schorg.MixedEventAttendanceMode import MixedEventAttendanceModeProperties
    from schorg.MixedEventAttendanceMode import AllProperties
    from schorg.MixedEventAttendanceMode import create_schema_org_model
    from schorg.MixedEventAttendanceMode import MixedEventAttendanceMode

    a = create_schema_org_model(type_=MixedEventAttendanceModeInheritedProperties)
    b = create_schema_org_model(type_=MixedEventAttendanceModeProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MixedEventAttendanceMode.schema()


def Dermatology_test():
    from schorg.Dermatology import DermatologyInheritedProperties
    from schorg.Dermatology import DermatologyProperties
    from schorg.Dermatology import AllProperties
    from schorg.Dermatology import create_schema_org_model
    from schorg.Dermatology import Dermatology

    a = create_schema_org_model(type_=DermatologyInheritedProperties)
    b = create_schema_org_model(type_=DermatologyProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Dermatology.schema()


def TherapeuticProcedure_test():
    from schorg.TherapeuticProcedure import TherapeuticProcedureInheritedProperties
    from schorg.TherapeuticProcedure import TherapeuticProcedureProperties
    from schorg.TherapeuticProcedure import AllProperties
    from schorg.TherapeuticProcedure import create_schema_org_model
    from schorg.TherapeuticProcedure import TherapeuticProcedure

    a = create_schema_org_model(type_=TherapeuticProcedureInheritedProperties)
    b = create_schema_org_model(type_=TherapeuticProcedureProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    TherapeuticProcedure.schema()


def MedicalTherapy_test():
    from schorg.MedicalTherapy import MedicalTherapyInheritedProperties
    from schorg.MedicalTherapy import MedicalTherapyProperties
    from schorg.MedicalTherapy import AllProperties
    from schorg.MedicalTherapy import create_schema_org_model
    from schorg.MedicalTherapy import MedicalTherapy

    a = create_schema_org_model(type_=MedicalTherapyInheritedProperties)
    b = create_schema_org_model(type_=MedicalTherapyProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MedicalTherapy.schema()


def Episode_test():
    from schorg.Episode import EpisodeInheritedProperties
    from schorg.Episode import EpisodeProperties
    from schorg.Episode import AllProperties
    from schorg.Episode import create_schema_org_model
    from schorg.Episode import Episode

    a = create_schema_org_model(type_=EpisodeInheritedProperties)
    b = create_schema_org_model(type_=EpisodeProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Episode.schema()


def RadioEpisode_test():
    from schorg.RadioEpisode import RadioEpisodeInheritedProperties
    from schorg.RadioEpisode import RadioEpisodeProperties
    from schorg.RadioEpisode import AllProperties
    from schorg.RadioEpisode import create_schema_org_model
    from schorg.RadioEpisode import RadioEpisode

    a = create_schema_org_model(type_=RadioEpisodeInheritedProperties)
    b = create_schema_org_model(type_=RadioEpisodeProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    RadioEpisode.schema()


def MedicalSignOrSymptom_test():
    from schorg.MedicalSignOrSymptom import MedicalSignOrSymptomInheritedProperties
    from schorg.MedicalSignOrSymptom import MedicalSignOrSymptomProperties
    from schorg.MedicalSignOrSymptom import AllProperties
    from schorg.MedicalSignOrSymptom import create_schema_org_model
    from schorg.MedicalSignOrSymptom import MedicalSignOrSymptom

    a = create_schema_org_model(type_=MedicalSignOrSymptomInheritedProperties)
    b = create_schema_org_model(type_=MedicalSignOrSymptomProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MedicalSignOrSymptom.schema()


def BodyMeasurementArm_test():
    from schorg.BodyMeasurementArm import BodyMeasurementArmInheritedProperties
    from schorg.BodyMeasurementArm import BodyMeasurementArmProperties
    from schorg.BodyMeasurementArm import AllProperties
    from schorg.BodyMeasurementArm import create_schema_org_model
    from schorg.BodyMeasurementArm import BodyMeasurementArm

    a = create_schema_org_model(type_=BodyMeasurementArmInheritedProperties)
    b = create_schema_org_model(type_=BodyMeasurementArmProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    BodyMeasurementArm.schema()


def ChooseAction_test():
    from schorg.ChooseAction import ChooseActionInheritedProperties
    from schorg.ChooseAction import ChooseActionProperties
    from schorg.ChooseAction import AllProperties
    from schorg.ChooseAction import create_schema_org_model
    from schorg.ChooseAction import ChooseAction

    a = create_schema_org_model(type_=ChooseActionInheritedProperties)
    b = create_schema_org_model(type_=ChooseActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ChooseAction.schema()


def VoteAction_test():
    from schorg.VoteAction import VoteActionInheritedProperties
    from schorg.VoteAction import VoteActionProperties
    from schorg.VoteAction import AllProperties
    from schorg.VoteAction import create_schema_org_model
    from schorg.VoteAction import VoteAction

    a = create_schema_org_model(type_=VoteActionInheritedProperties)
    b = create_schema_org_model(type_=VoteActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    VoteAction.schema()


def WPSideBar_test():
    from schorg.WPSideBar import WPSideBarInheritedProperties
    from schorg.WPSideBar import WPSideBarProperties
    from schorg.WPSideBar import AllProperties
    from schorg.WPSideBar import create_schema_org_model
    from schorg.WPSideBar import WPSideBar

    a = create_schema_org_model(type_=WPSideBarInheritedProperties)
    b = create_schema_org_model(type_=WPSideBarProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    WPSideBar.schema()


def Residence_test():
    from schorg.Residence import ResidenceInheritedProperties
    from schorg.Residence import ResidenceProperties
    from schorg.Residence import AllProperties
    from schorg.Residence import create_schema_org_model
    from schorg.Residence import Residence

    a = create_schema_org_model(type_=ResidenceInheritedProperties)
    b = create_schema_org_model(type_=ResidenceProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Residence.schema()


def ApartmentComplex_test():
    from schorg.ApartmentComplex import ApartmentComplexInheritedProperties
    from schorg.ApartmentComplex import ApartmentComplexProperties
    from schorg.ApartmentComplex import AllProperties
    from schorg.ApartmentComplex import create_schema_org_model
    from schorg.ApartmentComplex import ApartmentComplex

    a = create_schema_org_model(type_=ApartmentComplexInheritedProperties)
    b = create_schema_org_model(type_=ApartmentComplexProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ApartmentComplex.schema()


def Sculpture_test():
    from schorg.Sculpture import SculptureInheritedProperties
    from schorg.Sculpture import SculptureProperties
    from schorg.Sculpture import AllProperties
    from schorg.Sculpture import create_schema_org_model
    from schorg.Sculpture import Sculpture

    a = create_schema_org_model(type_=SculptureInheritedProperties)
    b = create_schema_org_model(type_=SculptureProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Sculpture.schema()


def Surgical_test():
    from schorg.Surgical import SurgicalInheritedProperties
    from schorg.Surgical import SurgicalProperties
    from schorg.Surgical import AllProperties
    from schorg.Surgical import create_schema_org_model
    from schorg.Surgical import Surgical

    a = create_schema_org_model(type_=SurgicalInheritedProperties)
    b = create_schema_org_model(type_=SurgicalProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Surgical.schema()


def Terminated_test():
    from schorg.Terminated import TerminatedInheritedProperties
    from schorg.Terminated import TerminatedProperties
    from schorg.Terminated import AllProperties
    from schorg.Terminated import create_schema_org_model
    from schorg.Terminated import Terminated

    a = create_schema_org_model(type_=TerminatedInheritedProperties)
    b = create_schema_org_model(type_=TerminatedProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Terminated.schema()


def EnergyStarEnergyEfficiencyEnumeration_test():
    from schorg.EnergyStarEnergyEfficiencyEnumeration import EnergyStarEnergyEfficiencyEnumerationInheritedProperties
    from schorg.EnergyStarEnergyEfficiencyEnumeration import EnergyStarEnergyEfficiencyEnumerationProperties
    from schorg.EnergyStarEnergyEfficiencyEnumeration import AllProperties
    from schorg.EnergyStarEnergyEfficiencyEnumeration import create_schema_org_model
    from schorg.EnergyStarEnergyEfficiencyEnumeration import EnergyStarEnergyEfficiencyEnumeration

    a = create_schema_org_model(type_=EnergyStarEnergyEfficiencyEnumerationInheritedProperties)
    b = create_schema_org_model(type_=EnergyStarEnergyEfficiencyEnumerationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    EnergyStarEnergyEfficiencyEnumeration.schema()


def BankAccount_test():
    from schorg.BankAccount import BankAccountInheritedProperties
    from schorg.BankAccount import BankAccountProperties
    from schorg.BankAccount import AllProperties
    from schorg.BankAccount import create_schema_org_model
    from schorg.BankAccount import BankAccount

    a = create_schema_org_model(type_=BankAccountInheritedProperties)
    b = create_schema_org_model(type_=BankAccountProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    BankAccount.schema()


def DepositAccount_test():
    from schorg.DepositAccount import DepositAccountInheritedProperties
    from schorg.DepositAccount import DepositAccountProperties
    from schorg.DepositAccount import AllProperties
    from schorg.DepositAccount import create_schema_org_model
    from schorg.DepositAccount import DepositAccount

    a = create_schema_org_model(type_=DepositAccountInheritedProperties)
    b = create_schema_org_model(type_=DepositAccountProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    DepositAccount.schema()


def MovingCompany_test():
    from schorg.MovingCompany import MovingCompanyInheritedProperties
    from schorg.MovingCompany import MovingCompanyProperties
    from schorg.MovingCompany import AllProperties
    from schorg.MovingCompany import create_schema_org_model
    from schorg.MovingCompany import MovingCompany

    a = create_schema_org_model(type_=MovingCompanyInheritedProperties)
    b = create_schema_org_model(type_=MovingCompanyProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MovingCompany.schema()


def Offer_test():
    from schorg.Offer import OfferInheritedProperties
    from schorg.Offer import OfferProperties
    from schorg.Offer import AllProperties
    from schorg.Offer import create_schema_org_model
    from schorg.Offer import Offer

    a = create_schema_org_model(type_=OfferInheritedProperties)
    b = create_schema_org_model(type_=OfferProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Offer.schema()


def AggregateOffer_test():
    from schorg.AggregateOffer import AggregateOfferInheritedProperties
    from schorg.AggregateOffer import AggregateOfferProperties
    from schorg.AggregateOffer import AllProperties
    from schorg.AggregateOffer import create_schema_org_model
    from schorg.AggregateOffer import AggregateOffer

    a = create_schema_org_model(type_=AggregateOfferInheritedProperties)
    b = create_schema_org_model(type_=AggregateOfferProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    AggregateOffer.schema()


def WearableSizeSystemGS1_test():
    from schorg.WearableSizeSystemGS1 import WearableSizeSystemGS1InheritedProperties
    from schorg.WearableSizeSystemGS1 import WearableSizeSystemGS1Properties
    from schorg.WearableSizeSystemGS1 import AllProperties
    from schorg.WearableSizeSystemGS1 import create_schema_org_model
    from schorg.WearableSizeSystemGS1 import WearableSizeSystemGS1

    a = create_schema_org_model(type_=WearableSizeSystemGS1InheritedProperties)
    b = create_schema_org_model(type_=WearableSizeSystemGS1Properties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    WearableSizeSystemGS1.schema()


def EmploymentAgency_test():
    from schorg.EmploymentAgency import EmploymentAgencyInheritedProperties
    from schorg.EmploymentAgency import EmploymentAgencyProperties
    from schorg.EmploymentAgency import AllProperties
    from schorg.EmploymentAgency import create_schema_org_model
    from schorg.EmploymentAgency import EmploymentAgency

    a = create_schema_org_model(type_=EmploymentAgencyInheritedProperties)
    b = create_schema_org_model(type_=EmploymentAgencyProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    EmploymentAgency.schema()


def Ligament_test():
    from schorg.Ligament import LigamentInheritedProperties
    from schorg.Ligament import LigamentProperties
    from schorg.Ligament import AllProperties
    from schorg.Ligament import create_schema_org_model
    from schorg.Ligament import Ligament

    a = create_schema_org_model(type_=LigamentInheritedProperties)
    b = create_schema_org_model(type_=LigamentProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Ligament.schema()


def FDAcategoryC_test():
    from schorg.FDAcategoryC import FDAcategoryCInheritedProperties
    from schorg.FDAcategoryC import FDAcategoryCProperties
    from schorg.FDAcategoryC import AllProperties
    from schorg.FDAcategoryC import create_schema_org_model
    from schorg.FDAcategoryC import FDAcategoryC

    a = create_schema_org_model(type_=FDAcategoryCInheritedProperties)
    b = create_schema_org_model(type_=FDAcategoryCProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    FDAcategoryC.schema()


def Optometric_test():
    from schorg.Optometric import OptometricInheritedProperties
    from schorg.Optometric import OptometricProperties
    from schorg.Optometric import AllProperties
    from schorg.Optometric import create_schema_org_model
    from schorg.Optometric import Optometric

    a = create_schema_org_model(type_=OptometricInheritedProperties)
    b = create_schema_org_model(type_=OptometricProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Optometric.schema()


def OutletStore_test():
    from schorg.OutletStore import OutletStoreInheritedProperties
    from schorg.OutletStore import OutletStoreProperties
    from schorg.OutletStore import AllProperties
    from schorg.OutletStore import create_schema_org_model
    from schorg.OutletStore import OutletStore

    a = create_schema_org_model(type_=OutletStoreInheritedProperties)
    b = create_schema_org_model(type_=OutletStoreProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    OutletStore.schema()


def RefundTypeEnumeration_test():
    from schorg.RefundTypeEnumeration import RefundTypeEnumerationInheritedProperties
    from schorg.RefundTypeEnumeration import RefundTypeEnumerationProperties
    from schorg.RefundTypeEnumeration import AllProperties
    from schorg.RefundTypeEnumeration import create_schema_org_model
    from schorg.RefundTypeEnumeration import RefundTypeEnumeration

    a = create_schema_org_model(type_=RefundTypeEnumerationInheritedProperties)
    b = create_schema_org_model(type_=RefundTypeEnumerationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    RefundTypeEnumeration.schema()


def StoreCreditRefund_test():
    from schorg.StoreCreditRefund import StoreCreditRefundInheritedProperties
    from schorg.StoreCreditRefund import StoreCreditRefundProperties
    from schorg.StoreCreditRefund import AllProperties
    from schorg.StoreCreditRefund import create_schema_org_model
    from schorg.StoreCreditRefund import StoreCreditRefund

    a = create_schema_org_model(type_=StoreCreditRefundInheritedProperties)
    b = create_schema_org_model(type_=StoreCreditRefundProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    StoreCreditRefund.schema()


def InternetCafe_test():
    from schorg.InternetCafe import InternetCafeInheritedProperties
    from schorg.InternetCafe import InternetCafeProperties
    from schorg.InternetCafe import AllProperties
    from schorg.InternetCafe import create_schema_org_model
    from schorg.InternetCafe import InternetCafe

    a = create_schema_org_model(type_=InternetCafeInheritedProperties)
    b = create_schema_org_model(type_=InternetCafeProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    InternetCafe.schema()


def AdministrativeArea_test():
    from schorg.AdministrativeArea import AdministrativeAreaInheritedProperties
    from schorg.AdministrativeArea import AdministrativeAreaProperties
    from schorg.AdministrativeArea import AllProperties
    from schorg.AdministrativeArea import create_schema_org_model
    from schorg.AdministrativeArea import AdministrativeArea

    a = create_schema_org_model(type_=AdministrativeAreaInheritedProperties)
    b = create_schema_org_model(type_=AdministrativeAreaProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    AdministrativeArea.schema()


def GameServerStatus_test():
    from schorg.GameServerStatus import GameServerStatusInheritedProperties
    from schorg.GameServerStatus import GameServerStatusProperties
    from schorg.GameServerStatus import AllProperties
    from schorg.GameServerStatus import create_schema_org_model
    from schorg.GameServerStatus import GameServerStatus

    a = create_schema_org_model(type_=GameServerStatusInheritedProperties)
    b = create_schema_org_model(type_=GameServerStatusProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    GameServerStatus.schema()


def OnlineFull_test():
    from schorg.OnlineFull import OnlineFullInheritedProperties
    from schorg.OnlineFull import OnlineFullProperties
    from schorg.OnlineFull import AllProperties
    from schorg.OnlineFull import create_schema_org_model
    from schorg.OnlineFull import OnlineFull

    a = create_schema_org_model(type_=OnlineFullInheritedProperties)
    b = create_schema_org_model(type_=OnlineFullProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    OnlineFull.schema()


def ConsumeAction_test():
    from schorg.ConsumeAction import ConsumeActionInheritedProperties
    from schorg.ConsumeAction import ConsumeActionProperties
    from schorg.ConsumeAction import AllProperties
    from schorg.ConsumeAction import create_schema_org_model
    from schorg.ConsumeAction import ConsumeAction

    a = create_schema_org_model(type_=ConsumeActionInheritedProperties)
    b = create_schema_org_model(type_=ConsumeActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ConsumeAction.schema()


def ListenAction_test():
    from schorg.ListenAction import ListenActionInheritedProperties
    from schorg.ListenAction import ListenActionProperties
    from schorg.ListenAction import AllProperties
    from schorg.ListenAction import create_schema_org_model
    from schorg.ListenAction import ListenAction

    a = create_schema_org_model(type_=ListenActionInheritedProperties)
    b = create_schema_org_model(type_=ListenActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ListenAction.schema()


def SocialMediaPosting_test():
    from schorg.SocialMediaPosting import SocialMediaPostingInheritedProperties
    from schorg.SocialMediaPosting import SocialMediaPostingProperties
    from schorg.SocialMediaPosting import AllProperties
    from schorg.SocialMediaPosting import create_schema_org_model
    from schorg.SocialMediaPosting import SocialMediaPosting

    a = create_schema_org_model(type_=SocialMediaPostingInheritedProperties)
    b = create_schema_org_model(type_=SocialMediaPostingProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    SocialMediaPosting.schema()


def MusicVenue_test():
    from schorg.MusicVenue import MusicVenueInheritedProperties
    from schorg.MusicVenue import MusicVenueProperties
    from schorg.MusicVenue import AllProperties
    from schorg.MusicVenue import create_schema_org_model
    from schorg.MusicVenue import MusicVenue

    a = create_schema_org_model(type_=MusicVenueInheritedProperties)
    b = create_schema_org_model(type_=MusicVenueProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MusicVenue.schema()


def Genetic_test():
    from schorg.Genetic import GeneticInheritedProperties
    from schorg.Genetic import GeneticProperties
    from schorg.Genetic import AllProperties
    from schorg.Genetic import create_schema_org_model
    from schorg.Genetic import Genetic

    a = create_schema_org_model(type_=GeneticInheritedProperties)
    b = create_schema_org_model(type_=GeneticProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Genetic.schema()


def Head_test():
    from schorg.Head import HeadInheritedProperties
    from schorg.Head import HeadProperties
    from schorg.Head import AllProperties
    from schorg.Head import create_schema_org_model
    from schorg.Head import Head

    a = create_schema_org_model(type_=HeadInheritedProperties)
    b = create_schema_org_model(type_=HeadProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Head.schema()


def MSRP_test():
    from schorg.MSRP import MSRPInheritedProperties
    from schorg.MSRP import MSRPProperties
    from schorg.MSRP import AllProperties
    from schorg.MSRP import create_schema_org_model
    from schorg.MSRP import MSRP

    a = create_schema_org_model(type_=MSRPInheritedProperties)
    b = create_schema_org_model(type_=MSRPProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MSRP.schema()


def PoliceStation_test():
    from schorg.PoliceStation import PoliceStationInheritedProperties
    from schorg.PoliceStation import PoliceStationProperties
    from schorg.PoliceStation import AllProperties
    from schorg.PoliceStation import create_schema_org_model
    from schorg.PoliceStation import PoliceStation

    a = create_schema_org_model(type_=PoliceStationInheritedProperties)
    b = create_schema_org_model(type_=PoliceStationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    PoliceStation.schema()


def Friday_test():
    from schorg.Friday import FridayInheritedProperties
    from schorg.Friday import FridayProperties
    from schorg.Friday import AllProperties
    from schorg.Friday import create_schema_org_model
    from schorg.Friday import Friday

    a = create_schema_org_model(type_=FridayInheritedProperties)
    b = create_schema_org_model(type_=FridayProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Friday.schema()


def PaymentStatusType_test():
    from schorg.PaymentStatusType import PaymentStatusTypeInheritedProperties
    from schorg.PaymentStatusType import PaymentStatusTypeProperties
    from schorg.PaymentStatusType import AllProperties
    from schorg.PaymentStatusType import create_schema_org_model
    from schorg.PaymentStatusType import PaymentStatusType

    a = create_schema_org_model(type_=PaymentStatusTypeInheritedProperties)
    b = create_schema_org_model(type_=PaymentStatusTypeProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    PaymentStatusType.schema()


def PaymentComplete_test():
    from schorg.PaymentComplete import PaymentCompleteInheritedProperties
    from schorg.PaymentComplete import PaymentCompleteProperties
    from schorg.PaymentComplete import AllProperties
    from schorg.PaymentComplete import create_schema_org_model
    from schorg.PaymentComplete import PaymentComplete

    a = create_schema_org_model(type_=PaymentCompleteInheritedProperties)
    b = create_schema_org_model(type_=PaymentCompleteProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    PaymentComplete.schema()


def CableOrSatelliteService_test():
    from schorg.CableOrSatelliteService import CableOrSatelliteServiceInheritedProperties
    from schorg.CableOrSatelliteService import CableOrSatelliteServiceProperties
    from schorg.CableOrSatelliteService import AllProperties
    from schorg.CableOrSatelliteService import create_schema_org_model
    from schorg.CableOrSatelliteService import CableOrSatelliteService

    a = create_schema_org_model(type_=CableOrSatelliteServiceInheritedProperties)
    b = create_schema_org_model(type_=CableOrSatelliteServiceProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    CableOrSatelliteService.schema()


def PayAction_test():
    from schorg.PayAction import PayActionInheritedProperties
    from schorg.PayAction import PayActionProperties
    from schorg.PayAction import AllProperties
    from schorg.PayAction import create_schema_org_model
    from schorg.PayAction import PayAction

    a = create_schema_org_model(type_=PayActionInheritedProperties)
    b = create_schema_org_model(type_=PayActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    PayAction.schema()


def DeliveryTimeSettings_test():
    from schorg.DeliveryTimeSettings import DeliveryTimeSettingsInheritedProperties
    from schorg.DeliveryTimeSettings import DeliveryTimeSettingsProperties
    from schorg.DeliveryTimeSettings import AllProperties
    from schorg.DeliveryTimeSettings import create_schema_org_model
    from schorg.DeliveryTimeSettings import DeliveryTimeSettings

    a = create_schema_org_model(type_=DeliveryTimeSettingsInheritedProperties)
    b = create_schema_org_model(type_=DeliveryTimeSettingsProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    DeliveryTimeSettings.schema()


def WarrantyPromise_test():
    from schorg.WarrantyPromise import WarrantyPromiseInheritedProperties
    from schorg.WarrantyPromise import WarrantyPromiseProperties
    from schorg.WarrantyPromise import AllProperties
    from schorg.WarrantyPromise import create_schema_org_model
    from schorg.WarrantyPromise import WarrantyPromise

    a = create_schema_org_model(type_=WarrantyPromiseInheritedProperties)
    b = create_schema_org_model(type_=WarrantyPromiseProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    WarrantyPromise.schema()


def MobilePhoneStore_test():
    from schorg.MobilePhoneStore import MobilePhoneStoreInheritedProperties
    from schorg.MobilePhoneStore import MobilePhoneStoreProperties
    from schorg.MobilePhoneStore import AllProperties
    from schorg.MobilePhoneStore import create_schema_org_model
    from schorg.MobilePhoneStore import MobilePhoneStore

    a = create_schema_org_model(type_=MobilePhoneStoreInheritedProperties)
    b = create_schema_org_model(type_=MobilePhoneStoreProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MobilePhoneStore.schema()


def Nonprofit501q_test():
    from schorg.Nonprofit501q import Nonprofit501qInheritedProperties
    from schorg.Nonprofit501q import Nonprofit501qProperties
    from schorg.Nonprofit501q import AllProperties
    from schorg.Nonprofit501q import create_schema_org_model
    from schorg.Nonprofit501q import Nonprofit501q

    a = create_schema_org_model(type_=Nonprofit501qInheritedProperties)
    b = create_schema_org_model(type_=Nonprofit501qProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Nonprofit501q.schema()


def DrugCost_test():
    from schorg.DrugCost import DrugCostInheritedProperties
    from schorg.DrugCost import DrugCostProperties
    from schorg.DrugCost import AllProperties
    from schorg.DrugCost import create_schema_org_model
    from schorg.DrugCost import DrugCost

    a = create_schema_org_model(type_=DrugCostInheritedProperties)
    b = create_schema_org_model(type_=DrugCostProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    DrugCost.schema()


def ReadPermission_test():
    from schorg.ReadPermission import ReadPermissionInheritedProperties
    from schorg.ReadPermission import ReadPermissionProperties
    from schorg.ReadPermission import AllProperties
    from schorg.ReadPermission import create_schema_org_model
    from schorg.ReadPermission import ReadPermission

    a = create_schema_org_model(type_=ReadPermissionInheritedProperties)
    b = create_schema_org_model(type_=ReadPermissionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ReadPermission.schema()


def WearableSizeSystemContinental_test():
    from schorg.WearableSizeSystemContinental import WearableSizeSystemContinentalInheritedProperties
    from schorg.WearableSizeSystemContinental import WearableSizeSystemContinentalProperties
    from schorg.WearableSizeSystemContinental import AllProperties
    from schorg.WearableSizeSystemContinental import create_schema_org_model
    from schorg.WearableSizeSystemContinental import WearableSizeSystemContinental

    a = create_schema_org_model(type_=WearableSizeSystemContinentalInheritedProperties)
    b = create_schema_org_model(type_=WearableSizeSystemContinentalProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    WearableSizeSystemContinental.schema()


def RentAction_test():
    from schorg.RentAction import RentActionInheritedProperties
    from schorg.RentAction import RentActionProperties
    from schorg.RentAction import AllProperties
    from schorg.RentAction import create_schema_org_model
    from schorg.RentAction import RentAction

    a = create_schema_org_model(type_=RentActionInheritedProperties)
    b = create_schema_org_model(type_=RentActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    RentAction.schema()


def ShortStory_test():
    from schorg.ShortStory import ShortStoryInheritedProperties
    from schorg.ShortStory import ShortStoryProperties
    from schorg.ShortStory import AllProperties
    from schorg.ShortStory import create_schema_org_model
    from schorg.ShortStory import ShortStory

    a = create_schema_org_model(type_=ShortStoryInheritedProperties)
    b = create_schema_org_model(type_=ShortStoryProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ShortStory.schema()


def BreadcrumbList_test():
    from schorg.BreadcrumbList import BreadcrumbListInheritedProperties
    from schorg.BreadcrumbList import BreadcrumbListProperties
    from schorg.BreadcrumbList import AllProperties
    from schorg.BreadcrumbList import create_schema_org_model
    from schorg.BreadcrumbList import BreadcrumbList

    a = create_schema_org_model(type_=BreadcrumbListInheritedProperties)
    b = create_schema_org_model(type_=BreadcrumbListProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    BreadcrumbList.schema()


def MedicalObservationalStudyDesign_test():
    from schorg.MedicalObservationalStudyDesign import MedicalObservationalStudyDesignInheritedProperties
    from schorg.MedicalObservationalStudyDesign import MedicalObservationalStudyDesignProperties
    from schorg.MedicalObservationalStudyDesign import AllProperties
    from schorg.MedicalObservationalStudyDesign import create_schema_org_model
    from schorg.MedicalObservationalStudyDesign import MedicalObservationalStudyDesign

    a = create_schema_org_model(type_=MedicalObservationalStudyDesignInheritedProperties)
    b = create_schema_org_model(type_=MedicalObservationalStudyDesignProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MedicalObservationalStudyDesign.schema()


def Observational_test():
    from schorg.Observational import ObservationalInheritedProperties
    from schorg.Observational import ObservationalProperties
    from schorg.Observational import AllProperties
    from schorg.Observational import create_schema_org_model
    from schorg.Observational import Observational

    a = create_schema_org_model(type_=ObservationalInheritedProperties)
    b = create_schema_org_model(type_=ObservationalProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Observational.schema()


def LandmarksOrHistoricalBuildings_test():
    from schorg.LandmarksOrHistoricalBuildings import LandmarksOrHistoricalBuildingsInheritedProperties
    from schorg.LandmarksOrHistoricalBuildings import LandmarksOrHistoricalBuildingsProperties
    from schorg.LandmarksOrHistoricalBuildings import AllProperties
    from schorg.LandmarksOrHistoricalBuildings import create_schema_org_model
    from schorg.LandmarksOrHistoricalBuildings import LandmarksOrHistoricalBuildings

    a = create_schema_org_model(type_=LandmarksOrHistoricalBuildingsInheritedProperties)
    b = create_schema_org_model(type_=LandmarksOrHistoricalBuildingsProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    LandmarksOrHistoricalBuildings.schema()


def Seat_test():
    from schorg.Seat import SeatInheritedProperties
    from schorg.Seat import SeatProperties
    from schorg.Seat import AllProperties
    from schorg.Seat import create_schema_org_model
    from schorg.Seat import Seat

    a = create_schema_org_model(type_=SeatInheritedProperties)
    b = create_schema_org_model(type_=SeatProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Seat.schema()


def PaymentService_test():
    from schorg.PaymentService import PaymentServiceInheritedProperties
    from schorg.PaymentService import PaymentServiceProperties
    from schorg.PaymentService import AllProperties
    from schorg.PaymentService import create_schema_org_model
    from schorg.PaymentService import PaymentService

    a = create_schema_org_model(type_=PaymentServiceInheritedProperties)
    b = create_schema_org_model(type_=PaymentServiceProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    PaymentService.schema()


def PercutaneousProcedure_test():
    from schorg.PercutaneousProcedure import PercutaneousProcedureInheritedProperties
    from schorg.PercutaneousProcedure import PercutaneousProcedureProperties
    from schorg.PercutaneousProcedure import AllProperties
    from schorg.PercutaneousProcedure import create_schema_org_model
    from schorg.PercutaneousProcedure import PercutaneousProcedure

    a = create_schema_org_model(type_=PercutaneousProcedureInheritedProperties)
    b = create_schema_org_model(type_=PercutaneousProcedureProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    PercutaneousProcedure.schema()


def OpenTrial_test():
    from schorg.OpenTrial import OpenTrialInheritedProperties
    from schorg.OpenTrial import OpenTrialProperties
    from schorg.OpenTrial import AllProperties
    from schorg.OpenTrial import create_schema_org_model
    from schorg.OpenTrial import OpenTrial

    a = create_schema_org_model(type_=OpenTrialInheritedProperties)
    b = create_schema_org_model(type_=OpenTrialProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    OpenTrial.schema()


def PaymentDeclined_test():
    from schorg.PaymentDeclined import PaymentDeclinedInheritedProperties
    from schorg.PaymentDeclined import PaymentDeclinedProperties
    from schorg.PaymentDeclined import AllProperties
    from schorg.PaymentDeclined import create_schema_org_model
    from schorg.PaymentDeclined import PaymentDeclined

    a = create_schema_org_model(type_=PaymentDeclinedInheritedProperties)
    b = create_schema_org_model(type_=PaymentDeclinedProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    PaymentDeclined.schema()


def MusicAlbumProductionType_test():
    from schorg.MusicAlbumProductionType import MusicAlbumProductionTypeInheritedProperties
    from schorg.MusicAlbumProductionType import MusicAlbumProductionTypeProperties
    from schorg.MusicAlbumProductionType import AllProperties
    from schorg.MusicAlbumProductionType import create_schema_org_model
    from schorg.MusicAlbumProductionType import MusicAlbumProductionType

    a = create_schema_org_model(type_=MusicAlbumProductionTypeInheritedProperties)
    b = create_schema_org_model(type_=MusicAlbumProductionTypeProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MusicAlbumProductionType.schema()


def Museum_test():
    from schorg.Museum import MuseumInheritedProperties
    from schorg.Museum import MuseumProperties
    from schorg.Museum import AllProperties
    from schorg.Museum import create_schema_org_model
    from schorg.Museum import Museum

    a = create_schema_org_model(type_=MuseumInheritedProperties)
    b = create_schema_org_model(type_=MuseumProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Museum.schema()


def Taxi_test():
    from schorg.Taxi import TaxiInheritedProperties
    from schorg.Taxi import TaxiProperties
    from schorg.Taxi import AllProperties
    from schorg.Taxi import create_schema_org_model
    from schorg.Taxi import Taxi

    a = create_schema_org_model(type_=TaxiInheritedProperties)
    b = create_schema_org_model(type_=TaxiProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Taxi.schema()


def TrainTrip_test():
    from schorg.TrainTrip import TrainTripInheritedProperties
    from schorg.TrainTrip import TrainTripProperties
    from schorg.TrainTrip import AllProperties
    from schorg.TrainTrip import create_schema_org_model
    from schorg.TrainTrip import TrainTrip

    a = create_schema_org_model(type_=TrainTripInheritedProperties)
    b = create_schema_org_model(type_=TrainTripProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    TrainTrip.schema()


def GeospatialGeometry_test():
    from schorg.GeospatialGeometry import GeospatialGeometryInheritedProperties
    from schorg.GeospatialGeometry import GeospatialGeometryProperties
    from schorg.GeospatialGeometry import AllProperties
    from schorg.GeospatialGeometry import create_schema_org_model
    from schorg.GeospatialGeometry import GeospatialGeometry

    a = create_schema_org_model(type_=GeospatialGeometryInheritedProperties)
    b = create_schema_org_model(type_=GeospatialGeometryProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    GeospatialGeometry.schema()


def HealthAndBeautyBusiness_test():
    from schorg.HealthAndBeautyBusiness import HealthAndBeautyBusinessInheritedProperties
    from schorg.HealthAndBeautyBusiness import HealthAndBeautyBusinessProperties
    from schorg.HealthAndBeautyBusiness import AllProperties
    from schorg.HealthAndBeautyBusiness import create_schema_org_model
    from schorg.HealthAndBeautyBusiness import HealthAndBeautyBusiness

    a = create_schema_org_model(type_=HealthAndBeautyBusinessInheritedProperties)
    b = create_schema_org_model(type_=HealthAndBeautyBusinessProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    HealthAndBeautyBusiness.schema()


def Nonprofit501c24_test():
    from schorg.Nonprofit501c24 import Nonprofit501c24InheritedProperties
    from schorg.Nonprofit501c24 import Nonprofit501c24Properties
    from schorg.Nonprofit501c24 import AllProperties
    from schorg.Nonprofit501c24 import create_schema_org_model
    from schorg.Nonprofit501c24 import Nonprofit501c24

    a = create_schema_org_model(type_=Nonprofit501c24InheritedProperties)
    b = create_schema_org_model(type_=Nonprofit501c24Properties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Nonprofit501c24.schema()


def Vessel_test():
    from schorg.Vessel import VesselInheritedProperties
    from schorg.Vessel import VesselProperties
    from schorg.Vessel import AllProperties
    from schorg.Vessel import create_schema_org_model
    from schorg.Vessel import Vessel

    a = create_schema_org_model(type_=VesselInheritedProperties)
    b = create_schema_org_model(type_=VesselProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Vessel.schema()


def Vein_test():
    from schorg.Vein import VeinInheritedProperties
    from schorg.Vein import VeinProperties
    from schorg.Vein import AllProperties
    from schorg.Vein import create_schema_org_model
    from schorg.Vein import Vein

    a = create_schema_org_model(type_=VeinInheritedProperties)
    b = create_schema_org_model(type_=VeinProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Vein.schema()


def ItemListOrderType_test():
    from schorg.ItemListOrderType import ItemListOrderTypeInheritedProperties
    from schorg.ItemListOrderType import ItemListOrderTypeProperties
    from schorg.ItemListOrderType import AllProperties
    from schorg.ItemListOrderType import create_schema_org_model
    from schorg.ItemListOrderType import ItemListOrderType

    a = create_schema_org_model(type_=ItemListOrderTypeInheritedProperties)
    b = create_schema_org_model(type_=ItemListOrderTypeProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ItemListOrderType.schema()


def ItemListOrderDescending_test():
    from schorg.ItemListOrderDescending import ItemListOrderDescendingInheritedProperties
    from schorg.ItemListOrderDescending import ItemListOrderDescendingProperties
    from schorg.ItemListOrderDescending import AllProperties
    from schorg.ItemListOrderDescending import create_schema_org_model
    from schorg.ItemListOrderDescending import ItemListOrderDescending

    a = create_schema_org_model(type_=ItemListOrderDescendingInheritedProperties)
    b = create_schema_org_model(type_=ItemListOrderDescendingProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ItemListOrderDescending.schema()


def MedicalEvidenceLevel_test():
    from schorg.MedicalEvidenceLevel import MedicalEvidenceLevelInheritedProperties
    from schorg.MedicalEvidenceLevel import MedicalEvidenceLevelProperties
    from schorg.MedicalEvidenceLevel import AllProperties
    from schorg.MedicalEvidenceLevel import create_schema_org_model
    from schorg.MedicalEvidenceLevel import MedicalEvidenceLevel

    a = create_schema_org_model(type_=MedicalEvidenceLevelInheritedProperties)
    b = create_schema_org_model(type_=MedicalEvidenceLevelProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MedicalEvidenceLevel.schema()


def EvidenceLevelC_test():
    from schorg.EvidenceLevelC import EvidenceLevelCInheritedProperties
    from schorg.EvidenceLevelC import EvidenceLevelCProperties
    from schorg.EvidenceLevelC import AllProperties
    from schorg.EvidenceLevelC import create_schema_org_model
    from schorg.EvidenceLevelC import EvidenceLevelC

    a = create_schema_org_model(type_=EvidenceLevelCInheritedProperties)
    b = create_schema_org_model(type_=EvidenceLevelCProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    EvidenceLevelC.schema()


def Artery_test():
    from schorg.Artery import ArteryInheritedProperties
    from schorg.Artery import ArteryProperties
    from schorg.Artery import AllProperties
    from schorg.Artery import create_schema_org_model
    from schorg.Artery import Artery

    a = create_schema_org_model(type_=ArteryInheritedProperties)
    b = create_schema_org_model(type_=ArteryProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Artery.schema()


def NoninvasiveProcedure_test():
    from schorg.NoninvasiveProcedure import NoninvasiveProcedureInheritedProperties
    from schorg.NoninvasiveProcedure import NoninvasiveProcedureProperties
    from schorg.NoninvasiveProcedure import AllProperties
    from schorg.NoninvasiveProcedure import create_schema_org_model
    from schorg.NoninvasiveProcedure import NoninvasiveProcedure

    a = create_schema_org_model(type_=NoninvasiveProcedureInheritedProperties)
    b = create_schema_org_model(type_=NoninvasiveProcedureProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    NoninvasiveProcedure.schema()


def SiteNavigationElement_test():
    from schorg.SiteNavigationElement import SiteNavigationElementInheritedProperties
    from schorg.SiteNavigationElement import SiteNavigationElementProperties
    from schorg.SiteNavigationElement import AllProperties
    from schorg.SiteNavigationElement import create_schema_org_model
    from schorg.SiteNavigationElement import SiteNavigationElement

    a = create_schema_org_model(type_=SiteNavigationElementInheritedProperties)
    b = create_schema_org_model(type_=SiteNavigationElementProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    SiteNavigationElement.schema()


def Neck_test():
    from schorg.Neck import NeckInheritedProperties
    from schorg.Neck import NeckProperties
    from schorg.Neck import AllProperties
    from schorg.Neck import create_schema_org_model
    from schorg.Neck import Neck

    a = create_schema_org_model(type_=NeckInheritedProperties)
    b = create_schema_org_model(type_=NeckProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Neck.schema()


def DoseSchedule_test():
    from schorg.DoseSchedule import DoseScheduleInheritedProperties
    from schorg.DoseSchedule import DoseScheduleProperties
    from schorg.DoseSchedule import AllProperties
    from schorg.DoseSchedule import create_schema_org_model
    from schorg.DoseSchedule import DoseSchedule

    a = create_schema_org_model(type_=DoseScheduleInheritedProperties)
    b = create_schema_org_model(type_=DoseScheduleProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    DoseSchedule.schema()


def ReturnLabelSourceEnumeration_test():
    from schorg.ReturnLabelSourceEnumeration import ReturnLabelSourceEnumerationInheritedProperties
    from schorg.ReturnLabelSourceEnumeration import ReturnLabelSourceEnumerationProperties
    from schorg.ReturnLabelSourceEnumeration import AllProperties
    from schorg.ReturnLabelSourceEnumeration import create_schema_org_model
    from schorg.ReturnLabelSourceEnumeration import ReturnLabelSourceEnumeration

    a = create_schema_org_model(type_=ReturnLabelSourceEnumerationInheritedProperties)
    b = create_schema_org_model(type_=ReturnLabelSourceEnumerationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ReturnLabelSourceEnumeration.schema()


def ReturnLabelInBox_test():
    from schorg.ReturnLabelInBox import ReturnLabelInBoxInheritedProperties
    from schorg.ReturnLabelInBox import ReturnLabelInBoxProperties
    from schorg.ReturnLabelInBox import AllProperties
    from schorg.ReturnLabelInBox import create_schema_org_model
    from schorg.ReturnLabelInBox import ReturnLabelInBox

    a = create_schema_org_model(type_=ReturnLabelInBoxInheritedProperties)
    b = create_schema_org_model(type_=ReturnLabelInBoxProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ReturnLabelInBox.schema()


def HealthcareConsideration_test():
    from schorg.HealthcareConsideration import HealthcareConsiderationInheritedProperties
    from schorg.HealthcareConsideration import HealthcareConsiderationProperties
    from schorg.HealthcareConsideration import AllProperties
    from schorg.HealthcareConsideration import create_schema_org_model
    from schorg.HealthcareConsideration import HealthcareConsideration

    a = create_schema_org_model(type_=HealthcareConsiderationInheritedProperties)
    b = create_schema_org_model(type_=HealthcareConsiderationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    HealthcareConsideration.schema()


def InformAction_test():
    from schorg.InformAction import InformActionInheritedProperties
    from schorg.InformAction import InformActionProperties
    from schorg.InformAction import AllProperties
    from schorg.InformAction import create_schema_org_model
    from schorg.InformAction import InformAction

    a = create_schema_org_model(type_=InformActionInheritedProperties)
    b = create_schema_org_model(type_=InformActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    InformAction.schema()


def ConfirmAction_test():
    from schorg.ConfirmAction import ConfirmActionInheritedProperties
    from schorg.ConfirmAction import ConfirmActionProperties
    from schorg.ConfirmAction import AllProperties
    from schorg.ConfirmAction import create_schema_org_model
    from schorg.ConfirmAction import ConfirmAction

    a = create_schema_org_model(type_=ConfirmActionInheritedProperties)
    b = create_schema_org_model(type_=ConfirmActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ConfirmAction.schema()


def FoodService_test():
    from schorg.FoodService import FoodServiceInheritedProperties
    from schorg.FoodService import FoodServiceProperties
    from schorg.FoodService import AllProperties
    from schorg.FoodService import create_schema_org_model
    from schorg.FoodService import FoodService

    a = create_schema_org_model(type_=FoodServiceInheritedProperties)
    b = create_schema_org_model(type_=FoodServiceProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    FoodService.schema()


def ControlAction_test():
    from schorg.ControlAction import ControlActionInheritedProperties
    from schorg.ControlAction import ControlActionProperties
    from schorg.ControlAction import AllProperties
    from schorg.ControlAction import create_schema_org_model
    from schorg.ControlAction import ControlAction

    a = create_schema_org_model(type_=ControlActionInheritedProperties)
    b = create_schema_org_model(type_=ControlActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ControlAction.schema()


def DeactivateAction_test():
    from schorg.DeactivateAction import DeactivateActionInheritedProperties
    from schorg.DeactivateAction import DeactivateActionProperties
    from schorg.DeactivateAction import AllProperties
    from schorg.DeactivateAction import create_schema_org_model
    from schorg.DeactivateAction import DeactivateAction

    a = create_schema_org_model(type_=DeactivateActionInheritedProperties)
    b = create_schema_org_model(type_=DeactivateActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    DeactivateAction.schema()


def TheaterGroup_test():
    from schorg.TheaterGroup import TheaterGroupInheritedProperties
    from schorg.TheaterGroup import TheaterGroupProperties
    from schorg.TheaterGroup import AllProperties
    from schorg.TheaterGroup import create_schema_org_model
    from schorg.TheaterGroup import TheaterGroup

    a = create_schema_org_model(type_=TheaterGroupInheritedProperties)
    b = create_schema_org_model(type_=TheaterGroupProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    TheaterGroup.schema()


def OrderPaymentDue_test():
    from schorg.OrderPaymentDue import OrderPaymentDueInheritedProperties
    from schorg.OrderPaymentDue import OrderPaymentDueProperties
    from schorg.OrderPaymentDue import AllProperties
    from schorg.OrderPaymentDue import create_schema_org_model
    from schorg.OrderPaymentDue import OrderPaymentDue

    a = create_schema_org_model(type_=OrderPaymentDueInheritedProperties)
    b = create_schema_org_model(type_=OrderPaymentDueProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    OrderPaymentDue.schema()


def AutoRental_test():
    from schorg.AutoRental import AutoRentalInheritedProperties
    from schorg.AutoRental import AutoRentalProperties
    from schorg.AutoRental import AllProperties
    from schorg.AutoRental import create_schema_org_model
    from schorg.AutoRental import AutoRental

    a = create_schema_org_model(type_=AutoRentalInheritedProperties)
    b = create_schema_org_model(type_=AutoRentalProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    AutoRental.schema()


def DigitalFormat_test():
    from schorg.DigitalFormat import DigitalFormatInheritedProperties
    from schorg.DigitalFormat import DigitalFormatProperties
    from schorg.DigitalFormat import AllProperties
    from schorg.DigitalFormat import create_schema_org_model
    from schorg.DigitalFormat import DigitalFormat

    a = create_schema_org_model(type_=DigitalFormatInheritedProperties)
    b = create_schema_org_model(type_=DigitalFormatProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    DigitalFormat.schema()


def InviteAction_test():
    from schorg.InviteAction import InviteActionInheritedProperties
    from schorg.InviteAction import InviteActionProperties
    from schorg.InviteAction import AllProperties
    from schorg.InviteAction import create_schema_org_model
    from schorg.InviteAction import InviteAction

    a = create_schema_org_model(type_=InviteActionInheritedProperties)
    b = create_schema_org_model(type_=InviteActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    InviteAction.schema()


def PodcastSeries_test():
    from schorg.PodcastSeries import PodcastSeriesInheritedProperties
    from schorg.PodcastSeries import PodcastSeriesProperties
    from schorg.PodcastSeries import AllProperties
    from schorg.PodcastSeries import create_schema_org_model
    from schorg.PodcastSeries import PodcastSeries

    a = create_schema_org_model(type_=PodcastSeriesInheritedProperties)
    b = create_schema_org_model(type_=PodcastSeriesProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    PodcastSeries.schema()


def SizeSpecification_test():
    from schorg.SizeSpecification import SizeSpecificationInheritedProperties
    from schorg.SizeSpecification import SizeSpecificationProperties
    from schorg.SizeSpecification import AllProperties
    from schorg.SizeSpecification import create_schema_org_model
    from schorg.SizeSpecification import SizeSpecification

    a = create_schema_org_model(type_=SizeSpecificationInheritedProperties)
    b = create_schema_org_model(type_=SizeSpecificationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    SizeSpecification.schema()


def WebContent_test():
    from schorg.WebContent import WebContentInheritedProperties
    from schorg.WebContent import WebContentProperties
    from schorg.WebContent import AllProperties
    from schorg.WebContent import create_schema_org_model
    from schorg.WebContent import WebContent

    a = create_schema_org_model(type_=WebContentInheritedProperties)
    b = create_schema_org_model(type_=WebContentProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    WebContent.schema()


def HealthTopicContent_test():
    from schorg.HealthTopicContent import HealthTopicContentInheritedProperties
    from schorg.HealthTopicContent import HealthTopicContentProperties
    from schorg.HealthTopicContent import AllProperties
    from schorg.HealthTopicContent import create_schema_org_model
    from schorg.HealthTopicContent import HealthTopicContent

    a = create_schema_org_model(type_=HealthTopicContentInheritedProperties)
    b = create_schema_org_model(type_=HealthTopicContentProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    HealthTopicContent.schema()


def CriticReview_test():
    from schorg.CriticReview import CriticReviewInheritedProperties
    from schorg.CriticReview import CriticReviewProperties
    from schorg.CriticReview import AllProperties
    from schorg.CriticReview import create_schema_org_model
    from schorg.CriticReview import CriticReview

    a = create_schema_org_model(type_=CriticReviewInheritedProperties)
    b = create_schema_org_model(type_=CriticReviewProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    CriticReview.schema()


def CleaningFee_test():
    from schorg.CleaningFee import CleaningFeeInheritedProperties
    from schorg.CleaningFee import CleaningFeeProperties
    from schorg.CleaningFee import AllProperties
    from schorg.CleaningFee import create_schema_org_model
    from schorg.CleaningFee import CleaningFee

    a = create_schema_org_model(type_=CleaningFeeInheritedProperties)
    b = create_schema_org_model(type_=CleaningFeeProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    CleaningFee.schema()


def Aquarium_test():
    from schorg.Aquarium import AquariumInheritedProperties
    from schorg.Aquarium import AquariumProperties
    from schorg.Aquarium import AllProperties
    from schorg.Aquarium import create_schema_org_model
    from schorg.Aquarium import Aquarium

    a = create_schema_org_model(type_=AquariumInheritedProperties)
    b = create_schema_org_model(type_=AquariumProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Aquarium.schema()


def WearableSizeSystemIT_test():
    from schorg.WearableSizeSystemIT import WearableSizeSystemITInheritedProperties
    from schorg.WearableSizeSystemIT import WearableSizeSystemITProperties
    from schorg.WearableSizeSystemIT import AllProperties
    from schorg.WearableSizeSystemIT import create_schema_org_model
    from schorg.WearableSizeSystemIT import WearableSizeSystemIT

    a = create_schema_org_model(type_=WearableSizeSystemITInheritedProperties)
    b = create_schema_org_model(type_=WearableSizeSystemITProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    WearableSizeSystemIT.schema()


def PublicSwimmingPool_test():
    from schorg.PublicSwimmingPool import PublicSwimmingPoolInheritedProperties
    from schorg.PublicSwimmingPool import PublicSwimmingPoolProperties
    from schorg.PublicSwimmingPool import AllProperties
    from schorg.PublicSwimmingPool import create_schema_org_model
    from schorg.PublicSwimmingPool import PublicSwimmingPool

    a = create_schema_org_model(type_=PublicSwimmingPoolInheritedProperties)
    b = create_schema_org_model(type_=PublicSwimmingPoolProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    PublicSwimmingPool.schema()


def WearableSizeGroupPlus_test():
    from schorg.WearableSizeGroupPlus import WearableSizeGroupPlusInheritedProperties
    from schorg.WearableSizeGroupPlus import WearableSizeGroupPlusProperties
    from schorg.WearableSizeGroupPlus import AllProperties
    from schorg.WearableSizeGroupPlus import create_schema_org_model
    from schorg.WearableSizeGroupPlus import WearableSizeGroupPlus

    a = create_schema_org_model(type_=WearableSizeGroupPlusInheritedProperties)
    b = create_schema_org_model(type_=WearableSizeGroupPlusProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    WearableSizeGroupPlus.schema()


def PodcastEpisode_test():
    from schorg.PodcastEpisode import PodcastEpisodeInheritedProperties
    from schorg.PodcastEpisode import PodcastEpisodeProperties
    from schorg.PodcastEpisode import AllProperties
    from schorg.PodcastEpisode import create_schema_org_model
    from schorg.PodcastEpisode import PodcastEpisode

    a = create_schema_org_model(type_=PodcastEpisodeInheritedProperties)
    b = create_schema_org_model(type_=PodcastEpisodeProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    PodcastEpisode.schema()


def Dataset_test():
    from schorg.Dataset import DatasetInheritedProperties
    from schorg.Dataset import DatasetProperties
    from schorg.Dataset import AllProperties
    from schorg.Dataset import create_schema_org_model
    from schorg.Dataset import Dataset

    a = create_schema_org_model(type_=DatasetInheritedProperties)
    b = create_schema_org_model(type_=DatasetProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Dataset.schema()


def Conversation_test():
    from schorg.Conversation import ConversationInheritedProperties
    from schorg.Conversation import ConversationProperties
    from schorg.Conversation import AllProperties
    from schorg.Conversation import create_schema_org_model
    from schorg.Conversation import Conversation

    a = create_schema_org_model(type_=ConversationInheritedProperties)
    b = create_schema_org_model(type_=ConversationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Conversation.schema()


def MedicalOrganization_test():
    from schorg.MedicalOrganization import MedicalOrganizationInheritedProperties
    from schorg.MedicalOrganization import MedicalOrganizationProperties
    from schorg.MedicalOrganization import AllProperties
    from schorg.MedicalOrganization import create_schema_org_model
    from schorg.MedicalOrganization import MedicalOrganization

    a = create_schema_org_model(type_=MedicalOrganizationInheritedProperties)
    b = create_schema_org_model(type_=MedicalOrganizationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MedicalOrganization.schema()


def MedicalClinic_test():
    from schorg.MedicalClinic import MedicalClinicInheritedProperties
    from schorg.MedicalClinic import MedicalClinicProperties
    from schorg.MedicalClinic import AllProperties
    from schorg.MedicalClinic import create_schema_org_model
    from schorg.MedicalClinic import MedicalClinic

    a = create_schema_org_model(type_=MedicalClinicInheritedProperties)
    b = create_schema_org_model(type_=MedicalClinicProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MedicalClinic.schema()


def CovidTestingFacility_test():
    from schorg.CovidTestingFacility import CovidTestingFacilityInheritedProperties
    from schorg.CovidTestingFacility import CovidTestingFacilityProperties
    from schorg.CovidTestingFacility import AllProperties
    from schorg.CovidTestingFacility import create_schema_org_model
    from schorg.CovidTestingFacility import CovidTestingFacility

    a = create_schema_org_model(type_=CovidTestingFacilityInheritedProperties)
    b = create_schema_org_model(type_=CovidTestingFacilityProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    CovidTestingFacility.schema()


def OutOfStock_test():
    from schorg.OutOfStock import OutOfStockInheritedProperties
    from schorg.OutOfStock import OutOfStockProperties
    from schorg.OutOfStock import AllProperties
    from schorg.OutOfStock import create_schema_org_model
    from schorg.OutOfStock import OutOfStock

    a = create_schema_org_model(type_=OutOfStockInheritedProperties)
    b = create_schema_org_model(type_=OutOfStockProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    OutOfStock.schema()


def PostalCodeRangeSpecification_test():
    from schorg.PostalCodeRangeSpecification import PostalCodeRangeSpecificationInheritedProperties
    from schorg.PostalCodeRangeSpecification import PostalCodeRangeSpecificationProperties
    from schorg.PostalCodeRangeSpecification import AllProperties
    from schorg.PostalCodeRangeSpecification import create_schema_org_model
    from schorg.PostalCodeRangeSpecification import PostalCodeRangeSpecification

    a = create_schema_org_model(type_=PostalCodeRangeSpecificationInheritedProperties)
    b = create_schema_org_model(type_=PostalCodeRangeSpecificationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    PostalCodeRangeSpecification.schema()


def Nonprofit501c18_test():
    from schorg.Nonprofit501c18 import Nonprofit501c18InheritedProperties
    from schorg.Nonprofit501c18 import Nonprofit501c18Properties
    from schorg.Nonprofit501c18 import AllProperties
    from schorg.Nonprofit501c18 import create_schema_org_model
    from schorg.Nonprofit501c18 import Nonprofit501c18

    a = create_schema_org_model(type_=Nonprofit501c18InheritedProperties)
    b = create_schema_org_model(type_=Nonprofit501c18Properties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Nonprofit501c18.schema()


def ReactAction_test():
    from schorg.ReactAction import ReactActionInheritedProperties
    from schorg.ReactAction import ReactActionProperties
    from schorg.ReactAction import AllProperties
    from schorg.ReactAction import create_schema_org_model
    from schorg.ReactAction import ReactAction

    a = create_schema_org_model(type_=ReactActionInheritedProperties)
    b = create_schema_org_model(type_=ReactActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ReactAction.schema()


def WantAction_test():
    from schorg.WantAction import WantActionInheritedProperties
    from schorg.WantAction import WantActionProperties
    from schorg.WantAction import AllProperties
    from schorg.WantAction import create_schema_org_model
    from schorg.WantAction import WantAction

    a = create_schema_org_model(type_=WantActionInheritedProperties)
    b = create_schema_org_model(type_=WantActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    WantAction.schema()


def MixtapeAlbum_test():
    from schorg.MixtapeAlbum import MixtapeAlbumInheritedProperties
    from schorg.MixtapeAlbum import MixtapeAlbumProperties
    from schorg.MixtapeAlbum import AllProperties
    from schorg.MixtapeAlbum import create_schema_org_model
    from schorg.MixtapeAlbum import MixtapeAlbum

    a = create_schema_org_model(type_=MixtapeAlbumInheritedProperties)
    b = create_schema_org_model(type_=MixtapeAlbumProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MixtapeAlbum.schema()


def Nonprofit501c20_test():
    from schorg.Nonprofit501c20 import Nonprofit501c20InheritedProperties
    from schorg.Nonprofit501c20 import Nonprofit501c20Properties
    from schorg.Nonprofit501c20 import AllProperties
    from schorg.Nonprofit501c20 import create_schema_org_model
    from schorg.Nonprofit501c20 import Nonprofit501c20

    a = create_schema_org_model(type_=Nonprofit501c20InheritedProperties)
    b = create_schema_org_model(type_=Nonprofit501c20Properties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Nonprofit501c20.schema()


def Nonprofit501c15_test():
    from schorg.Nonprofit501c15 import Nonprofit501c15InheritedProperties
    from schorg.Nonprofit501c15 import Nonprofit501c15Properties
    from schorg.Nonprofit501c15 import AllProperties
    from schorg.Nonprofit501c15 import create_schema_org_model
    from schorg.Nonprofit501c15 import Nonprofit501c15

    a = create_schema_org_model(type_=Nonprofit501c15InheritedProperties)
    b = create_schema_org_model(type_=Nonprofit501c15Properties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Nonprofit501c15.schema()


def BookFormatType_test():
    from schorg.BookFormatType import BookFormatTypeInheritedProperties
    from schorg.BookFormatType import BookFormatTypeProperties
    from schorg.BookFormatType import AllProperties
    from schorg.BookFormatType import create_schema_org_model
    from schorg.BookFormatType import BookFormatType

    a = create_schema_org_model(type_=BookFormatTypeInheritedProperties)
    b = create_schema_org_model(type_=BookFormatTypeProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    BookFormatType.schema()


def GraphicNovel_test():
    from schorg.GraphicNovel import GraphicNovelInheritedProperties
    from schorg.GraphicNovel import GraphicNovelProperties
    from schorg.GraphicNovel import AllProperties
    from schorg.GraphicNovel import create_schema_org_model
    from schorg.GraphicNovel import GraphicNovel

    a = create_schema_org_model(type_=GraphicNovelInheritedProperties)
    b = create_schema_org_model(type_=GraphicNovelProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    GraphicNovel.schema()


def TaxiReservation_test():
    from schorg.TaxiReservation import TaxiReservationInheritedProperties
    from schorg.TaxiReservation import TaxiReservationProperties
    from schorg.TaxiReservation import AllProperties
    from schorg.TaxiReservation import create_schema_org_model
    from schorg.TaxiReservation import TaxiReservation

    a = create_schema_org_model(type_=TaxiReservationInheritedProperties)
    b = create_schema_org_model(type_=TaxiReservationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    TaxiReservation.schema()


def Bacteria_test():
    from schorg.Bacteria import BacteriaInheritedProperties
    from schorg.Bacteria import BacteriaProperties
    from schorg.Bacteria import AllProperties
    from schorg.Bacteria import create_schema_org_model
    from schorg.Bacteria import Bacteria

    a = create_schema_org_model(type_=BacteriaInheritedProperties)
    b = create_schema_org_model(type_=BacteriaProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Bacteria.schema()


def NightClub_test():
    from schorg.NightClub import NightClubInheritedProperties
    from schorg.NightClub import NightClubProperties
    from schorg.NightClub import AllProperties
    from schorg.NightClub import create_schema_org_model
    from schorg.NightClub import NightClub

    a = create_schema_org_model(type_=NightClubInheritedProperties)
    b = create_schema_org_model(type_=NightClubProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    NightClub.schema()


def OrganizeAction_test():
    from schorg.OrganizeAction import OrganizeActionInheritedProperties
    from schorg.OrganizeAction import OrganizeActionProperties
    from schorg.OrganizeAction import AllProperties
    from schorg.OrganizeAction import create_schema_org_model
    from schorg.OrganizeAction import OrganizeAction

    a = create_schema_org_model(type_=OrganizeActionInheritedProperties)
    b = create_schema_org_model(type_=OrganizeActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    OrganizeAction.schema()


def PlanAction_test():
    from schorg.PlanAction import PlanActionInheritedProperties
    from schorg.PlanAction import PlanActionProperties
    from schorg.PlanAction import AllProperties
    from schorg.PlanAction import create_schema_org_model
    from schorg.PlanAction import PlanAction

    a = create_schema_org_model(type_=PlanActionInheritedProperties)
    b = create_schema_org_model(type_=PlanActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    PlanAction.schema()


def ScheduleAction_test():
    from schorg.ScheduleAction import ScheduleActionInheritedProperties
    from schorg.ScheduleAction import ScheduleActionProperties
    from schorg.ScheduleAction import AllProperties
    from schorg.ScheduleAction import create_schema_org_model
    from schorg.ScheduleAction import ScheduleAction

    a = create_schema_org_model(type_=ScheduleActionInheritedProperties)
    b = create_schema_org_model(type_=ScheduleActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ScheduleAction.schema()


def ScholarlyArticle_test():
    from schorg.ScholarlyArticle import ScholarlyArticleInheritedProperties
    from schorg.ScholarlyArticle import ScholarlyArticleProperties
    from schorg.ScholarlyArticle import AllProperties
    from schorg.ScholarlyArticle import create_schema_org_model
    from schorg.ScholarlyArticle import ScholarlyArticle

    a = create_schema_org_model(type_=ScholarlyArticleInheritedProperties)
    b = create_schema_org_model(type_=ScholarlyArticleProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ScholarlyArticle.schema()


def PlaceOfWorship_test():
    from schorg.PlaceOfWorship import PlaceOfWorshipInheritedProperties
    from schorg.PlaceOfWorship import PlaceOfWorshipProperties
    from schorg.PlaceOfWorship import AllProperties
    from schorg.PlaceOfWorship import create_schema_org_model
    from schorg.PlaceOfWorship import PlaceOfWorship

    a = create_schema_org_model(type_=PlaceOfWorshipInheritedProperties)
    b = create_schema_org_model(type_=PlaceOfWorshipProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    PlaceOfWorship.schema()


def BuddhistTemple_test():
    from schorg.BuddhistTemple import BuddhistTempleInheritedProperties
    from schorg.BuddhistTemple import BuddhistTempleProperties
    from schorg.BuddhistTemple import AllProperties
    from schorg.BuddhistTemple import create_schema_org_model
    from schorg.BuddhistTemple import BuddhistTemple

    a = create_schema_org_model(type_=BuddhistTempleInheritedProperties)
    b = create_schema_org_model(type_=BuddhistTempleProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    BuddhistTemple.schema()


def SatiricalArticle_test():
    from schorg.SatiricalArticle import SatiricalArticleInheritedProperties
    from schorg.SatiricalArticle import SatiricalArticleProperties
    from schorg.SatiricalArticle import AllProperties
    from schorg.SatiricalArticle import create_schema_org_model
    from schorg.SatiricalArticle import SatiricalArticle

    a = create_schema_org_model(type_=SatiricalArticleInheritedProperties)
    b = create_schema_org_model(type_=SatiricalArticleProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    SatiricalArticle.schema()


def FoodEstablishment_test():
    from schorg.FoodEstablishment import FoodEstablishmentInheritedProperties
    from schorg.FoodEstablishment import FoodEstablishmentProperties
    from schorg.FoodEstablishment import AllProperties
    from schorg.FoodEstablishment import create_schema_org_model
    from schorg.FoodEstablishment import FoodEstablishment

    a = create_schema_org_model(type_=FoodEstablishmentInheritedProperties)
    b = create_schema_org_model(type_=FoodEstablishmentProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    FoodEstablishment.schema()


def MarryAction_test():
    from schorg.MarryAction import MarryActionInheritedProperties
    from schorg.MarryAction import MarryActionProperties
    from schorg.MarryAction import AllProperties
    from schorg.MarryAction import create_schema_org_model
    from schorg.MarryAction import MarryAction

    a = create_schema_org_model(type_=MarryActionInheritedProperties)
    b = create_schema_org_model(type_=MarryActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MarryAction.schema()


def ProfilePage_test():
    from schorg.ProfilePage import ProfilePageInheritedProperties
    from schorg.ProfilePage import ProfilePageProperties
    from schorg.ProfilePage import AllProperties
    from schorg.ProfilePage import create_schema_org_model
    from schorg.ProfilePage import ProfilePage

    a = create_schema_org_model(type_=ProfilePageInheritedProperties)
    b = create_schema_org_model(type_=ProfilePageProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ProfilePage.schema()


def AmusementPark_test():
    from schorg.AmusementPark import AmusementParkInheritedProperties
    from schorg.AmusementPark import AmusementParkProperties
    from schorg.AmusementPark import AllProperties
    from schorg.AmusementPark import create_schema_org_model
    from schorg.AmusementPark import AmusementPark

    a = create_schema_org_model(type_=AmusementParkInheritedProperties)
    b = create_schema_org_model(type_=AmusementParkProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    AmusementPark.schema()


def BowlingAlley_test():
    from schorg.BowlingAlley import BowlingAlleyInheritedProperties
    from schorg.BowlingAlley import BowlingAlleyProperties
    from schorg.BowlingAlley import AllProperties
    from schorg.BowlingAlley import create_schema_org_model
    from schorg.BowlingAlley import BowlingAlley

    a = create_schema_org_model(type_=BowlingAlleyInheritedProperties)
    b = create_schema_org_model(type_=BowlingAlleyProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    BowlingAlley.schema()


def Sunday_test():
    from schorg.Sunday import SundayInheritedProperties
    from schorg.Sunday import SundayProperties
    from schorg.Sunday import AllProperties
    from schorg.Sunday import create_schema_org_model
    from schorg.Sunday import Sunday

    a = create_schema_org_model(type_=SundayInheritedProperties)
    b = create_schema_org_model(type_=SundayProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Sunday.schema()


def ScreeningHealthAspect_test():
    from schorg.ScreeningHealthAspect import ScreeningHealthAspectInheritedProperties
    from schorg.ScreeningHealthAspect import ScreeningHealthAspectProperties
    from schorg.ScreeningHealthAspect import AllProperties
    from schorg.ScreeningHealthAspect import create_schema_org_model
    from schorg.ScreeningHealthAspect import ScreeningHealthAspect

    a = create_schema_org_model(type_=ScreeningHealthAspectInheritedProperties)
    b = create_schema_org_model(type_=ScreeningHealthAspectProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ScreeningHealthAspect.schema()


def PaymentMethod_test():
    from schorg.PaymentMethod import PaymentMethodInheritedProperties
    from schorg.PaymentMethod import PaymentMethodProperties
    from schorg.PaymentMethod import AllProperties
    from schorg.PaymentMethod import create_schema_org_model
    from schorg.PaymentMethod import PaymentMethod

    a = create_schema_org_model(type_=PaymentMethodInheritedProperties)
    b = create_schema_org_model(type_=PaymentMethodProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    PaymentMethod.schema()


def PaymentCard_test():
    from schorg.PaymentCard import PaymentCardInheritedProperties
    from schorg.PaymentCard import PaymentCardProperties
    from schorg.PaymentCard import AllProperties
    from schorg.PaymentCard import create_schema_org_model
    from schorg.PaymentCard import PaymentCard

    a = create_schema_org_model(type_=PaymentCardInheritedProperties)
    b = create_schema_org_model(type_=PaymentCardProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    PaymentCard.schema()


def RespiratoryTherapy_test():
    from schorg.RespiratoryTherapy import RespiratoryTherapyInheritedProperties
    from schorg.RespiratoryTherapy import RespiratoryTherapyProperties
    from schorg.RespiratoryTherapy import AllProperties
    from schorg.RespiratoryTherapy import create_schema_org_model
    from schorg.RespiratoryTherapy import RespiratoryTherapy

    a = create_schema_org_model(type_=RespiratoryTherapyInheritedProperties)
    b = create_schema_org_model(type_=RespiratoryTherapyProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    RespiratoryTherapy.schema()


def DataFeed_test():
    from schorg.DataFeed import DataFeedInheritedProperties
    from schorg.DataFeed import DataFeedProperties
    from schorg.DataFeed import AllProperties
    from schorg.DataFeed import create_schema_org_model
    from schorg.DataFeed import DataFeed

    a = create_schema_org_model(type_=DataFeedInheritedProperties)
    b = create_schema_org_model(type_=DataFeedProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    DataFeed.schema()


def CarUsageType_test():
    from schorg.CarUsageType import CarUsageTypeInheritedProperties
    from schorg.CarUsageType import CarUsageTypeProperties
    from schorg.CarUsageType import AllProperties
    from schorg.CarUsageType import create_schema_org_model
    from schorg.CarUsageType import CarUsageType

    a = create_schema_org_model(type_=CarUsageTypeInheritedProperties)
    b = create_schema_org_model(type_=CarUsageTypeProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    CarUsageType.schema()


def TaxiVehicleUsage_test():
    from schorg.TaxiVehicleUsage import TaxiVehicleUsageInheritedProperties
    from schorg.TaxiVehicleUsage import TaxiVehicleUsageProperties
    from schorg.TaxiVehicleUsage import AllProperties
    from schorg.TaxiVehicleUsage import create_schema_org_model
    from schorg.TaxiVehicleUsage import TaxiVehicleUsage

    a = create_schema_org_model(type_=TaxiVehicleUsageInheritedProperties)
    b = create_schema_org_model(type_=TaxiVehicleUsageProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    TaxiVehicleUsage.schema()


def ElectronicsStore_test():
    from schorg.ElectronicsStore import ElectronicsStoreInheritedProperties
    from schorg.ElectronicsStore import ElectronicsStoreProperties
    from schorg.ElectronicsStore import AllProperties
    from schorg.ElectronicsStore import create_schema_org_model
    from schorg.ElectronicsStore import ElectronicsStore

    a = create_schema_org_model(type_=ElectronicsStoreInheritedProperties)
    b = create_schema_org_model(type_=ElectronicsStoreProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ElectronicsStore.schema()


def Toxicologic_test():
    from schorg.Toxicologic import ToxicologicInheritedProperties
    from schorg.Toxicologic import ToxicologicProperties
    from schorg.Toxicologic import AllProperties
    from schorg.Toxicologic import create_schema_org_model
    from schorg.Toxicologic import Toxicologic

    a = create_schema_org_model(type_=ToxicologicInheritedProperties)
    b = create_schema_org_model(type_=ToxicologicProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Toxicologic.schema()


def CDFormat_test():
    from schorg.CDFormat import CDFormatInheritedProperties
    from schorg.CDFormat import CDFormatProperties
    from schorg.CDFormat import AllProperties
    from schorg.CDFormat import create_schema_org_model
    from schorg.CDFormat import CDFormat

    a = create_schema_org_model(type_=CDFormatInheritedProperties)
    b = create_schema_org_model(type_=CDFormatProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    CDFormat.schema()


def VideoGameClip_test():
    from schorg.VideoGameClip import VideoGameClipInheritedProperties
    from schorg.VideoGameClip import VideoGameClipProperties
    from schorg.VideoGameClip import AllProperties
    from schorg.VideoGameClip import create_schema_org_model
    from schorg.VideoGameClip import VideoGameClip

    a = create_schema_org_model(type_=VideoGameClipInheritedProperties)
    b = create_schema_org_model(type_=VideoGameClipProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    VideoGameClip.schema()


def AchieveAction_test():
    from schorg.AchieveAction import AchieveActionInheritedProperties
    from schorg.AchieveAction import AchieveActionProperties
    from schorg.AchieveAction import AllProperties
    from schorg.AchieveAction import create_schema_org_model
    from schorg.AchieveAction import AchieveAction

    a = create_schema_org_model(type_=AchieveActionInheritedProperties)
    b = create_schema_org_model(type_=AchieveActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    AchieveAction.schema()


def TieAction_test():
    from schorg.TieAction import TieActionInheritedProperties
    from schorg.TieAction import TieActionProperties
    from schorg.TieAction import AllProperties
    from schorg.TieAction import create_schema_org_model
    from schorg.TieAction import TieAction

    a = create_schema_org_model(type_=TieActionInheritedProperties)
    b = create_schema_org_model(type_=TieActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    TieAction.schema()


def AllWheelDriveConfiguration_test():
    from schorg.AllWheelDriveConfiguration import AllWheelDriveConfigurationInheritedProperties
    from schorg.AllWheelDriveConfiguration import AllWheelDriveConfigurationProperties
    from schorg.AllWheelDriveConfiguration import AllProperties
    from schorg.AllWheelDriveConfiguration import create_schema_org_model
    from schorg.AllWheelDriveConfiguration import AllWheelDriveConfiguration

    a = create_schema_org_model(type_=AllWheelDriveConfigurationInheritedProperties)
    b = create_schema_org_model(type_=AllWheelDriveConfigurationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    AllWheelDriveConfiguration.schema()


def Bone_test():
    from schorg.Bone import BoneInheritedProperties
    from schorg.Bone import BoneProperties
    from schorg.Bone import AllProperties
    from schorg.Bone import create_schema_org_model
    from schorg.Bone import Bone

    a = create_schema_org_model(type_=BoneInheritedProperties)
    b = create_schema_org_model(type_=BoneProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Bone.schema()


def BroadcastChannel_test():
    from schorg.BroadcastChannel import BroadcastChannelInheritedProperties
    from schorg.BroadcastChannel import BroadcastChannelProperties
    from schorg.BroadcastChannel import AllProperties
    from schorg.BroadcastChannel import create_schema_org_model
    from schorg.BroadcastChannel import BroadcastChannel

    a = create_schema_org_model(type_=BroadcastChannelInheritedProperties)
    b = create_schema_org_model(type_=BroadcastChannelProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    BroadcastChannel.schema()


def RadioChannel_test():
    from schorg.RadioChannel import RadioChannelInheritedProperties
    from schorg.RadioChannel import RadioChannelProperties
    from schorg.RadioChannel import AllProperties
    from schorg.RadioChannel import create_schema_org_model
    from schorg.RadioChannel import RadioChannel

    a = create_schema_org_model(type_=RadioChannelInheritedProperties)
    b = create_schema_org_model(type_=RadioChannelProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    RadioChannel.schema()


def AMRadioChannel_test():
    from schorg.AMRadioChannel import AMRadioChannelInheritedProperties
    from schorg.AMRadioChannel import AMRadioChannelProperties
    from schorg.AMRadioChannel import AllProperties
    from schorg.AMRadioChannel import create_schema_org_model
    from schorg.AMRadioChannel import AMRadioChannel

    a = create_schema_org_model(type_=AMRadioChannelInheritedProperties)
    b = create_schema_org_model(type_=AMRadioChannelProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    AMRadioChannel.schema()


def PET_test():
    from schorg.PET import PETInheritedProperties
    from schorg.PET import PETProperties
    from schorg.PET import AllProperties
    from schorg.PET import create_schema_org_model
    from schorg.PET import PET

    a = create_schema_org_model(type_=PETInheritedProperties)
    b = create_schema_org_model(type_=PETProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    PET.schema()


def MusicAlbumReleaseType_test():
    from schorg.MusicAlbumReleaseType import MusicAlbumReleaseTypeInheritedProperties
    from schorg.MusicAlbumReleaseType import MusicAlbumReleaseTypeProperties
    from schorg.MusicAlbumReleaseType import AllProperties
    from schorg.MusicAlbumReleaseType import create_schema_org_model
    from schorg.MusicAlbumReleaseType import MusicAlbumReleaseType

    a = create_schema_org_model(type_=MusicAlbumReleaseTypeInheritedProperties)
    b = create_schema_org_model(type_=MusicAlbumReleaseTypeProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MusicAlbumReleaseType.schema()


def Nonprofit501n_test():
    from schorg.Nonprofit501n import Nonprofit501nInheritedProperties
    from schorg.Nonprofit501n import Nonprofit501nProperties
    from schorg.Nonprofit501n import AllProperties
    from schorg.Nonprofit501n import create_schema_org_model
    from schorg.Nonprofit501n import Nonprofit501n

    a = create_schema_org_model(type_=Nonprofit501nInheritedProperties)
    b = create_schema_org_model(type_=Nonprofit501nProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Nonprofit501n.schema()


def Project_test():
    from schorg.Project import ProjectInheritedProperties
    from schorg.Project import ProjectProperties
    from schorg.Project import AllProperties
    from schorg.Project import create_schema_org_model
    from schorg.Project import Project

    a = create_schema_org_model(type_=ProjectInheritedProperties)
    b = create_schema_org_model(type_=ProjectProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Project.schema()


def ResearchProject_test():
    from schorg.ResearchProject import ResearchProjectInheritedProperties
    from schorg.ResearchProject import ResearchProjectProperties
    from schorg.ResearchProject import AllProperties
    from schorg.ResearchProject import create_schema_org_model
    from schorg.ResearchProject import ResearchProject

    a = create_schema_org_model(type_=ResearchProjectInheritedProperties)
    b = create_schema_org_model(type_=ResearchProjectProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ResearchProject.schema()


def DislikeAction_test():
    from schorg.DislikeAction import DislikeActionInheritedProperties
    from schorg.DislikeAction import DislikeActionProperties
    from schorg.DislikeAction import AllProperties
    from schorg.DislikeAction import create_schema_org_model
    from schorg.DislikeAction import DislikeAction

    a = create_schema_org_model(type_=DislikeActionInheritedProperties)
    b = create_schema_org_model(type_=DislikeActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    DislikeAction.schema()


def Schedule_test():
    from schorg.Schedule import ScheduleInheritedProperties
    from schorg.Schedule import ScheduleProperties
    from schorg.Schedule import AllProperties
    from schorg.Schedule import create_schema_org_model
    from schorg.Schedule import Schedule

    a = create_schema_org_model(type_=ScheduleInheritedProperties)
    b = create_schema_org_model(type_=ScheduleProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Schedule.schema()


def ContactPage_test():
    from schorg.ContactPage import ContactPageInheritedProperties
    from schorg.ContactPage import ContactPageProperties
    from schorg.ContactPage import AllProperties
    from schorg.ContactPage import create_schema_org_model
    from schorg.ContactPage import ContactPage

    a = create_schema_org_model(type_=ContactPageInheritedProperties)
    b = create_schema_org_model(type_=ContactPageProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ContactPage.schema()


def AlignmentObject_test():
    from schorg.AlignmentObject import AlignmentObjectInheritedProperties
    from schorg.AlignmentObject import AlignmentObjectProperties
    from schorg.AlignmentObject import AllProperties
    from schorg.AlignmentObject import create_schema_org_model
    from schorg.AlignmentObject import AlignmentObject

    a = create_schema_org_model(type_=AlignmentObjectInheritedProperties)
    b = create_schema_org_model(type_=AlignmentObjectProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    AlignmentObject.schema()


def PriceSpecification_test():
    from schorg.PriceSpecification import PriceSpecificationInheritedProperties
    from schorg.PriceSpecification import PriceSpecificationProperties
    from schorg.PriceSpecification import AllProperties
    from schorg.PriceSpecification import create_schema_org_model
    from schorg.PriceSpecification import PriceSpecification

    a = create_schema_org_model(type_=PriceSpecificationInheritedProperties)
    b = create_schema_org_model(type_=PriceSpecificationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    PriceSpecification.schema()


def PaymentChargeSpecification_test():
    from schorg.PaymentChargeSpecification import PaymentChargeSpecificationInheritedProperties
    from schorg.PaymentChargeSpecification import PaymentChargeSpecificationProperties
    from schorg.PaymentChargeSpecification import AllProperties
    from schorg.PaymentChargeSpecification import create_schema_org_model
    from schorg.PaymentChargeSpecification import PaymentChargeSpecification

    a = create_schema_org_model(type_=PaymentChargeSpecificationInheritedProperties)
    b = create_schema_org_model(type_=PaymentChargeSpecificationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    PaymentChargeSpecification.schema()


def WebAPI_test():
    from schorg.WebAPI import WebAPIInheritedProperties
    from schorg.WebAPI import WebAPIProperties
    from schorg.WebAPI import AllProperties
    from schorg.WebAPI import create_schema_org_model
    from schorg.WebAPI import WebAPI

    a = create_schema_org_model(type_=WebAPIInheritedProperties)
    b = create_schema_org_model(type_=WebAPIProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    WebAPI.schema()


def TVClip_test():
    from schorg.TVClip import TVClipInheritedProperties
    from schorg.TVClip import TVClipProperties
    from schorg.TVClip import AllProperties
    from schorg.TVClip import create_schema_org_model
    from schorg.TVClip import TVClip

    a = create_schema_org_model(type_=TVClipInheritedProperties)
    b = create_schema_org_model(type_=TVClipProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    TVClip.schema()


def Quantity_test():
    from schorg.Quantity import QuantityInheritedProperties
    from schorg.Quantity import QuantityProperties
    from schorg.Quantity import AllProperties
    from schorg.Quantity import create_schema_org_model
    from schorg.Quantity import Quantity

    a = create_schema_org_model(type_=QuantityInheritedProperties)
    b = create_schema_org_model(type_=QuantityProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Quantity.schema()


def Mass_test():
    from schorg.Mass import MassInheritedProperties
    from schorg.Mass import MassProperties
    from schorg.Mass import AllProperties
    from schorg.Mass import create_schema_org_model
    from schorg.Mass import Mass

    a = create_schema_org_model(type_=MassInheritedProperties)
    b = create_schema_org_model(type_=MassProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Mass.schema()


def GenderType_test():
    from schorg.GenderType import GenderTypeInheritedProperties
    from schorg.GenderType import GenderTypeProperties
    from schorg.GenderType import AllProperties
    from schorg.GenderType import create_schema_org_model
    from schorg.GenderType import GenderType

    a = create_schema_org_model(type_=GenderTypeInheritedProperties)
    b = create_schema_org_model(type_=GenderTypeProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    GenderType.schema()


def Male_test():
    from schorg.Male import MaleInheritedProperties
    from schorg.Male import MaleProperties
    from schorg.Male import AllProperties
    from schorg.Male import create_schema_org_model
    from schorg.Male import Male

    a = create_schema_org_model(type_=MaleInheritedProperties)
    b = create_schema_org_model(type_=MaleProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Male.schema()


def DangerousGoodConsideration_test():
    from schorg.DangerousGoodConsideration import DangerousGoodConsiderationInheritedProperties
    from schorg.DangerousGoodConsideration import DangerousGoodConsiderationProperties
    from schorg.DangerousGoodConsideration import AllProperties
    from schorg.DangerousGoodConsideration import create_schema_org_model
    from schorg.DangerousGoodConsideration import DangerousGoodConsideration

    a = create_schema_org_model(type_=DangerousGoodConsiderationInheritedProperties)
    b = create_schema_org_model(type_=DangerousGoodConsiderationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    DangerousGoodConsideration.schema()


def HyperToc_test():
    from schorg.HyperToc import HyperTocInheritedProperties
    from schorg.HyperToc import HyperTocProperties
    from schorg.HyperToc import AllProperties
    from schorg.HyperToc import create_schema_org_model
    from schorg.HyperToc import HyperToc

    a = create_schema_org_model(type_=HyperTocInheritedProperties)
    b = create_schema_org_model(type_=HyperTocProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    HyperToc.schema()


def Restaurant_test():
    from schorg.Restaurant import RestaurantInheritedProperties
    from schorg.Restaurant import RestaurantProperties
    from schorg.Restaurant import AllProperties
    from schorg.Restaurant import create_schema_org_model
    from schorg.Restaurant import Restaurant

    a = create_schema_org_model(type_=RestaurantInheritedProperties)
    b = create_schema_org_model(type_=RestaurantProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Restaurant.schema()


def Permit_test():
    from schorg.Permit import PermitInheritedProperties
    from schorg.Permit import PermitProperties
    from schorg.Permit import AllProperties
    from schorg.Permit import create_schema_org_model
    from schorg.Permit import Permit

    a = create_schema_org_model(type_=PermitInheritedProperties)
    b = create_schema_org_model(type_=PermitProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Permit.schema()


def GovernmentPermit_test():
    from schorg.GovernmentPermit import GovernmentPermitInheritedProperties
    from schorg.GovernmentPermit import GovernmentPermitProperties
    from schorg.GovernmentPermit import AllProperties
    from schorg.GovernmentPermit import create_schema_org_model
    from schorg.GovernmentPermit import GovernmentPermit

    a = create_schema_org_model(type_=GovernmentPermitInheritedProperties)
    b = create_schema_org_model(type_=GovernmentPermitProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    GovernmentPermit.schema()


def SportsClub_test():
    from schorg.SportsClub import SportsClubInheritedProperties
    from schorg.SportsClub import SportsClubProperties
    from schorg.SportsClub import AllProperties
    from schorg.SportsClub import create_schema_org_model
    from schorg.SportsClub import SportsClub

    a = create_schema_org_model(type_=SportsClubInheritedProperties)
    b = create_schema_org_model(type_=SportsClubProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    SportsClub.schema()


def PublicationEvent_test():
    from schorg.PublicationEvent import PublicationEventInheritedProperties
    from schorg.PublicationEvent import PublicationEventProperties
    from schorg.PublicationEvent import AllProperties
    from schorg.PublicationEvent import create_schema_org_model
    from schorg.PublicationEvent import PublicationEvent

    a = create_schema_org_model(type_=PublicationEventInheritedProperties)
    b = create_schema_org_model(type_=PublicationEventProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    PublicationEvent.schema()


def TravelAgency_test():
    from schorg.TravelAgency import TravelAgencyInheritedProperties
    from schorg.TravelAgency import TravelAgencyProperties
    from schorg.TravelAgency import AllProperties
    from schorg.TravelAgency import create_schema_org_model
    from schorg.TravelAgency import TravelAgency

    a = create_schema_org_model(type_=TravelAgencyInheritedProperties)
    b = create_schema_org_model(type_=TravelAgencyProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    TravelAgency.schema()


def NailSalon_test():
    from schorg.NailSalon import NailSalonInheritedProperties
    from schorg.NailSalon import NailSalonProperties
    from schorg.NailSalon import AllProperties
    from schorg.NailSalon import create_schema_org_model
    from schorg.NailSalon import NailSalon

    a = create_schema_org_model(type_=NailSalonInheritedProperties)
    b = create_schema_org_model(type_=NailSalonProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    NailSalon.schema()


def RefurbishedCondition_test():
    from schorg.RefurbishedCondition import RefurbishedConditionInheritedProperties
    from schorg.RefurbishedCondition import RefurbishedConditionProperties
    from schorg.RefurbishedCondition import AllProperties
    from schorg.RefurbishedCondition import create_schema_org_model
    from schorg.RefurbishedCondition import RefurbishedCondition

    a = create_schema_org_model(type_=RefurbishedConditionInheritedProperties)
    b = create_schema_org_model(type_=RefurbishedConditionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    RefurbishedCondition.schema()


def Plumber_test():
    from schorg.Plumber import PlumberInheritedProperties
    from schorg.Plumber import PlumberProperties
    from schorg.Plumber import AllProperties
    from schorg.Plumber import create_schema_org_model
    from schorg.Plumber import Plumber

    a = create_schema_org_model(type_=PlumberInheritedProperties)
    b = create_schema_org_model(type_=PlumberProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Plumber.schema()


def TouristInformationCenter_test():
    from schorg.TouristInformationCenter import TouristInformationCenterInheritedProperties
    from schorg.TouristInformationCenter import TouristInformationCenterProperties
    from schorg.TouristInformationCenter import AllProperties
    from schorg.TouristInformationCenter import create_schema_org_model
    from schorg.TouristInformationCenter import TouristInformationCenter

    a = create_schema_org_model(type_=TouristInformationCenterInheritedProperties)
    b = create_schema_org_model(type_=TouristInformationCenterProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    TouristInformationCenter.schema()


def QuoteAction_test():
    from schorg.QuoteAction import QuoteActionInheritedProperties
    from schorg.QuoteAction import QuoteActionProperties
    from schorg.QuoteAction import AllProperties
    from schorg.QuoteAction import create_schema_org_model
    from schorg.QuoteAction import QuoteAction

    a = create_schema_org_model(type_=QuoteActionInheritedProperties)
    b = create_schema_org_model(type_=QuoteActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    QuoteAction.schema()


def WearableSizeGroupBoys_test():
    from schorg.WearableSizeGroupBoys import WearableSizeGroupBoysInheritedProperties
    from schorg.WearableSizeGroupBoys import WearableSizeGroupBoysProperties
    from schorg.WearableSizeGroupBoys import AllProperties
    from schorg.WearableSizeGroupBoys import create_schema_org_model
    from schorg.WearableSizeGroupBoys import WearableSizeGroupBoys

    a = create_schema_org_model(type_=WearableSizeGroupBoysInheritedProperties)
    b = create_schema_org_model(type_=WearableSizeGroupBoysProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    WearableSizeGroupBoys.schema()


def ActionStatusType_test():
    from schorg.ActionStatusType import ActionStatusTypeInheritedProperties
    from schorg.ActionStatusType import ActionStatusTypeProperties
    from schorg.ActionStatusType import AllProperties
    from schorg.ActionStatusType import create_schema_org_model
    from schorg.ActionStatusType import ActionStatusType

    a = create_schema_org_model(type_=ActionStatusTypeInheritedProperties)
    b = create_schema_org_model(type_=ActionStatusTypeProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ActionStatusType.schema()


def CompletedActionStatus_test():
    from schorg.CompletedActionStatus import CompletedActionStatusInheritedProperties
    from schorg.CompletedActionStatus import CompletedActionStatusProperties
    from schorg.CompletedActionStatus import AllProperties
    from schorg.CompletedActionStatus import create_schema_org_model
    from schorg.CompletedActionStatus import CompletedActionStatus

    a = create_schema_org_model(type_=CompletedActionStatusInheritedProperties)
    b = create_schema_org_model(type_=CompletedActionStatusProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    CompletedActionStatus.schema()


def BodyOfWater_test():
    from schorg.BodyOfWater import BodyOfWaterInheritedProperties
    from schorg.BodyOfWater import BodyOfWaterProperties
    from schorg.BodyOfWater import AllProperties
    from schorg.BodyOfWater import create_schema_org_model
    from schorg.BodyOfWater import BodyOfWater

    a = create_schema_org_model(type_=BodyOfWaterInheritedProperties)
    b = create_schema_org_model(type_=BodyOfWaterProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    BodyOfWater.schema()


def OceanBodyOfWater_test():
    from schorg.OceanBodyOfWater import OceanBodyOfWaterInheritedProperties
    from schorg.OceanBodyOfWater import OceanBodyOfWaterProperties
    from schorg.OceanBodyOfWater import AllProperties
    from schorg.OceanBodyOfWater import create_schema_org_model
    from schorg.OceanBodyOfWater import OceanBodyOfWater

    a = create_schema_org_model(type_=OceanBodyOfWaterInheritedProperties)
    b = create_schema_org_model(type_=OceanBodyOfWaterProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    OceanBodyOfWater.schema()


def PlayGameAction_test():
    from schorg.PlayGameAction import PlayGameActionInheritedProperties
    from schorg.PlayGameAction import PlayGameActionProperties
    from schorg.PlayGameAction import AllProperties
    from schorg.PlayGameAction import create_schema_org_model
    from schorg.PlayGameAction import PlayGameAction

    a = create_schema_org_model(type_=PlayGameActionInheritedProperties)
    b = create_schema_org_model(type_=PlayGameActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    PlayGameAction.schema()


def ActivateAction_test():
    from schorg.ActivateAction import ActivateActionInheritedProperties
    from schorg.ActivateAction import ActivateActionProperties
    from schorg.ActivateAction import AllProperties
    from schorg.ActivateAction import create_schema_org_model
    from schorg.ActivateAction import ActivateAction

    a = create_schema_org_model(type_=ActivateActionInheritedProperties)
    b = create_schema_org_model(type_=ActivateActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ActivateAction.schema()


def MenuSection_test():
    from schorg.MenuSection import MenuSectionInheritedProperties
    from schorg.MenuSection import MenuSectionProperties
    from schorg.MenuSection import AllProperties
    from schorg.MenuSection import create_schema_org_model
    from schorg.MenuSection import MenuSection

    a = create_schema_org_model(type_=MenuSectionInheritedProperties)
    b = create_schema_org_model(type_=MenuSectionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MenuSection.schema()


def MovieRentalStore_test():
    from schorg.MovieRentalStore import MovieRentalStoreInheritedProperties
    from schorg.MovieRentalStore import MovieRentalStoreProperties
    from schorg.MovieRentalStore import AllProperties
    from schorg.MovieRentalStore import create_schema_org_model
    from schorg.MovieRentalStore import MovieRentalStore

    a = create_schema_org_model(type_=MovieRentalStoreInheritedProperties)
    b = create_schema_org_model(type_=MovieRentalStoreProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MovieRentalStore.schema()


def Chapter_test():
    from schorg.Chapter import ChapterInheritedProperties
    from schorg.Chapter import ChapterProperties
    from schorg.Chapter import AllProperties
    from schorg.Chapter import create_schema_org_model
    from schorg.Chapter import Chapter

    a = create_schema_org_model(type_=ChapterInheritedProperties)
    b = create_schema_org_model(type_=ChapterProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Chapter.schema()


def BodyMeasurementUnderbust_test():
    from schorg.BodyMeasurementUnderbust import BodyMeasurementUnderbustInheritedProperties
    from schorg.BodyMeasurementUnderbust import BodyMeasurementUnderbustProperties
    from schorg.BodyMeasurementUnderbust import AllProperties
    from schorg.BodyMeasurementUnderbust import create_schema_org_model
    from schorg.BodyMeasurementUnderbust import BodyMeasurementUnderbust

    a = create_schema_org_model(type_=BodyMeasurementUnderbustInheritedProperties)
    b = create_schema_org_model(type_=BodyMeasurementUnderbustProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    BodyMeasurementUnderbust.schema()


def Order_test():
    from schorg.Order import OrderInheritedProperties
    from schorg.Order import OrderProperties
    from schorg.Order import AllProperties
    from schorg.Order import create_schema_org_model
    from schorg.Order import Order

    a = create_schema_org_model(type_=OrderInheritedProperties)
    b = create_schema_org_model(type_=OrderProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Order.schema()


def ArtGallery_test():
    from schorg.ArtGallery import ArtGalleryInheritedProperties
    from schorg.ArtGallery import ArtGalleryProperties
    from schorg.ArtGallery import AllProperties
    from schorg.ArtGallery import create_schema_org_model
    from schorg.ArtGallery import ArtGallery

    a = create_schema_org_model(type_=ArtGalleryInheritedProperties)
    b = create_schema_org_model(type_=ArtGalleryProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ArtGallery.schema()


def Nonprofit501c8_test():
    from schorg.Nonprofit501c8 import Nonprofit501c8InheritedProperties
    from schorg.Nonprofit501c8 import Nonprofit501c8Properties
    from schorg.Nonprofit501c8 import AllProperties
    from schorg.Nonprofit501c8 import create_schema_org_model
    from schorg.Nonprofit501c8 import Nonprofit501c8

    a = create_schema_org_model(type_=Nonprofit501c8InheritedProperties)
    b = create_schema_org_model(type_=Nonprofit501c8Properties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Nonprofit501c8.schema()


def SteeringPositionValue_test():
    from schorg.SteeringPositionValue import SteeringPositionValueInheritedProperties
    from schorg.SteeringPositionValue import SteeringPositionValueProperties
    from schorg.SteeringPositionValue import AllProperties
    from schorg.SteeringPositionValue import create_schema_org_model
    from schorg.SteeringPositionValue import SteeringPositionValue

    a = create_schema_org_model(type_=SteeringPositionValueInheritedProperties)
    b = create_schema_org_model(type_=SteeringPositionValueProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    SteeringPositionValue.schema()


def LeftHandDriving_test():
    from schorg.LeftHandDriving import LeftHandDrivingInheritedProperties
    from schorg.LeftHandDriving import LeftHandDrivingProperties
    from schorg.LeftHandDriving import AllProperties
    from schorg.LeftHandDriving import create_schema_org_model
    from schorg.LeftHandDriving import LeftHandDriving

    a = create_schema_org_model(type_=LeftHandDrivingInheritedProperties)
    b = create_schema_org_model(type_=LeftHandDrivingProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    LeftHandDriving.schema()


def ComicStory_test():
    from schorg.ComicStory import ComicStoryInheritedProperties
    from schorg.ComicStory import ComicStoryProperties
    from schorg.ComicStory import AllProperties
    from schorg.ComicStory import create_schema_org_model
    from schorg.ComicStory import ComicStory

    a = create_schema_org_model(type_=ComicStoryInheritedProperties)
    b = create_schema_org_model(type_=ComicStoryProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ComicStory.schema()


def ComicCoverArt_test():
    from schorg.ComicCoverArt import ComicCoverArtInheritedProperties
    from schorg.ComicCoverArt import ComicCoverArtProperties
    from schorg.ComicCoverArt import AllProperties
    from schorg.ComicCoverArt import create_schema_org_model
    from schorg.ComicCoverArt import ComicCoverArt

    a = create_schema_org_model(type_=ComicCoverArtInheritedProperties)
    b = create_schema_org_model(type_=ComicCoverArtProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ComicCoverArt.schema()


def LikeAction_test():
    from schorg.LikeAction import LikeActionInheritedProperties
    from schorg.LikeAction import LikeActionProperties
    from schorg.LikeAction import AllProperties
    from schorg.LikeAction import create_schema_org_model
    from schorg.LikeAction import LikeAction

    a = create_schema_org_model(type_=LikeActionInheritedProperties)
    b = create_schema_org_model(type_=LikeActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    LikeAction.schema()


def WearableMeasurementCollar_test():
    from schorg.WearableMeasurementCollar import WearableMeasurementCollarInheritedProperties
    from schorg.WearableMeasurementCollar import WearableMeasurementCollarProperties
    from schorg.WearableMeasurementCollar import AllProperties
    from schorg.WearableMeasurementCollar import create_schema_org_model
    from schorg.WearableMeasurementCollar import WearableMeasurementCollar

    a = create_schema_org_model(type_=WearableMeasurementCollarInheritedProperties)
    b = create_schema_org_model(type_=WearableMeasurementCollarProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    WearableMeasurementCollar.schema()


def ItemListUnordered_test():
    from schorg.ItemListUnordered import ItemListUnorderedInheritedProperties
    from schorg.ItemListUnordered import ItemListUnorderedProperties
    from schorg.ItemListUnordered import AllProperties
    from schorg.ItemListUnordered import create_schema_org_model
    from schorg.ItemListUnordered import ItemListUnordered

    a = create_schema_org_model(type_=ItemListUnorderedInheritedProperties)
    b = create_schema_org_model(type_=ItemListUnorderedProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ItemListUnordered.schema()


def GameAvailabilityEnumeration_test():
    from schorg.GameAvailabilityEnumeration import GameAvailabilityEnumerationInheritedProperties
    from schorg.GameAvailabilityEnumeration import GameAvailabilityEnumerationProperties
    from schorg.GameAvailabilityEnumeration import AllProperties
    from schorg.GameAvailabilityEnumeration import create_schema_org_model
    from schorg.GameAvailabilityEnumeration import GameAvailabilityEnumeration

    a = create_schema_org_model(type_=GameAvailabilityEnumerationInheritedProperties)
    b = create_schema_org_model(type_=GameAvailabilityEnumerationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    GameAvailabilityEnumeration.schema()


def DemoGameAvailability_test():
    from schorg.DemoGameAvailability import DemoGameAvailabilityInheritedProperties
    from schorg.DemoGameAvailability import DemoGameAvailabilityProperties
    from schorg.DemoGameAvailability import AllProperties
    from schorg.DemoGameAvailability import create_schema_org_model
    from schorg.DemoGameAvailability import DemoGameAvailability

    a = create_schema_org_model(type_=DemoGameAvailabilityInheritedProperties)
    b = create_schema_org_model(type_=DemoGameAvailabilityProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    DemoGameAvailability.schema()


def Canal_test():
    from schorg.Canal import CanalInheritedProperties
    from schorg.Canal import CanalProperties
    from schorg.Canal import AllProperties
    from schorg.Canal import create_schema_org_model
    from schorg.Canal import Canal

    a = create_schema_org_model(type_=CanalInheritedProperties)
    b = create_schema_org_model(type_=CanalProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Canal.schema()


def SideEffectsHealthAspect_test():
    from schorg.SideEffectsHealthAspect import SideEffectsHealthAspectInheritedProperties
    from schorg.SideEffectsHealthAspect import SideEffectsHealthAspectProperties
    from schorg.SideEffectsHealthAspect import AllProperties
    from schorg.SideEffectsHealthAspect import create_schema_org_model
    from schorg.SideEffectsHealthAspect import SideEffectsHealthAspect

    a = create_schema_org_model(type_=SideEffectsHealthAspectInheritedProperties)
    b = create_schema_org_model(type_=SideEffectsHealthAspectProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    SideEffectsHealthAspect.schema()


def AudiobookFormat_test():
    from schorg.AudiobookFormat import AudiobookFormatInheritedProperties
    from schorg.AudiobookFormat import AudiobookFormatProperties
    from schorg.AudiobookFormat import AllProperties
    from schorg.AudiobookFormat import create_schema_org_model
    from schorg.AudiobookFormat import AudiobookFormat

    a = create_schema_org_model(type_=AudiobookFormatInheritedProperties)
    b = create_schema_org_model(type_=AudiobookFormatProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    AudiobookFormat.schema()


def MathSolver_test():
    from schorg.MathSolver import MathSolverInheritedProperties
    from schorg.MathSolver import MathSolverProperties
    from schorg.MathSolver import AllProperties
    from schorg.MathSolver import create_schema_org_model
    from schorg.MathSolver import MathSolver

    a = create_schema_org_model(type_=MathSolverInheritedProperties)
    b = create_schema_org_model(type_=MathSolverProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MathSolver.schema()


def EUEnergyEfficiencyCategoryB_test():
    from schorg.EUEnergyEfficiencyCategoryB import EUEnergyEfficiencyCategoryBInheritedProperties
    from schorg.EUEnergyEfficiencyCategoryB import EUEnergyEfficiencyCategoryBProperties
    from schorg.EUEnergyEfficiencyCategoryB import AllProperties
    from schorg.EUEnergyEfficiencyCategoryB import create_schema_org_model
    from schorg.EUEnergyEfficiencyCategoryB import EUEnergyEfficiencyCategoryB

    a = create_schema_org_model(type_=EUEnergyEfficiencyCategoryBInheritedProperties)
    b = create_schema_org_model(type_=EUEnergyEfficiencyCategoryBProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    EUEnergyEfficiencyCategoryB.schema()


def PlayAction_test():
    from schorg.PlayAction import PlayActionInheritedProperties
    from schorg.PlayAction import PlayActionProperties
    from schorg.PlayAction import AllProperties
    from schorg.PlayAction import create_schema_org_model
    from schorg.PlayAction import PlayAction

    a = create_schema_org_model(type_=PlayActionInheritedProperties)
    b = create_schema_org_model(type_=PlayActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    PlayAction.schema()


def ExerciseAction_test():
    from schorg.ExerciseAction import ExerciseActionInheritedProperties
    from schorg.ExerciseAction import ExerciseActionProperties
    from schorg.ExerciseAction import AllProperties
    from schorg.ExerciseAction import create_schema_org_model
    from schorg.ExerciseAction import ExerciseAction

    a = create_schema_org_model(type_=ExerciseActionInheritedProperties)
    b = create_schema_org_model(type_=ExerciseActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ExerciseAction.schema()


def BioChemEntity_test():
    from schorg.BioChemEntity import BioChemEntityInheritedProperties
    from schorg.BioChemEntity import BioChemEntityProperties
    from schorg.BioChemEntity import AllProperties
    from schorg.BioChemEntity import create_schema_org_model
    from schorg.BioChemEntity import BioChemEntity

    a = create_schema_org_model(type_=BioChemEntityInheritedProperties)
    b = create_schema_org_model(type_=BioChemEntityProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    BioChemEntity.schema()


def Gene_test():
    from schorg.Gene import GeneInheritedProperties
    from schorg.Gene import GeneProperties
    from schorg.Gene import AllProperties
    from schorg.Gene import create_schema_org_model
    from schorg.Gene import Gene

    a = create_schema_org_model(type_=GeneInheritedProperties)
    b = create_schema_org_model(type_=GeneProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Gene.schema()


def Downpayment_test():
    from schorg.Downpayment import DownpaymentInheritedProperties
    from schorg.Downpayment import DownpaymentProperties
    from schorg.Downpayment import AllProperties
    from schorg.Downpayment import create_schema_org_model
    from schorg.Downpayment import Downpayment

    a = create_schema_org_model(type_=DownpaymentInheritedProperties)
    b = create_schema_org_model(type_=DownpaymentProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Downpayment.schema()


def Invoice_test():
    from schorg.Invoice import InvoiceInheritedProperties
    from schorg.Invoice import InvoiceProperties
    from schorg.Invoice import AllProperties
    from schorg.Invoice import create_schema_org_model
    from schorg.Invoice import Invoice

    a = create_schema_org_model(type_=InvoiceInheritedProperties)
    b = create_schema_org_model(type_=InvoiceProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Invoice.schema()


def GovernmentOffice_test():
    from schorg.GovernmentOffice import GovernmentOfficeInheritedProperties
    from schorg.GovernmentOffice import GovernmentOfficeProperties
    from schorg.GovernmentOffice import AllProperties
    from schorg.GovernmentOffice import create_schema_org_model
    from schorg.GovernmentOffice import GovernmentOffice

    a = create_schema_org_model(type_=GovernmentOfficeInheritedProperties)
    b = create_schema_org_model(type_=GovernmentOfficeProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    GovernmentOffice.schema()


def PostOffice_test():
    from schorg.PostOffice import PostOfficeInheritedProperties
    from schorg.PostOffice import PostOfficeProperties
    from schorg.PostOffice import AllProperties
    from schorg.PostOffice import create_schema_org_model
    from schorg.PostOffice import PostOffice

    a = create_schema_org_model(type_=PostOfficeInheritedProperties)
    b = create_schema_org_model(type_=PostOfficeProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    PostOffice.schema()


def DigitalDocument_test():
    from schorg.DigitalDocument import DigitalDocumentInheritedProperties
    from schorg.DigitalDocument import DigitalDocumentProperties
    from schorg.DigitalDocument import AllProperties
    from schorg.DigitalDocument import create_schema_org_model
    from schorg.DigitalDocument import DigitalDocument

    a = create_schema_org_model(type_=DigitalDocumentInheritedProperties)
    b = create_schema_org_model(type_=DigitalDocumentProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    DigitalDocument.schema()


def TextDigitalDocument_test():
    from schorg.TextDigitalDocument import TextDigitalDocumentInheritedProperties
    from schorg.TextDigitalDocument import TextDigitalDocumentProperties
    from schorg.TextDigitalDocument import AllProperties
    from schorg.TextDigitalDocument import create_schema_org_model
    from schorg.TextDigitalDocument import TextDigitalDocument

    a = create_schema_org_model(type_=TextDigitalDocumentInheritedProperties)
    b = create_schema_org_model(type_=TextDigitalDocumentProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    TextDigitalDocument.schema()


def Flight_test():
    from schorg.Flight import FlightInheritedProperties
    from schorg.Flight import FlightProperties
    from schorg.Flight import AllProperties
    from schorg.Flight import create_schema_org_model
    from schorg.Flight import Flight

    a = create_schema_org_model(type_=FlightInheritedProperties)
    b = create_schema_org_model(type_=FlightProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Flight.schema()


def DecontextualizedContent_test():
    from schorg.DecontextualizedContent import DecontextualizedContentInheritedProperties
    from schorg.DecontextualizedContent import DecontextualizedContentProperties
    from schorg.DecontextualizedContent import AllProperties
    from schorg.DecontextualizedContent import create_schema_org_model
    from schorg.DecontextualizedContent import DecontextualizedContent

    a = create_schema_org_model(type_=DecontextualizedContentInheritedProperties)
    b = create_schema_org_model(type_=DecontextualizedContentProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    DecontextualizedContent.schema()


def BedType_test():
    from schorg.BedType import BedTypeInheritedProperties
    from schorg.BedType import BedTypeProperties
    from schorg.BedType import AllProperties
    from schorg.BedType import create_schema_org_model
    from schorg.BedType import BedType

    a = create_schema_org_model(type_=BedTypeInheritedProperties)
    b = create_schema_org_model(type_=BedTypeProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    BedType.schema()


def BlogPosting_test():
    from schorg.BlogPosting import BlogPostingInheritedProperties
    from schorg.BlogPosting import BlogPostingProperties
    from schorg.BlogPosting import AllProperties
    from schorg.BlogPosting import create_schema_org_model
    from schorg.BlogPosting import BlogPosting

    a = create_schema_org_model(type_=BlogPostingInheritedProperties)
    b = create_schema_org_model(type_=BlogPostingProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    BlogPosting.schema()


def Distance_test():
    from schorg.Distance import DistanceInheritedProperties
    from schorg.Distance import DistanceProperties
    from schorg.Distance import AllProperties
    from schorg.Distance import create_schema_org_model
    from schorg.Distance import Distance

    a = create_schema_org_model(type_=DistanceInheritedProperties)
    b = create_schema_org_model(type_=DistanceProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Distance.schema()


def ReservationPending_test():
    from schorg.ReservationPending import ReservationPendingInheritedProperties
    from schorg.ReservationPending import ReservationPendingProperties
    from schorg.ReservationPending import AllProperties
    from schorg.ReservationPending import create_schema_org_model
    from schorg.ReservationPending import ReservationPending

    a = create_schema_org_model(type_=ReservationPendingInheritedProperties)
    b = create_schema_org_model(type_=ReservationPendingProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ReservationPending.schema()


def LodgingReservation_test():
    from schorg.LodgingReservation import LodgingReservationInheritedProperties
    from schorg.LodgingReservation import LodgingReservationProperties
    from schorg.LodgingReservation import AllProperties
    from schorg.LodgingReservation import create_schema_org_model
    from schorg.LodgingReservation import LodgingReservation

    a = create_schema_org_model(type_=LodgingReservationInheritedProperties)
    b = create_schema_org_model(type_=LodgingReservationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    LodgingReservation.schema()


def SearchResultsPage_test():
    from schorg.SearchResultsPage import SearchResultsPageInheritedProperties
    from schorg.SearchResultsPage import SearchResultsPageProperties
    from schorg.SearchResultsPage import AllProperties
    from schorg.SearchResultsPage import create_schema_org_model
    from schorg.SearchResultsPage import SearchResultsPage

    a = create_schema_org_model(type_=SearchResultsPageInheritedProperties)
    b = create_schema_org_model(type_=SearchResultsPageProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    SearchResultsPage.schema()


def TennisComplex_test():
    from schorg.TennisComplex import TennisComplexInheritedProperties
    from schorg.TennisComplex import TennisComplexProperties
    from schorg.TennisComplex import AllProperties
    from schorg.TennisComplex import create_schema_org_model
    from schorg.TennisComplex import TennisComplex

    a = create_schema_org_model(type_=TennisComplexInheritedProperties)
    b = create_schema_org_model(type_=TennisComplexProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    TennisComplex.schema()


def GovernmentBuilding_test():
    from schorg.GovernmentBuilding import GovernmentBuildingInheritedProperties
    from schorg.GovernmentBuilding import GovernmentBuildingProperties
    from schorg.GovernmentBuilding import AllProperties
    from schorg.GovernmentBuilding import create_schema_org_model
    from schorg.GovernmentBuilding import GovernmentBuilding

    a = create_schema_org_model(type_=GovernmentBuildingInheritedProperties)
    b = create_schema_org_model(type_=GovernmentBuildingProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    GovernmentBuilding.schema()


def Embassy_test():
    from schorg.Embassy import EmbassyInheritedProperties
    from schorg.Embassy import EmbassyProperties
    from schorg.Embassy import AllProperties
    from schorg.Embassy import create_schema_org_model
    from schorg.Embassy import Embassy

    a = create_schema_org_model(type_=EmbassyInheritedProperties)
    b = create_schema_org_model(type_=EmbassyProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Embassy.schema()


def DamagedCondition_test():
    from schorg.DamagedCondition import DamagedConditionInheritedProperties
    from schorg.DamagedCondition import DamagedConditionProperties
    from schorg.DamagedCondition import AllProperties
    from schorg.DamagedCondition import create_schema_org_model
    from schorg.DamagedCondition import DamagedCondition

    a = create_schema_org_model(type_=DamagedConditionInheritedProperties)
    b = create_schema_org_model(type_=DamagedConditionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    DamagedCondition.schema()


def LegalValueLevel_test():
    from schorg.LegalValueLevel import LegalValueLevelInheritedProperties
    from schorg.LegalValueLevel import LegalValueLevelProperties
    from schorg.LegalValueLevel import AllProperties
    from schorg.LegalValueLevel import create_schema_org_model
    from schorg.LegalValueLevel import LegalValueLevel

    a = create_schema_org_model(type_=LegalValueLevelInheritedProperties)
    b = create_schema_org_model(type_=LegalValueLevelProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    LegalValueLevel.schema()


def UnofficialLegalValue_test():
    from schorg.UnofficialLegalValue import UnofficialLegalValueInheritedProperties
    from schorg.UnofficialLegalValue import UnofficialLegalValueProperties
    from schorg.UnofficialLegalValue import AllProperties
    from schorg.UnofficialLegalValue import create_schema_org_model
    from schorg.UnofficialLegalValue import UnofficialLegalValue

    a = create_schema_org_model(type_=UnofficialLegalValueInheritedProperties)
    b = create_schema_org_model(type_=UnofficialLegalValueProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    UnofficialLegalValue.schema()


def MedicalGuideline_test():
    from schorg.MedicalGuideline import MedicalGuidelineInheritedProperties
    from schorg.MedicalGuideline import MedicalGuidelineProperties
    from schorg.MedicalGuideline import AllProperties
    from schorg.MedicalGuideline import create_schema_org_model
    from schorg.MedicalGuideline import MedicalGuideline

    a = create_schema_org_model(type_=MedicalGuidelineInheritedProperties)
    b = create_schema_org_model(type_=MedicalGuidelineProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MedicalGuideline.schema()


def CampingPitch_test():
    from schorg.CampingPitch import CampingPitchInheritedProperties
    from schorg.CampingPitch import CampingPitchProperties
    from schorg.CampingPitch import AllProperties
    from schorg.CampingPitch import create_schema_org_model
    from schorg.CampingPitch import CampingPitch

    a = create_schema_org_model(type_=CampingPitchInheritedProperties)
    b = create_schema_org_model(type_=CampingPitchProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    CampingPitch.schema()


def LoseAction_test():
    from schorg.LoseAction import LoseActionInheritedProperties
    from schorg.LoseAction import LoseActionProperties
    from schorg.LoseAction import AllProperties
    from schorg.LoseAction import create_schema_org_model
    from schorg.LoseAction import LoseAction

    a = create_schema_org_model(type_=LoseActionInheritedProperties)
    b = create_schema_org_model(type_=LoseActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    LoseAction.schema()


def WearableSizeGroupTall_test():
    from schorg.WearableSizeGroupTall import WearableSizeGroupTallInheritedProperties
    from schorg.WearableSizeGroupTall import WearableSizeGroupTallProperties
    from schorg.WearableSizeGroupTall import AllProperties
    from schorg.WearableSizeGroupTall import create_schema_org_model
    from schorg.WearableSizeGroupTall import WearableSizeGroupTall

    a = create_schema_org_model(type_=WearableSizeGroupTallInheritedProperties)
    b = create_schema_org_model(type_=WearableSizeGroupTallProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    WearableSizeGroupTall.schema()


def KosherDiet_test():
    from schorg.KosherDiet import KosherDietInheritedProperties
    from schorg.KosherDiet import KosherDietProperties
    from schorg.KosherDiet import AllProperties
    from schorg.KosherDiet import create_schema_org_model
    from schorg.KosherDiet import KosherDiet

    a = create_schema_org_model(type_=KosherDietInheritedProperties)
    b = create_schema_org_model(type_=KosherDietProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    KosherDiet.schema()


def FDAcategoryB_test():
    from schorg.FDAcategoryB import FDAcategoryBInheritedProperties
    from schorg.FDAcategoryB import FDAcategoryBProperties
    from schorg.FDAcategoryB import AllProperties
    from schorg.FDAcategoryB import create_schema_org_model
    from schorg.FDAcategoryB import FDAcategoryB

    a = create_schema_org_model(type_=FDAcategoryBInheritedProperties)
    b = create_schema_org_model(type_=FDAcategoryBProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    FDAcategoryB.schema()


def WearableSizeGroupJuniors_test():
    from schorg.WearableSizeGroupJuniors import WearableSizeGroupJuniorsInheritedProperties
    from schorg.WearableSizeGroupJuniors import WearableSizeGroupJuniorsProperties
    from schorg.WearableSizeGroupJuniors import AllProperties
    from schorg.WearableSizeGroupJuniors import create_schema_org_model
    from schorg.WearableSizeGroupJuniors import WearableSizeGroupJuniors

    a = create_schema_org_model(type_=WearableSizeGroupJuniorsInheritedProperties)
    b = create_schema_org_model(type_=WearableSizeGroupJuniorsProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    WearableSizeGroupJuniors.schema()


def ElementarySchool_test():
    from schorg.ElementarySchool import ElementarySchoolInheritedProperties
    from schorg.ElementarySchool import ElementarySchoolProperties
    from schorg.ElementarySchool import AllProperties
    from schorg.ElementarySchool import create_schema_org_model
    from schorg.ElementarySchool import ElementarySchool

    a = create_schema_org_model(type_=ElementarySchoolInheritedProperties)
    b = create_schema_org_model(type_=ElementarySchoolProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ElementarySchool.schema()


def Message_test():
    from schorg.Message import MessageInheritedProperties
    from schorg.Message import MessageProperties
    from schorg.Message import AllProperties
    from schorg.Message import create_schema_org_model
    from schorg.Message import Message

    a = create_schema_org_model(type_=MessageInheritedProperties)
    b = create_schema_org_model(type_=MessageProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Message.schema()


def EmailMessage_test():
    from schorg.EmailMessage import EmailMessageInheritedProperties
    from schorg.EmailMessage import EmailMessageProperties
    from schorg.EmailMessage import AllProperties
    from schorg.EmailMessage import create_schema_org_model
    from schorg.EmailMessage import EmailMessage

    a = create_schema_org_model(type_=EmailMessageInheritedProperties)
    b = create_schema_org_model(type_=EmailMessageProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    EmailMessage.schema()


def SaleEvent_test():
    from schorg.SaleEvent import SaleEventInheritedProperties
    from schorg.SaleEvent import SaleEventProperties
    from schorg.SaleEvent import AllProperties
    from schorg.SaleEvent import create_schema_org_model
    from schorg.SaleEvent import SaleEvent

    a = create_schema_org_model(type_=SaleEventInheritedProperties)
    b = create_schema_org_model(type_=SaleEventProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    SaleEvent.schema()


def MediaReviewItem_test():
    from schorg.MediaReviewItem import MediaReviewItemInheritedProperties
    from schorg.MediaReviewItem import MediaReviewItemProperties
    from schorg.MediaReviewItem import AllProperties
    from schorg.MediaReviewItem import create_schema_org_model
    from schorg.MediaReviewItem import MediaReviewItem

    a = create_schema_org_model(type_=MediaReviewItemInheritedProperties)
    b = create_schema_org_model(type_=MediaReviewItemProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MediaReviewItem.schema()


def ImageObject_test():
    from schorg.ImageObject import ImageObjectInheritedProperties
    from schorg.ImageObject import ImageObjectProperties
    from schorg.ImageObject import AllProperties
    from schorg.ImageObject import create_schema_org_model
    from schorg.ImageObject import ImageObject

    a = create_schema_org_model(type_=ImageObjectInheritedProperties)
    b = create_schema_org_model(type_=ImageObjectProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ImageObject.schema()


def ImageObjectSnapshot_test():
    from schorg.ImageObjectSnapshot import ImageObjectSnapshotInheritedProperties
    from schorg.ImageObjectSnapshot import ImageObjectSnapshotProperties
    from schorg.ImageObjectSnapshot import AllProperties
    from schorg.ImageObjectSnapshot import create_schema_org_model
    from schorg.ImageObjectSnapshot import ImageObjectSnapshot

    a = create_schema_org_model(type_=ImageObjectSnapshotInheritedProperties)
    b = create_schema_org_model(type_=ImageObjectSnapshotProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ImageObjectSnapshot.schema()


def Pharmacy_test():
    from schorg.Pharmacy import PharmacyInheritedProperties
    from schorg.Pharmacy import PharmacyProperties
    from schorg.Pharmacy import AllProperties
    from schorg.Pharmacy import create_schema_org_model
    from schorg.Pharmacy import Pharmacy

    a = create_schema_org_model(type_=PharmacyInheritedProperties)
    b = create_schema_org_model(type_=PharmacyProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Pharmacy.schema()


def ContactPoint_test():
    from schorg.ContactPoint import ContactPointInheritedProperties
    from schorg.ContactPoint import ContactPointProperties
    from schorg.ContactPoint import AllProperties
    from schorg.ContactPoint import create_schema_org_model
    from schorg.ContactPoint import ContactPoint

    a = create_schema_org_model(type_=ContactPointInheritedProperties)
    b = create_schema_org_model(type_=ContactPointProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ContactPoint.schema()


def PublicHolidays_test():
    from schorg.PublicHolidays import PublicHolidaysInheritedProperties
    from schorg.PublicHolidays import PublicHolidaysProperties
    from schorg.PublicHolidays import AllProperties
    from schorg.PublicHolidays import create_schema_org_model
    from schorg.PublicHolidays import PublicHolidays

    a = create_schema_org_model(type_=PublicHolidaysInheritedProperties)
    b = create_schema_org_model(type_=PublicHolidaysProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    PublicHolidays.schema()


def BusTrip_test():
    from schorg.BusTrip import BusTripInheritedProperties
    from schorg.BusTrip import BusTripProperties
    from schorg.BusTrip import AllProperties
    from schorg.BusTrip import create_schema_org_model
    from schorg.BusTrip import BusTrip

    a = create_schema_org_model(type_=BusTripInheritedProperties)
    b = create_schema_org_model(type_=BusTripProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    BusTrip.schema()


def Physician_test():
    from schorg.Physician import PhysicianInheritedProperties
    from schorg.Physician import PhysicianProperties
    from schorg.Physician import AllProperties
    from schorg.Physician import create_schema_org_model
    from schorg.Physician import Physician

    a = create_schema_org_model(type_=PhysicianInheritedProperties)
    b = create_schema_org_model(type_=PhysicianProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Physician.schema()


def EventStatusType_test():
    from schorg.EventStatusType import EventStatusTypeInheritedProperties
    from schorg.EventStatusType import EventStatusTypeProperties
    from schorg.EventStatusType import AllProperties
    from schorg.EventStatusType import create_schema_org_model
    from schorg.EventStatusType import EventStatusType

    a = create_schema_org_model(type_=EventStatusTypeInheritedProperties)
    b = create_schema_org_model(type_=EventStatusTypeProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    EventStatusType.schema()


def EventCancelled_test():
    from schorg.EventCancelled import EventCancelledInheritedProperties
    from schorg.EventCancelled import EventCancelledProperties
    from schorg.EventCancelled import AllProperties
    from schorg.EventCancelled import create_schema_org_model
    from schorg.EventCancelled import EventCancelled

    a = create_schema_org_model(type_=EventCancelledInheritedProperties)
    b = create_schema_org_model(type_=EventCancelledProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    EventCancelled.schema()


def ResultsNotAvailable_test():
    from schorg.ResultsNotAvailable import ResultsNotAvailableInheritedProperties
    from schorg.ResultsNotAvailable import ResultsNotAvailableProperties
    from schorg.ResultsNotAvailable import AllProperties
    from schorg.ResultsNotAvailable import create_schema_org_model
    from schorg.ResultsNotAvailable import ResultsNotAvailable

    a = create_schema_org_model(type_=ResultsNotAvailableInheritedProperties)
    b = create_schema_org_model(type_=ResultsNotAvailableProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ResultsNotAvailable.schema()


def Campground_test():
    from schorg.Campground import CampgroundInheritedProperties
    from schorg.Campground import CampgroundProperties
    from schorg.Campground import AllProperties
    from schorg.Campground import create_schema_org_model
    from schorg.Campground import Campground

    a = create_schema_org_model(type_=CampgroundInheritedProperties)
    b = create_schema_org_model(type_=CampgroundProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Campground.schema()


def Joint_test():
    from schorg.Joint import JointInheritedProperties
    from schorg.Joint import JointProperties
    from schorg.Joint import AllProperties
    from schorg.Joint import create_schema_org_model
    from schorg.Joint import Joint

    a = create_schema_org_model(type_=JointInheritedProperties)
    b = create_schema_org_model(type_=JointProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Joint.schema()


def MerchantReturnPolicy_test():
    from schorg.MerchantReturnPolicy import MerchantReturnPolicyInheritedProperties
    from schorg.MerchantReturnPolicy import MerchantReturnPolicyProperties
    from schorg.MerchantReturnPolicy import AllProperties
    from schorg.MerchantReturnPolicy import create_schema_org_model
    from schorg.MerchantReturnPolicy import MerchantReturnPolicy

    a = create_schema_org_model(type_=MerchantReturnPolicyInheritedProperties)
    b = create_schema_org_model(type_=MerchantReturnPolicyProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MerchantReturnPolicy.schema()


def CompleteDataFeed_test():
    from schorg.CompleteDataFeed import CompleteDataFeedInheritedProperties
    from schorg.CompleteDataFeed import CompleteDataFeedProperties
    from schorg.CompleteDataFeed import AllProperties
    from schorg.CompleteDataFeed import create_schema_org_model
    from schorg.CompleteDataFeed import CompleteDataFeed

    a = create_schema_org_model(type_=CompleteDataFeedInheritedProperties)
    b = create_schema_org_model(type_=CompleteDataFeedProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    CompleteDataFeed.schema()


def PrimaryCare_test():
    from schorg.PrimaryCare import PrimaryCareInheritedProperties
    from schorg.PrimaryCare import PrimaryCareProperties
    from schorg.PrimaryCare import AllProperties
    from schorg.PrimaryCare import create_schema_org_model
    from schorg.PrimaryCare import PrimaryCare

    a = create_schema_org_model(type_=PrimaryCareInheritedProperties)
    b = create_schema_org_model(type_=PrimaryCareProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    PrimaryCare.schema()


def City_test():
    from schorg.City import CityInheritedProperties
    from schorg.City import CityProperties
    from schorg.City import AllProperties
    from schorg.City import create_schema_org_model
    from schorg.City import City

    a = create_schema_org_model(type_=CityInheritedProperties)
    b = create_schema_org_model(type_=CityProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    City.schema()


def HealthPlanCostSharingSpecification_test():
    from schorg.HealthPlanCostSharingSpecification import HealthPlanCostSharingSpecificationInheritedProperties
    from schorg.HealthPlanCostSharingSpecification import HealthPlanCostSharingSpecificationProperties
    from schorg.HealthPlanCostSharingSpecification import AllProperties
    from schorg.HealthPlanCostSharingSpecification import create_schema_org_model
    from schorg.HealthPlanCostSharingSpecification import HealthPlanCostSharingSpecification

    a = create_schema_org_model(type_=HealthPlanCostSharingSpecificationInheritedProperties)
    b = create_schema_org_model(type_=HealthPlanCostSharingSpecificationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    HealthPlanCostSharingSpecification.schema()


def MedicalStudy_test():
    from schorg.MedicalStudy import MedicalStudyInheritedProperties
    from schorg.MedicalStudy import MedicalStudyProperties
    from schorg.MedicalStudy import AllProperties
    from schorg.MedicalStudy import create_schema_org_model
    from schorg.MedicalStudy import MedicalStudy

    a = create_schema_org_model(type_=MedicalStudyInheritedProperties)
    b = create_schema_org_model(type_=MedicalStudyProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MedicalStudy.schema()


def MedicalObservationalStudy_test():
    from schorg.MedicalObservationalStudy import MedicalObservationalStudyInheritedProperties
    from schorg.MedicalObservationalStudy import MedicalObservationalStudyProperties
    from schorg.MedicalObservationalStudy import AllProperties
    from schorg.MedicalObservationalStudy import create_schema_org_model
    from schorg.MedicalObservationalStudy import MedicalObservationalStudy

    a = create_schema_org_model(type_=MedicalObservationalStudyInheritedProperties)
    b = create_schema_org_model(type_=MedicalObservationalStudyProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MedicalObservationalStudy.schema()


def LockerDelivery_test():
    from schorg.LockerDelivery import LockerDeliveryInheritedProperties
    from schorg.LockerDelivery import LockerDeliveryProperties
    from schorg.LockerDelivery import AllProperties
    from schorg.LockerDelivery import create_schema_org_model
    from schorg.LockerDelivery import LockerDelivery

    a = create_schema_org_model(type_=LockerDeliveryInheritedProperties)
    b = create_schema_org_model(type_=LockerDeliveryProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    LockerDelivery.schema()


def ItemListOrderAscending_test():
    from schorg.ItemListOrderAscending import ItemListOrderAscendingInheritedProperties
    from schorg.ItemListOrderAscending import ItemListOrderAscendingProperties
    from schorg.ItemListOrderAscending import AllProperties
    from schorg.ItemListOrderAscending import create_schema_org_model
    from schorg.ItemListOrderAscending import ItemListOrderAscending

    a = create_schema_org_model(type_=ItemListOrderAscendingInheritedProperties)
    b = create_schema_org_model(type_=ItemListOrderAscendingProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ItemListOrderAscending.schema()


def AudioObjectSnapshot_test():
    from schorg.AudioObjectSnapshot import AudioObjectSnapshotInheritedProperties
    from schorg.AudioObjectSnapshot import AudioObjectSnapshotProperties
    from schorg.AudioObjectSnapshot import AllProperties
    from schorg.AudioObjectSnapshot import create_schema_org_model
    from schorg.AudioObjectSnapshot import AudioObjectSnapshot

    a = create_schema_org_model(type_=AudioObjectSnapshotInheritedProperties)
    b = create_schema_org_model(type_=AudioObjectSnapshotProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    AudioObjectSnapshot.schema()


def Statement_test():
    from schorg.Statement import StatementInheritedProperties
    from schorg.Statement import StatementProperties
    from schorg.Statement import AllProperties
    from schorg.Statement import create_schema_org_model
    from schorg.Statement import Statement

    a = create_schema_org_model(type_=StatementInheritedProperties)
    b = create_schema_org_model(type_=StatementProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Statement.schema()


def WearableMeasurementWaist_test():
    from schorg.WearableMeasurementWaist import WearableMeasurementWaistInheritedProperties
    from schorg.WearableMeasurementWaist import WearableMeasurementWaistProperties
    from schorg.WearableMeasurementWaist import AllProperties
    from schorg.WearableMeasurementWaist import create_schema_org_model
    from schorg.WearableMeasurementWaist import WearableMeasurementWaist

    a = create_schema_org_model(type_=WearableMeasurementWaistInheritedProperties)
    b = create_schema_org_model(type_=WearableMeasurementWaistProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    WearableMeasurementWaist.schema()


def WearableMeasurementBack_test():
    from schorg.WearableMeasurementBack import WearableMeasurementBackInheritedProperties
    from schorg.WearableMeasurementBack import WearableMeasurementBackProperties
    from schorg.WearableMeasurementBack import AllProperties
    from schorg.WearableMeasurementBack import create_schema_org_model
    from schorg.WearableMeasurementBack import WearableMeasurementBack

    a = create_schema_org_model(type_=WearableMeasurementBackInheritedProperties)
    b = create_schema_org_model(type_=WearableMeasurementBackProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    WearableMeasurementBack.schema()


def AnaerobicActivity_test():
    from schorg.AnaerobicActivity import AnaerobicActivityInheritedProperties
    from schorg.AnaerobicActivity import AnaerobicActivityProperties
    from schorg.AnaerobicActivity import AllProperties
    from schorg.AnaerobicActivity import create_schema_org_model
    from schorg.AnaerobicActivity import AnaerobicActivity

    a = create_schema_org_model(type_=AnaerobicActivityInheritedProperties)
    b = create_schema_org_model(type_=AnaerobicActivityProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    AnaerobicActivity.schema()


def ReducedRelevanceForChildrenConsideration_test():
    from schorg.ReducedRelevanceForChildrenConsideration import ReducedRelevanceForChildrenConsiderationInheritedProperties
    from schorg.ReducedRelevanceForChildrenConsideration import ReducedRelevanceForChildrenConsiderationProperties
    from schorg.ReducedRelevanceForChildrenConsideration import AllProperties
    from schorg.ReducedRelevanceForChildrenConsideration import create_schema_org_model
    from schorg.ReducedRelevanceForChildrenConsideration import ReducedRelevanceForChildrenConsideration

    a = create_schema_org_model(type_=ReducedRelevanceForChildrenConsiderationInheritedProperties)
    b = create_schema_org_model(type_=ReducedRelevanceForChildrenConsiderationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ReducedRelevanceForChildrenConsideration.schema()


def ResearchOrganization_test():
    from schorg.ResearchOrganization import ResearchOrganizationInheritedProperties
    from schorg.ResearchOrganization import ResearchOrganizationProperties
    from schorg.ResearchOrganization import AllProperties
    from schorg.ResearchOrganization import create_schema_org_model
    from schorg.ResearchOrganization import ResearchOrganization

    a = create_schema_org_model(type_=ResearchOrganizationInheritedProperties)
    b = create_schema_org_model(type_=ResearchOrganizationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ResearchOrganization.schema()


def Eye_test():
    from schorg.Eye import EyeInheritedProperties
    from schorg.Eye import EyeProperties
    from schorg.Eye import AllProperties
    from schorg.Eye import create_schema_org_model
    from schorg.Eye import Eye

    a = create_schema_org_model(type_=EyeInheritedProperties)
    b = create_schema_org_model(type_=EyeProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Eye.schema()


def QAPage_test():
    from schorg.QAPage import QAPageInheritedProperties
    from schorg.QAPage import QAPageProperties
    from schorg.QAPage import AllProperties
    from schorg.QAPage import create_schema_org_model
    from schorg.QAPage import QAPage

    a = create_schema_org_model(type_=QAPageInheritedProperties)
    b = create_schema_org_model(type_=QAPageProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    QAPage.schema()


def Playground_test():
    from schorg.Playground import PlaygroundInheritedProperties
    from schorg.Playground import PlaygroundProperties
    from schorg.Playground import AllProperties
    from schorg.Playground import create_schema_org_model
    from schorg.Playground import Playground

    a = create_schema_org_model(type_=PlaygroundInheritedProperties)
    b = create_schema_org_model(type_=PlaygroundProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Playground.schema()


def ChemicalSubstance_test():
    from schorg.ChemicalSubstance import ChemicalSubstanceInheritedProperties
    from schorg.ChemicalSubstance import ChemicalSubstanceProperties
    from schorg.ChemicalSubstance import AllProperties
    from schorg.ChemicalSubstance import create_schema_org_model
    from schorg.ChemicalSubstance import ChemicalSubstance

    a = create_schema_org_model(type_=ChemicalSubstanceInheritedProperties)
    b = create_schema_org_model(type_=ChemicalSubstanceProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ChemicalSubstance.schema()


def WearableSizeGroupRegular_test():
    from schorg.WearableSizeGroupRegular import WearableSizeGroupRegularInheritedProperties
    from schorg.WearableSizeGroupRegular import WearableSizeGroupRegularProperties
    from schorg.WearableSizeGroupRegular import AllProperties
    from schorg.WearableSizeGroupRegular import create_schema_org_model
    from schorg.WearableSizeGroupRegular import WearableSizeGroupRegular

    a = create_schema_org_model(type_=WearableSizeGroupRegularInheritedProperties)
    b = create_schema_org_model(type_=WearableSizeGroupRegularProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    WearableSizeGroupRegular.schema()


def SubwayStation_test():
    from schorg.SubwayStation import SubwayStationInheritedProperties
    from schorg.SubwayStation import SubwayStationProperties
    from schorg.SubwayStation import AllProperties
    from schorg.SubwayStation import create_schema_org_model
    from schorg.SubwayStation import SubwayStation

    a = create_schema_org_model(type_=SubwayStationInheritedProperties)
    b = create_schema_org_model(type_=SubwayStationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    SubwayStation.schema()


def SomeProducts_test():
    from schorg.SomeProducts import SomeProductsInheritedProperties
    from schorg.SomeProducts import SomeProductsProperties
    from schorg.SomeProducts import AllProperties
    from schorg.SomeProducts import create_schema_org_model
    from schorg.SomeProducts import SomeProducts

    a = create_schema_org_model(type_=SomeProductsInheritedProperties)
    b = create_schema_org_model(type_=SomeProductsProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    SomeProducts.schema()


def MonetaryAmount_test():
    from schorg.MonetaryAmount import MonetaryAmountInheritedProperties
    from schorg.MonetaryAmount import MonetaryAmountProperties
    from schorg.MonetaryAmount import AllProperties
    from schorg.MonetaryAmount import create_schema_org_model
    from schorg.MonetaryAmount import MonetaryAmount

    a = create_schema_org_model(type_=MonetaryAmountInheritedProperties)
    b = create_schema_org_model(type_=MonetaryAmountProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MonetaryAmount.schema()


def AddAction_test():
    from schorg.AddAction import AddActionInheritedProperties
    from schorg.AddAction import AddActionProperties
    from schorg.AddAction import AllProperties
    from schorg.AddAction import create_schema_org_model
    from schorg.AddAction import AddAction

    a = create_schema_org_model(type_=AddActionInheritedProperties)
    b = create_schema_org_model(type_=AddActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    AddAction.schema()


def InsertAction_test():
    from schorg.InsertAction import InsertActionInheritedProperties
    from schorg.InsertAction import InsertActionProperties
    from schorg.InsertAction import AllProperties
    from schorg.InsertAction import create_schema_org_model
    from schorg.InsertAction import InsertAction

    a = create_schema_org_model(type_=InsertActionInheritedProperties)
    b = create_schema_org_model(type_=InsertActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    InsertAction.schema()


def ProductGroup_test():
    from schorg.ProductGroup import ProductGroupInheritedProperties
    from schorg.ProductGroup import ProductGroupProperties
    from schorg.ProductGroup import AllProperties
    from schorg.ProductGroup import create_schema_org_model
    from schorg.ProductGroup import ProductGroup

    a = create_schema_org_model(type_=ProductGroupInheritedProperties)
    b = create_schema_org_model(type_=ProductGroupProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ProductGroup.schema()


def LivingWithHealthAspect_test():
    from schorg.LivingWithHealthAspect import LivingWithHealthAspectInheritedProperties
    from schorg.LivingWithHealthAspect import LivingWithHealthAspectProperties
    from schorg.LivingWithHealthAspect import AllProperties
    from schorg.LivingWithHealthAspect import create_schema_org_model
    from schorg.LivingWithHealthAspect import LivingWithHealthAspect

    a = create_schema_org_model(type_=LivingWithHealthAspectInheritedProperties)
    b = create_schema_org_model(type_=LivingWithHealthAspectProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    LivingWithHealthAspect.schema()


def RecommendedDoseSchedule_test():
    from schorg.RecommendedDoseSchedule import RecommendedDoseScheduleInheritedProperties
    from schorg.RecommendedDoseSchedule import RecommendedDoseScheduleProperties
    from schorg.RecommendedDoseSchedule import AllProperties
    from schorg.RecommendedDoseSchedule import create_schema_org_model
    from schorg.RecommendedDoseSchedule import RecommendedDoseSchedule

    a = create_schema_org_model(type_=RecommendedDoseScheduleInheritedProperties)
    b = create_schema_org_model(type_=RecommendedDoseScheduleProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    RecommendedDoseSchedule.schema()


def ActionAccessSpecification_test():
    from schorg.ActionAccessSpecification import ActionAccessSpecificationInheritedProperties
    from schorg.ActionAccessSpecification import ActionAccessSpecificationProperties
    from schorg.ActionAccessSpecification import AllProperties
    from schorg.ActionAccessSpecification import create_schema_org_model
    from schorg.ActionAccessSpecification import ActionAccessSpecification

    a = create_schema_org_model(type_=ActionAccessSpecificationInheritedProperties)
    b = create_schema_org_model(type_=ActionAccessSpecificationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ActionAccessSpecification.schema()


def Beach_test():
    from schorg.Beach import BeachInheritedProperties
    from schorg.Beach import BeachProperties
    from schorg.Beach import AllProperties
    from schorg.Beach import create_schema_org_model
    from schorg.Beach import Beach

    a = create_schema_org_model(type_=BeachInheritedProperties)
    b = create_schema_org_model(type_=BeachProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Beach.schema()


def OccupationalActivity_test():
    from schorg.OccupationalActivity import OccupationalActivityInheritedProperties
    from schorg.OccupationalActivity import OccupationalActivityProperties
    from schorg.OccupationalActivity import AllProperties
    from schorg.OccupationalActivity import create_schema_org_model
    from schorg.OccupationalActivity import OccupationalActivity

    a = create_schema_org_model(type_=OccupationalActivityInheritedProperties)
    b = create_schema_org_model(type_=OccupationalActivityProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    OccupationalActivity.schema()


def FDAcategoryD_test():
    from schorg.FDAcategoryD import FDAcategoryDInheritedProperties
    from schorg.FDAcategoryD import FDAcategoryDProperties
    from schorg.FDAcategoryD import AllProperties
    from schorg.FDAcategoryD import create_schema_org_model
    from schorg.FDAcategoryD import FDAcategoryD

    a = create_schema_org_model(type_=FDAcategoryDInheritedProperties)
    b = create_schema_org_model(type_=FDAcategoryDProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    FDAcategoryD.schema()


def Podiatric_test():
    from schorg.Podiatric import PodiatricInheritedProperties
    from schorg.Podiatric import PodiatricProperties
    from schorg.Podiatric import AllProperties
    from schorg.Podiatric import create_schema_org_model
    from schorg.Podiatric import Podiatric

    a = create_schema_org_model(type_=PodiatricInheritedProperties)
    b = create_schema_org_model(type_=PodiatricProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Podiatric.schema()


def MedicalScholarlyArticle_test():
    from schorg.MedicalScholarlyArticle import MedicalScholarlyArticleInheritedProperties
    from schorg.MedicalScholarlyArticle import MedicalScholarlyArticleProperties
    from schorg.MedicalScholarlyArticle import AllProperties
    from schorg.MedicalScholarlyArticle import create_schema_org_model
    from schorg.MedicalScholarlyArticle import MedicalScholarlyArticle

    a = create_schema_org_model(type_=MedicalScholarlyArticleInheritedProperties)
    b = create_schema_org_model(type_=MedicalScholarlyArticleProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MedicalScholarlyArticle.schema()


def OfferForLease_test():
    from schorg.OfferForLease import OfferForLeaseInheritedProperties
    from schorg.OfferForLease import OfferForLeaseProperties
    from schorg.OfferForLease import AllProperties
    from schorg.OfferForLease import create_schema_org_model
    from schorg.OfferForLease import OfferForLease

    a = create_schema_org_model(type_=OfferForLeaseInheritedProperties)
    b = create_schema_org_model(type_=OfferForLeaseProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    OfferForLease.schema()


def Church_test():
    from schorg.Church import ChurchInheritedProperties
    from schorg.Church import ChurchProperties
    from schorg.Church import AllProperties
    from schorg.Church import create_schema_org_model
    from schorg.Church import Church

    a = create_schema_org_model(type_=ChurchInheritedProperties)
    b = create_schema_org_model(type_=ChurchProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Church.schema()


def CatholicChurch_test():
    from schorg.CatholicChurch import CatholicChurchInheritedProperties
    from schorg.CatholicChurch import CatholicChurchProperties
    from schorg.CatholicChurch import AllProperties
    from schorg.CatholicChurch import create_schema_org_model
    from schorg.CatholicChurch import CatholicChurch

    a = create_schema_org_model(type_=CatholicChurchInheritedProperties)
    b = create_schema_org_model(type_=CatholicChurchProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    CatholicChurch.schema()


def ReservationHold_test():
    from schorg.ReservationHold import ReservationHoldInheritedProperties
    from schorg.ReservationHold import ReservationHoldProperties
    from schorg.ReservationHold import AllProperties
    from schorg.ReservationHold import create_schema_org_model
    from schorg.ReservationHold import ReservationHold

    a = create_schema_org_model(type_=ReservationHoldInheritedProperties)
    b = create_schema_org_model(type_=ReservationHoldProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ReservationHold.schema()


def Nonprofit501c6_test():
    from schorg.Nonprofit501c6 import Nonprofit501c6InheritedProperties
    from schorg.Nonprofit501c6 import Nonprofit501c6Properties
    from schorg.Nonprofit501c6 import AllProperties
    from schorg.Nonprofit501c6 import create_schema_org_model
    from schorg.Nonprofit501c6 import Nonprofit501c6

    a = create_schema_org_model(type_=Nonprofit501c6InheritedProperties)
    b = create_schema_org_model(type_=Nonprofit501c6Properties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Nonprofit501c6.schema()


def Midwifery_test():
    from schorg.Midwifery import MidwiferyInheritedProperties
    from schorg.Midwifery import MidwiferyProperties
    from schorg.Midwifery import AllProperties
    from schorg.Midwifery import create_schema_org_model
    from schorg.Midwifery import Midwifery

    a = create_schema_org_model(type_=MidwiferyInheritedProperties)
    b = create_schema_org_model(type_=MidwiferyProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Midwifery.schema()


def LiveAlbum_test():
    from schorg.LiveAlbum import LiveAlbumInheritedProperties
    from schorg.LiveAlbum import LiveAlbumProperties
    from schorg.LiveAlbum import AllProperties
    from schorg.LiveAlbum import create_schema_org_model
    from schorg.LiveAlbum import LiveAlbum

    a = create_schema_org_model(type_=LiveAlbumInheritedProperties)
    b = create_schema_org_model(type_=LiveAlbumProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    LiveAlbum.schema()


def ExhibitionEvent_test():
    from schorg.ExhibitionEvent import ExhibitionEventInheritedProperties
    from schorg.ExhibitionEvent import ExhibitionEventProperties
    from schorg.ExhibitionEvent import AllProperties
    from schorg.ExhibitionEvent import create_schema_org_model
    from schorg.ExhibitionEvent import ExhibitionEvent

    a = create_schema_org_model(type_=ExhibitionEventInheritedProperties)
    b = create_schema_org_model(type_=ExhibitionEventProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ExhibitionEvent.schema()


def FullGameAvailability_test():
    from schorg.FullGameAvailability import FullGameAvailabilityInheritedProperties
    from schorg.FullGameAvailability import FullGameAvailabilityProperties
    from schorg.FullGameAvailability import AllProperties
    from schorg.FullGameAvailability import create_schema_org_model
    from schorg.FullGameAvailability import FullGameAvailability

    a = create_schema_org_model(type_=FullGameAvailabilityInheritedProperties)
    b = create_schema_org_model(type_=FullGameAvailabilityProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    FullGameAvailability.schema()


def ResumeAction_test():
    from schorg.ResumeAction import ResumeActionInheritedProperties
    from schorg.ResumeAction import ResumeActionProperties
    from schorg.ResumeAction import AllProperties
    from schorg.ResumeAction import create_schema_org_model
    from schorg.ResumeAction import ResumeAction

    a = create_schema_org_model(type_=ResumeActionInheritedProperties)
    b = create_schema_org_model(type_=ResumeActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ResumeAction.schema()


def ProgramMembership_test():
    from schorg.ProgramMembership import ProgramMembershipInheritedProperties
    from schorg.ProgramMembership import ProgramMembershipProperties
    from schorg.ProgramMembership import AllProperties
    from schorg.ProgramMembership import create_schema_org_model
    from schorg.ProgramMembership import ProgramMembership

    a = create_schema_org_model(type_=ProgramMembershipInheritedProperties)
    b = create_schema_org_model(type_=ProgramMembershipProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ProgramMembership.schema()


def DiscoverAction_test():
    from schorg.DiscoverAction import DiscoverActionInheritedProperties
    from schorg.DiscoverAction import DiscoverActionProperties
    from schorg.DiscoverAction import AllProperties
    from schorg.DiscoverAction import create_schema_org_model
    from schorg.DiscoverAction import DiscoverAction

    a = create_schema_org_model(type_=DiscoverActionInheritedProperties)
    b = create_schema_org_model(type_=DiscoverActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    DiscoverAction.schema()


def OfflinePermanently_test():
    from schorg.OfflinePermanently import OfflinePermanentlyInheritedProperties
    from schorg.OfflinePermanently import OfflinePermanentlyProperties
    from schorg.OfflinePermanently import AllProperties
    from schorg.OfflinePermanently import create_schema_org_model
    from schorg.OfflinePermanently import OfflinePermanently

    a = create_schema_org_model(type_=OfflinePermanentlyInheritedProperties)
    b = create_schema_org_model(type_=OfflinePermanentlyProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    OfflinePermanently.schema()


def CafeOrCoffeeShop_test():
    from schorg.CafeOrCoffeeShop import CafeOrCoffeeShopInheritedProperties
    from schorg.CafeOrCoffeeShop import CafeOrCoffeeShopProperties
    from schorg.CafeOrCoffeeShop import AllProperties
    from schorg.CafeOrCoffeeShop import create_schema_org_model
    from schorg.CafeOrCoffeeShop import CafeOrCoffeeShop

    a = create_schema_org_model(type_=CafeOrCoffeeShopInheritedProperties)
    b = create_schema_org_model(type_=CafeOrCoffeeShopProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    CafeOrCoffeeShop.schema()


def ReimbursementCap_test():
    from schorg.ReimbursementCap import ReimbursementCapInheritedProperties
    from schorg.ReimbursementCap import ReimbursementCapProperties
    from schorg.ReimbursementCap import AllProperties
    from schorg.ReimbursementCap import create_schema_org_model
    from schorg.ReimbursementCap import ReimbursementCap

    a = create_schema_org_model(type_=ReimbursementCapInheritedProperties)
    b = create_schema_org_model(type_=ReimbursementCapProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ReimbursementCap.schema()


def DryCleaningOrLaundry_test():
    from schorg.DryCleaningOrLaundry import DryCleaningOrLaundryInheritedProperties
    from schorg.DryCleaningOrLaundry import DryCleaningOrLaundryProperties
    from schorg.DryCleaningOrLaundry import AllProperties
    from schorg.DryCleaningOrLaundry import create_schema_org_model
    from schorg.DryCleaningOrLaundry import DryCleaningOrLaundry

    a = create_schema_org_model(type_=DryCleaningOrLaundryInheritedProperties)
    b = create_schema_org_model(type_=DryCleaningOrLaundryProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    DryCleaningOrLaundry.schema()


def ContagiousnessHealthAspect_test():
    from schorg.ContagiousnessHealthAspect import ContagiousnessHealthAspectInheritedProperties
    from schorg.ContagiousnessHealthAspect import ContagiousnessHealthAspectProperties
    from schorg.ContagiousnessHealthAspect import AllProperties
    from schorg.ContagiousnessHealthAspect import create_schema_org_model
    from schorg.ContagiousnessHealthAspect import ContagiousnessHealthAspect

    a = create_schema_org_model(type_=ContagiousnessHealthAspectInheritedProperties)
    b = create_schema_org_model(type_=ContagiousnessHealthAspectProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ContagiousnessHealthAspect.schema()


def RVPark_test():
    from schorg.RVPark import RVParkInheritedProperties
    from schorg.RVPark import RVParkProperties
    from schorg.RVPark import AllProperties
    from schorg.RVPark import create_schema_org_model
    from schorg.RVPark import RVPark

    a = create_schema_org_model(type_=RVParkInheritedProperties)
    b = create_schema_org_model(type_=RVParkProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    RVPark.schema()


def LymphaticVessel_test():
    from schorg.LymphaticVessel import LymphaticVesselInheritedProperties
    from schorg.LymphaticVessel import LymphaticVesselProperties
    from schorg.LymphaticVessel import AllProperties
    from schorg.LymphaticVessel import create_schema_org_model
    from schorg.LymphaticVessel import LymphaticVessel

    a = create_schema_org_model(type_=LymphaticVesselInheritedProperties)
    b = create_schema_org_model(type_=LymphaticVesselProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    LymphaticVessel.schema()


def ExchangeRefund_test():
    from schorg.ExchangeRefund import ExchangeRefundInheritedProperties
    from schorg.ExchangeRefund import ExchangeRefundProperties
    from schorg.ExchangeRefund import AllProperties
    from schorg.ExchangeRefund import create_schema_org_model
    from schorg.ExchangeRefund import ExchangeRefund

    a = create_schema_org_model(type_=ExchangeRefundInheritedProperties)
    b = create_schema_org_model(type_=ExchangeRefundProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ExchangeRefund.schema()


def CharitableIncorporatedOrganization_test():
    from schorg.CharitableIncorporatedOrganization import CharitableIncorporatedOrganizationInheritedProperties
    from schorg.CharitableIncorporatedOrganization import CharitableIncorporatedOrganizationProperties
    from schorg.CharitableIncorporatedOrganization import AllProperties
    from schorg.CharitableIncorporatedOrganization import create_schema_org_model
    from schorg.CharitableIncorporatedOrganization import CharitableIncorporatedOrganization

    a = create_schema_org_model(type_=CharitableIncorporatedOrganizationInheritedProperties)
    b = create_schema_org_model(type_=CharitableIncorporatedOrganizationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    CharitableIncorporatedOrganization.schema()


def Discontinued_test():
    from schorg.Discontinued import DiscontinuedInheritedProperties
    from schorg.Discontinued import DiscontinuedProperties
    from schorg.Discontinued import AllProperties
    from schorg.Discontinued import create_schema_org_model
    from schorg.Discontinued import Discontinued

    a = create_schema_org_model(type_=DiscontinuedInheritedProperties)
    b = create_schema_org_model(type_=DiscontinuedProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Discontinued.schema()


def BodyMeasurementNeck_test():
    from schorg.BodyMeasurementNeck import BodyMeasurementNeckInheritedProperties
    from schorg.BodyMeasurementNeck import BodyMeasurementNeckProperties
    from schorg.BodyMeasurementNeck import AllProperties
    from schorg.BodyMeasurementNeck import create_schema_org_model
    from schorg.BodyMeasurementNeck import BodyMeasurementNeck

    a = create_schema_org_model(type_=BodyMeasurementNeckInheritedProperties)
    b = create_schema_org_model(type_=BodyMeasurementNeckProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    BodyMeasurementNeck.schema()


def EvidenceLevelA_test():
    from schorg.EvidenceLevelA import EvidenceLevelAInheritedProperties
    from schorg.EvidenceLevelA import EvidenceLevelAProperties
    from schorg.EvidenceLevelA import AllProperties
    from schorg.EvidenceLevelA import create_schema_org_model
    from schorg.EvidenceLevelA import EvidenceLevelA

    a = create_schema_org_model(type_=EvidenceLevelAInheritedProperties)
    b = create_schema_org_model(type_=EvidenceLevelAProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    EvidenceLevelA.schema()


def SpeechPathology_test():
    from schorg.SpeechPathology import SpeechPathologyInheritedProperties
    from schorg.SpeechPathology import SpeechPathologyProperties
    from schorg.SpeechPathology import AllProperties
    from schorg.SpeechPathology import create_schema_org_model
    from schorg.SpeechPathology import SpeechPathology

    a = create_schema_org_model(type_=SpeechPathologyInheritedProperties)
    b = create_schema_org_model(type_=SpeechPathologyProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    SpeechPathology.schema()


def OpeningHoursSpecification_test():
    from schorg.OpeningHoursSpecification import OpeningHoursSpecificationInheritedProperties
    from schorg.OpeningHoursSpecification import OpeningHoursSpecificationProperties
    from schorg.OpeningHoursSpecification import AllProperties
    from schorg.OpeningHoursSpecification import create_schema_org_model
    from schorg.OpeningHoursSpecification import OpeningHoursSpecification

    a = create_schema_org_model(type_=OpeningHoursSpecificationInheritedProperties)
    b = create_schema_org_model(type_=OpeningHoursSpecificationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    OpeningHoursSpecification.schema()


def PresentationDigitalDocument_test():
    from schorg.PresentationDigitalDocument import PresentationDigitalDocumentInheritedProperties
    from schorg.PresentationDigitalDocument import PresentationDigitalDocumentProperties
    from schorg.PresentationDigitalDocument import AllProperties
    from schorg.PresentationDigitalDocument import create_schema_org_model
    from schorg.PresentationDigitalDocument import PresentationDigitalDocument

    a = create_schema_org_model(type_=PresentationDigitalDocumentInheritedProperties)
    b = create_schema_org_model(type_=PresentationDigitalDocumentProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    PresentationDigitalDocument.schema()


def ProfessionalService_test():
    from schorg.ProfessionalService import ProfessionalServiceInheritedProperties
    from schorg.ProfessionalService import ProfessionalServiceProperties
    from schorg.ProfessionalService import AllProperties
    from schorg.ProfessionalService import create_schema_org_model
    from schorg.ProfessionalService import ProfessionalService

    a = create_schema_org_model(type_=ProfessionalServiceInheritedProperties)
    b = create_schema_org_model(type_=ProfessionalServiceProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ProfessionalService.schema()


def BankOrCreditUnion_test():
    from schorg.BankOrCreditUnion import BankOrCreditUnionInheritedProperties
    from schorg.BankOrCreditUnion import BankOrCreditUnionProperties
    from schorg.BankOrCreditUnion import AllProperties
    from schorg.BankOrCreditUnion import create_schema_org_model
    from schorg.BankOrCreditUnion import BankOrCreditUnion

    a = create_schema_org_model(type_=BankOrCreditUnionInheritedProperties)
    b = create_schema_org_model(type_=BankOrCreditUnionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    BankOrCreditUnion.schema()


def IngredientsHealthAspect_test():
    from schorg.IngredientsHealthAspect import IngredientsHealthAspectInheritedProperties
    from schorg.IngredientsHealthAspect import IngredientsHealthAspectProperties
    from schorg.IngredientsHealthAspect import AllProperties
    from schorg.IngredientsHealthAspect import create_schema_org_model
    from schorg.IngredientsHealthAspect import IngredientsHealthAspect

    a = create_schema_org_model(type_=IngredientsHealthAspectInheritedProperties)
    b = create_schema_org_model(type_=IngredientsHealthAspectProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    IngredientsHealthAspect.schema()


def PhysicalTherapy_test():
    from schorg.PhysicalTherapy import PhysicalTherapyInheritedProperties
    from schorg.PhysicalTherapy import PhysicalTherapyProperties
    from schorg.PhysicalTherapy import AllProperties
    from schorg.PhysicalTherapy import create_schema_org_model
    from schorg.PhysicalTherapy import PhysicalTherapy

    a = create_schema_org_model(type_=PhysicalTherapyInheritedProperties)
    b = create_schema_org_model(type_=PhysicalTherapyProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    PhysicalTherapy.schema()


def Substance_test():
    from schorg.Substance import SubstanceInheritedProperties
    from schorg.Substance import SubstanceProperties
    from schorg.Substance import AllProperties
    from schorg.Substance import create_schema_org_model
    from schorg.Substance import Substance

    a = create_schema_org_model(type_=SubstanceInheritedProperties)
    b = create_schema_org_model(type_=SubstanceProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Substance.schema()


def Drug_test():
    from schorg.Drug import DrugInheritedProperties
    from schorg.Drug import DrugProperties
    from schorg.Drug import AllProperties
    from schorg.Drug import create_schema_org_model
    from schorg.Drug import Drug

    a = create_schema_org_model(type_=DrugInheritedProperties)
    b = create_schema_org_model(type_=DrugProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Drug.schema()


def Season_test():
    from schorg.Season import SeasonInheritedProperties
    from schorg.Season import SeasonProperties
    from schorg.Season import AllProperties
    from schorg.Season import create_schema_org_model
    from schorg.Season import Season

    a = create_schema_org_model(type_=SeasonInheritedProperties)
    b = create_schema_org_model(type_=SeasonProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Season.schema()


def EventVenue_test():
    from schorg.EventVenue import EventVenueInheritedProperties
    from schorg.EventVenue import EventVenueProperties
    from schorg.EventVenue import AllProperties
    from schorg.EventVenue import create_schema_org_model
    from schorg.EventVenue import EventVenue

    a = create_schema_org_model(type_=EventVenueInheritedProperties)
    b = create_schema_org_model(type_=EventVenueProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    EventVenue.schema()


def EPRelease_test():
    from schorg.EPRelease import EPReleaseInheritedProperties
    from schorg.EPRelease import EPReleaseProperties
    from schorg.EPRelease import AllProperties
    from schorg.EPRelease import create_schema_org_model
    from schorg.EPRelease import EPRelease

    a = create_schema_org_model(type_=EPReleaseInheritedProperties)
    b = create_schema_org_model(type_=EPReleaseProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    EPRelease.schema()


def ReservationPackage_test():
    from schorg.ReservationPackage import ReservationPackageInheritedProperties
    from schorg.ReservationPackage import ReservationPackageProperties
    from schorg.ReservationPackage import AllProperties
    from schorg.ReservationPackage import create_schema_org_model
    from schorg.ReservationPackage import ReservationPackage

    a = create_schema_org_model(type_=ReservationPackageInheritedProperties)
    b = create_schema_org_model(type_=ReservationPackageProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ReservationPackage.schema()


def AutoBodyShop_test():
    from schorg.AutoBodyShop import AutoBodyShopInheritedProperties
    from schorg.AutoBodyShop import AutoBodyShopProperties
    from schorg.AutoBodyShop import AllProperties
    from schorg.AutoBodyShop import create_schema_org_model
    from schorg.AutoBodyShop import AutoBodyShop

    a = create_schema_org_model(type_=AutoBodyShopInheritedProperties)
    b = create_schema_org_model(type_=AutoBodyShopProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    AutoBodyShop.schema()


def TypesHealthAspect_test():
    from schorg.TypesHealthAspect import TypesHealthAspectInheritedProperties
    from schorg.TypesHealthAspect import TypesHealthAspectProperties
    from schorg.TypesHealthAspect import AllProperties
    from schorg.TypesHealthAspect import create_schema_org_model
    from schorg.TypesHealthAspect import TypesHealthAspect

    a = create_schema_org_model(type_=TypesHealthAspectInheritedProperties)
    b = create_schema_org_model(type_=TypesHealthAspectProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    TypesHealthAspect.schema()


def CheckAction_test():
    from schorg.CheckAction import CheckActionInheritedProperties
    from schorg.CheckAction import CheckActionProperties
    from schorg.CheckAction import AllProperties
    from schorg.CheckAction import create_schema_org_model
    from schorg.CheckAction import CheckAction

    a = create_schema_org_model(type_=CheckActionInheritedProperties)
    b = create_schema_org_model(type_=CheckActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    CheckAction.schema()


def StudioAlbum_test():
    from schorg.StudioAlbum import StudioAlbumInheritedProperties
    from schorg.StudioAlbum import StudioAlbumProperties
    from schorg.StudioAlbum import AllProperties
    from schorg.StudioAlbum import create_schema_org_model
    from schorg.StudioAlbum import StudioAlbum

    a = create_schema_org_model(type_=StudioAlbumInheritedProperties)
    b = create_schema_org_model(type_=StudioAlbumProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    StudioAlbum.schema()


def DisabilitySupport_test():
    from schorg.DisabilitySupport import DisabilitySupportInheritedProperties
    from schorg.DisabilitySupport import DisabilitySupportProperties
    from schorg.DisabilitySupport import AllProperties
    from schorg.DisabilitySupport import create_schema_org_model
    from schorg.DisabilitySupport import DisabilitySupport

    a = create_schema_org_model(type_=DisabilitySupportInheritedProperties)
    b = create_schema_org_model(type_=DisabilitySupportProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    DisabilitySupport.schema()


def StagesHealthAspect_test():
    from schorg.StagesHealthAspect import StagesHealthAspectInheritedProperties
    from schorg.StagesHealthAspect import StagesHealthAspectProperties
    from schorg.StagesHealthAspect import AllProperties
    from schorg.StagesHealthAspect import create_schema_org_model
    from schorg.StagesHealthAspect import StagesHealthAspect

    a = create_schema_org_model(type_=StagesHealthAspectInheritedProperties)
    b = create_schema_org_model(type_=StagesHealthAspectProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    StagesHealthAspect.schema()


def Legislation_test():
    from schorg.Legislation import LegislationInheritedProperties
    from schorg.Legislation import LegislationProperties
    from schorg.Legislation import AllProperties
    from schorg.Legislation import create_schema_org_model
    from schorg.Legislation import Legislation

    a = create_schema_org_model(type_=LegislationInheritedProperties)
    b = create_schema_org_model(type_=LegislationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Legislation.schema()


def LegislationObject_test():
    from schorg.LegislationObject import LegislationObjectInheritedProperties
    from schorg.LegislationObject import LegislationObjectProperties
    from schorg.LegislationObject import AllProperties
    from schorg.LegislationObject import create_schema_org_model
    from schorg.LegislationObject import LegislationObject

    a = create_schema_org_model(type_=LegislationObjectInheritedProperties)
    b = create_schema_org_model(type_=LegislationObjectProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    LegislationObject.schema()


def Airport_test():
    from schorg.Airport import AirportInheritedProperties
    from schorg.Airport import AirportProperties
    from schorg.Airport import AllProperties
    from schorg.Airport import create_schema_org_model
    from schorg.Airport import Airport

    a = create_schema_org_model(type_=AirportInheritedProperties)
    b = create_schema_org_model(type_=AirportProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Airport.schema()


def UserLikes_test():
    from schorg.UserLikes import UserLikesInheritedProperties
    from schorg.UserLikes import UserLikesProperties
    from schorg.UserLikes import AllProperties
    from schorg.UserLikes import create_schema_org_model
    from schorg.UserLikes import UserLikes

    a = create_schema_org_model(type_=UserLikesInheritedProperties)
    b = create_schema_org_model(type_=UserLikesProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    UserLikes.schema()


def AmpStory_test():
    from schorg.AmpStory import AmpStoryInheritedProperties
    from schorg.AmpStory import AmpStoryProperties
    from schorg.AmpStory import AllProperties
    from schorg.AmpStory import create_schema_org_model
    from schorg.AmpStory import AmpStory

    a = create_schema_org_model(type_=AmpStoryInheritedProperties)
    b = create_schema_org_model(type_=AmpStoryProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    AmpStory.schema()


def CookAction_test():
    from schorg.CookAction import CookActionInheritedProperties
    from schorg.CookAction import CookActionProperties
    from schorg.CookAction import AllProperties
    from schorg.CookAction import create_schema_org_model
    from schorg.CookAction import CookAction

    a = create_schema_org_model(type_=CookActionInheritedProperties)
    b = create_schema_org_model(type_=CookActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    CookAction.schema()


def MedicalWebPage_test():
    from schorg.MedicalWebPage import MedicalWebPageInheritedProperties
    from schorg.MedicalWebPage import MedicalWebPageProperties
    from schorg.MedicalWebPage import AllProperties
    from schorg.MedicalWebPage import create_schema_org_model
    from schorg.MedicalWebPage import MedicalWebPage

    a = create_schema_org_model(type_=MedicalWebPageInheritedProperties)
    b = create_schema_org_model(type_=MedicalWebPageProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MedicalWebPage.schema()


def Throat_test():
    from schorg.Throat import ThroatInheritedProperties
    from schorg.Throat import ThroatProperties
    from schorg.Throat import AllProperties
    from schorg.Throat import create_schema_org_model
    from schorg.Throat import Throat

    a = create_schema_org_model(type_=ThroatInheritedProperties)
    b = create_schema_org_model(type_=ThroatProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Throat.schema()


def Urologic_test():
    from schorg.Urologic import UrologicInheritedProperties
    from schorg.Urologic import UrologicProperties
    from schorg.Urologic import AllProperties
    from schorg.Urologic import create_schema_org_model
    from schorg.Urologic import Urologic

    a = create_schema_org_model(type_=UrologicInheritedProperties)
    b = create_schema_org_model(type_=UrologicProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Urologic.schema()


def StadiumOrArena_test():
    from schorg.StadiumOrArena import StadiumOrArenaInheritedProperties
    from schorg.StadiumOrArena import StadiumOrArenaProperties
    from schorg.StadiumOrArena import AllProperties
    from schorg.StadiumOrArena import create_schema_org_model
    from schorg.StadiumOrArena import StadiumOrArena

    a = create_schema_org_model(type_=StadiumOrArenaInheritedProperties)
    b = create_schema_org_model(type_=StadiumOrArenaProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    StadiumOrArena.schema()


def FDAnotEvaluated_test():
    from schorg.FDAnotEvaluated import FDAnotEvaluatedInheritedProperties
    from schorg.FDAnotEvaluated import FDAnotEvaluatedProperties
    from schorg.FDAnotEvaluated import AllProperties
    from schorg.FDAnotEvaluated import create_schema_org_model
    from schorg.FDAnotEvaluated import FDAnotEvaluated

    a = create_schema_org_model(type_=FDAnotEvaluatedInheritedProperties)
    b = create_schema_org_model(type_=FDAnotEvaluatedProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    FDAnotEvaluated.schema()


def Cardiovascular_test():
    from schorg.Cardiovascular import CardiovascularInheritedProperties
    from schorg.Cardiovascular import CardiovascularProperties
    from schorg.Cardiovascular import AllProperties
    from schorg.Cardiovascular import create_schema_org_model
    from schorg.Cardiovascular import Cardiovascular

    a = create_schema_org_model(type_=CardiovascularInheritedProperties)
    b = create_schema_org_model(type_=CardiovascularProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Cardiovascular.schema()


def UserComments_test():
    from schorg.UserComments import UserCommentsInheritedProperties
    from schorg.UserComments import UserCommentsProperties
    from schorg.UserComments import AllProperties
    from schorg.UserComments import create_schema_org_model
    from schorg.UserComments import UserComments

    a = create_schema_org_model(type_=UserCommentsInheritedProperties)
    b = create_schema_org_model(type_=UserCommentsProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    UserComments.schema()


def Lung_test():
    from schorg.Lung import LungInheritedProperties
    from schorg.Lung import LungProperties
    from schorg.Lung import AllProperties
    from schorg.Lung import create_schema_org_model
    from schorg.Lung import Lung

    a = create_schema_org_model(type_=LungInheritedProperties)
    b = create_schema_org_model(type_=LungProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Lung.schema()


def ReserveAction_test():
    from schorg.ReserveAction import ReserveActionInheritedProperties
    from schorg.ReserveAction import ReserveActionProperties
    from schorg.ReserveAction import AllProperties
    from schorg.ReserveAction import create_schema_org_model
    from schorg.ReserveAction import ReserveAction

    a = create_schema_org_model(type_=ReserveActionInheritedProperties)
    b = create_schema_org_model(type_=ReserveActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ReserveAction.schema()


def OrderInTransit_test():
    from schorg.OrderInTransit import OrderInTransitInheritedProperties
    from schorg.OrderInTransit import OrderInTransitProperties
    from schorg.OrderInTransit import AllProperties
    from schorg.OrderInTransit import create_schema_org_model
    from schorg.OrderInTransit import OrderInTransit

    a = create_schema_org_model(type_=OrderInTransitInheritedProperties)
    b = create_schema_org_model(type_=OrderInTransitProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    OrderInTransit.schema()


def BusinessEvent_test():
    from schorg.BusinessEvent import BusinessEventInheritedProperties
    from schorg.BusinessEvent import BusinessEventProperties
    from schorg.BusinessEvent import AllProperties
    from schorg.BusinessEvent import create_schema_org_model
    from schorg.BusinessEvent import BusinessEvent

    a = create_schema_org_model(type_=BusinessEventInheritedProperties)
    b = create_schema_org_model(type_=BusinessEventProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    BusinessEvent.schema()


def MusicComposition_test():
    from schorg.MusicComposition import MusicCompositionInheritedProperties
    from schorg.MusicComposition import MusicCompositionProperties
    from schorg.MusicComposition import AllProperties
    from schorg.MusicComposition import create_schema_org_model
    from schorg.MusicComposition import MusicComposition

    a = create_schema_org_model(type_=MusicCompositionInheritedProperties)
    b = create_schema_org_model(type_=MusicCompositionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MusicComposition.schema()


def WinAction_test():
    from schorg.WinAction import WinActionInheritedProperties
    from schorg.WinAction import WinActionProperties
    from schorg.WinAction import AllProperties
    from schorg.WinAction import create_schema_org_model
    from schorg.WinAction import WinAction

    a = create_schema_org_model(type_=WinActionInheritedProperties)
    b = create_schema_org_model(type_=WinActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    WinAction.schema()


def SalePrice_test():
    from schorg.SalePrice import SalePriceInheritedProperties
    from schorg.SalePrice import SalePriceProperties
    from schorg.SalePrice import AllProperties
    from schorg.SalePrice import create_schema_org_model
    from schorg.SalePrice import SalePrice

    a = create_schema_org_model(type_=SalePriceInheritedProperties)
    b = create_schema_org_model(type_=SalePriceProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    SalePrice.schema()


def ListItem_test():
    from schorg.ListItem import ListItemInheritedProperties
    from schorg.ListItem import ListItemProperties
    from schorg.ListItem import AllProperties
    from schorg.ListItem import create_schema_org_model
    from schorg.ListItem import ListItem

    a = create_schema_org_model(type_=ListItemInheritedProperties)
    b = create_schema_org_model(type_=ListItemProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ListItem.schema()


def HowToTip_test():
    from schorg.HowToTip import HowToTipInheritedProperties
    from schorg.HowToTip import HowToTipProperties
    from schorg.HowToTip import AllProperties
    from schorg.HowToTip import create_schema_org_model
    from schorg.HowToTip import HowToTip

    a = create_schema_org_model(type_=HowToTipInheritedProperties)
    b = create_schema_org_model(type_=HowToTipProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    HowToTip.schema()


def Longitudinal_test():
    from schorg.Longitudinal import LongitudinalInheritedProperties
    from schorg.Longitudinal import LongitudinalProperties
    from schorg.Longitudinal import AllProperties
    from schorg.Longitudinal import create_schema_org_model
    from schorg.Longitudinal import Longitudinal

    a = create_schema_org_model(type_=LongitudinalInheritedProperties)
    b = create_schema_org_model(type_=LongitudinalProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Longitudinal.schema()


def Hackathon_test():
    from schorg.Hackathon import HackathonInheritedProperties
    from schorg.Hackathon import HackathonProperties
    from schorg.Hackathon import AllProperties
    from schorg.Hackathon import create_schema_org_model
    from schorg.Hackathon import Hackathon

    a = create_schema_org_model(type_=HackathonInheritedProperties)
    b = create_schema_org_model(type_=HackathonProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Hackathon.schema()


def StatisticalPopulation_test():
    from schorg.StatisticalPopulation import StatisticalPopulationInheritedProperties
    from schorg.StatisticalPopulation import StatisticalPopulationProperties
    from schorg.StatisticalPopulation import AllProperties
    from schorg.StatisticalPopulation import create_schema_org_model
    from schorg.StatisticalPopulation import StatisticalPopulation

    a = create_schema_org_model(type_=StatisticalPopulationInheritedProperties)
    b = create_schema_org_model(type_=StatisticalPopulationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    StatisticalPopulation.schema()


def WriteAction_test():
    from schorg.WriteAction import WriteActionInheritedProperties
    from schorg.WriteAction import WriteActionProperties
    from schorg.WriteAction import AllProperties
    from schorg.WriteAction import create_schema_org_model
    from schorg.WriteAction import WriteAction

    a = create_schema_org_model(type_=WriteActionInheritedProperties)
    b = create_schema_org_model(type_=WriteActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    WriteAction.schema()


def HowToSection_test():
    from schorg.HowToSection import HowToSectionInheritedProperties
    from schorg.HowToSection import HowToSectionProperties
    from schorg.HowToSection import AllProperties
    from schorg.HowToSection import create_schema_org_model
    from schorg.HowToSection import HowToSection

    a = create_schema_org_model(type_=HowToSectionInheritedProperties)
    b = create_schema_org_model(type_=HowToSectionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    HowToSection.schema()


def HVACBusiness_test():
    from schorg.HVACBusiness import HVACBusinessInheritedProperties
    from schorg.HVACBusiness import HVACBusinessProperties
    from schorg.HVACBusiness import AllProperties
    from schorg.HVACBusiness import create_schema_org_model
    from schorg.HVACBusiness import HVACBusiness

    a = create_schema_org_model(type_=HVACBusinessInheritedProperties)
    b = create_schema_org_model(type_=HVACBusinessProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    HVACBusiness.schema()


def RepaymentSpecification_test():
    from schorg.RepaymentSpecification import RepaymentSpecificationInheritedProperties
    from schorg.RepaymentSpecification import RepaymentSpecificationProperties
    from schorg.RepaymentSpecification import AllProperties
    from schorg.RepaymentSpecification import create_schema_org_model
    from schorg.RepaymentSpecification import RepaymentSpecification

    a = create_schema_org_model(type_=RepaymentSpecificationInheritedProperties)
    b = create_schema_org_model(type_=RepaymentSpecificationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    RepaymentSpecification.schema()


def RelatedTopicsHealthAspect_test():
    from schorg.RelatedTopicsHealthAspect import RelatedTopicsHealthAspectInheritedProperties
    from schorg.RelatedTopicsHealthAspect import RelatedTopicsHealthAspectProperties
    from schorg.RelatedTopicsHealthAspect import AllProperties
    from schorg.RelatedTopicsHealthAspect import create_schema_org_model
    from schorg.RelatedTopicsHealthAspect import RelatedTopicsHealthAspect

    a = create_schema_org_model(type_=RelatedTopicsHealthAspectInheritedProperties)
    b = create_schema_org_model(type_=RelatedTopicsHealthAspectProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    RelatedTopicsHealthAspect.schema()


def UserPlusOnes_test():
    from schorg.UserPlusOnes import UserPlusOnesInheritedProperties
    from schorg.UserPlusOnes import UserPlusOnesProperties
    from schorg.UserPlusOnes import AllProperties
    from schorg.UserPlusOnes import create_schema_org_model
    from schorg.UserPlusOnes import UserPlusOnes

    a = create_schema_org_model(type_=UserPlusOnesInheritedProperties)
    b = create_schema_org_model(type_=UserPlusOnesProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    UserPlusOnes.schema()


def Gynecologic_test():
    from schorg.Gynecologic import GynecologicInheritedProperties
    from schorg.Gynecologic import GynecologicProperties
    from schorg.Gynecologic import AllProperties
    from schorg.Gynecologic import create_schema_org_model
    from schorg.Gynecologic import Gynecologic

    a = create_schema_org_model(type_=GynecologicInheritedProperties)
    b = create_schema_org_model(type_=GynecologicProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Gynecologic.schema()


def MerchantReturnNotPermitted_test():
    from schorg.MerchantReturnNotPermitted import MerchantReturnNotPermittedInheritedProperties
    from schorg.MerchantReturnNotPermitted import MerchantReturnNotPermittedProperties
    from schorg.MerchantReturnNotPermitted import AllProperties
    from schorg.MerchantReturnNotPermitted import create_schema_org_model
    from schorg.MerchantReturnNotPermitted import MerchantReturnNotPermitted

    a = create_schema_org_model(type_=MerchantReturnNotPermittedInheritedProperties)
    b = create_schema_org_model(type_=MerchantReturnNotPermittedProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MerchantReturnNotPermitted.schema()


def OrderPickupAvailable_test():
    from schorg.OrderPickupAvailable import OrderPickupAvailableInheritedProperties
    from schorg.OrderPickupAvailable import OrderPickupAvailableProperties
    from schorg.OrderPickupAvailable import AllProperties
    from schorg.OrderPickupAvailable import create_schema_org_model
    from schorg.OrderPickupAvailable import OrderPickupAvailable

    a = create_schema_org_model(type_=OrderPickupAvailableInheritedProperties)
    b = create_schema_org_model(type_=OrderPickupAvailableProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    OrderPickupAvailable.schema()


def DeliveryEvent_test():
    from schorg.DeliveryEvent import DeliveryEventInheritedProperties
    from schorg.DeliveryEvent import DeliveryEventProperties
    from schorg.DeliveryEvent import AllProperties
    from schorg.DeliveryEvent import create_schema_org_model
    from schorg.DeliveryEvent import DeliveryEvent

    a = create_schema_org_model(type_=DeliveryEventInheritedProperties)
    b = create_schema_org_model(type_=DeliveryEventProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    DeliveryEvent.schema()


def LimitedByGuaranteeCharity_test():
    from schorg.LimitedByGuaranteeCharity import LimitedByGuaranteeCharityInheritedProperties
    from schorg.LimitedByGuaranteeCharity import LimitedByGuaranteeCharityProperties
    from schorg.LimitedByGuaranteeCharity import AllProperties
    from schorg.LimitedByGuaranteeCharity import create_schema_org_model
    from schorg.LimitedByGuaranteeCharity import LimitedByGuaranteeCharity

    a = create_schema_org_model(type_=LimitedByGuaranteeCharityInheritedProperties)
    b = create_schema_org_model(type_=LimitedByGuaranteeCharityProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    LimitedByGuaranteeCharity.schema()


def ComputerLanguage_test():
    from schorg.ComputerLanguage import ComputerLanguageInheritedProperties
    from schorg.ComputerLanguage import ComputerLanguageProperties
    from schorg.ComputerLanguage import AllProperties
    from schorg.ComputerLanguage import create_schema_org_model
    from schorg.ComputerLanguage import ComputerLanguage

    a = create_schema_org_model(type_=ComputerLanguageInheritedProperties)
    b = create_schema_org_model(type_=ComputerLanguageProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ComputerLanguage.schema()


def WearableMeasurementCup_test():
    from schorg.WearableMeasurementCup import WearableMeasurementCupInheritedProperties
    from schorg.WearableMeasurementCup import WearableMeasurementCupProperties
    from schorg.WearableMeasurementCup import AllProperties
    from schorg.WearableMeasurementCup import create_schema_org_model
    from schorg.WearableMeasurementCup import WearableMeasurementCup

    a = create_schema_org_model(type_=WearableMeasurementCupInheritedProperties)
    b = create_schema_org_model(type_=WearableMeasurementCupProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    WearableMeasurementCup.schema()


def ReportedDoseSchedule_test():
    from schorg.ReportedDoseSchedule import ReportedDoseScheduleInheritedProperties
    from schorg.ReportedDoseSchedule import ReportedDoseScheduleProperties
    from schorg.ReportedDoseSchedule import AllProperties
    from schorg.ReportedDoseSchedule import create_schema_org_model
    from schorg.ReportedDoseSchedule import ReportedDoseSchedule

    a = create_schema_org_model(type_=ReportedDoseScheduleInheritedProperties)
    b = create_schema_org_model(type_=ReportedDoseScheduleProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ReportedDoseSchedule.schema()


def Vehicle_test():
    from schorg.Vehicle import VehicleInheritedProperties
    from schorg.Vehicle import VehicleProperties
    from schorg.Vehicle import AllProperties
    from schorg.Vehicle import create_schema_org_model
    from schorg.Vehicle import Vehicle

    a = create_schema_org_model(type_=VehicleInheritedProperties)
    b = create_schema_org_model(type_=VehicleProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Vehicle.schema()


def Motorcycle_test():
    from schorg.Motorcycle import MotorcycleInheritedProperties
    from schorg.Motorcycle import MotorcycleProperties
    from schorg.Motorcycle import AllProperties
    from schorg.Motorcycle import create_schema_org_model
    from schorg.Motorcycle import Motorcycle

    a = create_schema_org_model(type_=MotorcycleInheritedProperties)
    b = create_schema_org_model(type_=MotorcycleProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Motorcycle.schema()


def Nonprofit501c21_test():
    from schorg.Nonprofit501c21 import Nonprofit501c21InheritedProperties
    from schorg.Nonprofit501c21 import Nonprofit501c21Properties
    from schorg.Nonprofit501c21 import AllProperties
    from schorg.Nonprofit501c21 import create_schema_org_model
    from schorg.Nonprofit501c21 import Nonprofit501c21

    a = create_schema_org_model(type_=Nonprofit501c21InheritedProperties)
    b = create_schema_org_model(type_=Nonprofit501c21Properties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Nonprofit501c21.schema()


def FollowAction_test():
    from schorg.FollowAction import FollowActionInheritedProperties
    from schorg.FollowAction import FollowActionProperties
    from schorg.FollowAction import AllProperties
    from schorg.FollowAction import create_schema_org_model
    from schorg.FollowAction import FollowAction

    a = create_schema_org_model(type_=FollowActionInheritedProperties)
    b = create_schema_org_model(type_=FollowActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    FollowAction.schema()


def Game_test():
    from schorg.Game import GameInheritedProperties
    from schorg.Game import GameProperties
    from schorg.Game import AllProperties
    from schorg.Game import create_schema_org_model
    from schorg.Game import Game

    a = create_schema_org_model(type_=GameInheritedProperties)
    b = create_schema_org_model(type_=GameProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Game.schema()


def VideoGame_test():
    from schorg.VideoGame import VideoGameInheritedProperties
    from schorg.VideoGame import VideoGameProperties
    from schorg.VideoGame import AllProperties
    from schorg.VideoGame import create_schema_org_model
    from schorg.VideoGame import VideoGame

    a = create_schema_org_model(type_=VideoGameInheritedProperties)
    b = create_schema_org_model(type_=VideoGameProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    VideoGame.schema()


def OpinionNewsArticle_test():
    from schorg.OpinionNewsArticle import OpinionNewsArticleInheritedProperties
    from schorg.OpinionNewsArticle import OpinionNewsArticleProperties
    from schorg.OpinionNewsArticle import AllProperties
    from schorg.OpinionNewsArticle import create_schema_org_model
    from schorg.OpinionNewsArticle import OpinionNewsArticle

    a = create_schema_org_model(type_=OpinionNewsArticleInheritedProperties)
    b = create_schema_org_model(type_=OpinionNewsArticleProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    OpinionNewsArticle.schema()


def MapCategoryType_test():
    from schorg.MapCategoryType import MapCategoryTypeInheritedProperties
    from schorg.MapCategoryType import MapCategoryTypeProperties
    from schorg.MapCategoryType import AllProperties
    from schorg.MapCategoryType import create_schema_org_model
    from schorg.MapCategoryType import MapCategoryType

    a = create_schema_org_model(type_=MapCategoryTypeInheritedProperties)
    b = create_schema_org_model(type_=MapCategoryTypeProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MapCategoryType.schema()


def NGO_test():
    from schorg.NGO import NGOInheritedProperties
    from schorg.NGO import NGOProperties
    from schorg.NGO import AllProperties
    from schorg.NGO import create_schema_org_model
    from schorg.NGO import NGO

    a = create_schema_org_model(type_=NGOInheritedProperties)
    b = create_schema_org_model(type_=NGOProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    NGO.schema()


def BusStation_test():
    from schorg.BusStation import BusStationInheritedProperties
    from schorg.BusStation import BusStationProperties
    from schorg.BusStation import AllProperties
    from schorg.BusStation import create_schema_org_model
    from schorg.BusStation import BusStation

    a = create_schema_org_model(type_=BusStationInheritedProperties)
    b = create_schema_org_model(type_=BusStationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    BusStation.schema()


def TrainStation_test():
    from schorg.TrainStation import TrainStationInheritedProperties
    from schorg.TrainStation import TrainStationProperties
    from schorg.TrainStation import AllProperties
    from schorg.TrainStation import create_schema_org_model
    from schorg.TrainStation import TrainStation

    a = create_schema_org_model(type_=TrainStationInheritedProperties)
    b = create_schema_org_model(type_=TrainStationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    TrainStation.schema()


def SportingGoodsStore_test():
    from schorg.SportingGoodsStore import SportingGoodsStoreInheritedProperties
    from schorg.SportingGoodsStore import SportingGoodsStoreProperties
    from schorg.SportingGoodsStore import AllProperties
    from schorg.SportingGoodsStore import create_schema_org_model
    from schorg.SportingGoodsStore import SportingGoodsStore

    a = create_schema_org_model(type_=SportingGoodsStoreInheritedProperties)
    b = create_schema_org_model(type_=SportingGoodsStoreProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    SportingGoodsStore.schema()


def UnRegisterAction_test():
    from schorg.UnRegisterAction import UnRegisterActionInheritedProperties
    from schorg.UnRegisterAction import UnRegisterActionProperties
    from schorg.UnRegisterAction import AllProperties
    from schorg.UnRegisterAction import create_schema_org_model
    from schorg.UnRegisterAction import UnRegisterAction

    a = create_schema_org_model(type_=UnRegisterActionInheritedProperties)
    b = create_schema_org_model(type_=UnRegisterActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    UnRegisterAction.schema()


def DoubleBlindedTrial_test():
    from schorg.DoubleBlindedTrial import DoubleBlindedTrialInheritedProperties
    from schorg.DoubleBlindedTrial import DoubleBlindedTrialProperties
    from schorg.DoubleBlindedTrial import AllProperties
    from schorg.DoubleBlindedTrial import create_schema_org_model
    from schorg.DoubleBlindedTrial import DoubleBlindedTrial

    a = create_schema_org_model(type_=DoubleBlindedTrialInheritedProperties)
    b = create_schema_org_model(type_=DoubleBlindedTrialProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    DoubleBlindedTrial.schema()


def ToyStore_test():
    from schorg.ToyStore import ToyStoreInheritedProperties
    from schorg.ToyStore import ToyStoreProperties
    from schorg.ToyStore import AllProperties
    from schorg.ToyStore import create_schema_org_model
    from schorg.ToyStore import ToyStore

    a = create_schema_org_model(type_=ToyStoreInheritedProperties)
    b = create_schema_org_model(type_=ToyStoreProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ToyStore.schema()


def UnemploymentSupport_test():
    from schorg.UnemploymentSupport import UnemploymentSupportInheritedProperties
    from schorg.UnemploymentSupport import UnemploymentSupportProperties
    from schorg.UnemploymentSupport import AllProperties
    from schorg.UnemploymentSupport import create_schema_org_model
    from schorg.UnemploymentSupport import UnemploymentSupport

    a = create_schema_org_model(type_=UnemploymentSupportInheritedProperties)
    b = create_schema_org_model(type_=UnemploymentSupportProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    UnemploymentSupport.schema()


def MedicalSign_test():
    from schorg.MedicalSign import MedicalSignInheritedProperties
    from schorg.MedicalSign import MedicalSignProperties
    from schorg.MedicalSign import AllProperties
    from schorg.MedicalSign import create_schema_org_model
    from schorg.MedicalSign import MedicalSign

    a = create_schema_org_model(type_=MedicalSignInheritedProperties)
    b = create_schema_org_model(type_=MedicalSignProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MedicalSign.schema()


def MovieSeries_test():
    from schorg.MovieSeries import MovieSeriesInheritedProperties
    from schorg.MovieSeries import MovieSeriesProperties
    from schorg.MovieSeries import AllProperties
    from schorg.MovieSeries import create_schema_org_model
    from schorg.MovieSeries import MovieSeries

    a = create_schema_org_model(type_=MovieSeriesInheritedProperties)
    b = create_schema_org_model(type_=MovieSeriesProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MovieSeries.schema()


def Car_test():
    from schorg.Car import CarInheritedProperties
    from schorg.Car import CarProperties
    from schorg.Car import AllProperties
    from schorg.Car import create_schema_org_model
    from schorg.Car import Car

    a = create_schema_org_model(type_=CarInheritedProperties)
    b = create_schema_org_model(type_=CarProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Car.schema()


def SoldOut_test():
    from schorg.SoldOut import SoldOutInheritedProperties
    from schorg.SoldOut import SoldOutProperties
    from schorg.SoldOut import AllProperties
    from schorg.SoldOut import create_schema_org_model
    from schorg.SoldOut import SoldOut

    a = create_schema_org_model(type_=SoldOutInheritedProperties)
    b = create_schema_org_model(type_=SoldOutProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    SoldOut.schema()


def Physiotherapy_test():
    from schorg.Physiotherapy import PhysiotherapyInheritedProperties
    from schorg.Physiotherapy import PhysiotherapyProperties
    from schorg.Physiotherapy import AllProperties
    from schorg.Physiotherapy import create_schema_org_model
    from schorg.Physiotherapy import Physiotherapy

    a = create_schema_org_model(type_=PhysiotherapyInheritedProperties)
    b = create_schema_org_model(type_=PhysiotherapyProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Physiotherapy.schema()


def Pond_test():
    from schorg.Pond import PondInheritedProperties
    from schorg.Pond import PondProperties
    from schorg.Pond import AllProperties
    from schorg.Pond import create_schema_org_model
    from schorg.Pond import Pond

    a = create_schema_org_model(type_=PondInheritedProperties)
    b = create_schema_org_model(type_=PondProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Pond.schema()


def PropertyValueSpecification_test():
    from schorg.PropertyValueSpecification import PropertyValueSpecificationInheritedProperties
    from schorg.PropertyValueSpecification import PropertyValueSpecificationProperties
    from schorg.PropertyValueSpecification import AllProperties
    from schorg.PropertyValueSpecification import create_schema_org_model
    from schorg.PropertyValueSpecification import PropertyValueSpecification

    a = create_schema_org_model(type_=PropertyValueSpecificationInheritedProperties)
    b = create_schema_org_model(type_=PropertyValueSpecificationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    PropertyValueSpecification.schema()


def BorrowAction_test():
    from schorg.BorrowAction import BorrowActionInheritedProperties
    from schorg.BorrowAction import BorrowActionProperties
    from schorg.BorrowAction import AllProperties
    from schorg.BorrowAction import create_schema_org_model
    from schorg.BorrowAction import BorrowAction

    a = create_schema_org_model(type_=BorrowActionInheritedProperties)
    b = create_schema_org_model(type_=BorrowActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    BorrowAction.schema()


def HinduDiet_test():
    from schorg.HinduDiet import HinduDietInheritedProperties
    from schorg.HinduDiet import HinduDietProperties
    from schorg.HinduDiet import AllProperties
    from schorg.HinduDiet import create_schema_org_model
    from schorg.HinduDiet import HinduDiet

    a = create_schema_org_model(type_=HinduDietInheritedProperties)
    b = create_schema_org_model(type_=HinduDietProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    HinduDiet.schema()


def Hematologic_test():
    from schorg.Hematologic import HematologicInheritedProperties
    from schorg.Hematologic import HematologicProperties
    from schorg.Hematologic import AllProperties
    from schorg.Hematologic import create_schema_org_model
    from schorg.Hematologic import Hematologic

    a = create_schema_org_model(type_=HematologicInheritedProperties)
    b = create_schema_org_model(type_=HematologicProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Hematologic.schema()


def LowSaltDiet_test():
    from schorg.LowSaltDiet import LowSaltDietInheritedProperties
    from schorg.LowSaltDiet import LowSaltDietProperties
    from schorg.LowSaltDiet import AllProperties
    from schorg.LowSaltDiet import create_schema_org_model
    from schorg.LowSaltDiet import LowSaltDiet

    a = create_schema_org_model(type_=LowSaltDietInheritedProperties)
    b = create_schema_org_model(type_=LowSaltDietProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    LowSaltDiet.schema()


def XPathType_test():
    from schorg.XPathType import XPathTypeInheritedProperties
    from schorg.XPathType import XPathTypeProperties
    from schorg.XPathType import AllProperties
    from schorg.XPathType import create_schema_org_model
    from schorg.XPathType import XPathType

    a = create_schema_org_model(type_=XPathTypeInheritedProperties)
    b = create_schema_org_model(type_=XPathTypeProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    XPathType.schema()


def SingleBlindedTrial_test():
    from schorg.SingleBlindedTrial import SingleBlindedTrialInheritedProperties
    from schorg.SingleBlindedTrial import SingleBlindedTrialProperties
    from schorg.SingleBlindedTrial import AllProperties
    from schorg.SingleBlindedTrial import create_schema_org_model
    from schorg.SingleBlindedTrial import SingleBlindedTrial

    a = create_schema_org_model(type_=SingleBlindedTrialInheritedProperties)
    b = create_schema_org_model(type_=SingleBlindedTrialProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    SingleBlindedTrial.schema()


def SingleRelease_test():
    from schorg.SingleRelease import SingleReleaseInheritedProperties
    from schorg.SingleRelease import SingleReleaseProperties
    from schorg.SingleRelease import AllProperties
    from schorg.SingleRelease import create_schema_org_model
    from schorg.SingleRelease import SingleRelease

    a = create_schema_org_model(type_=SingleReleaseInheritedProperties)
    b = create_schema_org_model(type_=SingleReleaseProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    SingleRelease.schema()


def WearableSizeSystemAU_test():
    from schorg.WearableSizeSystemAU import WearableSizeSystemAUInheritedProperties
    from schorg.WearableSizeSystemAU import WearableSizeSystemAUProperties
    from schorg.WearableSizeSystemAU import AllProperties
    from schorg.WearableSizeSystemAU import create_schema_org_model
    from schorg.WearableSizeSystemAU import WearableSizeSystemAU

    a = create_schema_org_model(type_=WearableSizeSystemAUInheritedProperties)
    b = create_schema_org_model(type_=WearableSizeSystemAUProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    WearableSizeSystemAU.schema()


def UKTrust_test():
    from schorg.UKTrust import UKTrustInheritedProperties
    from schorg.UKTrust import UKTrustProperties
    from schorg.UKTrust import AllProperties
    from schorg.UKTrust import create_schema_org_model
    from schorg.UKTrust import UKTrust

    a = create_schema_org_model(type_=UKTrustInheritedProperties)
    b = create_schema_org_model(type_=UKTrustProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    UKTrust.schema()


def PaidLeave_test():
    from schorg.PaidLeave import PaidLeaveInheritedProperties
    from schorg.PaidLeave import PaidLeaveProperties
    from schorg.PaidLeave import AllProperties
    from schorg.PaidLeave import create_schema_org_model
    from schorg.PaidLeave import PaidLeave

    a = create_schema_org_model(type_=PaidLeaveInheritedProperties)
    b = create_schema_org_model(type_=PaidLeaveProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    PaidLeave.schema()


def EditedOrCroppedContent_test():
    from schorg.EditedOrCroppedContent import EditedOrCroppedContentInheritedProperties
    from schorg.EditedOrCroppedContent import EditedOrCroppedContentProperties
    from schorg.EditedOrCroppedContent import AllProperties
    from schorg.EditedOrCroppedContent import create_schema_org_model
    from schorg.EditedOrCroppedContent import EditedOrCroppedContent

    a = create_schema_org_model(type_=EditedOrCroppedContentInheritedProperties)
    b = create_schema_org_model(type_=EditedOrCroppedContentProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    EditedOrCroppedContent.schema()


def Nonprofit501c12_test():
    from schorg.Nonprofit501c12 import Nonprofit501c12InheritedProperties
    from schorg.Nonprofit501c12 import Nonprofit501c12Properties
    from schorg.Nonprofit501c12 import AllProperties
    from schorg.Nonprofit501c12 import create_schema_org_model
    from schorg.Nonprofit501c12 import Nonprofit501c12

    a = create_schema_org_model(type_=Nonprofit501c12InheritedProperties)
    b = create_schema_org_model(type_=Nonprofit501c12Properties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Nonprofit501c12.schema()


def VitalSign_test():
    from schorg.VitalSign import VitalSignInheritedProperties
    from schorg.VitalSign import VitalSignProperties
    from schorg.VitalSign import AllProperties
    from schorg.VitalSign import create_schema_org_model
    from schorg.VitalSign import VitalSign

    a = create_schema_org_model(type_=VitalSignInheritedProperties)
    b = create_schema_org_model(type_=VitalSignProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    VitalSign.schema()


def WearableSizeSystemMX_test():
    from schorg.WearableSizeSystemMX import WearableSizeSystemMXInheritedProperties
    from schorg.WearableSizeSystemMX import WearableSizeSystemMXProperties
    from schorg.WearableSizeSystemMX import AllProperties
    from schorg.WearableSizeSystemMX import create_schema_org_model
    from schorg.WearableSizeSystemMX import WearableSizeSystemMX

    a = create_schema_org_model(type_=WearableSizeSystemMXInheritedProperties)
    b = create_schema_org_model(type_=WearableSizeSystemMXProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    WearableSizeSystemMX.schema()


def GardenStore_test():
    from schorg.GardenStore import GardenStoreInheritedProperties
    from schorg.GardenStore import GardenStoreProperties
    from schorg.GardenStore import AllProperties
    from schorg.GardenStore import create_schema_org_model
    from schorg.GardenStore import GardenStore

    a = create_schema_org_model(type_=GardenStoreInheritedProperties)
    b = create_schema_org_model(type_=GardenStoreProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    GardenStore.schema()


def SearchRescueOrganization_test():
    from schorg.SearchRescueOrganization import SearchRescueOrganizationInheritedProperties
    from schorg.SearchRescueOrganization import SearchRescueOrganizationProperties
    from schorg.SearchRescueOrganization import AllProperties
    from schorg.SearchRescueOrganization import create_schema_org_model
    from schorg.SearchRescueOrganization import SearchRescueOrganization

    a = create_schema_org_model(type_=SearchRescueOrganizationInheritedProperties)
    b = create_schema_org_model(type_=SearchRescueOrganizationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    SearchRescueOrganization.schema()


def BrainStructure_test():
    from schorg.BrainStructure import BrainStructureInheritedProperties
    from schorg.BrainStructure import BrainStructureProperties
    from schorg.BrainStructure import AllProperties
    from schorg.BrainStructure import create_schema_org_model
    from schorg.BrainStructure import BrainStructure

    a = create_schema_org_model(type_=BrainStructureInheritedProperties)
    b = create_schema_org_model(type_=BrainStructureProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    BrainStructure.schema()


def TreatmentsHealthAspect_test():
    from schorg.TreatmentsHealthAspect import TreatmentsHealthAspectInheritedProperties
    from schorg.TreatmentsHealthAspect import TreatmentsHealthAspectProperties
    from schorg.TreatmentsHealthAspect import AllProperties
    from schorg.TreatmentsHealthAspect import create_schema_org_model
    from schorg.TreatmentsHealthAspect import TreatmentsHealthAspect

    a = create_schema_org_model(type_=TreatmentsHealthAspectInheritedProperties)
    b = create_schema_org_model(type_=TreatmentsHealthAspectProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    TreatmentsHealthAspect.schema()


def HowTo_test():
    from schorg.HowTo import HowToInheritedProperties
    from schorg.HowTo import HowToProperties
    from schorg.HowTo import AllProperties
    from schorg.HowTo import create_schema_org_model
    from schorg.HowTo import HowTo

    a = create_schema_org_model(type_=HowToInheritedProperties)
    b = create_schema_org_model(type_=HowToProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    HowTo.schema()


def Recipe_test():
    from schorg.Recipe import RecipeInheritedProperties
    from schorg.Recipe import RecipeProperties
    from schorg.Recipe import AllProperties
    from schorg.Recipe import create_schema_org_model
    from schorg.Recipe import Recipe

    a = create_schema_org_model(type_=RecipeInheritedProperties)
    b = create_schema_org_model(type_=RecipeProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Recipe.schema()


def WearableSizeGroupMaternity_test():
    from schorg.WearableSizeGroupMaternity import WearableSizeGroupMaternityInheritedProperties
    from schorg.WearableSizeGroupMaternity import WearableSizeGroupMaternityProperties
    from schorg.WearableSizeGroupMaternity import AllProperties
    from schorg.WearableSizeGroupMaternity import create_schema_org_model
    from schorg.WearableSizeGroupMaternity import WearableSizeGroupMaternity

    a = create_schema_org_model(type_=WearableSizeGroupMaternityInheritedProperties)
    b = create_schema_org_model(type_=WearableSizeGroupMaternityProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    WearableSizeGroupMaternity.schema()


def ReplaceAction_test():
    from schorg.ReplaceAction import ReplaceActionInheritedProperties
    from schorg.ReplaceAction import ReplaceActionProperties
    from schorg.ReplaceAction import AllProperties
    from schorg.ReplaceAction import create_schema_org_model
    from schorg.ReplaceAction import ReplaceAction

    a = create_schema_org_model(type_=ReplaceActionInheritedProperties)
    b = create_schema_org_model(type_=ReplaceActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ReplaceAction.schema()


def Code_test():
    from schorg.Code import CodeInheritedProperties
    from schorg.Code import CodeProperties
    from schorg.Code import AllProperties
    from schorg.Code import create_schema_org_model
    from schorg.Code import Code

    a = create_schema_org_model(type_=CodeInheritedProperties)
    b = create_schema_org_model(type_=CodeProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Code.schema()


def Nonprofit501c16_test():
    from schorg.Nonprofit501c16 import Nonprofit501c16InheritedProperties
    from schorg.Nonprofit501c16 import Nonprofit501c16Properties
    from schorg.Nonprofit501c16 import AllProperties
    from schorg.Nonprofit501c16 import create_schema_org_model
    from schorg.Nonprofit501c16 import Nonprofit501c16

    a = create_schema_org_model(type_=Nonprofit501c16InheritedProperties)
    b = create_schema_org_model(type_=Nonprofit501c16Properties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Nonprofit501c16.schema()


def SizeSystemMetric_test():
    from schorg.SizeSystemMetric import SizeSystemMetricInheritedProperties
    from schorg.SizeSystemMetric import SizeSystemMetricProperties
    from schorg.SizeSystemMetric import AllProperties
    from schorg.SizeSystemMetric import create_schema_org_model
    from schorg.SizeSystemMetric import SizeSystemMetric

    a = create_schema_org_model(type_=SizeSystemMetricInheritedProperties)
    b = create_schema_org_model(type_=SizeSystemMetricProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    SizeSystemMetric.schema()


def ChildCare_test():
    from schorg.ChildCare import ChildCareInheritedProperties
    from schorg.ChildCare import ChildCareProperties
    from schorg.ChildCare import AllProperties
    from schorg.ChildCare import create_schema_org_model
    from schorg.ChildCare import ChildCare

    a = create_schema_org_model(type_=ChildCareInheritedProperties)
    b = create_schema_org_model(type_=ChildCareProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ChildCare.schema()


def PropertyValue_test():
    from schorg.PropertyValue import PropertyValueInheritedProperties
    from schorg.PropertyValue import PropertyValueProperties
    from schorg.PropertyValue import AllProperties
    from schorg.PropertyValue import create_schema_org_model
    from schorg.PropertyValue import PropertyValue

    a = create_schema_org_model(type_=PropertyValueInheritedProperties)
    b = create_schema_org_model(type_=PropertyValueProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    PropertyValue.schema()


def LocationFeatureSpecification_test():
    from schorg.LocationFeatureSpecification import LocationFeatureSpecificationInheritedProperties
    from schorg.LocationFeatureSpecification import LocationFeatureSpecificationProperties
    from schorg.LocationFeatureSpecification import AllProperties
    from schorg.LocationFeatureSpecification import create_schema_org_model
    from schorg.LocationFeatureSpecification import LocationFeatureSpecification

    a = create_schema_org_model(type_=LocationFeatureSpecificationInheritedProperties)
    b = create_schema_org_model(type_=LocationFeatureSpecificationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    LocationFeatureSpecification.schema()


def RemixAlbum_test():
    from schorg.RemixAlbum import RemixAlbumInheritedProperties
    from schorg.RemixAlbum import RemixAlbumProperties
    from schorg.RemixAlbum import AllProperties
    from schorg.RemixAlbum import create_schema_org_model
    from schorg.RemixAlbum import RemixAlbum

    a = create_schema_org_model(type_=RemixAlbumInheritedProperties)
    b = create_schema_org_model(type_=RemixAlbumProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    RemixAlbum.schema()


def Date_test():
    from schorg.Date import DateInheritedProperties
    from schorg.Date import DateProperties
    from schorg.Date import AllProperties
    from schorg.Date import create_schema_org_model
    from schorg.Date import Date

    a = create_schema_org_model(type_=DateInheritedProperties)
    b = create_schema_org_model(type_=DateProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Date.schema()


def DrugPrescriptionStatus_test():
    from schorg.DrugPrescriptionStatus import DrugPrescriptionStatusInheritedProperties
    from schorg.DrugPrescriptionStatus import DrugPrescriptionStatusProperties
    from schorg.DrugPrescriptionStatus import AllProperties
    from schorg.DrugPrescriptionStatus import create_schema_org_model
    from schorg.DrugPrescriptionStatus import DrugPrescriptionStatus

    a = create_schema_org_model(type_=DrugPrescriptionStatusInheritedProperties)
    b = create_schema_org_model(type_=DrugPrescriptionStatusProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    DrugPrescriptionStatus.schema()


def OTC_test():
    from schorg.OTC import OTCInheritedProperties
    from schorg.OTC import OTCProperties
    from schorg.OTC import AllProperties
    from schorg.OTC import create_schema_org_model
    from schorg.OTC import OTC

    a = create_schema_org_model(type_=OTCInheritedProperties)
    b = create_schema_org_model(type_=OTCProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    OTC.schema()


def Taxon_test():
    from schorg.Taxon import TaxonInheritedProperties
    from schorg.Taxon import TaxonProperties
    from schorg.Taxon import AllProperties
    from schorg.Taxon import create_schema_org_model
    from schorg.Taxon import Taxon

    a = create_schema_org_model(type_=TaxonInheritedProperties)
    b = create_schema_org_model(type_=TaxonProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Taxon.schema()


def AccountingService_test():
    from schorg.AccountingService import AccountingServiceInheritedProperties
    from schorg.AccountingService import AccountingServiceProperties
    from schorg.AccountingService import AllProperties
    from schorg.AccountingService import create_schema_org_model
    from schorg.AccountingService import AccountingService

    a = create_schema_org_model(type_=AccountingServiceInheritedProperties)
    b = create_schema_org_model(type_=AccountingServiceProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    AccountingService.schema()


def EventScheduled_test():
    from schorg.EventScheduled import EventScheduledInheritedProperties
    from schorg.EventScheduled import EventScheduledProperties
    from schorg.EventScheduled import AllProperties
    from schorg.EventScheduled import create_schema_org_model
    from schorg.EventScheduled import EventScheduled

    a = create_schema_org_model(type_=EventScheduledInheritedProperties)
    b = create_schema_org_model(type_=EventScheduledProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    EventScheduled.schema()


def WearableMeasurementSleeve_test():
    from schorg.WearableMeasurementSleeve import WearableMeasurementSleeveInheritedProperties
    from schorg.WearableMeasurementSleeve import WearableMeasurementSleeveProperties
    from schorg.WearableMeasurementSleeve import AllProperties
    from schorg.WearableMeasurementSleeve import create_schema_org_model
    from schorg.WearableMeasurementSleeve import WearableMeasurementSleeve

    a = create_schema_org_model(type_=WearableMeasurementSleeveInheritedProperties)
    b = create_schema_org_model(type_=WearableMeasurementSleeveProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    WearableMeasurementSleeve.schema()


def ListPrice_test():
    from schorg.ListPrice import ListPriceInheritedProperties
    from schorg.ListPrice import ListPriceProperties
    from schorg.ListPrice import AllProperties
    from schorg.ListPrice import create_schema_org_model
    from schorg.ListPrice import ListPrice

    a = create_schema_org_model(type_=ListPriceInheritedProperties)
    b = create_schema_org_model(type_=ListPriceProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ListPrice.schema()


def WebApplication_test():
    from schorg.WebApplication import WebApplicationInheritedProperties
    from schorg.WebApplication import WebApplicationProperties
    from schorg.WebApplication import AllProperties
    from schorg.WebApplication import create_schema_org_model
    from schorg.WebApplication import WebApplication

    a = create_schema_org_model(type_=WebApplicationInheritedProperties)
    b = create_schema_org_model(type_=WebApplicationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    WebApplication.schema()


def Suspended_test():
    from schorg.Suspended import SuspendedInheritedProperties
    from schorg.Suspended import SuspendedProperties
    from schorg.Suspended import AllProperties
    from schorg.Suspended import create_schema_org_model
    from schorg.Suspended import Suspended

    a = create_schema_org_model(type_=SuspendedInheritedProperties)
    b = create_schema_org_model(type_=SuspendedProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Suspended.schema()


def Subscription_test():
    from schorg.Subscription import SubscriptionInheritedProperties
    from schorg.Subscription import SubscriptionProperties
    from schorg.Subscription import AllProperties
    from schorg.Subscription import create_schema_org_model
    from schorg.Subscription import Subscription

    a = create_schema_org_model(type_=SubscriptionInheritedProperties)
    b = create_schema_org_model(type_=SubscriptionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Subscription.schema()


def FreeReturn_test():
    from schorg.FreeReturn import FreeReturnInheritedProperties
    from schorg.FreeReturn import FreeReturnProperties
    from schorg.FreeReturn import AllProperties
    from schorg.FreeReturn import create_schema_org_model
    from schorg.FreeReturn import FreeReturn

    a = create_schema_org_model(type_=FreeReturnInheritedProperties)
    b = create_schema_org_model(type_=FreeReturnProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    FreeReturn.schema()


def HowToItem_test():
    from schorg.HowToItem import HowToItemInheritedProperties
    from schorg.HowToItem import HowToItemProperties
    from schorg.HowToItem import AllProperties
    from schorg.HowToItem import create_schema_org_model
    from schorg.HowToItem import HowToItem

    a = create_schema_org_model(type_=HowToItemInheritedProperties)
    b = create_schema_org_model(type_=HowToItemProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    HowToItem.schema()


def HowToTool_test():
    from schorg.HowToTool import HowToToolInheritedProperties
    from schorg.HowToTool import HowToToolProperties
    from schorg.HowToTool import AllProperties
    from schorg.HowToTool import create_schema_org_model
    from schorg.HowToTool import HowToTool

    a = create_schema_org_model(type_=HowToToolInheritedProperties)
    b = create_schema_org_model(type_=HowToToolProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    HowToTool.schema()


def InvestmentFund_test():
    from schorg.InvestmentFund import InvestmentFundInheritedProperties
    from schorg.InvestmentFund import InvestmentFundProperties
    from schorg.InvestmentFund import AllProperties
    from schorg.InvestmentFund import create_schema_org_model
    from schorg.InvestmentFund import InvestmentFund

    a = create_schema_org_model(type_=InvestmentFundInheritedProperties)
    b = create_schema_org_model(type_=InvestmentFundProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    InvestmentFund.schema()


def FailedActionStatus_test():
    from schorg.FailedActionStatus import FailedActionStatusInheritedProperties
    from schorg.FailedActionStatus import FailedActionStatusProperties
    from schorg.FailedActionStatus import AllProperties
    from schorg.FailedActionStatus import create_schema_org_model
    from schorg.FailedActionStatus import FailedActionStatus

    a = create_schema_org_model(type_=FailedActionStatusInheritedProperties)
    b = create_schema_org_model(type_=FailedActionStatusProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    FailedActionStatus.schema()


def RealEstateAgent_test():
    from schorg.RealEstateAgent import RealEstateAgentInheritedProperties
    from schorg.RealEstateAgent import RealEstateAgentProperties
    from schorg.RealEstateAgent import AllProperties
    from schorg.RealEstateAgent import create_schema_org_model
    from schorg.RealEstateAgent import RealEstateAgent

    a = create_schema_org_model(type_=RealEstateAgentInheritedProperties)
    b = create_schema_org_model(type_=RealEstateAgentProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    RealEstateAgent.schema()


def AdvertiserContentArticle_test():
    from schorg.AdvertiserContentArticle import AdvertiserContentArticleInheritedProperties
    from schorg.AdvertiserContentArticle import AdvertiserContentArticleProperties
    from schorg.AdvertiserContentArticle import AllProperties
    from schorg.AdvertiserContentArticle import create_schema_org_model
    from schorg.AdvertiserContentArticle import AdvertiserContentArticle

    a = create_schema_org_model(type_=AdvertiserContentArticleInheritedProperties)
    b = create_schema_org_model(type_=AdvertiserContentArticleProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    AdvertiserContentArticle.schema()


def Drawing_test():
    from schorg.Drawing import DrawingInheritedProperties
    from schorg.Drawing import DrawingProperties
    from schorg.Drawing import AllProperties
    from schorg.Drawing import create_schema_org_model
    from schorg.Drawing import Drawing

    a = create_schema_org_model(type_=DrawingInheritedProperties)
    b = create_schema_org_model(type_=DrawingProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Drawing.schema()


def RegisterAction_test():
    from schorg.RegisterAction import RegisterActionInheritedProperties
    from schorg.RegisterAction import RegisterActionProperties
    from schorg.RegisterAction import AllProperties
    from schorg.RegisterAction import create_schema_org_model
    from schorg.RegisterAction import RegisterAction

    a = create_schema_org_model(type_=RegisterActionInheritedProperties)
    b = create_schema_org_model(type_=RegisterActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    RegisterAction.schema()


def CommunityHealth_test():
    from schorg.CommunityHealth import CommunityHealthInheritedProperties
    from schorg.CommunityHealth import CommunityHealthProperties
    from schorg.CommunityHealth import AllProperties
    from schorg.CommunityHealth import create_schema_org_model
    from schorg.CommunityHealth import CommunityHealth

    a = create_schema_org_model(type_=CommunityHealthInheritedProperties)
    b = create_schema_org_model(type_=CommunityHealthProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    CommunityHealth.schema()


def LoanOrCredit_test():
    from schorg.LoanOrCredit import LoanOrCreditInheritedProperties
    from schorg.LoanOrCredit import LoanOrCreditProperties
    from schorg.LoanOrCredit import AllProperties
    from schorg.LoanOrCredit import create_schema_org_model
    from schorg.LoanOrCredit import LoanOrCredit

    a = create_schema_org_model(type_=LoanOrCreditInheritedProperties)
    b = create_schema_org_model(type_=LoanOrCreditProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    LoanOrCredit.schema()


def MortgageLoan_test():
    from schorg.MortgageLoan import MortgageLoanInheritedProperties
    from schorg.MortgageLoan import MortgageLoanProperties
    from schorg.MortgageLoan import AllProperties
    from schorg.MortgageLoan import create_schema_org_model
    from schorg.MortgageLoan import MortgageLoan

    a = create_schema_org_model(type_=MortgageLoanInheritedProperties)
    b = create_schema_org_model(type_=MortgageLoanProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MortgageLoan.schema()


def Comment_test():
    from schorg.Comment import CommentInheritedProperties
    from schorg.Comment import CommentProperties
    from schorg.Comment import AllProperties
    from schorg.Comment import create_schema_org_model
    from schorg.Comment import Comment

    a = create_schema_org_model(type_=CommentInheritedProperties)
    b = create_schema_org_model(type_=CommentProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Comment.schema()


def CorrectionComment_test():
    from schorg.CorrectionComment import CorrectionCommentInheritedProperties
    from schorg.CorrectionComment import CorrectionCommentProperties
    from schorg.CorrectionComment import AllProperties
    from schorg.CorrectionComment import create_schema_org_model
    from schorg.CorrectionComment import CorrectionComment

    a = create_schema_org_model(type_=CorrectionCommentInheritedProperties)
    b = create_schema_org_model(type_=CorrectionCommentProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    CorrectionComment.schema()


def BusStop_test():
    from schorg.BusStop import BusStopInheritedProperties
    from schorg.BusStop import BusStopProperties
    from schorg.BusStop import AllProperties
    from schorg.BusStop import create_schema_org_model
    from schorg.BusStop import BusStop

    a = create_schema_org_model(type_=BusStopInheritedProperties)
    b = create_schema_org_model(type_=BusStopProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    BusStop.schema()


def OfficeEquipmentStore_test():
    from schorg.OfficeEquipmentStore import OfficeEquipmentStoreInheritedProperties
    from schorg.OfficeEquipmentStore import OfficeEquipmentStoreProperties
    from schorg.OfficeEquipmentStore import AllProperties
    from schorg.OfficeEquipmentStore import create_schema_org_model
    from schorg.OfficeEquipmentStore import OfficeEquipmentStore

    a = create_schema_org_model(type_=OfficeEquipmentStoreInheritedProperties)
    b = create_schema_org_model(type_=OfficeEquipmentStoreProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    OfficeEquipmentStore.schema()


def MisconceptionsHealthAspect_test():
    from schorg.MisconceptionsHealthAspect import MisconceptionsHealthAspectInheritedProperties
    from schorg.MisconceptionsHealthAspect import MisconceptionsHealthAspectProperties
    from schorg.MisconceptionsHealthAspect import AllProperties
    from schorg.MisconceptionsHealthAspect import create_schema_org_model
    from schorg.MisconceptionsHealthAspect import MisconceptionsHealthAspect

    a = create_schema_org_model(type_=MisconceptionsHealthAspectInheritedProperties)
    b = create_schema_org_model(type_=MisconceptionsHealthAspectProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MisconceptionsHealthAspect.schema()


def WearableMeasurementHeight_test():
    from schorg.WearableMeasurementHeight import WearableMeasurementHeightInheritedProperties
    from schorg.WearableMeasurementHeight import WearableMeasurementHeightProperties
    from schorg.WearableMeasurementHeight import AllProperties
    from schorg.WearableMeasurementHeight import create_schema_org_model
    from schorg.WearableMeasurementHeight import WearableMeasurementHeight

    a = create_schema_org_model(type_=WearableMeasurementHeightInheritedProperties)
    b = create_schema_org_model(type_=WearableMeasurementHeightProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    WearableMeasurementHeight.schema()


def PrependAction_test():
    from schorg.PrependAction import PrependActionInheritedProperties
    from schorg.PrependAction import PrependActionProperties
    from schorg.PrependAction import AllProperties
    from schorg.PrependAction import create_schema_org_model
    from schorg.PrependAction import PrependAction

    a = create_schema_org_model(type_=PrependActionInheritedProperties)
    b = create_schema_org_model(type_=PrependActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    PrependAction.schema()


def Appearance_test():
    from schorg.Appearance import AppearanceInheritedProperties
    from schorg.Appearance import AppearanceProperties
    from schorg.Appearance import AllProperties
    from schorg.Appearance import create_schema_org_model
    from schorg.Appearance import Appearance

    a = create_schema_org_model(type_=AppearanceInheritedProperties)
    b = create_schema_org_model(type_=AppearanceProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Appearance.schema()


def Resort_test():
    from schorg.Resort import ResortInheritedProperties
    from schorg.Resort import ResortProperties
    from schorg.Resort import AllProperties
    from schorg.Resort import create_schema_org_model
    from schorg.Resort import Resort

    a = create_schema_org_model(type_=ResortInheritedProperties)
    b = create_schema_org_model(type_=ResortProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Resort.schema()


def SkiResort_test():
    from schorg.SkiResort import SkiResortInheritedProperties
    from schorg.SkiResort import SkiResortProperties
    from schorg.SkiResort import AllProperties
    from schorg.SkiResort import create_schema_org_model
    from schorg.SkiResort import SkiResort

    a = create_schema_org_model(type_=SkiResortInheritedProperties)
    b = create_schema_org_model(type_=SkiResortProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    SkiResort.schema()


def MedicalTrial_test():
    from schorg.MedicalTrial import MedicalTrialInheritedProperties
    from schorg.MedicalTrial import MedicalTrialProperties
    from schorg.MedicalTrial import AllProperties
    from schorg.MedicalTrial import create_schema_org_model
    from schorg.MedicalTrial import MedicalTrial

    a = create_schema_org_model(type_=MedicalTrialInheritedProperties)
    b = create_schema_org_model(type_=MedicalTrialProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MedicalTrial.schema()


def Nonprofit501c7_test():
    from schorg.Nonprofit501c7 import Nonprofit501c7InheritedProperties
    from schorg.Nonprofit501c7 import Nonprofit501c7Properties
    from schorg.Nonprofit501c7 import AllProperties
    from schorg.Nonprofit501c7 import create_schema_org_model
    from schorg.Nonprofit501c7 import Nonprofit501c7

    a = create_schema_org_model(type_=Nonprofit501c7InheritedProperties)
    b = create_schema_org_model(type_=Nonprofit501c7Properties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Nonprofit501c7.schema()


def DanceGroup_test():
    from schorg.DanceGroup import DanceGroupInheritedProperties
    from schorg.DanceGroup import DanceGroupProperties
    from schorg.DanceGroup import AllProperties
    from schorg.DanceGroup import create_schema_org_model
    from schorg.DanceGroup import DanceGroup

    a = create_schema_org_model(type_=DanceGroupInheritedProperties)
    b = create_schema_org_model(type_=DanceGroupProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    DanceGroup.schema()


def Photograph_test():
    from schorg.Photograph import PhotographInheritedProperties
    from schorg.Photograph import PhotographProperties
    from schorg.Photograph import AllProperties
    from schorg.Photograph import create_schema_org_model
    from schorg.Photograph import Photograph

    a = create_schema_org_model(type_=PhotographInheritedProperties)
    b = create_schema_org_model(type_=PhotographProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Photograph.schema()


def HousePainter_test():
    from schorg.HousePainter import HousePainterInheritedProperties
    from schorg.HousePainter import HousePainterProperties
    from schorg.HousePainter import AllProperties
    from schorg.HousePainter import create_schema_org_model
    from schorg.HousePainter import HousePainter

    a = create_schema_org_model(type_=HousePainterInheritedProperties)
    b = create_schema_org_model(type_=HousePainterProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    HousePainter.schema()


def OrderProblem_test():
    from schorg.OrderProblem import OrderProblemInheritedProperties
    from schorg.OrderProblem import OrderProblemProperties
    from schorg.OrderProblem import AllProperties
    from schorg.OrderProblem import create_schema_org_model
    from schorg.OrderProblem import OrderProblem

    a = create_schema_org_model(type_=OrderProblemInheritedProperties)
    b = create_schema_org_model(type_=OrderProblemProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    OrderProblem.schema()


def Nonprofit501a_test():
    from schorg.Nonprofit501a import Nonprofit501aInheritedProperties
    from schorg.Nonprofit501a import Nonprofit501aProperties
    from schorg.Nonprofit501a import AllProperties
    from schorg.Nonprofit501a import create_schema_org_model
    from schorg.Nonprofit501a import Nonprofit501a

    a = create_schema_org_model(type_=Nonprofit501aInheritedProperties)
    b = create_schema_org_model(type_=Nonprofit501aProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Nonprofit501a.schema()


def DiscussionForumPosting_test():
    from schorg.DiscussionForumPosting import DiscussionForumPostingInheritedProperties
    from schorg.DiscussionForumPosting import DiscussionForumPostingProperties
    from schorg.DiscussionForumPosting import AllProperties
    from schorg.DiscussionForumPosting import create_schema_org_model
    from schorg.DiscussionForumPosting import DiscussionForumPosting

    a = create_schema_org_model(type_=DiscussionForumPostingInheritedProperties)
    b = create_schema_org_model(type_=DiscussionForumPostingProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    DiscussionForumPosting.schema()


def CohortStudy_test():
    from schorg.CohortStudy import CohortStudyInheritedProperties
    from schorg.CohortStudy import CohortStudyProperties
    from schorg.CohortStudy import AllProperties
    from schorg.CohortStudy import create_schema_org_model
    from schorg.CohortStudy import CohortStudy

    a = create_schema_org_model(type_=CohortStudyInheritedProperties)
    b = create_schema_org_model(type_=CohortStudyProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    CohortStudy.schema()


def Wednesday_test():
    from schorg.Wednesday import WednesdayInheritedProperties
    from schorg.Wednesday import WednesdayProperties
    from schorg.Wednesday import AllProperties
    from schorg.Wednesday import create_schema_org_model
    from schorg.Wednesday import Wednesday

    a = create_schema_org_model(type_=WednesdayInheritedProperties)
    b = create_schema_org_model(type_=WednesdayProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Wednesday.schema()


def UnclassifiedAdultConsideration_test():
    from schorg.UnclassifiedAdultConsideration import UnclassifiedAdultConsiderationInheritedProperties
    from schorg.UnclassifiedAdultConsideration import UnclassifiedAdultConsiderationProperties
    from schorg.UnclassifiedAdultConsideration import AllProperties
    from schorg.UnclassifiedAdultConsideration import create_schema_org_model
    from schorg.UnclassifiedAdultConsideration import UnclassifiedAdultConsideration

    a = create_schema_org_model(type_=UnclassifiedAdultConsiderationInheritedProperties)
    b = create_schema_org_model(type_=UnclassifiedAdultConsiderationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    UnclassifiedAdultConsideration.schema()


def TransitMap_test():
    from schorg.TransitMap import TransitMapInheritedProperties
    from schorg.TransitMap import TransitMapProperties
    from schorg.TransitMap import AllProperties
    from schorg.TransitMap import create_schema_org_model
    from schorg.TransitMap import TransitMap

    a = create_schema_org_model(type_=TransitMapInheritedProperties)
    b = create_schema_org_model(type_=TransitMapProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    TransitMap.schema()


def RealEstateListing_test():
    from schorg.RealEstateListing import RealEstateListingInheritedProperties
    from schorg.RealEstateListing import RealEstateListingProperties
    from schorg.RealEstateListing import AllProperties
    from schorg.RealEstateListing import create_schema_org_model
    from schorg.RealEstateListing import RealEstateListing

    a = create_schema_org_model(type_=RealEstateListingInheritedProperties)
    b = create_schema_org_model(type_=RealEstateListingProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    RealEstateListing.schema()


def SellAction_test():
    from schorg.SellAction import SellActionInheritedProperties
    from schorg.SellAction import SellActionProperties
    from schorg.SellAction import AllProperties
    from schorg.SellAction import create_schema_org_model
    from schorg.SellAction import SellAction

    a = create_schema_org_model(type_=SellActionInheritedProperties)
    b = create_schema_org_model(type_=SellActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    SellAction.schema()


def ShareAction_test():
    from schorg.ShareAction import ShareActionInheritedProperties
    from schorg.ShareAction import ShareActionProperties
    from schorg.ShareAction import AllProperties
    from schorg.ShareAction import create_schema_org_model
    from schorg.ShareAction import ShareAction

    a = create_schema_org_model(type_=ShareActionInheritedProperties)
    b = create_schema_org_model(type_=ShareActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ShareAction.schema()


def Bakery_test():
    from schorg.Bakery import BakeryInheritedProperties
    from schorg.Bakery import BakeryProperties
    from schorg.Bakery import AllProperties
    from schorg.Bakery import create_schema_org_model
    from schorg.Bakery import Bakery

    a = create_schema_org_model(type_=BakeryInheritedProperties)
    b = create_schema_org_model(type_=BakeryProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Bakery.schema()


def WholesaleStore_test():
    from schorg.WholesaleStore import WholesaleStoreInheritedProperties
    from schorg.WholesaleStore import WholesaleStoreProperties
    from schorg.WholesaleStore import AllProperties
    from schorg.WholesaleStore import create_schema_org_model
    from schorg.WholesaleStore import WholesaleStore

    a = create_schema_org_model(type_=WholesaleStoreInheritedProperties)
    b = create_schema_org_model(type_=WholesaleStoreProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    WholesaleStore.schema()


def AllocateAction_test():
    from schorg.AllocateAction import AllocateActionInheritedProperties
    from schorg.AllocateAction import AllocateActionProperties
    from schorg.AllocateAction import AllProperties
    from schorg.AllocateAction import create_schema_org_model
    from schorg.AllocateAction import AllocateAction

    a = create_schema_org_model(type_=AllocateActionInheritedProperties)
    b = create_schema_org_model(type_=AllocateActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    AllocateAction.schema()


def RejectAction_test():
    from schorg.RejectAction import RejectActionInheritedProperties
    from schorg.RejectAction import RejectActionProperties
    from schorg.RejectAction import AllProperties
    from schorg.RejectAction import create_schema_org_model
    from schorg.RejectAction import RejectAction

    a = create_schema_org_model(type_=RejectActionInheritedProperties)
    b = create_schema_org_model(type_=RejectActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    RejectAction.schema()


def WarrantyScope_test():
    from schorg.WarrantyScope import WarrantyScopeInheritedProperties
    from schorg.WarrantyScope import WarrantyScopeProperties
    from schorg.WarrantyScope import AllProperties
    from schorg.WarrantyScope import create_schema_org_model
    from schorg.WarrantyScope import WarrantyScope

    a = create_schema_org_model(type_=WarrantyScopeInheritedProperties)
    b = create_schema_org_model(type_=WarrantyScopeProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    WarrantyScope.schema()


def SpeakableSpecification_test():
    from schorg.SpeakableSpecification import SpeakableSpecificationInheritedProperties
    from schorg.SpeakableSpecification import SpeakableSpecificationProperties
    from schorg.SpeakableSpecification import AllProperties
    from schorg.SpeakableSpecification import create_schema_org_model
    from schorg.SpeakableSpecification import SpeakableSpecification

    a = create_schema_org_model(type_=SpeakableSpecificationInheritedProperties)
    b = create_schema_org_model(type_=SpeakableSpecificationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    SpeakableSpecification.schema()


def DepartmentStore_test():
    from schorg.DepartmentStore import DepartmentStoreInheritedProperties
    from schorg.DepartmentStore import DepartmentStoreProperties
    from schorg.DepartmentStore import AllProperties
    from schorg.DepartmentStore import create_schema_org_model
    from schorg.DepartmentStore import DepartmentStore

    a = create_schema_org_model(type_=DepartmentStoreInheritedProperties)
    b = create_schema_org_model(type_=DepartmentStoreProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    DepartmentStore.schema()


def GasStation_test():
    from schorg.GasStation import GasStationInheritedProperties
    from schorg.GasStation import GasStationProperties
    from schorg.GasStation import AllProperties
    from schorg.GasStation import create_schema_org_model
    from schorg.GasStation import GasStation

    a = create_schema_org_model(type_=GasStationInheritedProperties)
    b = create_schema_org_model(type_=GasStationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    GasStation.schema()


def MotorcycleDealer_test():
    from schorg.MotorcycleDealer import MotorcycleDealerInheritedProperties
    from schorg.MotorcycleDealer import MotorcycleDealerProperties
    from schorg.MotorcycleDealer import AllProperties
    from schorg.MotorcycleDealer import create_schema_org_model
    from schorg.MotorcycleDealer import MotorcycleDealer

    a = create_schema_org_model(type_=MotorcycleDealerInheritedProperties)
    b = create_schema_org_model(type_=MotorcycleDealerProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MotorcycleDealer.schema()


def OfferCatalog_test():
    from schorg.OfferCatalog import OfferCatalogInheritedProperties
    from schorg.OfferCatalog import OfferCatalogProperties
    from schorg.OfferCatalog import AllProperties
    from schorg.OfferCatalog import create_schema_org_model
    from schorg.OfferCatalog import OfferCatalog

    a = create_schema_org_model(type_=OfferCatalogInheritedProperties)
    b = create_schema_org_model(type_=OfferCatalogProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    OfferCatalog.schema()


def GeneralContractor_test():
    from schorg.GeneralContractor import GeneralContractorInheritedProperties
    from schorg.GeneralContractor import GeneralContractorProperties
    from schorg.GeneralContractor import AllProperties
    from schorg.GeneralContractor import create_schema_org_model
    from schorg.GeneralContractor import GeneralContractor

    a = create_schema_org_model(type_=GeneralContractorInheritedProperties)
    b = create_schema_org_model(type_=GeneralContractorProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    GeneralContractor.schema()


def Online_test():
    from schorg.Online import OnlineInheritedProperties
    from schorg.Online import OnlineProperties
    from schorg.Online import AllProperties
    from schorg.Online import create_schema_org_model
    from schorg.Online import Online

    a = create_schema_org_model(type_=OnlineInheritedProperties)
    b = create_schema_org_model(type_=OnlineProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Online.schema()


def Observation_test():
    from schorg.Observation import ObservationInheritedProperties
    from schorg.Observation import ObservationProperties
    from schorg.Observation import AllProperties
    from schorg.Observation import create_schema_org_model
    from schorg.Observation import Observation

    a = create_schema_org_model(type_=ObservationInheritedProperties)
    b = create_schema_org_model(type_=ObservationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Observation.schema()


def DefinedTerm_test():
    from schorg.DefinedTerm import DefinedTermInheritedProperties
    from schorg.DefinedTerm import DefinedTermProperties
    from schorg.DefinedTerm import AllProperties
    from schorg.DefinedTerm import create_schema_org_model
    from schorg.DefinedTerm import DefinedTerm

    a = create_schema_org_model(type_=DefinedTermInheritedProperties)
    b = create_schema_org_model(type_=DefinedTermProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    DefinedTerm.schema()


def CategoryCode_test():
    from schorg.CategoryCode import CategoryCodeInheritedProperties
    from schorg.CategoryCode import CategoryCodeProperties
    from schorg.CategoryCode import AllProperties
    from schorg.CategoryCode import create_schema_org_model
    from schorg.CategoryCode import CategoryCode

    a = create_schema_org_model(type_=CategoryCodeInheritedProperties)
    b = create_schema_org_model(type_=CategoryCodeProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    CategoryCode.schema()


def DrinkAction_test():
    from schorg.DrinkAction import DrinkActionInheritedProperties
    from schorg.DrinkAction import DrinkActionProperties
    from schorg.DrinkAction import AllProperties
    from schorg.DrinkAction import create_schema_org_model
    from schorg.DrinkAction import DrinkAction

    a = create_schema_org_model(type_=DrinkActionInheritedProperties)
    b = create_schema_org_model(type_=DrinkActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    DrinkAction.schema()


def Nonprofit501c28_test():
    from schorg.Nonprofit501c28 import Nonprofit501c28InheritedProperties
    from schorg.Nonprofit501c28 import Nonprofit501c28Properties
    from schorg.Nonprofit501c28 import AllProperties
    from schorg.Nonprofit501c28 import create_schema_org_model
    from schorg.Nonprofit501c28 import Nonprofit501c28

    a = create_schema_org_model(type_=Nonprofit501c28InheritedProperties)
    b = create_schema_org_model(type_=Nonprofit501c28Properties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Nonprofit501c28.schema()


def Report_test():
    from schorg.Report import ReportInheritedProperties
    from schorg.Report import ReportProperties
    from schorg.Report import AllProperties
    from schorg.Report import create_schema_org_model
    from schorg.Report import Report

    a = create_schema_org_model(type_=ReportInheritedProperties)
    b = create_schema_org_model(type_=ReportProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Report.schema()


def OriginalShippingFees_test():
    from schorg.OriginalShippingFees import OriginalShippingFeesInheritedProperties
    from schorg.OriginalShippingFees import OriginalShippingFeesProperties
    from schorg.OriginalShippingFees import AllProperties
    from schorg.OriginalShippingFees import create_schema_org_model
    from schorg.OriginalShippingFees import OriginalShippingFees

    a = create_schema_org_model(type_=OriginalShippingFeesInheritedProperties)
    b = create_schema_org_model(type_=OriginalShippingFeesProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    OriginalShippingFees.schema()


def DaySpa_test():
    from schorg.DaySpa import DaySpaInheritedProperties
    from schorg.DaySpa import DaySpaProperties
    from schorg.DaySpa import AllProperties
    from schorg.DaySpa import create_schema_org_model
    from schorg.DaySpa import DaySpa

    a = create_schema_org_model(type_=DaySpaInheritedProperties)
    b = create_schema_org_model(type_=DaySpaProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    DaySpa.schema()


def Geriatric_test():
    from schorg.Geriatric import GeriatricInheritedProperties
    from schorg.Geriatric import GeriatricProperties
    from schorg.Geriatric import AllProperties
    from schorg.Geriatric import create_schema_org_model
    from schorg.Geriatric import Geriatric

    a = create_schema_org_model(type_=GeriatricInheritedProperties)
    b = create_schema_org_model(type_=GeriatricProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Geriatric.schema()


def AppendAction_test():
    from schorg.AppendAction import AppendActionInheritedProperties
    from schorg.AppendAction import AppendActionProperties
    from schorg.AppendAction import AllProperties
    from schorg.AppendAction import create_schema_org_model
    from schorg.AppendAction import AppendAction

    a = create_schema_org_model(type_=AppendActionInheritedProperties)
    b = create_schema_org_model(type_=AppendActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    AppendAction.schema()


def WearableSizeGroupWomens_test():
    from schorg.WearableSizeGroupWomens import WearableSizeGroupWomensInheritedProperties
    from schorg.WearableSizeGroupWomens import WearableSizeGroupWomensProperties
    from schorg.WearableSizeGroupWomens import AllProperties
    from schorg.WearableSizeGroupWomens import create_schema_org_model
    from schorg.WearableSizeGroupWomens import WearableSizeGroupWomens

    a = create_schema_org_model(type_=WearableSizeGroupWomensInheritedProperties)
    b = create_schema_org_model(type_=WearableSizeGroupWomensProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    WearableSizeGroupWomens.schema()


def Occupation_test():
    from schorg.Occupation import OccupationInheritedProperties
    from schorg.Occupation import OccupationProperties
    from schorg.Occupation import AllProperties
    from schorg.Occupation import create_schema_org_model
    from schorg.Occupation import Occupation

    a = create_schema_org_model(type_=OccupationInheritedProperties)
    b = create_schema_org_model(type_=OccupationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Occupation.schema()


def RadiationTherapy_test():
    from schorg.RadiationTherapy import RadiationTherapyInheritedProperties
    from schorg.RadiationTherapy import RadiationTherapyProperties
    from schorg.RadiationTherapy import AllProperties
    from schorg.RadiationTherapy import create_schema_org_model
    from schorg.RadiationTherapy import RadiationTherapy

    a = create_schema_org_model(type_=RadiationTherapyInheritedProperties)
    b = create_schema_org_model(type_=RadiationTherapyProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    RadiationTherapy.schema()


def BodyMeasurementHeight_test():
    from schorg.BodyMeasurementHeight import BodyMeasurementHeightInheritedProperties
    from schorg.BodyMeasurementHeight import BodyMeasurementHeightProperties
    from schorg.BodyMeasurementHeight import AllProperties
    from schorg.BodyMeasurementHeight import create_schema_org_model
    from schorg.BodyMeasurementHeight import BodyMeasurementHeight

    a = create_schema_org_model(type_=BodyMeasurementHeightInheritedProperties)
    b = create_schema_org_model(type_=BodyMeasurementHeightProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    BodyMeasurementHeight.schema()


def OfferShippingDetails_test():
    from schorg.OfferShippingDetails import OfferShippingDetailsInheritedProperties
    from schorg.OfferShippingDetails import OfferShippingDetailsProperties
    from schorg.OfferShippingDetails import AllProperties
    from schorg.OfferShippingDetails import create_schema_org_model
    from schorg.OfferShippingDetails import OfferShippingDetails

    a = create_schema_org_model(type_=OfferShippingDetailsInheritedProperties)
    b = create_schema_org_model(type_=OfferShippingDetailsProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    OfferShippingDetails.schema()


def Nonprofit501c5_test():
    from schorg.Nonprofit501c5 import Nonprofit501c5InheritedProperties
    from schorg.Nonprofit501c5 import Nonprofit501c5Properties
    from schorg.Nonprofit501c5 import AllProperties
    from schorg.Nonprofit501c5 import create_schema_org_model
    from schorg.Nonprofit501c5 import Nonprofit501c5

    a = create_schema_org_model(type_=Nonprofit501c5InheritedProperties)
    b = create_schema_org_model(type_=Nonprofit501c5Properties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Nonprofit501c5.schema()


def Nonprofit501c25_test():
    from schorg.Nonprofit501c25 import Nonprofit501c25InheritedProperties
    from schorg.Nonprofit501c25 import Nonprofit501c25Properties
    from schorg.Nonprofit501c25 import AllProperties
    from schorg.Nonprofit501c25 import create_schema_org_model
    from schorg.Nonprofit501c25 import Nonprofit501c25

    a = create_schema_org_model(type_=Nonprofit501c25InheritedProperties)
    b = create_schema_org_model(type_=Nonprofit501c25Properties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Nonprofit501c25.schema()


def MedicalResearcher_test():
    from schorg.MedicalResearcher import MedicalResearcherInheritedProperties
    from schorg.MedicalResearcher import MedicalResearcherProperties
    from schorg.MedicalResearcher import AllProperties
    from schorg.MedicalResearcher import create_schema_org_model
    from schorg.MedicalResearcher import MedicalResearcher

    a = create_schema_org_model(type_=MedicalResearcherInheritedProperties)
    b = create_schema_org_model(type_=MedicalResearcherProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MedicalResearcher.schema()


def RadioSeries_test():
    from schorg.RadioSeries import RadioSeriesInheritedProperties
    from schorg.RadioSeries import RadioSeriesProperties
    from schorg.RadioSeries import AllProperties
    from schorg.RadioSeries import create_schema_org_model
    from schorg.RadioSeries import RadioSeries

    a = create_schema_org_model(type_=RadioSeriesInheritedProperties)
    b = create_schema_org_model(type_=RadioSeriesProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    RadioSeries.schema()


def MedicalSymptom_test():
    from schorg.MedicalSymptom import MedicalSymptomInheritedProperties
    from schorg.MedicalSymptom import MedicalSymptomProperties
    from schorg.MedicalSymptom import AllProperties
    from schorg.MedicalSymptom import create_schema_org_model
    from schorg.MedicalSymptom import MedicalSymptom

    a = create_schema_org_model(type_=MedicalSymptomInheritedProperties)
    b = create_schema_org_model(type_=MedicalSymptomProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MedicalSymptom.schema()


def Nonprofit501c1_test():
    from schorg.Nonprofit501c1 import Nonprofit501c1InheritedProperties
    from schorg.Nonprofit501c1 import Nonprofit501c1Properties
    from schorg.Nonprofit501c1 import AllProperties
    from schorg.Nonprofit501c1 import create_schema_org_model
    from schorg.Nonprofit501c1 import Nonprofit501c1

    a = create_schema_org_model(type_=Nonprofit501c1InheritedProperties)
    b = create_schema_org_model(type_=Nonprofit501c1Properties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Nonprofit501c1.schema()


def TechArticle_test():
    from schorg.TechArticle import TechArticleInheritedProperties
    from schorg.TechArticle import TechArticleProperties
    from schorg.TechArticle import AllProperties
    from schorg.TechArticle import create_schema_org_model
    from schorg.TechArticle import TechArticle

    a = create_schema_org_model(type_=TechArticleInheritedProperties)
    b = create_schema_org_model(type_=TechArticleProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    TechArticle.schema()


def APIReference_test():
    from schorg.APIReference import APIReferenceInheritedProperties
    from schorg.APIReference import APIReferenceProperties
    from schorg.APIReference import AllProperties
    from schorg.APIReference import create_schema_org_model
    from schorg.APIReference import APIReference

    a = create_schema_org_model(type_=APIReferenceInheritedProperties)
    b = create_schema_org_model(type_=APIReferenceProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    APIReference.schema()


def Fungus_test():
    from schorg.Fungus import FungusInheritedProperties
    from schorg.Fungus import FungusProperties
    from schorg.Fungus import AllProperties
    from schorg.Fungus import create_schema_org_model
    from schorg.Fungus import Fungus

    a = create_schema_org_model(type_=FungusInheritedProperties)
    b = create_schema_org_model(type_=FungusProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Fungus.schema()


def MedicalRiskEstimator_test():
    from schorg.MedicalRiskEstimator import MedicalRiskEstimatorInheritedProperties
    from schorg.MedicalRiskEstimator import MedicalRiskEstimatorProperties
    from schorg.MedicalRiskEstimator import AllProperties
    from schorg.MedicalRiskEstimator import create_schema_org_model
    from schorg.MedicalRiskEstimator import MedicalRiskEstimator

    a = create_schema_org_model(type_=MedicalRiskEstimatorInheritedProperties)
    b = create_schema_org_model(type_=MedicalRiskEstimatorProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MedicalRiskEstimator.schema()


def MedicalRiskScore_test():
    from schorg.MedicalRiskScore import MedicalRiskScoreInheritedProperties
    from schorg.MedicalRiskScore import MedicalRiskScoreProperties
    from schorg.MedicalRiskScore import AllProperties
    from schorg.MedicalRiskScore import create_schema_org_model
    from schorg.MedicalRiskScore import MedicalRiskScore

    a = create_schema_org_model(type_=MedicalRiskScoreInheritedProperties)
    b = create_schema_org_model(type_=MedicalRiskScoreProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MedicalRiskScore.schema()


def Hotel_test():
    from schorg.Hotel import HotelInheritedProperties
    from schorg.Hotel import HotelProperties
    from schorg.Hotel import AllProperties
    from schorg.Hotel import create_schema_org_model
    from schorg.Hotel import Hotel

    a = create_schema_org_model(type_=HotelInheritedProperties)
    b = create_schema_org_model(type_=HotelProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Hotel.schema()


def AskAction_test():
    from schorg.AskAction import AskActionInheritedProperties
    from schorg.AskAction import AskActionProperties
    from schorg.AskAction import AllProperties
    from schorg.AskAction import create_schema_org_model
    from schorg.AskAction import AskAction

    a = create_schema_org_model(type_=AskActionInheritedProperties)
    b = create_schema_org_model(type_=AskActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    AskAction.schema()


def MediaGallery_test():
    from schorg.MediaGallery import MediaGalleryInheritedProperties
    from schorg.MediaGallery import MediaGalleryProperties
    from schorg.MediaGallery import AllProperties
    from schorg.MediaGallery import create_schema_org_model
    from schorg.MediaGallery import MediaGallery

    a = create_schema_org_model(type_=MediaGalleryInheritedProperties)
    b = create_schema_org_model(type_=MediaGalleryProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MediaGallery.schema()


def BodyMeasurementHand_test():
    from schorg.BodyMeasurementHand import BodyMeasurementHandInheritedProperties
    from schorg.BodyMeasurementHand import BodyMeasurementHandProperties
    from schorg.BodyMeasurementHand import AllProperties
    from schorg.BodyMeasurementHand import create_schema_org_model
    from schorg.BodyMeasurementHand import BodyMeasurementHand

    a = create_schema_org_model(type_=BodyMeasurementHandInheritedProperties)
    b = create_schema_org_model(type_=BodyMeasurementHandProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    BodyMeasurementHand.schema()


def SchoolDistrict_test():
    from schorg.SchoolDistrict import SchoolDistrictInheritedProperties
    from schorg.SchoolDistrict import SchoolDistrictProperties
    from schorg.SchoolDistrict import AllProperties
    from schorg.SchoolDistrict import create_schema_org_model
    from schorg.SchoolDistrict import SchoolDistrict

    a = create_schema_org_model(type_=SchoolDistrictInheritedProperties)
    b = create_schema_org_model(type_=SchoolDistrictProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    SchoolDistrict.schema()


def LinkRole_test():
    from schorg.LinkRole import LinkRoleInheritedProperties
    from schorg.LinkRole import LinkRoleProperties
    from schorg.LinkRole import AllProperties
    from schorg.LinkRole import create_schema_org_model
    from schorg.LinkRole import LinkRole

    a = create_schema_org_model(type_=LinkRoleInheritedProperties)
    b = create_schema_org_model(type_=LinkRoleProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    LinkRole.schema()


def TVEpisode_test():
    from schorg.TVEpisode import TVEpisodeInheritedProperties
    from schorg.TVEpisode import TVEpisodeProperties
    from schorg.TVEpisode import AllProperties
    from schorg.TVEpisode import create_schema_org_model
    from schorg.TVEpisode import TVEpisode

    a = create_schema_org_model(type_=TVEpisodeInheritedProperties)
    b = create_schema_org_model(type_=TVEpisodeProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    TVEpisode.schema()


def FMRadioChannel_test():
    from schorg.FMRadioChannel import FMRadioChannelInheritedProperties
    from schorg.FMRadioChannel import FMRadioChannelProperties
    from schorg.FMRadioChannel import AllProperties
    from schorg.FMRadioChannel import create_schema_org_model
    from schorg.FMRadioChannel import FMRadioChannel

    a = create_schema_org_model(type_=FMRadioChannelInheritedProperties)
    b = create_schema_org_model(type_=FMRadioChannelProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    FMRadioChannel.schema()


def WritePermission_test():
    from schorg.WritePermission import WritePermissionInheritedProperties
    from schorg.WritePermission import WritePermissionProperties
    from schorg.WritePermission import AllProperties
    from schorg.WritePermission import create_schema_org_model
    from schorg.WritePermission import WritePermission

    a = create_schema_org_model(type_=WritePermissionInheritedProperties)
    b = create_schema_org_model(type_=WritePermissionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    WritePermission.schema()


def Menu_test():
    from schorg.Menu import MenuInheritedProperties
    from schorg.Menu import MenuProperties
    from schorg.Menu import AllProperties
    from schorg.Menu import create_schema_org_model
    from schorg.Menu import Menu

    a = create_schema_org_model(type_=MenuInheritedProperties)
    b = create_schema_org_model(type_=MenuProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Menu.schema()


def DownloadAction_test():
    from schorg.DownloadAction import DownloadActionInheritedProperties
    from schorg.DownloadAction import DownloadActionProperties
    from schorg.DownloadAction import AllProperties
    from schorg.DownloadAction import create_schema_org_model
    from schorg.DownloadAction import DownloadAction

    a = create_schema_org_model(type_=DownloadActionInheritedProperties)
    b = create_schema_org_model(type_=DownloadActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    DownloadAction.schema()


def UserTweets_test():
    from schorg.UserTweets import UserTweetsInheritedProperties
    from schorg.UserTweets import UserTweetsProperties
    from schorg.UserTweets import AllProperties
    from schorg.UserTweets import create_schema_org_model
    from schorg.UserTweets import UserTweets

    a = create_schema_org_model(type_=UserTweetsInheritedProperties)
    b = create_schema_org_model(type_=UserTweetsProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    UserTweets.schema()


def Anesthesia_test():
    from schorg.Anesthesia import AnesthesiaInheritedProperties
    from schorg.Anesthesia import AnesthesiaProperties
    from schorg.Anesthesia import AllProperties
    from schorg.Anesthesia import create_schema_org_model
    from schorg.Anesthesia import Anesthesia

    a = create_schema_org_model(type_=AnesthesiaInheritedProperties)
    b = create_schema_org_model(type_=AnesthesiaProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Anesthesia.schema()


def WearableSizeSystemCN_test():
    from schorg.WearableSizeSystemCN import WearableSizeSystemCNInheritedProperties
    from schorg.WearableSizeSystemCN import WearableSizeSystemCNProperties
    from schorg.WearableSizeSystemCN import AllProperties
    from schorg.WearableSizeSystemCN import create_schema_org_model
    from schorg.WearableSizeSystemCN import WearableSizeSystemCN

    a = create_schema_org_model(type_=WearableSizeSystemCNInheritedProperties)
    b = create_schema_org_model(type_=WearableSizeSystemCNProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    WearableSizeSystemCN.schema()


def VinylFormat_test():
    from schorg.VinylFormat import VinylFormatInheritedProperties
    from schorg.VinylFormat import VinylFormatProperties
    from schorg.VinylFormat import AllProperties
    from schorg.VinylFormat import create_schema_org_model
    from schorg.VinylFormat import VinylFormat

    a = create_schema_org_model(type_=VinylFormatInheritedProperties)
    b = create_schema_org_model(type_=VinylFormatProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    VinylFormat.schema()


def FourWheelDriveConfiguration_test():
    from schorg.FourWheelDriveConfiguration import FourWheelDriveConfigurationInheritedProperties
    from schorg.FourWheelDriveConfiguration import FourWheelDriveConfigurationProperties
    from schorg.FourWheelDriveConfiguration import AllProperties
    from schorg.FourWheelDriveConfiguration import create_schema_org_model
    from schorg.FourWheelDriveConfiguration import FourWheelDriveConfiguration

    a = create_schema_org_model(type_=FourWheelDriveConfigurationInheritedProperties)
    b = create_schema_org_model(type_=FourWheelDriveConfigurationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    FourWheelDriveConfiguration.schema()


def PerformingArtsTheater_test():
    from schorg.PerformingArtsTheater import PerformingArtsTheaterInheritedProperties
    from schorg.PerformingArtsTheater import PerformingArtsTheaterProperties
    from schorg.PerformingArtsTheater import AllProperties
    from schorg.PerformingArtsTheater import create_schema_org_model
    from schorg.PerformingArtsTheater import PerformingArtsTheater

    a = create_schema_org_model(type_=PerformingArtsTheaterInheritedProperties)
    b = create_schema_org_model(type_=PerformingArtsTheaterProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    PerformingArtsTheater.schema()


def MedicalDevicePurpose_test():
    from schorg.MedicalDevicePurpose import MedicalDevicePurposeInheritedProperties
    from schorg.MedicalDevicePurpose import MedicalDevicePurposeProperties
    from schorg.MedicalDevicePurpose import AllProperties
    from schorg.MedicalDevicePurpose import create_schema_org_model
    from schorg.MedicalDevicePurpose import MedicalDevicePurpose

    a = create_schema_org_model(type_=MedicalDevicePurposeInheritedProperties)
    b = create_schema_org_model(type_=MedicalDevicePurposeProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MedicalDevicePurpose.schema()


def Zoo_test():
    from schorg.Zoo import ZooInheritedProperties
    from schorg.Zoo import ZooProperties
    from schorg.Zoo import AllProperties
    from schorg.Zoo import create_schema_org_model
    from schorg.Zoo import Zoo

    a = create_schema_org_model(type_=ZooInheritedProperties)
    b = create_schema_org_model(type_=ZooProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Zoo.schema()


def BasicIncome_test():
    from schorg.BasicIncome import BasicIncomeInheritedProperties
    from schorg.BasicIncome import BasicIncomeProperties
    from schorg.BasicIncome import AllProperties
    from schorg.BasicIncome import create_schema_org_model
    from schorg.BasicIncome import BasicIncome

    a = create_schema_org_model(type_=BasicIncomeInheritedProperties)
    b = create_schema_org_model(type_=BasicIncomeProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    BasicIncome.schema()


def Flexibility_test():
    from schorg.Flexibility import FlexibilityInheritedProperties
    from schorg.Flexibility import FlexibilityProperties
    from schorg.Flexibility import AllProperties
    from schorg.Flexibility import create_schema_org_model
    from schorg.Flexibility import Flexibility

    a = create_schema_org_model(type_=FlexibilityInheritedProperties)
    b = create_schema_org_model(type_=FlexibilityProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Flexibility.schema()


def JoinAction_test():
    from schorg.JoinAction import JoinActionInheritedProperties
    from schorg.JoinAction import JoinActionProperties
    from schorg.JoinAction import AllProperties
    from schorg.JoinAction import create_schema_org_model
    from schorg.JoinAction import JoinAction

    a = create_schema_org_model(type_=JoinActionInheritedProperties)
    b = create_schema_org_model(type_=JoinActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    JoinAction.schema()


def IceCreamShop_test():
    from schorg.IceCreamShop import IceCreamShopInheritedProperties
    from schorg.IceCreamShop import IceCreamShopProperties
    from schorg.IceCreamShop import AllProperties
    from schorg.IceCreamShop import create_schema_org_model
    from schorg.IceCreamShop import IceCreamShop

    a = create_schema_org_model(type_=IceCreamShopInheritedProperties)
    b = create_schema_org_model(type_=IceCreamShopProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    IceCreamShop.schema()


def HinduTemple_test():
    from schorg.HinduTemple import HinduTempleInheritedProperties
    from schorg.HinduTemple import HinduTempleProperties
    from schorg.HinduTemple import AllProperties
    from schorg.HinduTemple import create_schema_org_model
    from schorg.HinduTemple import HinduTemple

    a = create_schema_org_model(type_=HinduTempleInheritedProperties)
    b = create_schema_org_model(type_=HinduTempleProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    HinduTemple.schema()


def NarcoticConsideration_test():
    from schorg.NarcoticConsideration import NarcoticConsiderationInheritedProperties
    from schorg.NarcoticConsideration import NarcoticConsiderationProperties
    from schorg.NarcoticConsideration import AllProperties
    from schorg.NarcoticConsideration import create_schema_org_model
    from schorg.NarcoticConsideration import NarcoticConsideration

    a = create_schema_org_model(type_=NarcoticConsiderationInheritedProperties)
    b = create_schema_org_model(type_=NarcoticConsiderationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    NarcoticConsideration.schema()


def CancelAction_test():
    from schorg.CancelAction import CancelActionInheritedProperties
    from schorg.CancelAction import CancelActionProperties
    from schorg.CancelAction import AllProperties
    from schorg.CancelAction import create_schema_org_model
    from schorg.CancelAction import CancelAction

    a = create_schema_org_model(type_=CancelActionInheritedProperties)
    b = create_schema_org_model(type_=CancelActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    CancelAction.schema()


def RadioSeason_test():
    from schorg.RadioSeason import RadioSeasonInheritedProperties
    from schorg.RadioSeason import RadioSeasonProperties
    from schorg.RadioSeason import AllProperties
    from schorg.RadioSeason import create_schema_org_model
    from schorg.RadioSeason import RadioSeason

    a = create_schema_org_model(type_=RadioSeasonInheritedProperties)
    b = create_schema_org_model(type_=RadioSeasonProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    RadioSeason.schema()


def Dentist_test():
    from schorg.Dentist import DentistInheritedProperties
    from schorg.Dentist import DentistProperties
    from schorg.Dentist import AllProperties
    from schorg.Dentist import create_schema_org_model
    from schorg.Dentist import Dentist

    a = create_schema_org_model(type_=DentistInheritedProperties)
    b = create_schema_org_model(type_=DentistProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Dentist.schema()


def Nonprofit501c11_test():
    from schorg.Nonprofit501c11 import Nonprofit501c11InheritedProperties
    from schorg.Nonprofit501c11 import Nonprofit501c11Properties
    from schorg.Nonprofit501c11 import AllProperties
    from schorg.Nonprofit501c11 import create_schema_org_model
    from schorg.Nonprofit501c11 import Nonprofit501c11

    a = create_schema_org_model(type_=Nonprofit501c11InheritedProperties)
    b = create_schema_org_model(type_=Nonprofit501c11Properties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Nonprofit501c11.schema()


def DrugClass_test():
    from schorg.DrugClass import DrugClassInheritedProperties
    from schorg.DrugClass import DrugClassProperties
    from schorg.DrugClass import AllProperties
    from schorg.DrugClass import create_schema_org_model
    from schorg.DrugClass import DrugClass

    a = create_schema_org_model(type_=DrugClassInheritedProperties)
    b = create_schema_org_model(type_=DrugClassProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    DrugClass.schema()


def Musculoskeletal_test():
    from schorg.Musculoskeletal import MusculoskeletalInheritedProperties
    from schorg.Musculoskeletal import MusculoskeletalProperties
    from schorg.Musculoskeletal import AllProperties
    from schorg.Musculoskeletal import create_schema_org_model
    from schorg.Musculoskeletal import Musculoskeletal

    a = create_schema_org_model(type_=MusculoskeletalInheritedProperties)
    b = create_schema_org_model(type_=MusculoskeletalProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Musculoskeletal.schema()


def CityHall_test():
    from schorg.CityHall import CityHallInheritedProperties
    from schorg.CityHall import CityHallProperties
    from schorg.CityHall import AllProperties
    from schorg.CityHall import create_schema_org_model
    from schorg.CityHall import CityHall

    a = create_schema_org_model(type_=CityHallInheritedProperties)
    b = create_schema_org_model(type_=CityHallProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    CityHall.schema()


def PharmacySpecialty_test():
    from schorg.PharmacySpecialty import PharmacySpecialtyInheritedProperties
    from schorg.PharmacySpecialty import PharmacySpecialtyProperties
    from schorg.PharmacySpecialty import AllProperties
    from schorg.PharmacySpecialty import create_schema_org_model
    from schorg.PharmacySpecialty import PharmacySpecialty

    a = create_schema_org_model(type_=PharmacySpecialtyInheritedProperties)
    b = create_schema_org_model(type_=PharmacySpecialtyProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    PharmacySpecialty.schema()


def HowToDirection_test():
    from schorg.HowToDirection import HowToDirectionInheritedProperties
    from schorg.HowToDirection import HowToDirectionProperties
    from schorg.HowToDirection import AllProperties
    from schorg.HowToDirection import create_schema_org_model
    from schorg.HowToDirection import HowToDirection

    a = create_schema_org_model(type_=HowToDirectionInheritedProperties)
    b = create_schema_org_model(type_=HowToDirectionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    HowToDirection.schema()


def BuyAction_test():
    from schorg.BuyAction import BuyActionInheritedProperties
    from schorg.BuyAction import BuyActionProperties
    from schorg.BuyAction import AllProperties
    from schorg.BuyAction import create_schema_org_model
    from schorg.BuyAction import BuyAction

    a = create_schema_org_model(type_=BuyActionInheritedProperties)
    b = create_schema_org_model(type_=BuyActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    BuyAction.schema()


def Nonprofit501e_test():
    from schorg.Nonprofit501e import Nonprofit501eInheritedProperties
    from schorg.Nonprofit501e import Nonprofit501eProperties
    from schorg.Nonprofit501e import AllProperties
    from schorg.Nonprofit501e import create_schema_org_model
    from schorg.Nonprofit501e import Nonprofit501e

    a = create_schema_org_model(type_=Nonprofit501eInheritedProperties)
    b = create_schema_org_model(type_=Nonprofit501eProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Nonprofit501e.schema()


def HearingImpairedSupported_test():
    from schorg.HearingImpairedSupported import HearingImpairedSupportedInheritedProperties
    from schorg.HearingImpairedSupported import HearingImpairedSupportedProperties
    from schorg.HearingImpairedSupported import AllProperties
    from schorg.HearingImpairedSupported import create_schema_org_model
    from schorg.HearingImpairedSupported import HearingImpairedSupported

    a = create_schema_org_model(type_=HearingImpairedSupportedInheritedProperties)
    b = create_schema_org_model(type_=HearingImpairedSupportedProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    HearingImpairedSupported.schema()


def Nonprofit501c3_test():
    from schorg.Nonprofit501c3 import Nonprofit501c3InheritedProperties
    from schorg.Nonprofit501c3 import Nonprofit501c3Properties
    from schorg.Nonprofit501c3 import AllProperties
    from schorg.Nonprofit501c3 import create_schema_org_model
    from schorg.Nonprofit501c3 import Nonprofit501c3

    a = create_schema_org_model(type_=Nonprofit501c3InheritedProperties)
    b = create_schema_org_model(type_=Nonprofit501c3Properties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Nonprofit501c3.schema()


def Manuscript_test():
    from schorg.Manuscript import ManuscriptInheritedProperties
    from schorg.Manuscript import ManuscriptProperties
    from schorg.Manuscript import AllProperties
    from schorg.Manuscript import create_schema_org_model
    from schorg.Manuscript import Manuscript

    a = create_schema_org_model(type_=ManuscriptInheritedProperties)
    b = create_schema_org_model(type_=ManuscriptProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Manuscript.schema()


def CompilationAlbum_test():
    from schorg.CompilationAlbum import CompilationAlbumInheritedProperties
    from schorg.CompilationAlbum import CompilationAlbumProperties
    from schorg.CompilationAlbum import AllProperties
    from schorg.CompilationAlbum import create_schema_org_model
    from schorg.CompilationAlbum import CompilationAlbum

    a = create_schema_org_model(type_=CompilationAlbumInheritedProperties)
    b = create_schema_org_model(type_=CompilationAlbumProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    CompilationAlbum.schema()


def BookSeries_test():
    from schorg.BookSeries import BookSeriesInheritedProperties
    from schorg.BookSeries import BookSeriesProperties
    from schorg.BookSeries import AllProperties
    from schorg.BookSeries import create_schema_org_model
    from schorg.BookSeries import BookSeries

    a = create_schema_org_model(type_=BookSeriesInheritedProperties)
    b = create_schema_org_model(type_=BookSeriesProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    BookSeries.schema()


def ReturnAtKiosk_test():
    from schorg.ReturnAtKiosk import ReturnAtKioskInheritedProperties
    from schorg.ReturnAtKiosk import ReturnAtKioskProperties
    from schorg.ReturnAtKiosk import AllProperties
    from schorg.ReturnAtKiosk import create_schema_org_model
    from schorg.ReturnAtKiosk import ReturnAtKiosk

    a = create_schema_org_model(type_=ReturnAtKioskInheritedProperties)
    b = create_schema_org_model(type_=ReturnAtKioskProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ReturnAtKiosk.schema()


def TouristDestination_test():
    from schorg.TouristDestination import TouristDestinationInheritedProperties
    from schorg.TouristDestination import TouristDestinationProperties
    from schorg.TouristDestination import AllProperties
    from schorg.TouristDestination import create_schema_org_model
    from schorg.TouristDestination import TouristDestination

    a = create_schema_org_model(type_=TouristDestinationInheritedProperties)
    b = create_schema_org_model(type_=TouristDestinationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    TouristDestination.schema()


def RsvpResponseType_test():
    from schorg.RsvpResponseType import RsvpResponseTypeInheritedProperties
    from schorg.RsvpResponseType import RsvpResponseTypeProperties
    from schorg.RsvpResponseType import AllProperties
    from schorg.RsvpResponseType import create_schema_org_model
    from schorg.RsvpResponseType import RsvpResponseType

    a = create_schema_org_model(type_=RsvpResponseTypeInheritedProperties)
    b = create_schema_org_model(type_=RsvpResponseTypeProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    RsvpResponseType.schema()


def BroadcastService_test():
    from schorg.BroadcastService import BroadcastServiceInheritedProperties
    from schorg.BroadcastService import BroadcastServiceProperties
    from schorg.BroadcastService import AllProperties
    from schorg.BroadcastService import create_schema_org_model
    from schorg.BroadcastService import BroadcastService

    a = create_schema_org_model(type_=BroadcastServiceInheritedProperties)
    b = create_schema_org_model(type_=BroadcastServiceProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    BroadcastService.schema()


def RadioBroadcastService_test():
    from schorg.RadioBroadcastService import RadioBroadcastServiceInheritedProperties
    from schorg.RadioBroadcastService import RadioBroadcastServiceProperties
    from schorg.RadioBroadcastService import AllProperties
    from schorg.RadioBroadcastService import create_schema_org_model
    from schorg.RadioBroadcastService import RadioBroadcastService

    a = create_schema_org_model(type_=RadioBroadcastServiceInheritedProperties)
    b = create_schema_org_model(type_=RadioBroadcastServiceProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    RadioBroadcastService.schema()


def MusicStore_test():
    from schorg.MusicStore import MusicStoreInheritedProperties
    from schorg.MusicStore import MusicStoreProperties
    from schorg.MusicStore import AllProperties
    from schorg.MusicStore import create_schema_org_model
    from schorg.MusicStore import MusicStore

    a = create_schema_org_model(type_=MusicStoreInheritedProperties)
    b = create_schema_org_model(type_=MusicStoreProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MusicStore.schema()


def InstallAction_test():
    from schorg.InstallAction import InstallActionInheritedProperties
    from schorg.InstallAction import InstallActionProperties
    from schorg.InstallAction import AllProperties
    from schorg.InstallAction import create_schema_org_model
    from schorg.InstallAction import InstallAction

    a = create_schema_org_model(type_=InstallActionInheritedProperties)
    b = create_schema_org_model(type_=InstallActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    InstallAction.schema()


def Nursing_test():
    from schorg.Nursing import NursingInheritedProperties
    from schorg.Nursing import NursingProperties
    from schorg.Nursing import AllProperties
    from schorg.Nursing import create_schema_org_model
    from schorg.Nursing import Nursing

    a = create_schema_org_model(type_=NursingInheritedProperties)
    b = create_schema_org_model(type_=NursingProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Nursing.schema()


def BarOrPub_test():
    from schorg.BarOrPub import BarOrPubInheritedProperties
    from schorg.BarOrPub import BarOrPubProperties
    from schorg.BarOrPub import AllProperties
    from schorg.BarOrPub import create_schema_org_model
    from schorg.BarOrPub import BarOrPub

    a = create_schema_org_model(type_=BarOrPubInheritedProperties)
    b = create_schema_org_model(type_=BarOrPubProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    BarOrPub.schema()


def IndividualProduct_test():
    from schorg.IndividualProduct import IndividualProductInheritedProperties
    from schorg.IndividualProduct import IndividualProductProperties
    from schorg.IndividualProduct import AllProperties
    from schorg.IndividualProduct import create_schema_org_model
    from schorg.IndividualProduct import IndividualProduct

    a = create_schema_org_model(type_=IndividualProductInheritedProperties)
    b = create_schema_org_model(type_=IndividualProductProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    IndividualProduct.schema()


def SportsTeam_test():
    from schorg.SportsTeam import SportsTeamInheritedProperties
    from schorg.SportsTeam import SportsTeamProperties
    from schorg.SportsTeam import AllProperties
    from schorg.SportsTeam import create_schema_org_model
    from schorg.SportsTeam import SportsTeam

    a = create_schema_org_model(type_=SportsTeamInheritedProperties)
    b = create_schema_org_model(type_=SportsTeamProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    SportsTeam.schema()


def HairSalon_test():
    from schorg.HairSalon import HairSalonInheritedProperties
    from schorg.HairSalon import HairSalonProperties
    from schorg.HairSalon import AllProperties
    from schorg.HairSalon import create_schema_org_model
    from schorg.HairSalon import HairSalon

    a = create_schema_org_model(type_=HairSalonInheritedProperties)
    b = create_schema_org_model(type_=HairSalonProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    HairSalon.schema()


def UseAction_test():
    from schorg.UseAction import UseActionInheritedProperties
    from schorg.UseAction import UseActionProperties
    from schorg.UseAction import AllProperties
    from schorg.UseAction import create_schema_org_model
    from schorg.UseAction import UseAction

    a = create_schema_org_model(type_=UseActionInheritedProperties)
    b = create_schema_org_model(type_=UseActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    UseAction.schema()


def SoundtrackAlbum_test():
    from schorg.SoundtrackAlbum import SoundtrackAlbumInheritedProperties
    from schorg.SoundtrackAlbum import SoundtrackAlbumProperties
    from schorg.SoundtrackAlbum import AllProperties
    from schorg.SoundtrackAlbum import create_schema_org_model
    from schorg.SoundtrackAlbum import SoundtrackAlbum

    a = create_schema_org_model(type_=SoundtrackAlbumInheritedProperties)
    b = create_schema_org_model(type_=SoundtrackAlbumProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    SoundtrackAlbum.schema()


def HowToStep_test():
    from schorg.HowToStep import HowToStepInheritedProperties
    from schorg.HowToStep import HowToStepProperties
    from schorg.HowToStep import AllProperties
    from schorg.HowToStep import create_schema_org_model
    from schorg.HowToStep import HowToStep

    a = create_schema_org_model(type_=HowToStepInheritedProperties)
    b = create_schema_org_model(type_=HowToStepProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    HowToStep.schema()


def HardwareStore_test():
    from schorg.HardwareStore import HardwareStoreInheritedProperties
    from schorg.HardwareStore import HardwareStoreProperties
    from schorg.HardwareStore import AllProperties
    from schorg.HardwareStore import create_schema_org_model
    from schorg.HardwareStore import HardwareStore

    a = create_schema_org_model(type_=HardwareStoreInheritedProperties)
    b = create_schema_org_model(type_=HardwareStoreProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    HardwareStore.schema()


def Virus_test():
    from schorg.Virus import VirusInheritedProperties
    from schorg.Virus import VirusProperties
    from schorg.Virus import AllProperties
    from schorg.Virus import create_schema_org_model
    from schorg.Virus import Virus

    a = create_schema_org_model(type_=VirusInheritedProperties)
    b = create_schema_org_model(type_=VirusProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Virus.schema()


def EndorsementRating_test():
    from schorg.EndorsementRating import EndorsementRatingInheritedProperties
    from schorg.EndorsementRating import EndorsementRatingProperties
    from schorg.EndorsementRating import AllProperties
    from schorg.EndorsementRating import create_schema_org_model
    from schorg.EndorsementRating import EndorsementRating

    a = create_schema_org_model(type_=EndorsementRatingInheritedProperties)
    b = create_schema_org_model(type_=EndorsementRatingProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    EndorsementRating.schema()


def Brewery_test():
    from schorg.Brewery import BreweryInheritedProperties
    from schorg.Brewery import BreweryProperties
    from schorg.Brewery import AllProperties
    from schorg.Brewery import create_schema_org_model
    from schorg.Brewery import Brewery

    a = create_schema_org_model(type_=BreweryInheritedProperties)
    b = create_schema_org_model(type_=BreweryProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Brewery.schema()


def Country_test():
    from schorg.Country import CountryInheritedProperties
    from schorg.Country import CountryProperties
    from schorg.Country import AllProperties
    from schorg.Country import create_schema_org_model
    from schorg.Country import Country

    a = create_schema_org_model(type_=CountryInheritedProperties)
    b = create_schema_org_model(type_=CountryProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Country.schema()


def BoatTerminal_test():
    from schorg.BoatTerminal import BoatTerminalInheritedProperties
    from schorg.BoatTerminal import BoatTerminalProperties
    from schorg.BoatTerminal import AllProperties
    from schorg.BoatTerminal import create_schema_org_model
    from schorg.BoatTerminal import BoatTerminal

    a = create_schema_org_model(type_=BoatTerminalInheritedProperties)
    b = create_schema_org_model(type_=BoatTerminalProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    BoatTerminal.schema()


def Play_test():
    from schorg.Play import PlayInheritedProperties
    from schorg.Play import PlayProperties
    from schorg.Play import AllProperties
    from schorg.Play import create_schema_org_model
    from schorg.Play import Play

    a = create_schema_org_model(type_=PlayInheritedProperties)
    b = create_schema_org_model(type_=PlayProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Play.schema()


def ParkingFacility_test():
    from schorg.ParkingFacility import ParkingFacilityInheritedProperties
    from schorg.ParkingFacility import ParkingFacilityProperties
    from schorg.ParkingFacility import AllProperties
    from schorg.ParkingFacility import create_schema_org_model
    from schorg.ParkingFacility import ParkingFacility

    a = create_schema_org_model(type_=ParkingFacilityInheritedProperties)
    b = create_schema_org_model(type_=ParkingFacilityProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ParkingFacility.schema()


def MedicalDevice_test():
    from schorg.MedicalDevice import MedicalDeviceInheritedProperties
    from schorg.MedicalDevice import MedicalDeviceProperties
    from schorg.MedicalDevice import AllProperties
    from schorg.MedicalDevice import create_schema_org_model
    from schorg.MedicalDevice import MedicalDevice

    a = create_schema_org_model(type_=MedicalDeviceInheritedProperties)
    b = create_schema_org_model(type_=MedicalDeviceProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MedicalDevice.schema()


def Winery_test():
    from schorg.Winery import WineryInheritedProperties
    from schorg.Winery import WineryProperties
    from schorg.Winery import AllProperties
    from schorg.Winery import create_schema_org_model
    from schorg.Winery import Winery

    a = create_schema_org_model(type_=WineryInheritedProperties)
    b = create_schema_org_model(type_=WineryProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Winery.schema()


def CheckOutAction_test():
    from schorg.CheckOutAction import CheckOutActionInheritedProperties
    from schorg.CheckOutAction import CheckOutActionProperties
    from schorg.CheckOutAction import AllProperties
    from schorg.CheckOutAction import create_schema_org_model
    from schorg.CheckOutAction import CheckOutAction

    a = create_schema_org_model(type_=CheckOutActionInheritedProperties)
    b = create_schema_org_model(type_=CheckOutActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    CheckOutAction.schema()


def ArchiveOrganization_test():
    from schorg.ArchiveOrganization import ArchiveOrganizationInheritedProperties
    from schorg.ArchiveOrganization import ArchiveOrganizationProperties
    from schorg.ArchiveOrganization import AllProperties
    from schorg.ArchiveOrganization import create_schema_org_model
    from schorg.ArchiveOrganization import ArchiveOrganization

    a = create_schema_org_model(type_=ArchiveOrganizationInheritedProperties)
    b = create_schema_org_model(type_=ArchiveOrganizationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ArchiveOrganization.schema()


def PaymentPastDue_test():
    from schorg.PaymentPastDue import PaymentPastDueInheritedProperties
    from schorg.PaymentPastDue import PaymentPastDueProperties
    from schorg.PaymentPastDue import AllProperties
    from schorg.PaymentPastDue import create_schema_org_model
    from schorg.PaymentPastDue import PaymentPastDue

    a = create_schema_org_model(type_=PaymentPastDueInheritedProperties)
    b = create_schema_org_model(type_=PaymentPastDueProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    PaymentPastDue.schema()


def GroceryStore_test():
    from schorg.GroceryStore import GroceryStoreInheritedProperties
    from schorg.GroceryStore import GroceryStoreProperties
    from schorg.GroceryStore import AllProperties
    from schorg.GroceryStore import create_schema_org_model
    from schorg.GroceryStore import GroceryStore

    a = create_schema_org_model(type_=GroceryStoreInheritedProperties)
    b = create_schema_org_model(type_=GroceryStoreProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    GroceryStore.schema()


def EffectivenessHealthAspect_test():
    from schorg.EffectivenessHealthAspect import EffectivenessHealthAspectInheritedProperties
    from schorg.EffectivenessHealthAspect import EffectivenessHealthAspectProperties
    from schorg.EffectivenessHealthAspect import AllProperties
    from schorg.EffectivenessHealthAspect import create_schema_org_model
    from schorg.EffectivenessHealthAspect import EffectivenessHealthAspect

    a = create_schema_org_model(type_=EffectivenessHealthAspectInheritedProperties)
    b = create_schema_org_model(type_=EffectivenessHealthAspectProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    EffectivenessHealthAspect.schema()


def OccupationalTherapy_test():
    from schorg.OccupationalTherapy import OccupationalTherapyInheritedProperties
    from schorg.OccupationalTherapy import OccupationalTherapyProperties
    from schorg.OccupationalTherapy import AllProperties
    from schorg.OccupationalTherapy import create_schema_org_model
    from schorg.OccupationalTherapy import OccupationalTherapy

    a = create_schema_org_model(type_=OccupationalTherapyInheritedProperties)
    b = create_schema_org_model(type_=OccupationalTherapyProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    OccupationalTherapy.schema()


def VenueMap_test():
    from schorg.VenueMap import VenueMapInheritedProperties
    from schorg.VenueMap import VenueMapProperties
    from schorg.VenueMap import AllProperties
    from schorg.VenueMap import create_schema_org_model
    from schorg.VenueMap import VenueMap

    a = create_schema_org_model(type_=VenueMapInheritedProperties)
    b = create_schema_org_model(type_=VenueMapProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    VenueMap.schema()


def EventMovedOnline_test():
    from schorg.EventMovedOnline import EventMovedOnlineInheritedProperties
    from schorg.EventMovedOnline import EventMovedOnlineProperties
    from schorg.EventMovedOnline import AllProperties
    from schorg.EventMovedOnline import create_schema_org_model
    from schorg.EventMovedOnline import EventMovedOnline

    a = create_schema_org_model(type_=EventMovedOnlineInheritedProperties)
    b = create_schema_org_model(type_=EventMovedOnlineProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    EventMovedOnline.schema()


def Barcode_test():
    from schorg.Barcode import BarcodeInheritedProperties
    from schorg.Barcode import BarcodeProperties
    from schorg.Barcode import AllProperties
    from schorg.Barcode import create_schema_org_model
    from schorg.Barcode import Barcode

    a = create_schema_org_model(type_=BarcodeInheritedProperties)
    b = create_schema_org_model(type_=BarcodeProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Barcode.schema()


def VeterinaryCare_test():
    from schorg.VeterinaryCare import VeterinaryCareInheritedProperties
    from schorg.VeterinaryCare import VeterinaryCareProperties
    from schorg.VeterinaryCare import AllProperties
    from schorg.VeterinaryCare import create_schema_org_model
    from schorg.VeterinaryCare import VeterinaryCare

    a = create_schema_org_model(type_=VeterinaryCareInheritedProperties)
    b = create_schema_org_model(type_=VeterinaryCareProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    VeterinaryCare.schema()


def BeautySalon_test():
    from schorg.BeautySalon import BeautySalonInheritedProperties
    from schorg.BeautySalon import BeautySalonProperties
    from schorg.BeautySalon import AllProperties
    from schorg.BeautySalon import create_schema_org_model
    from schorg.BeautySalon import BeautySalon

    a = create_schema_org_model(type_=BeautySalonInheritedProperties)
    b = create_schema_org_model(type_=BeautySalonProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    BeautySalon.schema()


def WebSite_test():
    from schorg.WebSite import WebSiteInheritedProperties
    from schorg.WebSite import WebSiteProperties
    from schorg.WebSite import AllProperties
    from schorg.WebSite import create_schema_org_model
    from schorg.WebSite import WebSite

    a = create_schema_org_model(type_=WebSiteInheritedProperties)
    b = create_schema_org_model(type_=WebSiteProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    WebSite.schema()


def Electrician_test():
    from schorg.Electrician import ElectricianInheritedProperties
    from schorg.Electrician import ElectricianProperties
    from schorg.Electrician import AllProperties
    from schorg.Electrician import create_schema_org_model
    from schorg.Electrician import Electrician

    a = create_schema_org_model(type_=ElectricianInheritedProperties)
    b = create_schema_org_model(type_=ElectricianProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Electrician.schema()


def EUEnergyEfficiencyCategoryE_test():
    from schorg.EUEnergyEfficiencyCategoryE import EUEnergyEfficiencyCategoryEInheritedProperties
    from schorg.EUEnergyEfficiencyCategoryE import EUEnergyEfficiencyCategoryEProperties
    from schorg.EUEnergyEfficiencyCategoryE import AllProperties
    from schorg.EUEnergyEfficiencyCategoryE import create_schema_org_model
    from schorg.EUEnergyEfficiencyCategoryE import EUEnergyEfficiencyCategoryE

    a = create_schema_org_model(type_=EUEnergyEfficiencyCategoryEInheritedProperties)
    b = create_schema_org_model(type_=EUEnergyEfficiencyCategoryEProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    EUEnergyEfficiencyCategoryE.schema()


def BusinessEntityType_test():
    from schorg.BusinessEntityType import BusinessEntityTypeInheritedProperties
    from schorg.BusinessEntityType import BusinessEntityTypeProperties
    from schorg.BusinessEntityType import AllProperties
    from schorg.BusinessEntityType import create_schema_org_model
    from schorg.BusinessEntityType import BusinessEntityType

    a = create_schema_org_model(type_=BusinessEntityTypeInheritedProperties)
    b = create_schema_org_model(type_=BusinessEntityTypeProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    BusinessEntityType.schema()


def ReturnAction_test():
    from schorg.ReturnAction import ReturnActionInheritedProperties
    from schorg.ReturnAction import ReturnActionProperties
    from schorg.ReturnAction import AllProperties
    from schorg.ReturnAction import create_schema_org_model
    from schorg.ReturnAction import ReturnAction

    a = create_schema_org_model(type_=ReturnActionInheritedProperties)
    b = create_schema_org_model(type_=ReturnActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ReturnAction.schema()


def PerformanceRole_test():
    from schorg.PerformanceRole import PerformanceRoleInheritedProperties
    from schorg.PerformanceRole import PerformanceRoleProperties
    from schorg.PerformanceRole import AllProperties
    from schorg.PerformanceRole import create_schema_org_model
    from schorg.PerformanceRole import PerformanceRole

    a = create_schema_org_model(type_=PerformanceRoleInheritedProperties)
    b = create_schema_org_model(type_=PerformanceRoleProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    PerformanceRole.schema()


def Protein_test():
    from schorg.Protein import ProteinInheritedProperties
    from schorg.Protein import ProteinProperties
    from schorg.Protein import AllProperties
    from schorg.Protein import create_schema_org_model
    from schorg.Protein import Protein

    a = create_schema_org_model(type_=ProteinInheritedProperties)
    b = create_schema_org_model(type_=ProteinProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Protein.schema()


def TrackAction_test():
    from schorg.TrackAction import TrackActionInheritedProperties
    from schorg.TrackAction import TrackActionProperties
    from schorg.TrackAction import AllProperties
    from schorg.TrackAction import create_schema_org_model
    from schorg.TrackAction import TrackAction

    a = create_schema_org_model(type_=TrackActionInheritedProperties)
    b = create_schema_org_model(type_=TrackActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    TrackAction.schema()


def DeliveryChargeSpecification_test():
    from schorg.DeliveryChargeSpecification import DeliveryChargeSpecificationInheritedProperties
    from schorg.DeliveryChargeSpecification import DeliveryChargeSpecificationProperties
    from schorg.DeliveryChargeSpecification import AllProperties
    from schorg.DeliveryChargeSpecification import create_schema_org_model
    from schorg.DeliveryChargeSpecification import DeliveryChargeSpecification

    a = create_schema_org_model(type_=DeliveryChargeSpecificationInheritedProperties)
    b = create_schema_org_model(type_=DeliveryChargeSpecificationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    DeliveryChargeSpecification.schema()


def PublicationIssue_test():
    from schorg.PublicationIssue import PublicationIssueInheritedProperties
    from schorg.PublicationIssue import PublicationIssueProperties
    from schorg.PublicationIssue import AllProperties
    from schorg.PublicationIssue import create_schema_org_model
    from schorg.PublicationIssue import PublicationIssue

    a = create_schema_org_model(type_=PublicationIssueInheritedProperties)
    b = create_schema_org_model(type_=PublicationIssueProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    PublicationIssue.schema()


def ComicIssue_test():
    from schorg.ComicIssue import ComicIssueInheritedProperties
    from schorg.ComicIssue import ComicIssueProperties
    from schorg.ComicIssue import AllProperties
    from schorg.ComicIssue import create_schema_org_model
    from schorg.ComicIssue import ComicIssue

    a = create_schema_org_model(type_=ComicIssueInheritedProperties)
    b = create_schema_org_model(type_=ComicIssueProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ComicIssue.schema()


def AgreeAction_test():
    from schorg.AgreeAction import AgreeActionInheritedProperties
    from schorg.AgreeAction import AgreeActionProperties
    from schorg.AgreeAction import AllProperties
    from schorg.AgreeAction import create_schema_org_model
    from schorg.AgreeAction import AgreeAction

    a = create_schema_org_model(type_=AgreeActionInheritedProperties)
    b = create_schema_org_model(type_=AgreeActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    AgreeAction.schema()


def ActiveNotRecruiting_test():
    from schorg.ActiveNotRecruiting import ActiveNotRecruitingInheritedProperties
    from schorg.ActiveNotRecruiting import ActiveNotRecruitingProperties
    from schorg.ActiveNotRecruiting import AllProperties
    from schorg.ActiveNotRecruiting import create_schema_org_model
    from schorg.ActiveNotRecruiting import ActiveNotRecruiting

    a = create_schema_org_model(type_=ActiveNotRecruitingInheritedProperties)
    b = create_schema_org_model(type_=ActiveNotRecruitingProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ActiveNotRecruiting.schema()


def Tuesday_test():
    from schorg.Tuesday import TuesdayInheritedProperties
    from schorg.Tuesday import TuesdayProperties
    from schorg.Tuesday import AllProperties
    from schorg.Tuesday import create_schema_org_model
    from schorg.Tuesday import Tuesday

    a = create_schema_org_model(type_=TuesdayInheritedProperties)
    b = create_schema_org_model(type_=TuesdayProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Tuesday.schema()


def Protozoa_test():
    from schorg.Protozoa import ProtozoaInheritedProperties
    from schorg.Protozoa import ProtozoaProperties
    from schorg.Protozoa import AllProperties
    from schorg.Protozoa import create_schema_org_model
    from schorg.Protozoa import Protozoa

    a = create_schema_org_model(type_=ProtozoaInheritedProperties)
    b = create_schema_org_model(type_=ProtozoaProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Protozoa.schema()


def LeisureTimeActivity_test():
    from schorg.LeisureTimeActivity import LeisureTimeActivityInheritedProperties
    from schorg.LeisureTimeActivity import LeisureTimeActivityProperties
    from schorg.LeisureTimeActivity import AllProperties
    from schorg.LeisureTimeActivity import create_schema_org_model
    from schorg.LeisureTimeActivity import LeisureTimeActivity

    a = create_schema_org_model(type_=LeisureTimeActivityInheritedProperties)
    b = create_schema_org_model(type_=LeisureTimeActivityProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    LeisureTimeActivity.schema()


def AcceptAction_test():
    from schorg.AcceptAction import AcceptActionInheritedProperties
    from schorg.AcceptAction import AcceptActionProperties
    from schorg.AcceptAction import AllProperties
    from schorg.AcceptAction import create_schema_org_model
    from schorg.AcceptAction import AcceptAction

    a = create_schema_org_model(type_=AcceptActionInheritedProperties)
    b = create_schema_org_model(type_=AcceptActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    AcceptAction.schema()


def Nonprofit501c27_test():
    from schorg.Nonprofit501c27 import Nonprofit501c27InheritedProperties
    from schorg.Nonprofit501c27 import Nonprofit501c27Properties
    from schorg.Nonprofit501c27 import AllProperties
    from schorg.Nonprofit501c27 import create_schema_org_model
    from schorg.Nonprofit501c27 import Nonprofit501c27

    a = create_schema_org_model(type_=Nonprofit501c27InheritedProperties)
    b = create_schema_org_model(type_=Nonprofit501c27Properties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Nonprofit501c27.schema()


def AlcoholConsideration_test():
    from schorg.AlcoholConsideration import AlcoholConsiderationInheritedProperties
    from schorg.AlcoholConsideration import AlcoholConsiderationProperties
    from schorg.AlcoholConsideration import AllProperties
    from schorg.AlcoholConsideration import create_schema_org_model
    from schorg.AlcoholConsideration import AlcoholConsideration

    a = create_schema_org_model(type_=AlcoholConsiderationInheritedProperties)
    b = create_schema_org_model(type_=AlcoholConsiderationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    AlcoholConsideration.schema()


def CDCPMDRecord_test():
    from schorg.CDCPMDRecord import CDCPMDRecordInheritedProperties
    from schorg.CDCPMDRecord import CDCPMDRecordProperties
    from schorg.CDCPMDRecord import AllProperties
    from schorg.CDCPMDRecord import create_schema_org_model
    from schorg.CDCPMDRecord import CDCPMDRecord

    a = create_schema_org_model(type_=CDCPMDRecordInheritedProperties)
    b = create_schema_org_model(type_=CDCPMDRecordProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    CDCPMDRecord.schema()


def MensClothingStore_test():
    from schorg.MensClothingStore import MensClothingStoreInheritedProperties
    from schorg.MensClothingStore import MensClothingStoreProperties
    from schorg.MensClothingStore import AllProperties
    from schorg.MensClothingStore import create_schema_org_model
    from schorg.MensClothingStore import MensClothingStore

    a = create_schema_org_model(type_=MensClothingStoreInheritedProperties)
    b = create_schema_org_model(type_=MensClothingStoreProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MensClothingStore.schema()


def CollegeOrUniversity_test():
    from schorg.CollegeOrUniversity import CollegeOrUniversityInheritedProperties
    from schorg.CollegeOrUniversity import CollegeOrUniversityProperties
    from schorg.CollegeOrUniversity import AllProperties
    from schorg.CollegeOrUniversity import create_schema_org_model
    from schorg.CollegeOrUniversity import CollegeOrUniversity

    a = create_schema_org_model(type_=CollegeOrUniversityInheritedProperties)
    b = create_schema_org_model(type_=CollegeOrUniversityProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    CollegeOrUniversity.schema()


def SheetMusic_test():
    from schorg.SheetMusic import SheetMusicInheritedProperties
    from schorg.SheetMusic import SheetMusicProperties
    from schorg.SheetMusic import AllProperties
    from schorg.SheetMusic import create_schema_org_model
    from schorg.SheetMusic import SheetMusic

    a = create_schema_org_model(type_=SheetMusicInheritedProperties)
    b = create_schema_org_model(type_=SheetMusicProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    SheetMusic.schema()


def WPAdBlock_test():
    from schorg.WPAdBlock import WPAdBlockInheritedProperties
    from schorg.WPAdBlock import WPAdBlockProperties
    from schorg.WPAdBlock import AllProperties
    from schorg.WPAdBlock import create_schema_org_model
    from schorg.WPAdBlock import WPAdBlock

    a = create_schema_org_model(type_=WPAdBlockInheritedProperties)
    b = create_schema_org_model(type_=WPAdBlockProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    WPAdBlock.schema()


def UserBlocks_test():
    from schorg.UserBlocks import UserBlocksInheritedProperties
    from schorg.UserBlocks import UserBlocksProperties
    from schorg.UserBlocks import AllProperties
    from schorg.UserBlocks import create_schema_org_model
    from schorg.UserBlocks import UserBlocks

    a = create_schema_org_model(type_=UserBlocksInheritedProperties)
    b = create_schema_org_model(type_=UserBlocksProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    UserBlocks.schema()


def SeaBodyOfWater_test():
    from schorg.SeaBodyOfWater import SeaBodyOfWaterInheritedProperties
    from schorg.SeaBodyOfWater import SeaBodyOfWaterProperties
    from schorg.SeaBodyOfWater import AllProperties
    from schorg.SeaBodyOfWater import create_schema_org_model
    from schorg.SeaBodyOfWater import SeaBodyOfWater

    a = create_schema_org_model(type_=SeaBodyOfWaterInheritedProperties)
    b = create_schema_org_model(type_=SeaBodyOfWaterProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    SeaBodyOfWater.schema()


def WearableMeasurementWidth_test():
    from schorg.WearableMeasurementWidth import WearableMeasurementWidthInheritedProperties
    from schorg.WearableMeasurementWidth import WearableMeasurementWidthProperties
    from schorg.WearableMeasurementWidth import AllProperties
    from schorg.WearableMeasurementWidth import create_schema_org_model
    from schorg.WearableMeasurementWidth import WearableMeasurementWidth

    a = create_schema_org_model(type_=WearableMeasurementWidthInheritedProperties)
    b = create_schema_org_model(type_=WearableMeasurementWidthProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    WearableMeasurementWidth.schema()


def VisualArtsEvent_test():
    from schorg.VisualArtsEvent import VisualArtsEventInheritedProperties
    from schorg.VisualArtsEvent import VisualArtsEventProperties
    from schorg.VisualArtsEvent import AllProperties
    from schorg.VisualArtsEvent import create_schema_org_model
    from schorg.VisualArtsEvent import VisualArtsEvent

    a = create_schema_org_model(type_=VisualArtsEventInheritedProperties)
    b = create_schema_org_model(type_=VisualArtsEventProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    VisualArtsEvent.schema()


def Language_test():
    from schorg.Language import LanguageInheritedProperties
    from schorg.Language import LanguageProperties
    from schorg.Language import AllProperties
    from schorg.Language import create_schema_org_model
    from schorg.Language import Language

    a = create_schema_org_model(type_=LanguageInheritedProperties)
    b = create_schema_org_model(type_=LanguageProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Language.schema()


def TollFree_test():
    from schorg.TollFree import TollFreeInheritedProperties
    from schorg.TollFree import TollFreeProperties
    from schorg.TollFree import AllProperties
    from schorg.TollFree import create_schema_org_model
    from schorg.TollFree import TollFree

    a = create_schema_org_model(type_=TollFreeInheritedProperties)
    b = create_schema_org_model(type_=TollFreeProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    TollFree.schema()


def PathologyTest_test():
    from schorg.PathologyTest import PathologyTestInheritedProperties
    from schorg.PathologyTest import PathologyTestProperties
    from schorg.PathologyTest import AllProperties
    from schorg.PathologyTest import create_schema_org_model
    from schorg.PathologyTest import PathologyTest

    a = create_schema_org_model(type_=PathologyTestInheritedProperties)
    b = create_schema_org_model(type_=PathologyTestProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    PathologyTest.schema()


def DrivingSchoolVehicleUsage_test():
    from schorg.DrivingSchoolVehicleUsage import DrivingSchoolVehicleUsageInheritedProperties
    from schorg.DrivingSchoolVehicleUsage import DrivingSchoolVehicleUsageProperties
    from schorg.DrivingSchoolVehicleUsage import AllProperties
    from schorg.DrivingSchoolVehicleUsage import create_schema_org_model
    from schorg.DrivingSchoolVehicleUsage import DrivingSchoolVehicleUsage

    a = create_schema_org_model(type_=DrivingSchoolVehicleUsageInheritedProperties)
    b = create_schema_org_model(type_=DrivingSchoolVehicleUsageProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    DrivingSchoolVehicleUsage.schema()


def VideoGameSeries_test():
    from schorg.VideoGameSeries import VideoGameSeriesInheritedProperties
    from schorg.VideoGameSeries import VideoGameSeriesProperties
    from schorg.VideoGameSeries import AllProperties
    from schorg.VideoGameSeries import create_schema_org_model
    from schorg.VideoGameSeries import VideoGameSeries

    a = create_schema_org_model(type_=VideoGameSeriesInheritedProperties)
    b = create_schema_org_model(type_=VideoGameSeriesProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    VideoGameSeries.schema()


def OnDemandEvent_test():
    from schorg.OnDemandEvent import OnDemandEventInheritedProperties
    from schorg.OnDemandEvent import OnDemandEventProperties
    from schorg.OnDemandEvent import AllProperties
    from schorg.OnDemandEvent import create_schema_org_model
    from schorg.OnDemandEvent import OnDemandEvent

    a = create_schema_org_model(type_=OnDemandEventInheritedProperties)
    b = create_schema_org_model(type_=OnDemandEventProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    OnDemandEvent.schema()


def Pulmonary_test():
    from schorg.Pulmonary import PulmonaryInheritedProperties
    from schorg.Pulmonary import PulmonaryProperties
    from schorg.Pulmonary import AllProperties
    from schorg.Pulmonary import create_schema_org_model
    from schorg.Pulmonary import Pulmonary

    a = create_schema_org_model(type_=PulmonaryInheritedProperties)
    b = create_schema_org_model(type_=PulmonaryProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Pulmonary.schema()


def HealthClub_test():
    from schorg.HealthClub import HealthClubInheritedProperties
    from schorg.HealthClub import HealthClubProperties
    from schorg.HealthClub import AllProperties
    from schorg.HealthClub import create_schema_org_model
    from schorg.HealthClub import HealthClub

    a = create_schema_org_model(type_=HealthClubInheritedProperties)
    b = create_schema_org_model(type_=HealthClubProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    HealthClub.schema()


def StagedContent_test():
    from schorg.StagedContent import StagedContentInheritedProperties
    from schorg.StagedContent import StagedContentProperties
    from schorg.StagedContent import AllProperties
    from schorg.StagedContent import create_schema_org_model
    from schorg.StagedContent import StagedContent

    a = create_schema_org_model(type_=StagedContentInheritedProperties)
    b = create_schema_org_model(type_=StagedContentProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    StagedContent.schema()


def Nonprofit501c9_test():
    from schorg.Nonprofit501c9 import Nonprofit501c9InheritedProperties
    from schorg.Nonprofit501c9 import Nonprofit501c9Properties
    from schorg.Nonprofit501c9 import AllProperties
    from schorg.Nonprofit501c9 import create_schema_org_model
    from schorg.Nonprofit501c9 import Nonprofit501c9

    a = create_schema_org_model(type_=Nonprofit501c9InheritedProperties)
    b = create_schema_org_model(type_=Nonprofit501c9Properties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Nonprofit501c9.schema()


def FastFoodRestaurant_test():
    from schorg.FastFoodRestaurant import FastFoodRestaurantInheritedProperties
    from schorg.FastFoodRestaurant import FastFoodRestaurantProperties
    from schorg.FastFoodRestaurant import AllProperties
    from schorg.FastFoodRestaurant import create_schema_org_model
    from schorg.FastFoodRestaurant import FastFoodRestaurant

    a = create_schema_org_model(type_=FastFoodRestaurantInheritedProperties)
    b = create_schema_org_model(type_=FastFoodRestaurantProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    FastFoodRestaurant.schema()


def BusinessFunction_test():
    from schorg.BusinessFunction import BusinessFunctionInheritedProperties
    from schorg.BusinessFunction import BusinessFunctionProperties
    from schorg.BusinessFunction import AllProperties
    from schorg.BusinessFunction import create_schema_org_model
    from schorg.BusinessFunction import BusinessFunction

    a = create_schema_org_model(type_=BusinessFunctionInheritedProperties)
    b = create_schema_org_model(type_=BusinessFunctionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    BusinessFunction.schema()


def Dermatologic_test():
    from schorg.Dermatologic import DermatologicInheritedProperties
    from schorg.Dermatologic import DermatologicProperties
    from schorg.Dermatologic import AllProperties
    from schorg.Dermatologic import create_schema_org_model
    from schorg.Dermatologic import Dermatologic

    a = create_schema_org_model(type_=DermatologicInheritedProperties)
    b = create_schema_org_model(type_=DermatologicProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Dermatologic.schema()


def PaymentDue_test():
    from schorg.PaymentDue import PaymentDueInheritedProperties
    from schorg.PaymentDue import PaymentDueProperties
    from schorg.PaymentDue import AllProperties
    from schorg.PaymentDue import create_schema_org_model
    from schorg.PaymentDue import PaymentDue

    a = create_schema_org_model(type_=PaymentDueInheritedProperties)
    b = create_schema_org_model(type_=PaymentDueProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    PaymentDue.schema()


def DJMixAlbum_test():
    from schorg.DJMixAlbum import DJMixAlbumInheritedProperties
    from schorg.DJMixAlbum import DJMixAlbumProperties
    from schorg.DJMixAlbum import AllProperties
    from schorg.DJMixAlbum import create_schema_org_model
    from schorg.DJMixAlbum import DJMixAlbum

    a = create_schema_org_model(type_=DJMixAlbumInheritedProperties)
    b = create_schema_org_model(type_=DJMixAlbumProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    DJMixAlbum.schema()


def URL_test():
    from schorg.URL import URLInheritedProperties
    from schorg.URL import URLProperties
    from schorg.URL import AllProperties
    from schorg.URL import create_schema_org_model
    from schorg.URL import URL

    a = create_schema_org_model(type_=URLInheritedProperties)
    b = create_schema_org_model(type_=URLProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    URL.schema()


def EducationalAudience_test():
    from schorg.EducationalAudience import EducationalAudienceInheritedProperties
    from schorg.EducationalAudience import EducationalAudienceProperties
    from schorg.EducationalAudience import AllProperties
    from schorg.EducationalAudience import create_schema_org_model
    from schorg.EducationalAudience import EducationalAudience

    a = create_schema_org_model(type_=EducationalAudienceInheritedProperties)
    b = create_schema_org_model(type_=EducationalAudienceProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    EducationalAudience.schema()


def GamePlayMode_test():
    from schorg.GamePlayMode import GamePlayModeInheritedProperties
    from schorg.GamePlayMode import GamePlayModeProperties
    from schorg.GamePlayMode import AllProperties
    from schorg.GamePlayMode import create_schema_org_model
    from schorg.GamePlayMode import GamePlayMode

    a = create_schema_org_model(type_=GamePlayModeInheritedProperties)
    b = create_schema_org_model(type_=GamePlayModeProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    GamePlayMode.schema()


def SinglePlayer_test():
    from schorg.SinglePlayer import SinglePlayerInheritedProperties
    from schorg.SinglePlayer import SinglePlayerProperties
    from schorg.SinglePlayer import AllProperties
    from schorg.SinglePlayer import create_schema_org_model
    from schorg.SinglePlayer import SinglePlayer

    a = create_schema_org_model(type_=SinglePlayerInheritedProperties)
    b = create_schema_org_model(type_=SinglePlayerProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    SinglePlayer.schema()


def HealthCare_test():
    from schorg.HealthCare import HealthCareInheritedProperties
    from schorg.HealthCare import HealthCareProperties
    from schorg.HealthCare import AllProperties
    from schorg.HealthCare import create_schema_org_model
    from schorg.HealthCare import HealthCare

    a = create_schema_org_model(type_=HealthCareInheritedProperties)
    b = create_schema_org_model(type_=HealthCareProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    HealthCare.schema()


def PreventionHealthAspect_test():
    from schorg.PreventionHealthAspect import PreventionHealthAspectInheritedProperties
    from schorg.PreventionHealthAspect import PreventionHealthAspectProperties
    from schorg.PreventionHealthAspect import AllProperties
    from schorg.PreventionHealthAspect import create_schema_org_model
    from schorg.PreventionHealthAspect import PreventionHealthAspect

    a = create_schema_org_model(type_=PreventionHealthAspectInheritedProperties)
    b = create_schema_org_model(type_=PreventionHealthAspectProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    PreventionHealthAspect.schema()


def DepartAction_test():
    from schorg.DepartAction import DepartActionInheritedProperties
    from schorg.DepartAction import DepartActionProperties
    from schorg.DepartAction import AllProperties
    from schorg.DepartAction import create_schema_org_model
    from schorg.DepartAction import DepartAction

    a = create_schema_org_model(type_=DepartActionInheritedProperties)
    b = create_schema_org_model(type_=DepartActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    DepartAction.schema()


def EnergyConsumptionDetails_test():
    from schorg.EnergyConsumptionDetails import EnergyConsumptionDetailsInheritedProperties
    from schorg.EnergyConsumptionDetails import EnergyConsumptionDetailsProperties
    from schorg.EnergyConsumptionDetails import AllProperties
    from schorg.EnergyConsumptionDetails import create_schema_org_model
    from schorg.EnergyConsumptionDetails import EnergyConsumptionDetails

    a = create_schema_org_model(type_=EnergyConsumptionDetailsInheritedProperties)
    b = create_schema_org_model(type_=EnergyConsumptionDetailsProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    EnergyConsumptionDetails.schema()


def Painting_test():
    from schorg.Painting import PaintingInheritedProperties
    from schorg.Painting import PaintingProperties
    from schorg.Painting import AllProperties
    from schorg.Painting import create_schema_org_model
    from schorg.Painting import Painting

    a = create_schema_org_model(type_=PaintingInheritedProperties)
    b = create_schema_org_model(type_=PaintingProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Painting.schema()


def MultiPlayer_test():
    from schorg.MultiPlayer import MultiPlayerInheritedProperties
    from schorg.MultiPlayer import MultiPlayerProperties
    from schorg.MultiPlayer import AllProperties
    from schorg.MultiPlayer import create_schema_org_model
    from schorg.MultiPlayer import MultiPlayer

    a = create_schema_org_model(type_=MultiPlayerInheritedProperties)
    b = create_schema_org_model(type_=MultiPlayerProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MultiPlayer.schema()


def CreditCard_test():
    from schorg.CreditCard import CreditCardInheritedProperties
    from schorg.CreditCard import CreditCardProperties
    from schorg.CreditCard import AllProperties
    from schorg.CreditCard import create_schema_org_model
    from schorg.CreditCard import CreditCard

    a = create_schema_org_model(type_=CreditCardInheritedProperties)
    b = create_schema_org_model(type_=CreditCardProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    CreditCard.schema()


def LimitedAvailability_test():
    from schorg.LimitedAvailability import LimitedAvailabilityInheritedProperties
    from schorg.LimitedAvailability import LimitedAvailabilityProperties
    from schorg.LimitedAvailability import AllProperties
    from schorg.LimitedAvailability import create_schema_org_model
    from schorg.LimitedAvailability import LimitedAvailability

    a = create_schema_org_model(type_=LimitedAvailabilityInheritedProperties)
    b = create_schema_org_model(type_=LimitedAvailabilityProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    LimitedAvailability.schema()


def VeganDiet_test():
    from schorg.VeganDiet import VeganDietInheritedProperties
    from schorg.VeganDiet import VeganDietProperties
    from schorg.VeganDiet import AllProperties
    from schorg.VeganDiet import create_schema_org_model
    from schorg.VeganDiet import VeganDiet

    a = create_schema_org_model(type_=VeganDietInheritedProperties)
    b = create_schema_org_model(type_=VeganDietProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    VeganDiet.schema()


def ApplyAction_test():
    from schorg.ApplyAction import ApplyActionInheritedProperties
    from schorg.ApplyAction import ApplyActionProperties
    from schorg.ApplyAction import AllProperties
    from schorg.ApplyAction import create_schema_org_model
    from schorg.ApplyAction import ApplyAction

    a = create_schema_org_model(type_=ApplyActionInheritedProperties)
    b = create_schema_org_model(type_=ApplyActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ApplyAction.schema()


def ParkingMap_test():
    from schorg.ParkingMap import ParkingMapInheritedProperties
    from schorg.ParkingMap import ParkingMapProperties
    from schorg.ParkingMap import AllProperties
    from schorg.ParkingMap import create_schema_org_model
    from schorg.ParkingMap import ParkingMap

    a = create_schema_org_model(type_=ParkingMapInheritedProperties)
    b = create_schema_org_model(type_=ParkingMapProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ParkingMap.schema()


def GiveAction_test():
    from schorg.GiveAction import GiveActionInheritedProperties
    from schorg.GiveAction import GiveActionProperties
    from schorg.GiveAction import AllProperties
    from schorg.GiveAction import create_schema_org_model
    from schorg.GiveAction import GiveAction

    a = create_schema_org_model(type_=GiveActionInheritedProperties)
    b = create_schema_org_model(type_=GiveActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    GiveAction.schema()


def Ayurvedic_test():
    from schorg.Ayurvedic import AyurvedicInheritedProperties
    from schorg.Ayurvedic import AyurvedicProperties
    from schorg.Ayurvedic import AllProperties
    from schorg.Ayurvedic import create_schema_org_model
    from schorg.Ayurvedic import Ayurvedic

    a = create_schema_org_model(type_=AyurvedicInheritedProperties)
    b = create_schema_org_model(type_=AyurvedicProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Ayurvedic.schema()


def WearableSizeGroupExtraTall_test():
    from schorg.WearableSizeGroupExtraTall import WearableSizeGroupExtraTallInheritedProperties
    from schorg.WearableSizeGroupExtraTall import WearableSizeGroupExtraTallProperties
    from schorg.WearableSizeGroupExtraTall import AllProperties
    from schorg.WearableSizeGroupExtraTall import create_schema_org_model
    from schorg.WearableSizeGroupExtraTall import WearableSizeGroupExtraTall

    a = create_schema_org_model(type_=WearableSizeGroupExtraTallInheritedProperties)
    b = create_schema_org_model(type_=WearableSizeGroupExtraTallProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    WearableSizeGroupExtraTall.schema()


def TVSeries_test():
    from schorg.TVSeries import TVSeriesInheritedProperties
    from schorg.TVSeries import TVSeriesProperties
    from schorg.TVSeries import AllProperties
    from schorg.TVSeries import create_schema_org_model
    from schorg.TVSeries import TVSeries

    a = create_schema_org_model(type_=TVSeriesInheritedProperties)
    b = create_schema_org_model(type_=TVSeriesProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    TVSeries.schema()


def FloorPlan_test():
    from schorg.FloorPlan import FloorPlanInheritedProperties
    from schorg.FloorPlan import FloorPlanProperties
    from schorg.FloorPlan import AllProperties
    from schorg.FloorPlan import create_schema_org_model
    from schorg.FloorPlan import FloorPlan

    a = create_schema_org_model(type_=FloorPlanInheritedProperties)
    b = create_schema_org_model(type_=FloorPlanProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    FloorPlan.schema()


def NotInForce_test():
    from schorg.NotInForce import NotInForceInheritedProperties
    from schorg.NotInForce import NotInForceProperties
    from schorg.NotInForce import AllProperties
    from schorg.NotInForce import create_schema_org_model
    from schorg.NotInForce import NotInForce

    a = create_schema_org_model(type_=NotInForceInheritedProperties)
    b = create_schema_org_model(type_=NotInForceProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    NotInForce.schema()


def Radiography_test():
    from schorg.Radiography import RadiographyInheritedProperties
    from schorg.Radiography import RadiographyProperties
    from schorg.Radiography import AllProperties
    from schorg.Radiography import create_schema_org_model
    from schorg.Radiography import Radiography

    a = create_schema_org_model(type_=RadiographyInheritedProperties)
    b = create_schema_org_model(type_=RadiographyProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Radiography.schema()


def CoOp_test():
    from schorg.CoOp import CoOpInheritedProperties
    from schorg.CoOp import CoOpProperties
    from schorg.CoOp import AllProperties
    from schorg.CoOp import create_schema_org_model
    from schorg.CoOp import CoOp

    a = create_schema_org_model(type_=CoOpInheritedProperties)
    b = create_schema_org_model(type_=CoOpProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    CoOp.schema()


def _3DModel_test():
    from schorg._3DModel import _3DModelInheritedProperties
    from schorg._3DModel import _3DModelProperties
    from schorg._3DModel import AllProperties
    from schorg._3DModel import create_schema_org_model
    from schorg._3DModel import _3DModel

    a = create_schema_org_model(type_=_3DModelInheritedProperties)
    b = create_schema_org_model(type_=_3DModelProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    _3DModel.schema()


def BackgroundNewsArticle_test():
    from schorg.BackgroundNewsArticle import BackgroundNewsArticleInheritedProperties
    from schorg.BackgroundNewsArticle import BackgroundNewsArticleProperties
    from schorg.BackgroundNewsArticle import AllProperties
    from schorg.BackgroundNewsArticle import create_schema_org_model
    from schorg.BackgroundNewsArticle import BackgroundNewsArticle

    a = create_schema_org_model(type_=BackgroundNewsArticleInheritedProperties)
    b = create_schema_org_model(type_=BackgroundNewsArticleProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    BackgroundNewsArticle.schema()


def Diet_test():
    from schorg.Diet import DietInheritedProperties
    from schorg.Diet import DietProperties
    from schorg.Diet import AllProperties
    from schorg.Diet import create_schema_org_model
    from schorg.Diet import Diet

    a = create_schema_org_model(type_=DietInheritedProperties)
    b = create_schema_org_model(type_=DietProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Diet.schema()


def House_test():
    from schorg.House import HouseInheritedProperties
    from schorg.House import HouseProperties
    from schorg.House import AllProperties
    from schorg.House import create_schema_org_model
    from schorg.House import House

    a = create_schema_org_model(type_=HouseInheritedProperties)
    b = create_schema_org_model(type_=HouseProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    House.schema()


def Course_test():
    from schorg.Course import CourseInheritedProperties
    from schorg.Course import CourseProperties
    from schorg.Course import AllProperties
    from schorg.Course import create_schema_org_model
    from schorg.Course import Course

    a = create_schema_org_model(type_=CourseInheritedProperties)
    b = create_schema_org_model(type_=CourseProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Course.schema()


def InStock_test():
    from schorg.InStock import InStockInheritedProperties
    from schorg.InStock import InStockProperties
    from schorg.InStock import AllProperties
    from schorg.InStock import create_schema_org_model
    from schorg.InStock import InStock

    a = create_schema_org_model(type_=InStockInheritedProperties)
    b = create_schema_org_model(type_=InStockProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    InStock.schema()


def SolveMathAction_test():
    from schorg.SolveMathAction import SolveMathActionInheritedProperties
    from schorg.SolveMathAction import SolveMathActionProperties
    from schorg.SolveMathAction import AllProperties
    from schorg.SolveMathAction import create_schema_org_model
    from schorg.SolveMathAction import SolveMathAction

    a = create_schema_org_model(type_=SolveMathActionInheritedProperties)
    b = create_schema_org_model(type_=SolveMathActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    SolveMathAction.schema()


def Volcano_test():
    from schorg.Volcano import VolcanoInheritedProperties
    from schorg.Volcano import VolcanoProperties
    from schorg.Volcano import AllProperties
    from schorg.Volcano import create_schema_org_model
    from schorg.Volcano import Volcano

    a = create_schema_org_model(type_=VolcanoInheritedProperties)
    b = create_schema_org_model(type_=VolcanoProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Volcano.schema()


def RentalVehicleUsage_test():
    from schorg.RentalVehicleUsage import RentalVehicleUsageInheritedProperties
    from schorg.RentalVehicleUsage import RentalVehicleUsageProperties
    from schorg.RentalVehicleUsage import AllProperties
    from schorg.RentalVehicleUsage import create_schema_org_model
    from schorg.RentalVehicleUsage import RentalVehicleUsage

    a = create_schema_org_model(type_=RentalVehicleUsageInheritedProperties)
    b = create_schema_org_model(type_=RentalVehicleUsageProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    RentalVehicleUsage.schema()


def ViewAction_test():
    from schorg.ViewAction import ViewActionInheritedProperties
    from schorg.ViewAction import ViewActionProperties
    from schorg.ViewAction import AllProperties
    from schorg.ViewAction import create_schema_org_model
    from schorg.ViewAction import ViewAction

    a = create_schema_org_model(type_=ViewActionInheritedProperties)
    b = create_schema_org_model(type_=ViewActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ViewAction.schema()


def NonprofitANBI_test():
    from schorg.NonprofitANBI import NonprofitANBIInheritedProperties
    from schorg.NonprofitANBI import NonprofitANBIProperties
    from schorg.NonprofitANBI import AllProperties
    from schorg.NonprofitANBI import create_schema_org_model
    from schorg.NonprofitANBI import NonprofitANBI

    a = create_schema_org_model(type_=NonprofitANBIInheritedProperties)
    b = create_schema_org_model(type_=NonprofitANBIProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    NonprofitANBI.schema()


def Nonprofit501c22_test():
    from schorg.Nonprofit501c22 import Nonprofit501c22InheritedProperties
    from schorg.Nonprofit501c22 import Nonprofit501c22Properties
    from schorg.Nonprofit501c22 import AllProperties
    from schorg.Nonprofit501c22 import create_schema_org_model
    from schorg.Nonprofit501c22 import Nonprofit501c22

    a = create_schema_org_model(type_=Nonprofit501c22InheritedProperties)
    b = create_schema_org_model(type_=Nonprofit501c22Properties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Nonprofit501c22.schema()


def Clinician_test():
    from schorg.Clinician import ClinicianInheritedProperties
    from schorg.Clinician import ClinicianProperties
    from schorg.Clinician import AllProperties
    from schorg.Clinician import create_schema_org_model
    from schorg.Clinician import Clinician

    a = create_schema_org_model(type_=ClinicianInheritedProperties)
    b = create_schema_org_model(type_=ClinicianProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Clinician.schema()


def PawnShop_test():
    from schorg.PawnShop import PawnShopInheritedProperties
    from schorg.PawnShop import PawnShopProperties
    from schorg.PawnShop import AllProperties
    from schorg.PawnShop import create_schema_org_model
    from schorg.PawnShop import PawnShop

    a = create_schema_org_model(type_=PawnShopInheritedProperties)
    b = create_schema_org_model(type_=PawnShopProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    PawnShop.schema()


def DanceEvent_test():
    from schorg.DanceEvent import DanceEventInheritedProperties
    from schorg.DanceEvent import DanceEventProperties
    from schorg.DanceEvent import AllProperties
    from schorg.DanceEvent import create_schema_org_model
    from schorg.DanceEvent import DanceEvent

    a = create_schema_org_model(type_=DanceEventInheritedProperties)
    b = create_schema_org_model(type_=DanceEventProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    DanceEvent.schema()


def DefinedTermSet_test():
    from schorg.DefinedTermSet import DefinedTermSetInheritedProperties
    from schorg.DefinedTermSet import DefinedTermSetProperties
    from schorg.DefinedTermSet import AllProperties
    from schorg.DefinedTermSet import create_schema_org_model
    from schorg.DefinedTermSet import DefinedTermSet

    a = create_schema_org_model(type_=DefinedTermSetInheritedProperties)
    b = create_schema_org_model(type_=DefinedTermSetProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    DefinedTermSet.schema()


def CategoryCodeSet_test():
    from schorg.CategoryCodeSet import CategoryCodeSetInheritedProperties
    from schorg.CategoryCodeSet import CategoryCodeSetProperties
    from schorg.CategoryCodeSet import AllProperties
    from schorg.CategoryCodeSet import create_schema_org_model
    from schorg.CategoryCodeSet import CategoryCodeSet

    a = create_schema_org_model(type_=CategoryCodeSetInheritedProperties)
    b = create_schema_org_model(type_=CategoryCodeSetProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    CategoryCodeSet.schema()


def Nonprofit501k_test():
    from schorg.Nonprofit501k import Nonprofit501kInheritedProperties
    from schorg.Nonprofit501k import Nonprofit501kProperties
    from schorg.Nonprofit501k import AllProperties
    from schorg.Nonprofit501k import create_schema_org_model
    from schorg.Nonprofit501k import Nonprofit501k

    a = create_schema_org_model(type_=Nonprofit501kInheritedProperties)
    b = create_schema_org_model(type_=Nonprofit501kProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Nonprofit501k.schema()


def PregnancyHealthAspect_test():
    from schorg.PregnancyHealthAspect import PregnancyHealthAspectInheritedProperties
    from schorg.PregnancyHealthAspect import PregnancyHealthAspectProperties
    from schorg.PregnancyHealthAspect import AllProperties
    from schorg.PregnancyHealthAspect import create_schema_org_model
    from schorg.PregnancyHealthAspect import PregnancyHealthAspect

    a = create_schema_org_model(type_=PregnancyHealthAspectInheritedProperties)
    b = create_schema_org_model(type_=PregnancyHealthAspectProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    PregnancyHealthAspect.schema()


def MobileWebPlatform_test():
    from schorg.MobileWebPlatform import MobileWebPlatformInheritedProperties
    from schorg.MobileWebPlatform import MobileWebPlatformProperties
    from schorg.MobileWebPlatform import AllProperties
    from schorg.MobileWebPlatform import create_schema_org_model
    from schorg.MobileWebPlatform import MobileWebPlatform

    a = create_schema_org_model(type_=MobileWebPlatformInheritedProperties)
    b = create_schema_org_model(type_=MobileWebPlatformProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MobileWebPlatform.schema()


def ApprovedIndication_test():
    from schorg.ApprovedIndication import ApprovedIndicationInheritedProperties
    from schorg.ApprovedIndication import ApprovedIndicationProperties
    from schorg.ApprovedIndication import AllProperties
    from schorg.ApprovedIndication import create_schema_org_model
    from schorg.ApprovedIndication import ApprovedIndication

    a = create_schema_org_model(type_=ApprovedIndicationInheritedProperties)
    b = create_schema_org_model(type_=ApprovedIndicationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ApprovedIndication.schema()


def MedicalGuidelineContraindication_test():
    from schorg.MedicalGuidelineContraindication import MedicalGuidelineContraindicationInheritedProperties
    from schorg.MedicalGuidelineContraindication import MedicalGuidelineContraindicationProperties
    from schorg.MedicalGuidelineContraindication import AllProperties
    from schorg.MedicalGuidelineContraindication import create_schema_org_model
    from schorg.MedicalGuidelineContraindication import MedicalGuidelineContraindication

    a = create_schema_org_model(type_=MedicalGuidelineContraindicationInheritedProperties)
    b = create_schema_org_model(type_=MedicalGuidelineContraindicationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MedicalGuidelineContraindication.schema()


def GolfCourse_test():
    from schorg.GolfCourse import GolfCourseInheritedProperties
    from schorg.GolfCourse import GolfCourseProperties
    from schorg.GolfCourse import AllProperties
    from schorg.GolfCourse import create_schema_org_model
    from schorg.GolfCourse import GolfCourse

    a = create_schema_org_model(type_=GolfCourseInheritedProperties)
    b = create_schema_org_model(type_=GolfCourseProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    GolfCourse.schema()


def BefriendAction_test():
    from schorg.BefriendAction import BefriendActionInheritedProperties
    from schorg.BefriendAction import BefriendActionProperties
    from schorg.BefriendAction import AllProperties
    from schorg.BefriendAction import create_schema_org_model
    from schorg.BefriendAction import BefriendAction

    a = create_schema_org_model(type_=BefriendActionInheritedProperties)
    b = create_schema_org_model(type_=BefriendActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    BefriendAction.schema()


def Motel_test():
    from schorg.Motel import MotelInheritedProperties
    from schorg.Motel import MotelProperties
    from schorg.Motel import AllProperties
    from schorg.Motel import create_schema_org_model
    from schorg.Motel import Motel

    a = create_schema_org_model(type_=MotelInheritedProperties)
    b = create_schema_org_model(type_=MotelProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Motel.schema()


def EatAction_test():
    from schorg.EatAction import EatActionInheritedProperties
    from schorg.EatAction import EatActionProperties
    from schorg.EatAction import AllProperties
    from schorg.EatAction import create_schema_org_model
    from schorg.EatAction import EatAction

    a = create_schema_org_model(type_=EatActionInheritedProperties)
    b = create_schema_org_model(type_=EatActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    EatAction.schema()


def OrderProcessing_test():
    from schorg.OrderProcessing import OrderProcessingInheritedProperties
    from schorg.OrderProcessing import OrderProcessingProperties
    from schorg.OrderProcessing import AllProperties
    from schorg.OrderProcessing import create_schema_org_model
    from schorg.OrderProcessing import OrderProcessing

    a = create_schema_org_model(type_=OrderProcessingInheritedProperties)
    b = create_schema_org_model(type_=OrderProcessingProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    OrderProcessing.schema()


def FullRefund_test():
    from schorg.FullRefund import FullRefundInheritedProperties
    from schorg.FullRefund import FullRefundProperties
    from schorg.FullRefund import AllProperties
    from schorg.FullRefund import create_schema_org_model
    from schorg.FullRefund import FullRefund

    a = create_schema_org_model(type_=FullRefundInheritedProperties)
    b = create_schema_org_model(type_=FullRefundProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    FullRefund.schema()


def PreventionIndication_test():
    from schorg.PreventionIndication import PreventionIndicationInheritedProperties
    from schorg.PreventionIndication import PreventionIndicationProperties
    from schorg.PreventionIndication import AllProperties
    from schorg.PreventionIndication import create_schema_org_model
    from schorg.PreventionIndication import PreventionIndication

    a = create_schema_org_model(type_=PreventionIndicationInheritedProperties)
    b = create_schema_org_model(type_=PreventionIndicationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    PreventionIndication.schema()


def MolecularEntity_test():
    from schorg.MolecularEntity import MolecularEntityInheritedProperties
    from schorg.MolecularEntity import MolecularEntityProperties
    from schorg.MolecularEntity import AllProperties
    from schorg.MolecularEntity import create_schema_org_model
    from schorg.MolecularEntity import MolecularEntity

    a = create_schema_org_model(type_=MolecularEntityInheritedProperties)
    b = create_schema_org_model(type_=MolecularEntityProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MolecularEntity.schema()


def FAQPage_test():
    from schorg.FAQPage import FAQPageInheritedProperties
    from schorg.FAQPage import FAQPageProperties
    from schorg.FAQPage import AllProperties
    from schorg.FAQPage import create_schema_org_model
    from schorg.FAQPage import FAQPage

    a = create_schema_org_model(type_=FAQPageInheritedProperties)
    b = create_schema_org_model(type_=FAQPageProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    FAQPage.schema()


def BodyMeasurementInsideLeg_test():
    from schorg.BodyMeasurementInsideLeg import BodyMeasurementInsideLegInheritedProperties
    from schorg.BodyMeasurementInsideLeg import BodyMeasurementInsideLegProperties
    from schorg.BodyMeasurementInsideLeg import AllProperties
    from schorg.BodyMeasurementInsideLeg import create_schema_org_model
    from schorg.BodyMeasurementInsideLeg import BodyMeasurementInsideLeg

    a = create_schema_org_model(type_=BodyMeasurementInsideLegInheritedProperties)
    b = create_schema_org_model(type_=BodyMeasurementInsideLegProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    BodyMeasurementInsideLeg.schema()


def ReportageNewsArticle_test():
    from schorg.ReportageNewsArticle import ReportageNewsArticleInheritedProperties
    from schorg.ReportageNewsArticle import ReportageNewsArticleProperties
    from schorg.ReportageNewsArticle import AllProperties
    from schorg.ReportageNewsArticle import create_schema_org_model
    from schorg.ReportageNewsArticle import ReportageNewsArticle

    a = create_schema_org_model(type_=ReportageNewsArticleInheritedProperties)
    b = create_schema_org_model(type_=ReportageNewsArticleProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ReportageNewsArticle.schema()


def EUEnergyEfficiencyCategoryF_test():
    from schorg.EUEnergyEfficiencyCategoryF import EUEnergyEfficiencyCategoryFInheritedProperties
    from schorg.EUEnergyEfficiencyCategoryF import EUEnergyEfficiencyCategoryFProperties
    from schorg.EUEnergyEfficiencyCategoryF import AllProperties
    from schorg.EUEnergyEfficiencyCategoryF import create_schema_org_model
    from schorg.EUEnergyEfficiencyCategoryF import EUEnergyEfficiencyCategoryF

    a = create_schema_org_model(type_=EUEnergyEfficiencyCategoryFInheritedProperties)
    b = create_schema_org_model(type_=EUEnergyEfficiencyCategoryFProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    EUEnergyEfficiencyCategoryF.schema()


def TobaccoNicotineConsideration_test():
    from schorg.TobaccoNicotineConsideration import TobaccoNicotineConsiderationInheritedProperties
    from schorg.TobaccoNicotineConsideration import TobaccoNicotineConsiderationProperties
    from schorg.TobaccoNicotineConsideration import AllProperties
    from schorg.TobaccoNicotineConsideration import create_schema_org_model
    from schorg.TobaccoNicotineConsideration import TobaccoNicotineConsideration

    a = create_schema_org_model(type_=TobaccoNicotineConsiderationInheritedProperties)
    b = create_schema_org_model(type_=TobaccoNicotineConsiderationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    TobaccoNicotineConsideration.schema()


def MinimumAdvertisedPrice_test():
    from schorg.MinimumAdvertisedPrice import MinimumAdvertisedPriceInheritedProperties
    from schorg.MinimumAdvertisedPrice import MinimumAdvertisedPriceProperties
    from schorg.MinimumAdvertisedPrice import AllProperties
    from schorg.MinimumAdvertisedPrice import create_schema_org_model
    from schorg.MinimumAdvertisedPrice import MinimumAdvertisedPrice

    a = create_schema_org_model(type_=MinimumAdvertisedPriceInheritedProperties)
    b = create_schema_org_model(type_=MinimumAdvertisedPriceProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MinimumAdvertisedPrice.schema()


def CardiovascularExam_test():
    from schorg.CardiovascularExam import CardiovascularExamInheritedProperties
    from schorg.CardiovascularExam import CardiovascularExamProperties
    from schorg.CardiovascularExam import AllProperties
    from schorg.CardiovascularExam import create_schema_org_model
    from schorg.CardiovascularExam import CardiovascularExam

    a = create_schema_org_model(type_=CardiovascularExamInheritedProperties)
    b = create_schema_org_model(type_=CardiovascularExamProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    CardiovascularExam.schema()


def QuantitativeValue_test():
    from schorg.QuantitativeValue import QuantitativeValueInheritedProperties
    from schorg.QuantitativeValue import QuantitativeValueProperties
    from schorg.QuantitativeValue import AllProperties
    from schorg.QuantitativeValue import create_schema_org_model
    from schorg.QuantitativeValue import QuantitativeValue

    a = create_schema_org_model(type_=QuantitativeValueInheritedProperties)
    b = create_schema_org_model(type_=QuantitativeValueProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    QuantitativeValue.schema()


def WearableSizeSystemEurope_test():
    from schorg.WearableSizeSystemEurope import WearableSizeSystemEuropeInheritedProperties
    from schorg.WearableSizeSystemEurope import WearableSizeSystemEuropeProperties
    from schorg.WearableSizeSystemEurope import AllProperties
    from schorg.WearableSizeSystemEurope import create_schema_org_model
    from schorg.WearableSizeSystemEurope import WearableSizeSystemEurope

    a = create_schema_org_model(type_=WearableSizeSystemEuropeInheritedProperties)
    b = create_schema_org_model(type_=WearableSizeSystemEuropeProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    WearableSizeSystemEurope.schema()


def Blog_test():
    from schorg.Blog import BlogInheritedProperties
    from schorg.Blog import BlogProperties
    from schorg.Blog import AllProperties
    from schorg.Blog import create_schema_org_model
    from schorg.Blog import Blog

    a = create_schema_org_model(type_=BlogInheritedProperties)
    b = create_schema_org_model(type_=BlogProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Blog.schema()


def DeleteAction_test():
    from schorg.DeleteAction import DeleteActionInheritedProperties
    from schorg.DeleteAction import DeleteActionProperties
    from schorg.DeleteAction import AllProperties
    from schorg.DeleteAction import create_schema_org_model
    from schorg.DeleteAction import DeleteAction

    a = create_schema_org_model(type_=DeleteActionInheritedProperties)
    b = create_schema_org_model(type_=DeleteActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    DeleteAction.schema()


def BoardingPolicyType_test():
    from schorg.BoardingPolicyType import BoardingPolicyTypeInheritedProperties
    from schorg.BoardingPolicyType import BoardingPolicyTypeProperties
    from schorg.BoardingPolicyType import AllProperties
    from schorg.BoardingPolicyType import create_schema_org_model
    from schorg.BoardingPolicyType import BoardingPolicyType

    a = create_schema_org_model(type_=BoardingPolicyTypeInheritedProperties)
    b = create_schema_org_model(type_=BoardingPolicyTypeProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    BoardingPolicyType.schema()


def GroupBoardingPolicy_test():
    from schorg.GroupBoardingPolicy import GroupBoardingPolicyInheritedProperties
    from schorg.GroupBoardingPolicy import GroupBoardingPolicyProperties
    from schorg.GroupBoardingPolicy import AllProperties
    from schorg.GroupBoardingPolicy import create_schema_org_model
    from schorg.GroupBoardingPolicy import GroupBoardingPolicy

    a = create_schema_org_model(type_=GroupBoardingPolicyInheritedProperties)
    b = create_schema_org_model(type_=GroupBoardingPolicyProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    GroupBoardingPolicy.schema()


def BikeStore_test():
    from schorg.BikeStore import BikeStoreInheritedProperties
    from schorg.BikeStore import BikeStoreProperties
    from schorg.BikeStore import AllProperties
    from schorg.BikeStore import create_schema_org_model
    from schorg.BikeStore import BikeStore

    a = create_schema_org_model(type_=BikeStoreInheritedProperties)
    b = create_schema_org_model(type_=BikeStoreProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    BikeStore.schema()


def OnSitePickup_test():
    from schorg.OnSitePickup import OnSitePickupInheritedProperties
    from schorg.OnSitePickup import OnSitePickupProperties
    from schorg.OnSitePickup import AllProperties
    from schorg.OnSitePickup import create_schema_org_model
    from schorg.OnSitePickup import OnSitePickup

    a = create_schema_org_model(type_=OnSitePickupInheritedProperties)
    b = create_schema_org_model(type_=OnSitePickupProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    OnSitePickup.schema()


def HighSchool_test():
    from schorg.HighSchool import HighSchoolInheritedProperties
    from schorg.HighSchool import HighSchoolProperties
    from schorg.HighSchool import AllProperties
    from schorg.HighSchool import create_schema_org_model
    from schorg.HighSchool import HighSchool

    a = create_schema_org_model(type_=HighSchoolInheritedProperties)
    b = create_schema_org_model(type_=HighSchoolProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    HighSchool.schema()


def Synagogue_test():
    from schorg.Synagogue import SynagogueInheritedProperties
    from schorg.Synagogue import SynagogueProperties
    from schorg.Synagogue import AllProperties
    from schorg.Synagogue import create_schema_org_model
    from schorg.Synagogue import Synagogue

    a = create_schema_org_model(type_=SynagogueInheritedProperties)
    b = create_schema_org_model(type_=SynagogueProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Synagogue.schema()


def PalliativeProcedure_test():
    from schorg.PalliativeProcedure import PalliativeProcedureInheritedProperties
    from schorg.PalliativeProcedure import PalliativeProcedureProperties
    from schorg.PalliativeProcedure import AllProperties
    from schorg.PalliativeProcedure import create_schema_org_model
    from schorg.PalliativeProcedure import PalliativeProcedure

    a = create_schema_org_model(type_=PalliativeProcedureInheritedProperties)
    b = create_schema_org_model(type_=PalliativeProcedureProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    PalliativeProcedure.schema()


def Optician_test():
    from schorg.Optician import OpticianInheritedProperties
    from schorg.Optician import OpticianProperties
    from schorg.Optician import AllProperties
    from schorg.Optician import create_schema_org_model
    from schorg.Optician import Optician

    a = create_schema_org_model(type_=OpticianInheritedProperties)
    b = create_schema_org_model(type_=OpticianProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Optician.schema()


def TelevisionChannel_test():
    from schorg.TelevisionChannel import TelevisionChannelInheritedProperties
    from schorg.TelevisionChannel import TelevisionChannelProperties
    from schorg.TelevisionChannel import AllProperties
    from schorg.TelevisionChannel import create_schema_org_model
    from schorg.TelevisionChannel import TelevisionChannel

    a = create_schema_org_model(type_=TelevisionChannelInheritedProperties)
    b = create_schema_org_model(type_=TelevisionChannelProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    TelevisionChannel.schema()


def GenericWebPlatform_test():
    from schorg.GenericWebPlatform import GenericWebPlatformInheritedProperties
    from schorg.GenericWebPlatform import GenericWebPlatformProperties
    from schorg.GenericWebPlatform import AllProperties
    from schorg.GenericWebPlatform import create_schema_org_model
    from schorg.GenericWebPlatform import GenericWebPlatform

    a = create_schema_org_model(type_=GenericWebPlatformInheritedProperties)
    b = create_schema_org_model(type_=GenericWebPlatformProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    GenericWebPlatform.schema()


def PublicationVolume_test():
    from schorg.PublicationVolume import PublicationVolumeInheritedProperties
    from schorg.PublicationVolume import PublicationVolumeProperties
    from schorg.PublicationVolume import AllProperties
    from schorg.PublicationVolume import create_schema_org_model
    from schorg.PublicationVolume import PublicationVolume

    a = create_schema_org_model(type_=PublicationVolumeInheritedProperties)
    b = create_schema_org_model(type_=PublicationVolumeProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    PublicationVolume.schema()


def ShippingDeliveryTime_test():
    from schorg.ShippingDeliveryTime import ShippingDeliveryTimeInheritedProperties
    from schorg.ShippingDeliveryTime import ShippingDeliveryTimeProperties
    from schorg.ShippingDeliveryTime import AllProperties
    from schorg.ShippingDeliveryTime import create_schema_org_model
    from schorg.ShippingDeliveryTime import ShippingDeliveryTime

    a = create_schema_org_model(type_=ShippingDeliveryTimeInheritedProperties)
    b = create_schema_org_model(type_=ShippingDeliveryTimeProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ShippingDeliveryTime.schema()


def UnitPriceSpecification_test():
    from schorg.UnitPriceSpecification import UnitPriceSpecificationInheritedProperties
    from schorg.UnitPriceSpecification import UnitPriceSpecificationProperties
    from schorg.UnitPriceSpecification import AllProperties
    from schorg.UnitPriceSpecification import create_schema_org_model
    from schorg.UnitPriceSpecification import UnitPriceSpecification

    a = create_schema_org_model(type_=UnitPriceSpecificationInheritedProperties)
    b = create_schema_org_model(type_=UnitPriceSpecificationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    UnitPriceSpecification.schema()


def RadioClip_test():
    from schorg.RadioClip import RadioClipInheritedProperties
    from schorg.RadioClip import RadioClipProperties
    from schorg.RadioClip import AllProperties
    from schorg.RadioClip import create_schema_org_model
    from schorg.RadioClip import RadioClip

    a = create_schema_org_model(type_=RadioClipInheritedProperties)
    b = create_schema_org_model(type_=RadioClipProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    RadioClip.schema()


def Nonprofit501d_test():
    from schorg.Nonprofit501d import Nonprofit501dInheritedProperties
    from schorg.Nonprofit501d import Nonprofit501dProperties
    from schorg.Nonprofit501d import AllProperties
    from schorg.Nonprofit501d import create_schema_org_model
    from schorg.Nonprofit501d import Nonprofit501d

    a = create_schema_org_model(type_=Nonprofit501dInheritedProperties)
    b = create_schema_org_model(type_=Nonprofit501dProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Nonprofit501d.schema()


def HowOrWhereHealthAspect_test():
    from schorg.HowOrWhereHealthAspect import HowOrWhereHealthAspectInheritedProperties
    from schorg.HowOrWhereHealthAspect import HowOrWhereHealthAspectProperties
    from schorg.HowOrWhereHealthAspect import AllProperties
    from schorg.HowOrWhereHealthAspect import create_schema_org_model
    from schorg.HowOrWhereHealthAspect import HowOrWhereHealthAspect

    a = create_schema_org_model(type_=HowOrWhereHealthAspectInheritedProperties)
    b = create_schema_org_model(type_=HowOrWhereHealthAspectProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    HowOrWhereHealthAspect.schema()


def Otolaryngologic_test():
    from schorg.Otolaryngologic import OtolaryngologicInheritedProperties
    from schorg.Otolaryngologic import OtolaryngologicProperties
    from schorg.Otolaryngologic import AllProperties
    from schorg.Otolaryngologic import create_schema_org_model
    from schorg.Otolaryngologic import Otolaryngologic

    a = create_schema_org_model(type_=OtolaryngologicInheritedProperties)
    b = create_schema_org_model(type_=OtolaryngologicProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Otolaryngologic.schema()


def PreSale_test():
    from schorg.PreSale import PreSaleInheritedProperties
    from schorg.PreSale import PreSaleProperties
    from schorg.PreSale import AllProperties
    from schorg.PreSale import create_schema_org_model
    from schorg.PreSale import PreSale

    a = create_schema_org_model(type_=PreSaleInheritedProperties)
    b = create_schema_org_model(type_=PreSaleProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    PreSale.schema()


def Hostel_test():
    from schorg.Hostel import HostelInheritedProperties
    from schorg.Hostel import HostelProperties
    from schorg.Hostel import AllProperties
    from schorg.Hostel import create_schema_org_model
    from schorg.Hostel import Hostel

    a = create_schema_org_model(type_=HostelInheritedProperties)
    b = create_schema_org_model(type_=HostelProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Hostel.schema()


def PsychologicalTreatment_test():
    from schorg.PsychologicalTreatment import PsychologicalTreatmentInheritedProperties
    from schorg.PsychologicalTreatment import PsychologicalTreatmentProperties
    from schorg.PsychologicalTreatment import AllProperties
    from schorg.PsychologicalTreatment import create_schema_org_model
    from schorg.PsychologicalTreatment import PsychologicalTreatment

    a = create_schema_org_model(type_=PsychologicalTreatmentInheritedProperties)
    b = create_schema_org_model(type_=PsychologicalTreatmentProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    PsychologicalTreatment.schema()


def PerformAction_test():
    from schorg.PerformAction import PerformActionInheritedProperties
    from schorg.PerformAction import PerformActionProperties
    from schorg.PerformAction import AllProperties
    from schorg.PerformAction import create_schema_org_model
    from schorg.PerformAction import PerformAction

    a = create_schema_org_model(type_=PerformActionInheritedProperties)
    b = create_schema_org_model(type_=PerformActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    PerformAction.schema()


def PreOrder_test():
    from schorg.PreOrder import PreOrderInheritedProperties
    from schorg.PreOrder import PreOrderProperties
    from schorg.PreOrder import AllProperties
    from schorg.PreOrder import create_schema_org_model
    from schorg.PreOrder import PreOrder

    a = create_schema_org_model(type_=PreOrderInheritedProperties)
    b = create_schema_org_model(type_=PreOrderProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    PreOrder.schema()


def ChildrensEvent_test():
    from schorg.ChildrensEvent import ChildrensEventInheritedProperties
    from schorg.ChildrensEvent import ChildrensEventProperties
    from schorg.ChildrensEvent import AllProperties
    from schorg.ChildrensEvent import create_schema_org_model
    from schorg.ChildrensEvent import ChildrensEvent

    a = create_schema_org_model(type_=ChildrensEventInheritedProperties)
    b = create_schema_org_model(type_=ChildrensEventProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ChildrensEvent.schema()


def AuthoritativeLegalValue_test():
    from schorg.AuthoritativeLegalValue import AuthoritativeLegalValueInheritedProperties
    from schorg.AuthoritativeLegalValue import AuthoritativeLegalValueProperties
    from schorg.AuthoritativeLegalValue import AllProperties
    from schorg.AuthoritativeLegalValue import create_schema_org_model
    from schorg.AuthoritativeLegalValue import AuthoritativeLegalValue

    a = create_schema_org_model(type_=AuthoritativeLegalValueInheritedProperties)
    b = create_schema_org_model(type_=AuthoritativeLegalValueProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    AuthoritativeLegalValue.schema()


def WearableSizeSystemFR_test():
    from schorg.WearableSizeSystemFR import WearableSizeSystemFRInheritedProperties
    from schorg.WearableSizeSystemFR import WearableSizeSystemFRProperties
    from schorg.WearableSizeSystemFR import AllProperties
    from schorg.WearableSizeSystemFR import create_schema_org_model
    from schorg.WearableSizeSystemFR import WearableSizeSystemFR

    a = create_schema_org_model(type_=WearableSizeSystemFRInheritedProperties)
    b = create_schema_org_model(type_=WearableSizeSystemFRProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    WearableSizeSystemFR.schema()


def BroadcastRelease_test():
    from schorg.BroadcastRelease import BroadcastReleaseInheritedProperties
    from schorg.BroadcastRelease import BroadcastReleaseProperties
    from schorg.BroadcastRelease import AllProperties
    from schorg.BroadcastRelease import create_schema_org_model
    from schorg.BroadcastRelease import BroadcastRelease

    a = create_schema_org_model(type_=BroadcastReleaseInheritedProperties)
    b = create_schema_org_model(type_=BroadcastReleaseProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    BroadcastRelease.schema()


def TaxiService_test():
    from schorg.TaxiService import TaxiServiceInheritedProperties
    from schorg.TaxiService import TaxiServiceProperties
    from schorg.TaxiService import AllProperties
    from schorg.TaxiService import create_schema_org_model
    from schorg.TaxiService import TaxiService

    a = create_schema_org_model(type_=TaxiServiceInheritedProperties)
    b = create_schema_org_model(type_=TaxiServiceProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    TaxiService.schema()


def TattooParlor_test():
    from schorg.TattooParlor import TattooParlorInheritedProperties
    from schorg.TattooParlor import TattooParlorProperties
    from schorg.TattooParlor import AllProperties
    from schorg.TattooParlor import create_schema_org_model
    from schorg.TattooParlor import TattooParlor

    a = create_schema_org_model(type_=TattooParlorInheritedProperties)
    b = create_schema_org_model(type_=TattooParlorProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    TattooParlor.schema()


def EnergyStarCertified_test():
    from schorg.EnergyStarCertified import EnergyStarCertifiedInheritedProperties
    from schorg.EnergyStarCertified import EnergyStarCertifiedProperties
    from schorg.EnergyStarCertified import AllProperties
    from schorg.EnergyStarCertified import create_schema_org_model
    from schorg.EnergyStarCertified import EnergyStarCertified

    a = create_schema_org_model(type_=EnergyStarCertifiedInheritedProperties)
    b = create_schema_org_model(type_=EnergyStarCertifiedProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    EnergyStarCertified.schema()


def SendAction_test():
    from schorg.SendAction import SendActionInheritedProperties
    from schorg.SendAction import SendActionProperties
    from schorg.SendAction import AllProperties
    from schorg.SendAction import create_schema_org_model
    from schorg.SendAction import SendAction

    a = create_schema_org_model(type_=SendActionInheritedProperties)
    b = create_schema_org_model(type_=SendActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    SendAction.schema()


def Demand_test():
    from schorg.Demand import DemandInheritedProperties
    from schorg.Demand import DemandProperties
    from schorg.Demand import AllProperties
    from schorg.Demand import create_schema_org_model
    from schorg.Demand import Demand

    a = create_schema_org_model(type_=DemandInheritedProperties)
    b = create_schema_org_model(type_=DemandProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Demand.schema()


def SubscribeAction_test():
    from schorg.SubscribeAction import SubscribeActionInheritedProperties
    from schorg.SubscribeAction import SubscribeActionProperties
    from schorg.SubscribeAction import AllProperties
    from schorg.SubscribeAction import create_schema_org_model
    from schorg.SubscribeAction import SubscribeAction

    a = create_schema_org_model(type_=SubscribeActionInheritedProperties)
    b = create_schema_org_model(type_=SubscribeActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    SubscribeAction.schema()


def Number_test():
    from schorg.Number import NumberInheritedProperties
    from schorg.Number import NumberProperties
    from schorg.Number import AllProperties
    from schorg.Number import create_schema_org_model
    from schorg.Number import Number

    a = create_schema_org_model(type_=NumberInheritedProperties)
    b = create_schema_org_model(type_=NumberProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Number.schema()


def Waterfall_test():
    from schorg.Waterfall import WaterfallInheritedProperties
    from schorg.Waterfall import WaterfallProperties
    from schorg.Waterfall import AllProperties
    from schorg.Waterfall import create_schema_org_model
    from schorg.Waterfall import Waterfall

    a = create_schema_org_model(type_=WaterfallInheritedProperties)
    b = create_schema_org_model(type_=WaterfallProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Waterfall.schema()


def TakeAction_test():
    from schorg.TakeAction import TakeActionInheritedProperties
    from schorg.TakeAction import TakeActionProperties
    from schorg.TakeAction import AllProperties
    from schorg.TakeAction import create_schema_org_model
    from schorg.TakeAction import TakeAction

    a = create_schema_org_model(type_=TakeActionInheritedProperties)
    b = create_schema_org_model(type_=TakeActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    TakeAction.schema()


def State_test():
    from schorg.State import StateInheritedProperties
    from schorg.State import StateProperties
    from schorg.State import AllProperties
    from schorg.State import create_schema_org_model
    from schorg.State import State

    a = create_schema_org_model(type_=StateInheritedProperties)
    b = create_schema_org_model(type_=StateProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    State.schema()


def ReturnFeesCustomerResponsibility_test():
    from schorg.ReturnFeesCustomerResponsibility import ReturnFeesCustomerResponsibilityInheritedProperties
    from schorg.ReturnFeesCustomerResponsibility import ReturnFeesCustomerResponsibilityProperties
    from schorg.ReturnFeesCustomerResponsibility import AllProperties
    from schorg.ReturnFeesCustomerResponsibility import create_schema_org_model
    from schorg.ReturnFeesCustomerResponsibility import ReturnFeesCustomerResponsibility

    a = create_schema_org_model(type_=ReturnFeesCustomerResponsibilityInheritedProperties)
    b = create_schema_org_model(type_=ReturnFeesCustomerResponsibilityProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ReturnFeesCustomerResponsibility.schema()


def NewCondition_test():
    from schorg.NewCondition import NewConditionInheritedProperties
    from schorg.NewCondition import NewConditionProperties
    from schorg.NewCondition import AllProperties
    from schorg.NewCondition import create_schema_org_model
    from schorg.NewCondition import NewCondition

    a = create_schema_org_model(type_=NewConditionInheritedProperties)
    b = create_schema_org_model(type_=NewConditionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    NewCondition.schema()


def LeaveAction_test():
    from schorg.LeaveAction import LeaveActionInheritedProperties
    from schorg.LeaveAction import LeaveActionProperties
    from schorg.LeaveAction import AllProperties
    from schorg.LeaveAction import create_schema_org_model
    from schorg.LeaveAction import LeaveAction

    a = create_schema_org_model(type_=LeaveActionInheritedProperties)
    b = create_schema_org_model(type_=LeaveActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    LeaveAction.schema()


def WearableMeasurementChestOrBust_test():
    from schorg.WearableMeasurementChestOrBust import WearableMeasurementChestOrBustInheritedProperties
    from schorg.WearableMeasurementChestOrBust import WearableMeasurementChestOrBustProperties
    from schorg.WearableMeasurementChestOrBust import AllProperties
    from schorg.WearableMeasurementChestOrBust import create_schema_org_model
    from schorg.WearableMeasurementChestOrBust import WearableMeasurementChestOrBust

    a = create_schema_org_model(type_=WearableMeasurementChestOrBustInheritedProperties)
    b = create_schema_org_model(type_=WearableMeasurementChestOrBustProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    WearableMeasurementChestOrBust.schema()


def Property_test():
    from schorg.Property import PropertyInheritedProperties
    from schorg.Property import PropertyProperties
    from schorg.Property import AllProperties
    from schorg.Property import create_schema_org_model
    from schorg.Property import Property

    a = create_schema_org_model(type_=PropertyInheritedProperties)
    b = create_schema_org_model(type_=PropertyProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Property.schema()


def TVSeason_test():
    from schorg.TVSeason import TVSeasonInheritedProperties
    from schorg.TVSeason import TVSeasonProperties
    from schorg.TVSeason import AllProperties
    from schorg.TVSeason import create_schema_org_model
    from schorg.TVSeason import TVSeason

    a = create_schema_org_model(type_=TVSeasonInheritedProperties)
    b = create_schema_org_model(type_=TVSeasonProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    TVSeason.schema()


def WPHeader_test():
    from schorg.WPHeader import WPHeaderInheritedProperties
    from schorg.WPHeader import WPHeaderProperties
    from schorg.WPHeader import AllProperties
    from schorg.WPHeader import create_schema_org_model
    from schorg.WPHeader import WPHeader

    a = create_schema_org_model(type_=WPHeaderInheritedProperties)
    b = create_schema_org_model(type_=WPHeaderProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    WPHeader.schema()


def Nonprofit501c26_test():
    from schorg.Nonprofit501c26 import Nonprofit501c26InheritedProperties
    from schorg.Nonprofit501c26 import Nonprofit501c26Properties
    from schorg.Nonprofit501c26 import AllProperties
    from schorg.Nonprofit501c26 import create_schema_org_model
    from schorg.Nonprofit501c26 import Nonprofit501c26

    a = create_schema_org_model(type_=Nonprofit501c26InheritedProperties)
    b = create_schema_org_model(type_=Nonprofit501c26Properties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Nonprofit501c26.schema()


def ShoppingCenter_test():
    from schorg.ShoppingCenter import ShoppingCenterInheritedProperties
    from schorg.ShoppingCenter import ShoppingCenterProperties
    from schorg.ShoppingCenter import AllProperties
    from schorg.ShoppingCenter import create_schema_org_model
    from schorg.ShoppingCenter import ShoppingCenter

    a = create_schema_org_model(type_=ShoppingCenterInheritedProperties)
    b = create_schema_org_model(type_=ShoppingCenterProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ShoppingCenter.schema()


def MedicalCode_test():
    from schorg.MedicalCode import MedicalCodeInheritedProperties
    from schorg.MedicalCode import MedicalCodeProperties
    from schorg.MedicalCode import AllProperties
    from schorg.MedicalCode import create_schema_org_model
    from schorg.MedicalCode import MedicalCode

    a = create_schema_org_model(type_=MedicalCodeInheritedProperties)
    b = create_schema_org_model(type_=MedicalCodeProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MedicalCode.schema()


def PronounceableText_test():
    from schorg.PronounceableText import PronounceableTextInheritedProperties
    from schorg.PronounceableText import PronounceableTextProperties
    from schorg.PronounceableText import AllProperties
    from schorg.PronounceableText import create_schema_org_model
    from schorg.PronounceableText import PronounceableText

    a = create_schema_org_model(type_=PronounceableTextInheritedProperties)
    b = create_schema_org_model(type_=PronounceableTextProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    PronounceableText.schema()


def TransformedContent_test():
    from schorg.TransformedContent import TransformedContentInheritedProperties
    from schorg.TransformedContent import TransformedContentProperties
    from schorg.TransformedContent import AllProperties
    from schorg.TransformedContent import create_schema_org_model
    from schorg.TransformedContent import TransformedContent

    a = create_schema_org_model(type_=TransformedContentInheritedProperties)
    b = create_schema_org_model(type_=TransformedContentProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    TransformedContent.schema()


def MotorcycleRepair_test():
    from schorg.MotorcycleRepair import MotorcycleRepairInheritedProperties
    from schorg.MotorcycleRepair import MotorcycleRepairProperties
    from schorg.MotorcycleRepair import AllProperties
    from schorg.MotorcycleRepair import create_schema_org_model
    from schorg.MotorcycleRepair import MotorcycleRepair

    a = create_schema_org_model(type_=MotorcycleRepairInheritedProperties)
    b = create_schema_org_model(type_=MotorcycleRepairProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MotorcycleRepair.schema()


def ActiveActionStatus_test():
    from schorg.ActiveActionStatus import ActiveActionStatusInheritedProperties
    from schorg.ActiveActionStatus import ActiveActionStatusProperties
    from schorg.ActiveActionStatus import AllProperties
    from schorg.ActiveActionStatus import create_schema_org_model
    from schorg.ActiveActionStatus import ActiveActionStatus

    a = create_schema_org_model(type_=ActiveActionStatusInheritedProperties)
    b = create_schema_org_model(type_=ActiveActionStatusProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ActiveActionStatus.schema()


def EducationalOccupationalProgram_test():
    from schorg.EducationalOccupationalProgram import EducationalOccupationalProgramInheritedProperties
    from schorg.EducationalOccupationalProgram import EducationalOccupationalProgramProperties
    from schorg.EducationalOccupationalProgram import AllProperties
    from schorg.EducationalOccupationalProgram import create_schema_org_model
    from schorg.EducationalOccupationalProgram import EducationalOccupationalProgram

    a = create_schema_org_model(type_=EducationalOccupationalProgramInheritedProperties)
    b = create_schema_org_model(type_=EducationalOccupationalProgramProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    EducationalOccupationalProgram.schema()


def WorkBasedProgram_test():
    from schorg.WorkBasedProgram import WorkBasedProgramInheritedProperties
    from schorg.WorkBasedProgram import WorkBasedProgramProperties
    from schorg.WorkBasedProgram import AllProperties
    from schorg.WorkBasedProgram import create_schema_org_model
    from schorg.WorkBasedProgram import WorkBasedProgram

    a = create_schema_org_model(type_=WorkBasedProgramInheritedProperties)
    b = create_schema_org_model(type_=WorkBasedProgramProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    WorkBasedProgram.schema()


def DefinedRegion_test():
    from schorg.DefinedRegion import DefinedRegionInheritedProperties
    from schorg.DefinedRegion import DefinedRegionProperties
    from schorg.DefinedRegion import AllProperties
    from schorg.DefinedRegion import create_schema_org_model
    from schorg.DefinedRegion import DefinedRegion

    a = create_schema_org_model(type_=DefinedRegionInheritedProperties)
    b = create_schema_org_model(type_=DefinedRegionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    DefinedRegion.schema()


def Distillery_test():
    from schorg.Distillery import DistilleryInheritedProperties
    from schorg.Distillery import DistilleryProperties
    from schorg.Distillery import AllProperties
    from schorg.Distillery import create_schema_org_model
    from schorg.Distillery import Distillery

    a = create_schema_org_model(type_=DistilleryInheritedProperties)
    b = create_schema_org_model(type_=DistilleryProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Distillery.schema()


def BusOrCoach_test():
    from schorg.BusOrCoach import BusOrCoachInheritedProperties
    from schorg.BusOrCoach import BusOrCoachProperties
    from schorg.BusOrCoach import AllProperties
    from schorg.BusOrCoach import create_schema_org_model
    from schorg.BusOrCoach import BusOrCoach

    a = create_schema_org_model(type_=BusOrCoachInheritedProperties)
    b = create_schema_org_model(type_=BusOrCoachProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    BusOrCoach.schema()


def BodyMeasurementHips_test():
    from schorg.BodyMeasurementHips import BodyMeasurementHipsInheritedProperties
    from schorg.BodyMeasurementHips import BodyMeasurementHipsProperties
    from schorg.BodyMeasurementHips import AllProperties
    from schorg.BodyMeasurementHips import create_schema_org_model
    from schorg.BodyMeasurementHips import BodyMeasurementHips

    a = create_schema_org_model(type_=BodyMeasurementHipsInheritedProperties)
    b = create_schema_org_model(type_=BodyMeasurementHipsProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    BodyMeasurementHips.schema()


def Researcher_test():
    from schorg.Researcher import ResearcherInheritedProperties
    from schorg.Researcher import ResearcherProperties
    from schorg.Researcher import AllProperties
    from schorg.Researcher import create_schema_org_model
    from schorg.Researcher import Researcher

    a = create_schema_org_model(type_=ResearcherInheritedProperties)
    b = create_schema_org_model(type_=ResearcherProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Researcher.schema()


def IOSPlatform_test():
    from schorg.IOSPlatform import IOSPlatformInheritedProperties
    from schorg.IOSPlatform import IOSPlatformProperties
    from schorg.IOSPlatform import AllProperties
    from schorg.IOSPlatform import create_schema_org_model
    from schorg.IOSPlatform import IOSPlatform

    a = create_schema_org_model(type_=IOSPlatformInheritedProperties)
    b = create_schema_org_model(type_=IOSPlatformProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    IOSPlatform.schema()


def Quiz_test():
    from schorg.Quiz import QuizInheritedProperties
    from schorg.Quiz import QuizProperties
    from schorg.Quiz import AllProperties
    from schorg.Quiz import create_schema_org_model
    from schorg.Quiz import Quiz

    a = create_schema_org_model(type_=QuizInheritedProperties)
    b = create_schema_org_model(type_=QuizProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Quiz.schema()


def LowFatDiet_test():
    from schorg.LowFatDiet import LowFatDietInheritedProperties
    from schorg.LowFatDiet import LowFatDietProperties
    from schorg.LowFatDiet import AllProperties
    from schorg.LowFatDiet import create_schema_org_model
    from schorg.LowFatDiet import LowFatDiet

    a = create_schema_org_model(type_=LowFatDietInheritedProperties)
    b = create_schema_org_model(type_=LowFatDietProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    LowFatDiet.schema()


def Airline_test():
    from schorg.Airline import AirlineInheritedProperties
    from schorg.Airline import AirlineProperties
    from schorg.Airline import AllProperties
    from schorg.Airline import create_schema_org_model
    from schorg.Airline import Airline

    a = create_schema_org_model(type_=AirlineInheritedProperties)
    b = create_schema_org_model(type_=AirlineProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Airline.schema()


def Chiropractic_test():
    from schorg.Chiropractic import ChiropracticInheritedProperties
    from schorg.Chiropractic import ChiropracticProperties
    from schorg.Chiropractic import AllProperties
    from schorg.Chiropractic import create_schema_org_model
    from schorg.Chiropractic import Chiropractic

    a = create_schema_org_model(type_=ChiropracticInheritedProperties)
    b = create_schema_org_model(type_=ChiropracticProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Chiropractic.schema()


def WesternConventional_test():
    from schorg.WesternConventional import WesternConventionalInheritedProperties
    from schorg.WesternConventional import WesternConventionalProperties
    from schorg.WesternConventional import AllProperties
    from schorg.WesternConventional import create_schema_org_model
    from schorg.WesternConventional import WesternConventional

    a = create_schema_org_model(type_=WesternConventionalInheritedProperties)
    b = create_schema_org_model(type_=WesternConventionalProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    WesternConventional.schema()


def MerchantReturnUnspecified_test():
    from schorg.MerchantReturnUnspecified import MerchantReturnUnspecifiedInheritedProperties
    from schorg.MerchantReturnUnspecified import MerchantReturnUnspecifiedProperties
    from schorg.MerchantReturnUnspecified import AllProperties
    from schorg.MerchantReturnUnspecified import create_schema_org_model
    from schorg.MerchantReturnUnspecified import MerchantReturnUnspecified

    a = create_schema_org_model(type_=MerchantReturnUnspecifiedInheritedProperties)
    b = create_schema_org_model(type_=MerchantReturnUnspecifiedProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MerchantReturnUnspecified.schema()


def ReceiveAction_test():
    from schorg.ReceiveAction import ReceiveActionInheritedProperties
    from schorg.ReceiveAction import ReceiveActionProperties
    from schorg.ReceiveAction import AllProperties
    from schorg.ReceiveAction import create_schema_org_model
    from schorg.ReceiveAction import ReceiveAction

    a = create_schema_org_model(type_=ReceiveActionInheritedProperties)
    b = create_schema_org_model(type_=ReceiveActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ReceiveAction.schema()


def ReplyAction_test():
    from schorg.ReplyAction import ReplyActionInheritedProperties
    from schorg.ReplyAction import ReplyActionProperties
    from schorg.ReplyAction import AllProperties
    from schorg.ReplyAction import create_schema_org_model
    from schorg.ReplyAction import ReplyAction

    a = create_schema_org_model(type_=ReplyActionInheritedProperties)
    b = create_schema_org_model(type_=ReplyActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ReplyAction.schema()


def RightHandDriving_test():
    from schorg.RightHandDriving import RightHandDrivingInheritedProperties
    from schorg.RightHandDriving import RightHandDrivingProperties
    from schorg.RightHandDriving import AllProperties
    from schorg.RightHandDriving import create_schema_org_model
    from schorg.RightHandDriving import RightHandDriving

    a = create_schema_org_model(type_=RightHandDrivingInheritedProperties)
    b = create_schema_org_model(type_=RightHandDrivingProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    RightHandDriving.schema()


def SearchAction_test():
    from schorg.SearchAction import SearchActionInheritedProperties
    from schorg.SearchAction import SearchActionProperties
    from schorg.SearchAction import AllProperties
    from schorg.SearchAction import create_schema_org_model
    from schorg.SearchAction import SearchAction

    a = create_schema_org_model(type_=SearchActionInheritedProperties)
    b = create_schema_org_model(type_=SearchActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    SearchAction.schema()


def InternationalTrial_test():
    from schorg.InternationalTrial import InternationalTrialInheritedProperties
    from schorg.InternationalTrial import InternationalTrialProperties
    from schorg.InternationalTrial import AllProperties
    from schorg.InternationalTrial import create_schema_org_model
    from schorg.InternationalTrial import InternationalTrial

    a = create_schema_org_model(type_=InternationalTrialInheritedProperties)
    b = create_schema_org_model(type_=InternationalTrialProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    InternationalTrial.schema()


def MedicalRiskCalculator_test():
    from schorg.MedicalRiskCalculator import MedicalRiskCalculatorInheritedProperties
    from schorg.MedicalRiskCalculator import MedicalRiskCalculatorProperties
    from schorg.MedicalRiskCalculator import AllProperties
    from schorg.MedicalRiskCalculator import create_schema_org_model
    from schorg.MedicalRiskCalculator import MedicalRiskCalculator

    a = create_schema_org_model(type_=MedicalRiskCalculatorInheritedProperties)
    b = create_schema_org_model(type_=MedicalRiskCalculatorProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MedicalRiskCalculator.schema()


def MovieTheater_test():
    from schorg.MovieTheater import MovieTheaterInheritedProperties
    from schorg.MovieTheater import MovieTheaterProperties
    from schorg.MovieTheater import AllProperties
    from schorg.MovieTheater import create_schema_org_model
    from schorg.MovieTheater import MovieTheater

    a = create_schema_org_model(type_=MovieTheaterInheritedProperties)
    b = create_schema_org_model(type_=MovieTheaterProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MovieTheater.schema()


def ShippingRateSettings_test():
    from schorg.ShippingRateSettings import ShippingRateSettingsInheritedProperties
    from schorg.ShippingRateSettings import ShippingRateSettingsProperties
    from schorg.ShippingRateSettings import AllProperties
    from schorg.ShippingRateSettings import create_schema_org_model
    from schorg.ShippingRateSettings import ShippingRateSettings

    a = create_schema_org_model(type_=ShippingRateSettingsInheritedProperties)
    b = create_schema_org_model(type_=ShippingRateSettingsProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ShippingRateSettings.schema()


def RsvpResponseMaybe_test():
    from schorg.RsvpResponseMaybe import RsvpResponseMaybeInheritedProperties
    from schorg.RsvpResponseMaybe import RsvpResponseMaybeProperties
    from schorg.RsvpResponseMaybe import AllProperties
    from schorg.RsvpResponseMaybe import create_schema_org_model
    from schorg.RsvpResponseMaybe import RsvpResponseMaybe

    a = create_schema_org_model(type_=RsvpResponseMaybeInheritedProperties)
    b = create_schema_org_model(type_=RsvpResponseMaybeProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    RsvpResponseMaybe.schema()


def Ear_test():
    from schorg.Ear import EarInheritedProperties
    from schorg.Ear import EarProperties
    from schorg.Ear import AllProperties
    from schorg.Ear import create_schema_org_model
    from schorg.Ear import Ear

    a = create_schema_org_model(type_=EarInheritedProperties)
    b = create_schema_org_model(type_=EarProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Ear.schema()


def WearAction_test():
    from schorg.WearAction import WearActionInheritedProperties
    from schorg.WearAction import WearActionProperties
    from schorg.WearAction import AllProperties
    from schorg.WearAction import create_schema_org_model
    from schorg.WearAction import WearAction

    a = create_schema_org_model(type_=WearActionInheritedProperties)
    b = create_schema_org_model(type_=WearActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    WearAction.schema()


def BusReservation_test():
    from schorg.BusReservation import BusReservationInheritedProperties
    from schorg.BusReservation import BusReservationProperties
    from schorg.BusReservation import AllProperties
    from schorg.BusReservation import create_schema_org_model
    from schorg.BusReservation import BusReservation

    a = create_schema_org_model(type_=BusReservationInheritedProperties)
    b = create_schema_org_model(type_=BusReservationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    BusReservation.schema()


def ArchiveComponent_test():
    from schorg.ArchiveComponent import ArchiveComponentInheritedProperties
    from schorg.ArchiveComponent import ArchiveComponentProperties
    from schorg.ArchiveComponent import AllProperties
    from schorg.ArchiveComponent import create_schema_org_model
    from schorg.ArchiveComponent import ArchiveComponent

    a = create_schema_org_model(type_=ArchiveComponentInheritedProperties)
    b = create_schema_org_model(type_=ArchiveComponentProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ArchiveComponent.schema()


def Library_test():
    from schorg.Library import LibraryInheritedProperties
    from schorg.Library import LibraryProperties
    from schorg.Library import AllProperties
    from schorg.Library import create_schema_org_model
    from schorg.Library import Library

    a = create_schema_org_model(type_=LibraryInheritedProperties)
    b = create_schema_org_model(type_=LibraryProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Library.schema()


def MerchantReturnFiniteReturnWindow_test():
    from schorg.MerchantReturnFiniteReturnWindow import MerchantReturnFiniteReturnWindowInheritedProperties
    from schorg.MerchantReturnFiniteReturnWindow import MerchantReturnFiniteReturnWindowProperties
    from schorg.MerchantReturnFiniteReturnWindow import AllProperties
    from schorg.MerchantReturnFiniteReturnWindow import create_schema_org_model
    from schorg.MerchantReturnFiniteReturnWindow import MerchantReturnFiniteReturnWindow

    a = create_schema_org_model(type_=MerchantReturnFiniteReturnWindowInheritedProperties)
    b = create_schema_org_model(type_=MerchantReturnFiniteReturnWindowProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MerchantReturnFiniteReturnWindow.schema()


def SpecialAnnouncement_test():
    from schorg.SpecialAnnouncement import SpecialAnnouncementInheritedProperties
    from schorg.SpecialAnnouncement import SpecialAnnouncementProperties
    from schorg.SpecialAnnouncement import AllProperties
    from schorg.SpecialAnnouncement import create_schema_org_model
    from schorg.SpecialAnnouncement import SpecialAnnouncement

    a = create_schema_org_model(type_=SpecialAnnouncementInheritedProperties)
    b = create_schema_org_model(type_=SpecialAnnouncementProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    SpecialAnnouncement.schema()


def EmployerReview_test():
    from schorg.EmployerReview import EmployerReviewInheritedProperties
    from schorg.EmployerReview import EmployerReviewProperties
    from schorg.EmployerReview import AllProperties
    from schorg.EmployerReview import create_schema_org_model
    from schorg.EmployerReview import EmployerReview

    a = create_schema_org_model(type_=EmployerReviewInheritedProperties)
    b = create_schema_org_model(type_=EmployerReviewProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    EmployerReview.schema()


def RsvpResponseNo_test():
    from schorg.RsvpResponseNo import RsvpResponseNoInheritedProperties
    from schorg.RsvpResponseNo import RsvpResponseNoProperties
    from schorg.RsvpResponseNo import AllProperties
    from schorg.RsvpResponseNo import create_schema_org_model
    from schorg.RsvpResponseNo import RsvpResponseNo

    a = create_schema_org_model(type_=RsvpResponseNoInheritedProperties)
    b = create_schema_org_model(type_=RsvpResponseNoProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    RsvpResponseNo.schema()


def HyperTocEntry_test():
    from schorg.HyperTocEntry import HyperTocEntryInheritedProperties
    from schorg.HyperTocEntry import HyperTocEntryProperties
    from schorg.HyperTocEntry import AllProperties
    from schorg.HyperTocEntry import create_schema_org_model
    from schorg.HyperTocEntry import HyperTocEntry

    a = create_schema_org_model(type_=HyperTocEntryInheritedProperties)
    b = create_schema_org_model(type_=HyperTocEntryProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    HyperTocEntry.schema()


def SurgicalProcedure_test():
    from schorg.SurgicalProcedure import SurgicalProcedureInheritedProperties
    from schorg.SurgicalProcedure import SurgicalProcedureProperties
    from schorg.SurgicalProcedure import AllProperties
    from schorg.SurgicalProcedure import create_schema_org_model
    from schorg.SurgicalProcedure import SurgicalProcedure

    a = create_schema_org_model(type_=SurgicalProcedureInheritedProperties)
    b = create_schema_org_model(type_=SurgicalProcedureProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    SurgicalProcedure.schema()


def GettingAccessHealthAspect_test():
    from schorg.GettingAccessHealthAspect import GettingAccessHealthAspectInheritedProperties
    from schorg.GettingAccessHealthAspect import GettingAccessHealthAspectProperties
    from schorg.GettingAccessHealthAspect import AllProperties
    from schorg.GettingAccessHealthAspect import create_schema_org_model
    from schorg.GettingAccessHealthAspect import GettingAccessHealthAspect

    a = create_schema_org_model(type_=GettingAccessHealthAspectInheritedProperties)
    b = create_schema_org_model(type_=GettingAccessHealthAspectProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    GettingAccessHealthAspect.schema()


def VideoGallery_test():
    from schorg.VideoGallery import VideoGalleryInheritedProperties
    from schorg.VideoGallery import VideoGalleryProperties
    from schorg.VideoGallery import AllProperties
    from schorg.VideoGallery import create_schema_org_model
    from schorg.VideoGallery import VideoGallery

    a = create_schema_org_model(type_=VideoGalleryInheritedProperties)
    b = create_schema_org_model(type_=VideoGalleryProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    VideoGallery.schema()


def ScreeningEvent_test():
    from schorg.ScreeningEvent import ScreeningEventInheritedProperties
    from schorg.ScreeningEvent import ScreeningEventProperties
    from schorg.ScreeningEvent import AllProperties
    from schorg.ScreeningEvent import create_schema_org_model
    from schorg.ScreeningEvent import ScreeningEvent

    a = create_schema_org_model(type_=ScreeningEventInheritedProperties)
    b = create_schema_org_model(type_=ScreeningEventProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ScreeningEvent.schema()


def AndroidPlatform_test():
    from schorg.AndroidPlatform import AndroidPlatformInheritedProperties
    from schorg.AndroidPlatform import AndroidPlatformProperties
    from schorg.AndroidPlatform import AllProperties
    from schorg.AndroidPlatform import create_schema_org_model
    from schorg.AndroidPlatform import AndroidPlatform

    a = create_schema_org_model(type_=AndroidPlatformInheritedProperties)
    b = create_schema_org_model(type_=AndroidPlatformProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    AndroidPlatform.schema()


def Claim_test():
    from schorg.Claim import ClaimInheritedProperties
    from schorg.Claim import ClaimProperties
    from schorg.Claim import AllProperties
    from schorg.Claim import create_schema_org_model
    from schorg.Claim import Claim

    a = create_schema_org_model(type_=ClaimInheritedProperties)
    b = create_schema_org_model(type_=ClaimProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Claim.schema()


def Mosque_test():
    from schorg.Mosque import MosqueInheritedProperties
    from schorg.Mosque import MosqueProperties
    from schorg.Mosque import AllProperties
    from schorg.Mosque import create_schema_org_model
    from schorg.Mosque import Mosque

    a = create_schema_org_model(type_=MosqueInheritedProperties)
    b = create_schema_org_model(type_=MosqueProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Mosque.schema()


def LibrarySystem_test():
    from schorg.LibrarySystem import LibrarySystemInheritedProperties
    from schorg.LibrarySystem import LibrarySystemProperties
    from schorg.LibrarySystem import AllProperties
    from schorg.LibrarySystem import create_schema_org_model
    from schorg.LibrarySystem import LibrarySystem

    a = create_schema_org_model(type_=LibrarySystemInheritedProperties)
    b = create_schema_org_model(type_=LibrarySystemProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    LibrarySystem.schema()


def Nerve_test():
    from schorg.Nerve import NerveInheritedProperties
    from schorg.Nerve import NerveProperties
    from schorg.Nerve import AllProperties
    from schorg.Nerve import create_schema_org_model
    from schorg.Nerve import Nerve

    a = create_schema_org_model(type_=NerveInheritedProperties)
    b = create_schema_org_model(type_=NerveProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Nerve.schema()


def Notary_test():
    from schorg.Notary import NotaryInheritedProperties
    from schorg.Notary import NotaryProperties
    from schorg.Notary import AllProperties
    from schorg.Notary import create_schema_org_model
    from schorg.Notary import Notary

    a = create_schema_org_model(type_=NotaryInheritedProperties)
    b = create_schema_org_model(type_=NotaryProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Notary.schema()


def WatchAction_test():
    from schorg.WatchAction import WatchActionInheritedProperties
    from schorg.WatchAction import WatchActionProperties
    from schorg.WatchAction import AllProperties
    from schorg.WatchAction import create_schema_org_model
    from schorg.WatchAction import WatchAction

    a = create_schema_org_model(type_=WatchActionInheritedProperties)
    b = create_schema_org_model(type_=WatchActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    WatchAction.schema()


def AutoWash_test():
    from schorg.AutoWash import AutoWashInheritedProperties
    from schorg.AutoWash import AutoWashProperties
    from schorg.AutoWash import AllProperties
    from schorg.AutoWash import create_schema_org_model
    from schorg.AutoWash import AutoWash

    a = create_schema_org_model(type_=AutoWashInheritedProperties)
    b = create_schema_org_model(type_=AutoWashProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    AutoWash.schema()


def UsageOrScheduleHealthAspect_test():
    from schorg.UsageOrScheduleHealthAspect import UsageOrScheduleHealthAspectInheritedProperties
    from schorg.UsageOrScheduleHealthAspect import UsageOrScheduleHealthAspectProperties
    from schorg.UsageOrScheduleHealthAspect import AllProperties
    from schorg.UsageOrScheduleHealthAspect import create_schema_org_model
    from schorg.UsageOrScheduleHealthAspect import UsageOrScheduleHealthAspect

    a = create_schema_org_model(type_=UsageOrScheduleHealthAspectInheritedProperties)
    b = create_schema_org_model(type_=UsageOrScheduleHealthAspectProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    UsageOrScheduleHealthAspect.schema()


def CommentAction_test():
    from schorg.CommentAction import CommentActionInheritedProperties
    from schorg.CommentAction import CommentActionProperties
    from schorg.CommentAction import AllProperties
    from schorg.CommentAction import create_schema_org_model
    from schorg.CommentAction import CommentAction

    a = create_schema_org_model(type_=CommentActionInheritedProperties)
    b = create_schema_org_model(type_=CommentActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    CommentAction.schema()


def JewelryStore_test():
    from schorg.JewelryStore import JewelryStoreInheritedProperties
    from schorg.JewelryStore import JewelryStoreProperties
    from schorg.JewelryStore import AllProperties
    from schorg.JewelryStore import create_schema_org_model
    from schorg.JewelryStore import JewelryStore

    a = create_schema_org_model(type_=JewelryStoreInheritedProperties)
    b = create_schema_org_model(type_=JewelryStoreProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    JewelryStore.schema()


def Skin_test():
    from schorg.Skin import SkinInheritedProperties
    from schorg.Skin import SkinProperties
    from schorg.Skin import AllProperties
    from schorg.Skin import create_schema_org_model
    from schorg.Skin import Skin

    a = create_schema_org_model(type_=SkinInheritedProperties)
    b = create_schema_org_model(type_=SkinProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Skin.schema()


def ReviewAction_test():
    from schorg.ReviewAction import ReviewActionInheritedProperties
    from schorg.ReviewAction import ReviewActionProperties
    from schorg.ReviewAction import AllProperties
    from schorg.ReviewAction import create_schema_org_model
    from schorg.ReviewAction import ReviewAction

    a = create_schema_org_model(type_=ReviewActionInheritedProperties)
    b = create_schema_org_model(type_=ReviewActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ReviewAction.schema()


def WearableSizeGroupMisses_test():
    from schorg.WearableSizeGroupMisses import WearableSizeGroupMissesInheritedProperties
    from schorg.WearableSizeGroupMisses import WearableSizeGroupMissesProperties
    from schorg.WearableSizeGroupMisses import AllProperties
    from schorg.WearableSizeGroupMisses import create_schema_org_model
    from schorg.WearableSizeGroupMisses import WearableSizeGroupMisses

    a = create_schema_org_model(type_=WearableSizeGroupMissesInheritedProperties)
    b = create_schema_org_model(type_=WearableSizeGroupMissesProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    WearableSizeGroupMisses.schema()


def MusculoskeletalExam_test():
    from schorg.MusculoskeletalExam import MusculoskeletalExamInheritedProperties
    from schorg.MusculoskeletalExam import MusculoskeletalExamProperties
    from schorg.MusculoskeletalExam import AllProperties
    from schorg.MusculoskeletalExam import create_schema_org_model
    from schorg.MusculoskeletalExam import MusculoskeletalExam

    a = create_schema_org_model(type_=MusculoskeletalExamInheritedProperties)
    b = create_schema_org_model(type_=MusculoskeletalExamProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MusculoskeletalExam.schema()


def AnimalShelter_test():
    from schorg.AnimalShelter import AnimalShelterInheritedProperties
    from schorg.AnimalShelter import AnimalShelterProperties
    from schorg.AnimalShelter import AllProperties
    from schorg.AnimalShelter import create_schema_org_model
    from schorg.AnimalShelter import AnimalShelter

    a = create_schema_org_model(type_=AnimalShelterInheritedProperties)
    b = create_schema_org_model(type_=AnimalShelterProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    AnimalShelter.schema()


def Emergency_test():
    from schorg.Emergency import EmergencyInheritedProperties
    from schorg.Emergency import EmergencyProperties
    from schorg.Emergency import AllProperties
    from schorg.Emergency import create_schema_org_model
    from schorg.Emergency import Emergency

    a = create_schema_org_model(type_=EmergencyInheritedProperties)
    b = create_schema_org_model(type_=EmergencyProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Emergency.schema()


def ImageGallery_test():
    from schorg.ImageGallery import ImageGalleryInheritedProperties
    from schorg.ImageGallery import ImageGalleryProperties
    from schorg.ImageGallery import AllProperties
    from schorg.ImageGallery import create_schema_org_model
    from schorg.ImageGallery import ImageGallery

    a = create_schema_org_model(type_=ImageGalleryInheritedProperties)
    b = create_schema_org_model(type_=ImageGalleryProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ImageGallery.schema()


def LiveBlogPosting_test():
    from schorg.LiveBlogPosting import LiveBlogPostingInheritedProperties
    from schorg.LiveBlogPosting import LiveBlogPostingProperties
    from schorg.LiveBlogPosting import AllProperties
    from schorg.LiveBlogPosting import create_schema_org_model
    from schorg.LiveBlogPosting import LiveBlogPosting

    a = create_schema_org_model(type_=LiveBlogPostingInheritedProperties)
    b = create_schema_org_model(type_=LiveBlogPostingProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    LiveBlogPosting.schema()


def WearableSizeGroupInfants_test():
    from schorg.WearableSizeGroupInfants import WearableSizeGroupInfantsInheritedProperties
    from schorg.WearableSizeGroupInfants import WearableSizeGroupInfantsProperties
    from schorg.WearableSizeGroupInfants import AllProperties
    from schorg.WearableSizeGroupInfants import create_schema_org_model
    from schorg.WearableSizeGroupInfants import WearableSizeGroupInfants

    a = create_schema_org_model(type_=WearableSizeGroupInfantsInheritedProperties)
    b = create_schema_org_model(type_=WearableSizeGroupInfantsProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    WearableSizeGroupInfants.schema()


def PublicToilet_test():
    from schorg.PublicToilet import PublicToiletInheritedProperties
    from schorg.PublicToilet import PublicToiletProperties
    from schorg.PublicToilet import AllProperties
    from schorg.PublicToilet import create_schema_org_model
    from schorg.PublicToilet import PublicToilet

    a = create_schema_org_model(type_=PublicToiletInheritedProperties)
    b = create_schema_org_model(type_=PublicToiletProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    PublicToilet.schema()


def FDAcategoryA_test():
    from schorg.FDAcategoryA import FDAcategoryAInheritedProperties
    from schorg.FDAcategoryA import FDAcategoryAProperties
    from schorg.FDAcategoryA import AllProperties
    from schorg.FDAcategoryA import create_schema_org_model
    from schorg.FDAcategoryA import FDAcategoryA

    a = create_schema_org_model(type_=FDAcategoryAInheritedProperties)
    b = create_schema_org_model(type_=FDAcategoryAProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    FDAcategoryA.schema()


def MedicalContraindication_test():
    from schorg.MedicalContraindication import MedicalContraindicationInheritedProperties
    from schorg.MedicalContraindication import MedicalContraindicationProperties
    from schorg.MedicalContraindication import AllProperties
    from schorg.MedicalContraindication import create_schema_org_model
    from schorg.MedicalContraindication import MedicalContraindication

    a = create_schema_org_model(type_=MedicalContraindicationInheritedProperties)
    b = create_schema_org_model(type_=MedicalContraindicationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MedicalContraindication.schema()


def ComedyEvent_test():
    from schorg.ComedyEvent import ComedyEventInheritedProperties
    from schorg.ComedyEvent import ComedyEventProperties
    from schorg.ComedyEvent import AllProperties
    from schorg.ComedyEvent import create_schema_org_model
    from schorg.ComedyEvent import ComedyEvent

    a = create_schema_org_model(type_=ComedyEventInheritedProperties)
    b = create_schema_org_model(type_=ComedyEventProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ComedyEvent.schema()


def SuspendAction_test():
    from schorg.SuspendAction import SuspendActionInheritedProperties
    from schorg.SuspendAction import SuspendActionProperties
    from schorg.SuspendAction import AllProperties
    from schorg.SuspendAction import create_schema_org_model
    from schorg.SuspendAction import SuspendAction

    a = create_schema_org_model(type_=SuspendActionInheritedProperties)
    b = create_schema_org_model(type_=SuspendActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    SuspendAction.schema()


def Pathology_test():
    from schorg.Pathology import PathologyInheritedProperties
    from schorg.Pathology import PathologyProperties
    from schorg.Pathology import AllProperties
    from schorg.Pathology import create_schema_org_model
    from schorg.Pathology import Pathology

    a = create_schema_org_model(type_=PathologyInheritedProperties)
    b = create_schema_org_model(type_=PathologyProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Pathology.schema()


def ParentalSupport_test():
    from schorg.ParentalSupport import ParentalSupportInheritedProperties
    from schorg.ParentalSupport import ParentalSupportProperties
    from schorg.ParentalSupport import AllProperties
    from schorg.ParentalSupport import create_schema_org_model
    from schorg.ParentalSupport import ParentalSupport

    a = create_schema_org_model(type_=ParentalSupportInheritedProperties)
    b = create_schema_org_model(type_=ParentalSupportProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ParentalSupport.schema()


def LendAction_test():
    from schorg.LendAction import LendActionInheritedProperties
    from schorg.LendAction import LendActionProperties
    from schorg.LendAction import AllProperties
    from schorg.LendAction import create_schema_org_model
    from schorg.LendAction import LendAction

    a = create_schema_org_model(type_=LendActionInheritedProperties)
    b = create_schema_org_model(type_=LendActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    LendAction.schema()


def Hardcover_test():
    from schorg.Hardcover import HardcoverInheritedProperties
    from schorg.Hardcover import HardcoverProperties
    from schorg.Hardcover import AllProperties
    from schorg.Hardcover import create_schema_org_model
    from schorg.Hardcover import Hardcover

    a = create_schema_org_model(type_=HardcoverInheritedProperties)
    b = create_schema_org_model(type_=HardcoverProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Hardcover.schema()


def FundingScheme_test():
    from schorg.FundingScheme import FundingSchemeInheritedProperties
    from schorg.FundingScheme import FundingSchemeProperties
    from schorg.FundingScheme import AllProperties
    from schorg.FundingScheme import create_schema_org_model
    from schorg.FundingScheme import FundingScheme

    a = create_schema_org_model(type_=FundingSchemeInheritedProperties)
    b = create_schema_org_model(type_=FundingSchemeProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    FundingScheme.schema()


def PatientExperienceHealthAspect_test():
    from schorg.PatientExperienceHealthAspect import PatientExperienceHealthAspectInheritedProperties
    from schorg.PatientExperienceHealthAspect import PatientExperienceHealthAspectProperties
    from schorg.PatientExperienceHealthAspect import AllProperties
    from schorg.PatientExperienceHealthAspect import create_schema_org_model
    from schorg.PatientExperienceHealthAspect import PatientExperienceHealthAspect

    a = create_schema_org_model(type_=PatientExperienceHealthAspectInheritedProperties)
    b = create_schema_org_model(type_=PatientExperienceHealthAspectProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    PatientExperienceHealthAspect.schema()


def TelevisionStation_test():
    from schorg.TelevisionStation import TelevisionStationInheritedProperties
    from schorg.TelevisionStation import TelevisionStationProperties
    from schorg.TelevisionStation import AllProperties
    from schorg.TelevisionStation import create_schema_org_model
    from schorg.TelevisionStation import TelevisionStation

    a = create_schema_org_model(type_=TelevisionStationInheritedProperties)
    b = create_schema_org_model(type_=TelevisionStationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    TelevisionStation.schema()


def MRI_test():
    from schorg.MRI import MRIInheritedProperties
    from schorg.MRI import MRIProperties
    from schorg.MRI import AllProperties
    from schorg.MRI import create_schema_org_model
    from schorg.MRI import MRI

    a = create_schema_org_model(type_=MRIInheritedProperties)
    b = create_schema_org_model(type_=MRIProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MRI.schema()


def MotorizedBicycle_test():
    from schorg.MotorizedBicycle import MotorizedBicycleInheritedProperties
    from schorg.MotorizedBicycle import MotorizedBicycleProperties
    from schorg.MotorizedBicycle import AllProperties
    from schorg.MotorizedBicycle import create_schema_org_model
    from schorg.MotorizedBicycle import MotorizedBicycle

    a = create_schema_org_model(type_=MotorizedBicycleInheritedProperties)
    b = create_schema_org_model(type_=MotorizedBicycleProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MotorizedBicycle.schema()


def Poster_test():
    from schorg.Poster import PosterInheritedProperties
    from schorg.Poster import PosterProperties
    from schorg.Poster import AllProperties
    from schorg.Poster import create_schema_org_model
    from schorg.Poster import Poster

    a = create_schema_org_model(type_=PosterInheritedProperties)
    b = create_schema_org_model(type_=PosterProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Poster.schema()


def RsvpResponseYes_test():
    from schorg.RsvpResponseYes import RsvpResponseYesInheritedProperties
    from schorg.RsvpResponseYes import RsvpResponseYesProperties
    from schorg.RsvpResponseYes import AllProperties
    from schorg.RsvpResponseYes import create_schema_org_model
    from schorg.RsvpResponseYes import RsvpResponseYes

    a = create_schema_org_model(type_=RsvpResponseYesInheritedProperties)
    b = create_schema_org_model(type_=RsvpResponseYesProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    RsvpResponseYes.schema()


def EventRescheduled_test():
    from schorg.EventRescheduled import EventRescheduledInheritedProperties
    from schorg.EventRescheduled import EventRescheduledProperties
    from schorg.EventRescheduled import AllProperties
    from schorg.EventRescheduled import create_schema_org_model
    from schorg.EventRescheduled import EventRescheduled

    a = create_schema_org_model(type_=EventRescheduledInheritedProperties)
    b = create_schema_org_model(type_=EventRescheduledProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    EventRescheduled.schema()


def BodyMeasurementHead_test():
    from schorg.BodyMeasurementHead import BodyMeasurementHeadInheritedProperties
    from schorg.BodyMeasurementHead import BodyMeasurementHeadProperties
    from schorg.BodyMeasurementHead import AllProperties
    from schorg.BodyMeasurementHead import create_schema_org_model
    from schorg.BodyMeasurementHead import BodyMeasurementHead

    a = create_schema_org_model(type_=BodyMeasurementHeadInheritedProperties)
    b = create_schema_org_model(type_=BodyMeasurementHeadProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    BodyMeasurementHead.schema()


def UserPlays_test():
    from schorg.UserPlays import UserPlaysInheritedProperties
    from schorg.UserPlays import UserPlaysProperties
    from schorg.UserPlays import AllProperties
    from schorg.UserPlays import create_schema_org_model
    from schorg.UserPlays import UserPlays

    a = create_schema_org_model(type_=UserPlaysInheritedProperties)
    b = create_schema_org_model(type_=UserPlaysProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    UserPlays.schema()


def MiddleSchool_test():
    from schorg.MiddleSchool import MiddleSchoolInheritedProperties
    from schorg.MiddleSchool import MiddleSchoolProperties
    from schorg.MiddleSchool import AllProperties
    from schorg.MiddleSchool import create_schema_org_model
    from schorg.MiddleSchool import MiddleSchool

    a = create_schema_org_model(type_=MiddleSchoolInheritedProperties)
    b = create_schema_org_model(type_=MiddleSchoolProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MiddleSchool.schema()


def LakeBodyOfWater_test():
    from schorg.LakeBodyOfWater import LakeBodyOfWaterInheritedProperties
    from schorg.LakeBodyOfWater import LakeBodyOfWaterProperties
    from schorg.LakeBodyOfWater import AllProperties
    from schorg.LakeBodyOfWater import create_schema_org_model
    from schorg.LakeBodyOfWater import LakeBodyOfWater

    a = create_schema_org_model(type_=LakeBodyOfWaterInheritedProperties)
    b = create_schema_org_model(type_=LakeBodyOfWaterProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    LakeBodyOfWater.schema()


def Monday_test():
    from schorg.Monday import MondayInheritedProperties
    from schorg.Monday import MondayProperties
    from schorg.Monday import AllProperties
    from schorg.Monday import create_schema_org_model
    from schorg.Monday import Monday

    a = create_schema_org_model(type_=MondayInheritedProperties)
    b = create_schema_org_model(type_=MondayProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Monday.schema()


def AboutPage_test():
    from schorg.AboutPage import AboutPageInheritedProperties
    from schorg.AboutPage import AboutPageProperties
    from schorg.AboutPage import AllProperties
    from schorg.AboutPage import create_schema_org_model
    from schorg.AboutPage import AboutPage

    a = create_schema_org_model(type_=AboutPageInheritedProperties)
    b = create_schema_org_model(type_=AboutPageProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    AboutPage.schema()


def GameServer_test():
    from schorg.GameServer import GameServerInheritedProperties
    from schorg.GameServer import GameServerProperties
    from schorg.GameServer import AllProperties
    from schorg.GameServer import create_schema_org_model
    from schorg.GameServer import GameServer

    a = create_schema_org_model(type_=GameServerInheritedProperties)
    b = create_schema_org_model(type_=GameServerProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    GameServer.schema()


def PreOrderAction_test():
    from schorg.PreOrderAction import PreOrderActionInheritedProperties
    from schorg.PreOrderAction import PreOrderActionProperties
    from schorg.PreOrderAction import AllProperties
    from schorg.PreOrderAction import create_schema_org_model
    from schorg.PreOrderAction import PreOrderAction

    a = create_schema_org_model(type_=PreOrderActionInheritedProperties)
    b = create_schema_org_model(type_=PreOrderActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    PreOrderAction.schema()


def Duration_test():
    from schorg.Duration import DurationInheritedProperties
    from schorg.Duration import DurationProperties
    from schorg.Duration import AllProperties
    from schorg.Duration import create_schema_org_model
    from schorg.Duration import Duration

    a = create_schema_org_model(type_=DurationInheritedProperties)
    b = create_schema_org_model(type_=DurationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Duration.schema()


def BroadcastEvent_test():
    from schorg.BroadcastEvent import BroadcastEventInheritedProperties
    from schorg.BroadcastEvent import BroadcastEventProperties
    from schorg.BroadcastEvent import AllProperties
    from schorg.BroadcastEvent import create_schema_org_model
    from schorg.BroadcastEvent import BroadcastEvent

    a = create_schema_org_model(type_=BroadcastEventInheritedProperties)
    b = create_schema_org_model(type_=BroadcastEventProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    BroadcastEvent.schema()


def MedicalRiskFactor_test():
    from schorg.MedicalRiskFactor import MedicalRiskFactorInheritedProperties
    from schorg.MedicalRiskFactor import MedicalRiskFactorProperties
    from schorg.MedicalRiskFactor import AllProperties
    from schorg.MedicalRiskFactor import create_schema_org_model
    from schorg.MedicalRiskFactor import MedicalRiskFactor

    a = create_schema_org_model(type_=MedicalRiskFactorInheritedProperties)
    b = create_schema_org_model(type_=MedicalRiskFactorProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MedicalRiskFactor.schema()


def ConvenienceStore_test():
    from schorg.ConvenienceStore import ConvenienceStoreInheritedProperties
    from schorg.ConvenienceStore import ConvenienceStoreProperties
    from schorg.ConvenienceStore import AllProperties
    from schorg.ConvenienceStore import create_schema_org_model
    from schorg.ConvenienceStore import ConvenienceStore

    a = create_schema_org_model(type_=ConvenienceStoreInheritedProperties)
    b = create_schema_org_model(type_=ConvenienceStoreProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ConvenienceStore.schema()


def AlbumRelease_test():
    from schorg.AlbumRelease import AlbumReleaseInheritedProperties
    from schorg.AlbumRelease import AlbumReleaseProperties
    from schorg.AlbumRelease import AllProperties
    from schorg.AlbumRelease import create_schema_org_model
    from schorg.AlbumRelease import AlbumRelease

    a = create_schema_org_model(type_=AlbumReleaseInheritedProperties)
    b = create_schema_org_model(type_=AlbumReleaseProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    AlbumRelease.schema()


def SingleFamilyResidence_test():
    from schorg.SingleFamilyResidence import SingleFamilyResidenceInheritedProperties
    from schorg.SingleFamilyResidence import SingleFamilyResidenceProperties
    from schorg.SingleFamilyResidence import AllProperties
    from schorg.SingleFamilyResidence import create_schema_org_model
    from schorg.SingleFamilyResidence import SingleFamilyResidence

    a = create_schema_org_model(type_=SingleFamilyResidenceInheritedProperties)
    b = create_schema_org_model(type_=SingleFamilyResidenceProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    SingleFamilyResidence.schema()


def MusicRelease_test():
    from schorg.MusicRelease import MusicReleaseInheritedProperties
    from schorg.MusicRelease import MusicReleaseProperties
    from schorg.MusicRelease import AllProperties
    from schorg.MusicRelease import create_schema_org_model
    from schorg.MusicRelease import MusicRelease

    a = create_schema_org_model(type_=MusicReleaseInheritedProperties)
    b = create_schema_org_model(type_=MusicReleaseProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MusicRelease.schema()


def EmployerAggregateRating_test():
    from schorg.EmployerAggregateRating import EmployerAggregateRatingInheritedProperties
    from schorg.EmployerAggregateRating import EmployerAggregateRatingProperties
    from schorg.EmployerAggregateRating import AllProperties
    from schorg.EmployerAggregateRating import create_schema_org_model
    from schorg.EmployerAggregateRating import EmployerAggregateRating

    a = create_schema_org_model(type_=EmployerAggregateRatingInheritedProperties)
    b = create_schema_org_model(type_=EmployerAggregateRatingProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    EmployerAggregateRating.schema()


def Female_test():
    from schorg.Female import FemaleInheritedProperties
    from schorg.Female import FemaleProperties
    from schorg.Female import AllProperties
    from schorg.Female import create_schema_org_model
    from schorg.Female import Female

    a = create_schema_org_model(type_=FemaleInheritedProperties)
    b = create_schema_org_model(type_=FemaleProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Female.schema()


def ReviewNewsArticle_test():
    from schorg.ReviewNewsArticle import ReviewNewsArticleInheritedProperties
    from schorg.ReviewNewsArticle import ReviewNewsArticleProperties
    from schorg.ReviewNewsArticle import AllProperties
    from schorg.ReviewNewsArticle import create_schema_org_model
    from schorg.ReviewNewsArticle import ReviewNewsArticle

    a = create_schema_org_model(type_=ReviewNewsArticleInheritedProperties)
    b = create_schema_org_model(type_=ReviewNewsArticleProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ReviewNewsArticle.schema()


def SeatingMap_test():
    from schorg.SeatingMap import SeatingMapInheritedProperties
    from schorg.SeatingMap import SeatingMapProperties
    from schorg.SeatingMap import AllProperties
    from schorg.SeatingMap import create_schema_org_model
    from schorg.SeatingMap import SeatingMap

    a = create_schema_org_model(type_=SeatingMapInheritedProperties)
    b = create_schema_org_model(type_=SeatingMapProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    SeatingMap.schema()


def EvidenceLevelB_test():
    from schorg.EvidenceLevelB import EvidenceLevelBInheritedProperties
    from schorg.EvidenceLevelB import EvidenceLevelBProperties
    from schorg.EvidenceLevelB import AllProperties
    from schorg.EvidenceLevelB import create_schema_org_model
    from schorg.EvidenceLevelB import EvidenceLevelB

    a = create_schema_org_model(type_=EvidenceLevelBInheritedProperties)
    b = create_schema_org_model(type_=EvidenceLevelBProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    EvidenceLevelB.schema()


def BodyMeasurementBust_test():
    from schorg.BodyMeasurementBust import BodyMeasurementBustInheritedProperties
    from schorg.BodyMeasurementBust import BodyMeasurementBustProperties
    from schorg.BodyMeasurementBust import AllProperties
    from schorg.BodyMeasurementBust import create_schema_org_model
    from schorg.BodyMeasurementBust import BodyMeasurementBust

    a = create_schema_org_model(type_=BodyMeasurementBustInheritedProperties)
    b = create_schema_org_model(type_=BodyMeasurementBustProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    BodyMeasurementBust.schema()


def HomeGoodsStore_test():
    from schorg.HomeGoodsStore import HomeGoodsStoreInheritedProperties
    from schorg.HomeGoodsStore import HomeGoodsStoreProperties
    from schorg.HomeGoodsStore import AllProperties
    from schorg.HomeGoodsStore import create_schema_org_model
    from schorg.HomeGoodsStore import HomeGoodsStore

    a = create_schema_org_model(type_=HomeGoodsStoreInheritedProperties)
    b = create_schema_org_model(type_=HomeGoodsStoreProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    HomeGoodsStore.schema()


def ClaimReview_test():
    from schorg.ClaimReview import ClaimReviewInheritedProperties
    from schorg.ClaimReview import ClaimReviewProperties
    from schorg.ClaimReview import AllProperties
    from schorg.ClaimReview import create_schema_org_model
    from schorg.ClaimReview import ClaimReview

    a = create_schema_org_model(type_=ClaimReviewInheritedProperties)
    b = create_schema_org_model(type_=ClaimReviewProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ClaimReview.schema()


def NutritionInformation_test():
    from schorg.NutritionInformation import NutritionInformationInheritedProperties
    from schorg.NutritionInformation import NutritionInformationProperties
    from schorg.NutritionInformation import AllProperties
    from schorg.NutritionInformation import create_schema_org_model
    from schorg.NutritionInformation import NutritionInformation

    a = create_schema_org_model(type_=NutritionInformationInheritedProperties)
    b = create_schema_org_model(type_=NutritionInformationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    NutritionInformation.schema()


def CT_test():
    from schorg.CT import CTInheritedProperties
    from schorg.CT import CTProperties
    from schorg.CT import AllProperties
    from schorg.CT import create_schema_org_model
    from schorg.CT import CT

    a = create_schema_org_model(type_=CTInheritedProperties)
    b = create_schema_org_model(type_=CTProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    CT.schema()


def Nonprofit527_test():
    from schorg.Nonprofit527 import Nonprofit527InheritedProperties
    from schorg.Nonprofit527 import Nonprofit527Properties
    from schorg.Nonprofit527 import AllProperties
    from schorg.Nonprofit527 import create_schema_org_model
    from schorg.Nonprofit527 import Nonprofit527

    a = create_schema_org_model(type_=Nonprofit527InheritedProperties)
    b = create_schema_org_model(type_=Nonprofit527Properties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Nonprofit527.schema()


def MenuItem_test():
    from schorg.MenuItem import MenuItemInheritedProperties
    from schorg.MenuItem import MenuItemProperties
    from schorg.MenuItem import AllProperties
    from schorg.MenuItem import create_schema_org_model
    from schorg.MenuItem import MenuItem

    a = create_schema_org_model(type_=MenuItemInheritedProperties)
    b = create_schema_org_model(type_=MenuItemProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MenuItem.schema()


def OnlineEventAttendanceMode_test():
    from schorg.OnlineEventAttendanceMode import OnlineEventAttendanceModeInheritedProperties
    from schorg.OnlineEventAttendanceMode import OnlineEventAttendanceModeProperties
    from schorg.OnlineEventAttendanceMode import AllProperties
    from schorg.OnlineEventAttendanceMode import create_schema_org_model
    from schorg.OnlineEventAttendanceMode import OnlineEventAttendanceMode

    a = create_schema_org_model(type_=OnlineEventAttendanceModeInheritedProperties)
    b = create_schema_org_model(type_=OnlineEventAttendanceModeProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    OnlineEventAttendanceMode.schema()


def SizeSystemImperial_test():
    from schorg.SizeSystemImperial import SizeSystemImperialInheritedProperties
    from schorg.SizeSystemImperial import SizeSystemImperialProperties
    from schorg.SizeSystemImperial import AllProperties
    from schorg.SizeSystemImperial import create_schema_org_model
    from schorg.SizeSystemImperial import SizeSystemImperial

    a = create_schema_org_model(type_=SizeSystemImperialInheritedProperties)
    b = create_schema_org_model(type_=SizeSystemImperialProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    SizeSystemImperial.schema()


def Recruiting_test():
    from schorg.Recruiting import RecruitingInheritedProperties
    from schorg.Recruiting import RecruitingProperties
    from schorg.Recruiting import AllProperties
    from schorg.Recruiting import create_schema_org_model
    from schorg.Recruiting import Recruiting

    a = create_schema_org_model(type_=RecruitingInheritedProperties)
    b = create_schema_org_model(type_=RecruitingProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Recruiting.schema()


def Nonprofit501c23_test():
    from schorg.Nonprofit501c23 import Nonprofit501c23InheritedProperties
    from schorg.Nonprofit501c23 import Nonprofit501c23Properties
    from schorg.Nonprofit501c23 import AllProperties
    from schorg.Nonprofit501c23 import create_schema_org_model
    from schorg.Nonprofit501c23 import Nonprofit501c23

    a = create_schema_org_model(type_=Nonprofit501c23InheritedProperties)
    b = create_schema_org_model(type_=Nonprofit501c23Properties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Nonprofit501c23.schema()


def PotentialActionStatus_test():
    from schorg.PotentialActionStatus import PotentialActionStatusInheritedProperties
    from schorg.PotentialActionStatus import PotentialActionStatusProperties
    from schorg.PotentialActionStatus import AllProperties
    from schorg.PotentialActionStatus import create_schema_org_model
    from schorg.PotentialActionStatus import PotentialActionStatus

    a = create_schema_org_model(type_=PotentialActionStatusInheritedProperties)
    b = create_schema_org_model(type_=PotentialActionStatusProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    PotentialActionStatus.schema()


def OneTimePayments_test():
    from schorg.OneTimePayments import OneTimePaymentsInheritedProperties
    from schorg.OneTimePayments import OneTimePaymentsProperties
    from schorg.OneTimePayments import AllProperties
    from schorg.OneTimePayments import create_schema_org_model
    from schorg.OneTimePayments import OneTimePayments

    a = create_schema_org_model(type_=OneTimePaymentsInheritedProperties)
    b = create_schema_org_model(type_=OneTimePaymentsProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    OneTimePayments.schema()


def TravelAction_test():
    from schorg.TravelAction import TravelActionInheritedProperties
    from schorg.TravelAction import TravelActionProperties
    from schorg.TravelAction import AllProperties
    from schorg.TravelAction import create_schema_org_model
    from schorg.TravelAction import TravelAction

    a = create_schema_org_model(type_=TravelActionInheritedProperties)
    b = create_schema_org_model(type_=TravelActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    TravelAction.schema()


def EUEnergyEfficiencyCategoryD_test():
    from schorg.EUEnergyEfficiencyCategoryD import EUEnergyEfficiencyCategoryDInheritedProperties
    from schorg.EUEnergyEfficiencyCategoryD import EUEnergyEfficiencyCategoryDProperties
    from schorg.EUEnergyEfficiencyCategoryD import AllProperties
    from schorg.EUEnergyEfficiencyCategoryD import create_schema_org_model
    from schorg.EUEnergyEfficiencyCategoryD import EUEnergyEfficiencyCategoryD

    a = create_schema_org_model(type_=EUEnergyEfficiencyCategoryDInheritedProperties)
    b = create_schema_org_model(type_=EUEnergyEfficiencyCategoryDProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    EUEnergyEfficiencyCategoryD.schema()


def MaximumDoseSchedule_test():
    from schorg.MaximumDoseSchedule import MaximumDoseScheduleInheritedProperties
    from schorg.MaximumDoseSchedule import MaximumDoseScheduleProperties
    from schorg.MaximumDoseSchedule import AllProperties
    from schorg.MaximumDoseSchedule import create_schema_org_model
    from schorg.MaximumDoseSchedule import MaximumDoseSchedule

    a = create_schema_org_model(type_=MaximumDoseScheduleInheritedProperties)
    b = create_schema_org_model(type_=MaximumDoseScheduleProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MaximumDoseSchedule.schema()


def Brand_test():
    from schorg.Brand import BrandInheritedProperties
    from schorg.Brand import BrandProperties
    from schorg.Brand import AllProperties
    from schorg.Brand import create_schema_org_model
    from schorg.Brand import Brand

    a = create_schema_org_model(type_=BrandInheritedProperties)
    b = create_schema_org_model(type_=BrandProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Brand.schema()


def HowToSupply_test():
    from schorg.HowToSupply import HowToSupplyInheritedProperties
    from schorg.HowToSupply import HowToSupplyProperties
    from schorg.HowToSupply import AllProperties
    from schorg.HowToSupply import create_schema_org_model
    from schorg.HowToSupply import HowToSupply

    a = create_schema_org_model(type_=HowToSupplyInheritedProperties)
    b = create_schema_org_model(type_=HowToSupplyProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    HowToSupply.schema()


def ZoneBoardingPolicy_test():
    from schorg.ZoneBoardingPolicy import ZoneBoardingPolicyInheritedProperties
    from schorg.ZoneBoardingPolicy import ZoneBoardingPolicyProperties
    from schorg.ZoneBoardingPolicy import AllProperties
    from schorg.ZoneBoardingPolicy import create_schema_org_model
    from schorg.ZoneBoardingPolicy import ZoneBoardingPolicy

    a = create_schema_org_model(type_=ZoneBoardingPolicyInheritedProperties)
    b = create_schema_org_model(type_=ZoneBoardingPolicyProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ZoneBoardingPolicy.schema()


def Nonprofit501f_test():
    from schorg.Nonprofit501f import Nonprofit501fInheritedProperties
    from schorg.Nonprofit501f import Nonprofit501fProperties
    from schorg.Nonprofit501f import AllProperties
    from schorg.Nonprofit501f import create_schema_org_model
    from schorg.Nonprofit501f import Nonprofit501f

    a = create_schema_org_model(type_=Nonprofit501fInheritedProperties)
    b = create_schema_org_model(type_=Nonprofit501fProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Nonprofit501f.schema()


def ParcelDelivery_test():
    from schorg.ParcelDelivery import ParcelDeliveryInheritedProperties
    from schorg.ParcelDelivery import ParcelDeliveryProperties
    from schorg.ParcelDelivery import AllProperties
    from schorg.ParcelDelivery import create_schema_org_model
    from schorg.ParcelDelivery import ParcelDelivery

    a = create_schema_org_model(type_=ParcelDeliveryInheritedProperties)
    b = create_schema_org_model(type_=ParcelDeliveryProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ParcelDelivery.schema()


def SeekToAction_test():
    from schorg.SeekToAction import SeekToActionInheritedProperties
    from schorg.SeekToAction import SeekToActionProperties
    from schorg.SeekToAction import AllProperties
    from schorg.SeekToAction import create_schema_org_model
    from schorg.SeekToAction import SeekToAction

    a = create_schema_org_model(type_=SeekToActionInheritedProperties)
    b = create_schema_org_model(type_=SeekToActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    SeekToAction.schema()


def Balance_test():
    from schorg.Balance import BalanceInheritedProperties
    from schorg.Balance import BalanceProperties
    from schorg.Balance import AllProperties
    from schorg.Balance import create_schema_org_model
    from schorg.Balance import Balance

    a = create_schema_org_model(type_=BalanceInheritedProperties)
    b = create_schema_org_model(type_=BalanceProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Balance.schema()


def InForce_test():
    from schorg.InForce import InForceInheritedProperties
    from schorg.InForce import InForceProperties
    from schorg.InForce import AllProperties
    from schorg.InForce import create_schema_org_model
    from schorg.InForce import InForce

    a = create_schema_org_model(type_=InForceInheritedProperties)
    b = create_schema_org_model(type_=InForceProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    InForce.schema()


def AuthorizeAction_test():
    from schorg.AuthorizeAction import AuthorizeActionInheritedProperties
    from schorg.AuthorizeAction import AuthorizeActionProperties
    from schorg.AuthorizeAction import AllProperties
    from schorg.AuthorizeAction import create_schema_org_model
    from schorg.AuthorizeAction import AuthorizeAction

    a = create_schema_org_model(type_=AuthorizeActionInheritedProperties)
    b = create_schema_org_model(type_=AuthorizeActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    AuthorizeAction.schema()


def InvoicePrice_test():
    from schorg.InvoicePrice import InvoicePriceInheritedProperties
    from schorg.InvoicePrice import InvoicePriceProperties
    from schorg.InvoicePrice import AllProperties
    from schorg.InvoicePrice import create_schema_org_model
    from schorg.InvoicePrice import InvoicePrice

    a = create_schema_org_model(type_=InvoicePriceInheritedProperties)
    b = create_schema_org_model(type_=InvoicePriceProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    InvoicePrice.schema()


def Neurologic_test():
    from schorg.Neurologic import NeurologicInheritedProperties
    from schorg.Neurologic import NeurologicProperties
    from schorg.Neurologic import AllProperties
    from schorg.Neurologic import create_schema_org_model
    from schorg.Neurologic import Neurologic

    a = create_schema_org_model(type_=NeurologicInheritedProperties)
    b = create_schema_org_model(type_=NeurologicProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Neurologic.schema()


def CassetteFormat_test():
    from schorg.CassetteFormat import CassetteFormatInheritedProperties
    from schorg.CassetteFormat import CassetteFormatProperties
    from schorg.CassetteFormat import AllProperties
    from schorg.CassetteFormat import create_schema_org_model
    from schorg.CassetteFormat import CassetteFormat

    a = create_schema_org_model(type_=CassetteFormatInheritedProperties)
    b = create_schema_org_model(type_=CassetteFormatProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    CassetteFormat.schema()


def TraditionalChinese_test():
    from schorg.TraditionalChinese import TraditionalChineseInheritedProperties
    from schorg.TraditionalChinese import TraditionalChineseProperties
    from schorg.TraditionalChinese import AllProperties
    from schorg.TraditionalChinese import create_schema_org_model
    from schorg.TraditionalChinese import TraditionalChinese

    a = create_schema_org_model(type_=TraditionalChineseInheritedProperties)
    b = create_schema_org_model(type_=TraditionalChineseProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    TraditionalChinese.schema()


def Homeopathic_test():
    from schorg.Homeopathic import HomeopathicInheritedProperties
    from schorg.Homeopathic import HomeopathicProperties
    from schorg.Homeopathic import AllProperties
    from schorg.Homeopathic import create_schema_org_model
    from schorg.Homeopathic import Homeopathic

    a = create_schema_org_model(type_=HomeopathicInheritedProperties)
    b = create_schema_org_model(type_=HomeopathicProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Homeopathic.schema()


def TouristAttraction_test():
    from schorg.TouristAttraction import TouristAttractionInheritedProperties
    from schorg.TouristAttraction import TouristAttractionProperties
    from schorg.TouristAttraction import AllProperties
    from schorg.TouristAttraction import create_schema_org_model
    from schorg.TouristAttraction import TouristAttraction

    a = create_schema_org_model(type_=TouristAttractionInheritedProperties)
    b = create_schema_org_model(type_=TouristAttractionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    TouristAttraction.schema()


def Energy_test():
    from schorg.Energy import EnergyInheritedProperties
    from schorg.Energy import EnergyProperties
    from schorg.Energy import AllProperties
    from schorg.Energy import create_schema_org_model
    from schorg.Energy import Energy

    a = create_schema_org_model(type_=EnergyInheritedProperties)
    b = create_schema_org_model(type_=EnergyProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Energy.schema()


def Nonprofit501c19_test():
    from schorg.Nonprofit501c19 import Nonprofit501c19InheritedProperties
    from schorg.Nonprofit501c19 import Nonprofit501c19Properties
    from schorg.Nonprofit501c19 import AllProperties
    from schorg.Nonprofit501c19 import create_schema_org_model
    from schorg.Nonprofit501c19 import Nonprofit501c19

    a = create_schema_org_model(type_=Nonprofit501c19InheritedProperties)
    b = create_schema_org_model(type_=Nonprofit501c19Properties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Nonprofit501c19.schema()


def OfferForPurchase_test():
    from schorg.OfferForPurchase import OfferForPurchaseInheritedProperties
    from schorg.OfferForPurchase import OfferForPurchaseProperties
    from schorg.OfferForPurchase import AllProperties
    from schorg.OfferForPurchase import create_schema_org_model
    from schorg.OfferForPurchase import OfferForPurchase

    a = create_schema_org_model(type_=OfferForPurchaseInheritedProperties)
    b = create_schema_org_model(type_=OfferForPurchaseProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    OfferForPurchase.schema()


def EntryPoint_test():
    from schorg.EntryPoint import EntryPointInheritedProperties
    from schorg.EntryPoint import EntryPointProperties
    from schorg.EntryPoint import AllProperties
    from schorg.EntryPoint import create_schema_org_model
    from schorg.EntryPoint import EntryPoint

    a = create_schema_org_model(type_=EntryPointInheritedProperties)
    b = create_schema_org_model(type_=EntryPointProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    EntryPoint.schema()


def OfficialLegalValue_test():
    from schorg.OfficialLegalValue import OfficialLegalValueInheritedProperties
    from schorg.OfficialLegalValue import OfficialLegalValueProperties
    from schorg.OfficialLegalValue import AllProperties
    from schorg.OfficialLegalValue import create_schema_org_model
    from schorg.OfficialLegalValue import OfficialLegalValue

    a = create_schema_org_model(type_=OfficialLegalValueInheritedProperties)
    b = create_schema_org_model(type_=OfficialLegalValueProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    OfficialLegalValue.schema()


def HowItWorksHealthAspect_test():
    from schorg.HowItWorksHealthAspect import HowItWorksHealthAspectInheritedProperties
    from schorg.HowItWorksHealthAspect import HowItWorksHealthAspectProperties
    from schorg.HowItWorksHealthAspect import AllProperties
    from schorg.HowItWorksHealthAspect import create_schema_org_model
    from schorg.HowItWorksHealthAspect import HowItWorksHealthAspect

    a = create_schema_org_model(type_=HowItWorksHealthAspectInheritedProperties)
    b = create_schema_org_model(type_=HowItWorksHealthAspectProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    HowItWorksHealthAspect.schema()


def Table_test():
    from schorg.Table import TableInheritedProperties
    from schorg.Table import TableProperties
    from schorg.Table import AllProperties
    from schorg.Table import create_schema_org_model
    from schorg.Table import Table

    a = create_schema_org_model(type_=TableInheritedProperties)
    b = create_schema_org_model(type_=TableProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Table.schema()


def EnrollingByInvitation_test():
    from schorg.EnrollingByInvitation import EnrollingByInvitationInheritedProperties
    from schorg.EnrollingByInvitation import EnrollingByInvitationProperties
    from schorg.EnrollingByInvitation import AllProperties
    from schorg.EnrollingByInvitation import create_schema_org_model
    from schorg.EnrollingByInvitation import EnrollingByInvitation

    a = create_schema_org_model(type_=EnrollingByInvitationInheritedProperties)
    b = create_schema_org_model(type_=EnrollingByInvitationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    EnrollingByInvitation.schema()


def MayTreatHealthAspect_test():
    from schorg.MayTreatHealthAspect import MayTreatHealthAspectInheritedProperties
    from schorg.MayTreatHealthAspect import MayTreatHealthAspectProperties
    from schorg.MayTreatHealthAspect import AllProperties
    from schorg.MayTreatHealthAspect import create_schema_org_model
    from schorg.MayTreatHealthAspect import MayTreatHealthAspect

    a = create_schema_org_model(type_=MayTreatHealthAspectInheritedProperties)
    b = create_schema_org_model(type_=MayTreatHealthAspectProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MayTreatHealthAspect.schema()


def OrderReturned_test():
    from schorg.OrderReturned import OrderReturnedInheritedProperties
    from schorg.OrderReturned import OrderReturnedProperties
    from schorg.OrderReturned import AllProperties
    from schorg.OrderReturned import create_schema_org_model
    from schorg.OrderReturned import OrderReturned

    a = create_schema_org_model(type_=OrderReturnedInheritedProperties)
    b = create_schema_org_model(type_=OrderReturnedProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    OrderReturned.schema()


def FoodEvent_test():
    from schorg.FoodEvent import FoodEventInheritedProperties
    from schorg.FoodEvent import FoodEventProperties
    from schorg.FoodEvent import AllProperties
    from schorg.FoodEvent import create_schema_org_model
    from schorg.FoodEvent import FoodEvent

    a = create_schema_org_model(type_=FoodEventInheritedProperties)
    b = create_schema_org_model(type_=FoodEventProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    FoodEvent.schema()


def CrossSectional_test():
    from schorg.CrossSectional import CrossSectionalInheritedProperties
    from schorg.CrossSectional import CrossSectionalProperties
    from schorg.CrossSectional import AllProperties
    from schorg.CrossSectional import create_schema_org_model
    from schorg.CrossSectional import CrossSectional

    a = create_schema_org_model(type_=CrossSectionalInheritedProperties)
    b = create_schema_org_model(type_=CrossSectionalProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    CrossSectional.schema()


def AutoDealer_test():
    from schorg.AutoDealer import AutoDealerInheritedProperties
    from schorg.AutoDealer import AutoDealerProperties
    from schorg.AutoDealer import AllProperties
    from schorg.AutoDealer import create_schema_org_model
    from schorg.AutoDealer import AutoDealer

    a = create_schema_org_model(type_=AutoDealerInheritedProperties)
    b = create_schema_org_model(type_=AutoDealerProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    AutoDealer.schema()


def InsuranceAgency_test():
    from schorg.InsuranceAgency import InsuranceAgencyInheritedProperties
    from schorg.InsuranceAgency import InsuranceAgencyProperties
    from schorg.InsuranceAgency import AllProperties
    from schorg.InsuranceAgency import create_schema_org_model
    from schorg.InsuranceAgency import InsuranceAgency

    a = create_schema_org_model(type_=InsuranceAgencyInheritedProperties)
    b = create_schema_org_model(type_=InsuranceAgencyProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    InsuranceAgency.schema()


def MusicRecording_test():
    from schorg.MusicRecording import MusicRecordingInheritedProperties
    from schorg.MusicRecording import MusicRecordingProperties
    from schorg.MusicRecording import AllProperties
    from schorg.MusicRecording import create_schema_org_model
    from schorg.MusicRecording import MusicRecording

    a = create_schema_org_model(type_=MusicRecordingInheritedProperties)
    b = create_schema_org_model(type_=MusicRecordingProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MusicRecording.schema()


def HalalDiet_test():
    from schorg.HalalDiet import HalalDietInheritedProperties
    from schorg.HalalDiet import HalalDietProperties
    from schorg.HalalDiet import AllProperties
    from schorg.HalalDiet import create_schema_org_model
    from schorg.HalalDiet import HalalDiet

    a = create_schema_org_model(type_=HalalDietInheritedProperties)
    b = create_schema_org_model(type_=HalalDietProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    HalalDiet.schema()


def Time_test():
    from schorg.Time import TimeInheritedProperties
    from schorg.Time import TimeProperties
    from schorg.Time import AllProperties
    from schorg.Time import create_schema_org_model
    from schorg.Time import Time

    a = create_schema_org_model(type_=TimeInheritedProperties)
    b = create_schema_org_model(type_=TimeProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Time.schema()


def WearableSizeGroupBig_test():
    from schorg.WearableSizeGroupBig import WearableSizeGroupBigInheritedProperties
    from schorg.WearableSizeGroupBig import WearableSizeGroupBigProperties
    from schorg.WearableSizeGroupBig import AllProperties
    from schorg.WearableSizeGroupBig import create_schema_org_model
    from schorg.WearableSizeGroupBig import WearableSizeGroupBig

    a = create_schema_org_model(type_=WearableSizeGroupBigInheritedProperties)
    b = create_schema_org_model(type_=WearableSizeGroupBigProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    WearableSizeGroupBig.schema()


def GatedResidenceCommunity_test():
    from schorg.GatedResidenceCommunity import GatedResidenceCommunityInheritedProperties
    from schorg.GatedResidenceCommunity import GatedResidenceCommunityProperties
    from schorg.GatedResidenceCommunity import AllProperties
    from schorg.GatedResidenceCommunity import create_schema_org_model
    from schorg.GatedResidenceCommunity import GatedResidenceCommunity

    a = create_schema_org_model(type_=GatedResidenceCommunityInheritedProperties)
    b = create_schema_org_model(type_=GatedResidenceCommunityProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    GatedResidenceCommunity.schema()


def Diagnostic_test():
    from schorg.Diagnostic import DiagnosticInheritedProperties
    from schorg.Diagnostic import DiagnosticProperties
    from schorg.Diagnostic import AllProperties
    from schorg.Diagnostic import create_schema_org_model
    from schorg.Diagnostic import Diagnostic

    a = create_schema_org_model(type_=DiagnosticInheritedProperties)
    b = create_schema_org_model(type_=DiagnosticProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Diagnostic.schema()


def Courthouse_test():
    from schorg.Courthouse import CourthouseInheritedProperties
    from schorg.Courthouse import CourthouseProperties
    from schorg.Courthouse import AllProperties
    from schorg.Courthouse import create_schema_org_model
    from schorg.Courthouse import Courthouse

    a = create_schema_org_model(type_=CourthouseInheritedProperties)
    b = create_schema_org_model(type_=CourthouseProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Courthouse.schema()


def ComedyClub_test():
    from schorg.ComedyClub import ComedyClubInheritedProperties
    from schorg.ComedyClub import ComedyClubProperties
    from schorg.ComedyClub import AllProperties
    from schorg.ComedyClub import create_schema_org_model
    from schorg.ComedyClub import ComedyClub

    a = create_schema_org_model(type_=ComedyClubInheritedProperties)
    b = create_schema_org_model(type_=ComedyClubProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ComedyClub.schema()


def AerobicActivity_test():
    from schorg.AerobicActivity import AerobicActivityInheritedProperties
    from schorg.AerobicActivity import AerobicActivityProperties
    from schorg.AerobicActivity import AllProperties
    from schorg.AerobicActivity import create_schema_org_model
    from schorg.AerobicActivity import AerobicActivity

    a = create_schema_org_model(type_=AerobicActivityInheritedProperties)
    b = create_schema_org_model(type_=AerobicActivityProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    AerobicActivity.schema()


def SpreadsheetDigitalDocument_test():
    from schorg.SpreadsheetDigitalDocument import SpreadsheetDigitalDocumentInheritedProperties
    from schorg.SpreadsheetDigitalDocument import SpreadsheetDigitalDocumentProperties
    from schorg.SpreadsheetDigitalDocument import AllProperties
    from schorg.SpreadsheetDigitalDocument import create_schema_org_model
    from schorg.SpreadsheetDigitalDocument import SpreadsheetDigitalDocument

    a = create_schema_org_model(type_=SpreadsheetDigitalDocumentInheritedProperties)
    b = create_schema_org_model(type_=SpreadsheetDigitalDocumentProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    SpreadsheetDigitalDocument.schema()


def Locksmith_test():
    from schorg.Locksmith import LocksmithInheritedProperties
    from schorg.Locksmith import LocksmithProperties
    from schorg.Locksmith import AllProperties
    from schorg.Locksmith import create_schema_org_model
    from schorg.Locksmith import Locksmith

    a = create_schema_org_model(type_=LocksmithInheritedProperties)
    b = create_schema_org_model(type_=LocksmithProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Locksmith.schema()


def Boolean_test():
    from schorg.Boolean import BooleanInheritedProperties
    from schorg.Boolean import BooleanProperties
    from schorg.Boolean import AllProperties
    from schorg.Boolean import create_schema_org_model
    from schorg.Boolean import Boolean

    a = create_schema_org_model(type_=BooleanInheritedProperties)
    b = create_schema_org_model(type_=BooleanProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Boolean.schema()


def True__test():
    from schorg.True_ import True_InheritedProperties
    from schorg.True_ import True_Properties
    from schorg.True_ import AllProperties
    from schorg.True_ import create_schema_org_model
    from schorg.True_ import True_

    a = create_schema_org_model(type_=True_InheritedProperties)
    b = create_schema_org_model(type_=True_Properties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    True_.schema()


def DietarySupplement_test():
    from schorg.DietarySupplement import DietarySupplementInheritedProperties
    from schorg.DietarySupplement import DietarySupplementProperties
    from schorg.DietarySupplement import AllProperties
    from schorg.DietarySupplement import create_schema_org_model
    from schorg.DietarySupplement import DietarySupplement

    a = create_schema_org_model(type_=DietarySupplementInheritedProperties)
    b = create_schema_org_model(type_=DietarySupplementProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    DietarySupplement.schema()


def WeaponConsideration_test():
    from schorg.WeaponConsideration import WeaponConsiderationInheritedProperties
    from schorg.WeaponConsideration import WeaponConsiderationProperties
    from schorg.WeaponConsideration import AllProperties
    from schorg.WeaponConsideration import create_schema_org_model
    from schorg.WeaponConsideration import WeaponConsideration

    a = create_schema_org_model(type_=WeaponConsiderationInheritedProperties)
    b = create_schema_org_model(type_=WeaponConsiderationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    WeaponConsideration.schema()


def WearableSizeSystemUS_test():
    from schorg.WearableSizeSystemUS import WearableSizeSystemUSInheritedProperties
    from schorg.WearableSizeSystemUS import WearableSizeSystemUSProperties
    from schorg.WearableSizeSystemUS import AllProperties
    from schorg.WearableSizeSystemUS import create_schema_org_model
    from schorg.WearableSizeSystemUS import WearableSizeSystemUS

    a = create_schema_org_model(type_=WearableSizeSystemUSInheritedProperties)
    b = create_schema_org_model(type_=WearableSizeSystemUSProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    WearableSizeSystemUS.schema()


def Withdrawn_test():
    from schorg.Withdrawn import WithdrawnInheritedProperties
    from schorg.Withdrawn import WithdrawnProperties
    from schorg.Withdrawn import AllProperties
    from schorg.Withdrawn import create_schema_org_model
    from schorg.Withdrawn import Withdrawn

    a = create_schema_org_model(type_=WithdrawnInheritedProperties)
    b = create_schema_org_model(type_=WithdrawnProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Withdrawn.schema()


def OwnershipInfo_test():
    from schorg.OwnershipInfo import OwnershipInfoInheritedProperties
    from schorg.OwnershipInfo import OwnershipInfoProperties
    from schorg.OwnershipInfo import AllProperties
    from schorg.OwnershipInfo import create_schema_org_model
    from schorg.OwnershipInfo import OwnershipInfo

    a = create_schema_org_model(type_=OwnershipInfoInheritedProperties)
    b = create_schema_org_model(type_=OwnershipInfoProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    OwnershipInfo.schema()


def Completed_test():
    from schorg.Completed import CompletedInheritedProperties
    from schorg.Completed import CompletedProperties
    from schorg.Completed import AllProperties
    from schorg.Completed import create_schema_org_model
    from schorg.Completed import Completed

    a = create_schema_org_model(type_=CompletedInheritedProperties)
    b = create_schema_org_model(type_=CompletedProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Completed.schema()


def NoteDigitalDocument_test():
    from schorg.NoteDigitalDocument import NoteDigitalDocumentInheritedProperties
    from schorg.NoteDigitalDocument import NoteDigitalDocumentProperties
    from schorg.NoteDigitalDocument import AllProperties
    from schorg.NoteDigitalDocument import create_schema_org_model
    from schorg.NoteDigitalDocument import NoteDigitalDocument

    a = create_schema_org_model(type_=NoteDigitalDocumentInheritedProperties)
    b = create_schema_org_model(type_=NoteDigitalDocumentProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    NoteDigitalDocument.schema()


def Float_test():
    from schorg.Float import FloatInheritedProperties
    from schorg.Float import FloatProperties
    from schorg.Float import AllProperties
    from schorg.Float import create_schema_org_model
    from schorg.Float import Float

    a = create_schema_org_model(type_=FloatInheritedProperties)
    b = create_schema_org_model(type_=FloatProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Float.schema()


def Consortium_test():
    from schorg.Consortium import ConsortiumInheritedProperties
    from schorg.Consortium import ConsortiumProperties
    from schorg.Consortium import AllProperties
    from schorg.Consortium import create_schema_org_model
    from schorg.Consortium import Consortium

    a = create_schema_org_model(type_=ConsortiumInheritedProperties)
    b = create_schema_org_model(type_=ConsortiumProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Consortium.schema()


def PrescriptionOnly_test():
    from schorg.PrescriptionOnly import PrescriptionOnlyInheritedProperties
    from schorg.PrescriptionOnly import PrescriptionOnlyProperties
    from schorg.PrescriptionOnly import AllProperties
    from schorg.PrescriptionOnly import create_schema_org_model
    from schorg.PrescriptionOnly import PrescriptionOnly

    a = create_schema_org_model(type_=PrescriptionOnlyInheritedProperties)
    b = create_schema_org_model(type_=PrescriptionOnlyProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    PrescriptionOnly.schema()


def GovernmentOrganization_test():
    from schorg.GovernmentOrganization import GovernmentOrganizationInheritedProperties
    from schorg.GovernmentOrganization import GovernmentOrganizationProperties
    from schorg.GovernmentOrganization import AllProperties
    from schorg.GovernmentOrganization import create_schema_org_model
    from schorg.GovernmentOrganization import GovernmentOrganization

    a = create_schema_org_model(type_=GovernmentOrganizationInheritedProperties)
    b = create_schema_org_model(type_=GovernmentOrganizationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    GovernmentOrganization.schema()


def CurrencyConversionService_test():
    from schorg.CurrencyConversionService import CurrencyConversionServiceInheritedProperties
    from schorg.CurrencyConversionService import CurrencyConversionServiceProperties
    from schorg.CurrencyConversionService import AllProperties
    from schorg.CurrencyConversionService import create_schema_org_model
    from schorg.CurrencyConversionService import CurrencyConversionService

    a = create_schema_org_model(type_=CurrencyConversionServiceInheritedProperties)
    b = create_schema_org_model(type_=CurrencyConversionServiceProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    CurrencyConversionService.schema()


def UnincorporatedAssociationCharity_test():
    from schorg.UnincorporatedAssociationCharity import UnincorporatedAssociationCharityInheritedProperties
    from schorg.UnincorporatedAssociationCharity import UnincorporatedAssociationCharityProperties
    from schorg.UnincorporatedAssociationCharity import AllProperties
    from schorg.UnincorporatedAssociationCharity import create_schema_org_model
    from schorg.UnincorporatedAssociationCharity import UnincorporatedAssociationCharity

    a = create_schema_org_model(type_=UnincorporatedAssociationCharityInheritedProperties)
    b = create_schema_org_model(type_=UnincorporatedAssociationCharityProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    UnincorporatedAssociationCharity.schema()


def WearableSizeGroupGirls_test():
    from schorg.WearableSizeGroupGirls import WearableSizeGroupGirlsInheritedProperties
    from schorg.WearableSizeGroupGirls import WearableSizeGroupGirlsProperties
    from schorg.WearableSizeGroupGirls import AllProperties
    from schorg.WearableSizeGroupGirls import create_schema_org_model
    from schorg.WearableSizeGroupGirls import WearableSizeGroupGirls

    a = create_schema_org_model(type_=WearableSizeGroupGirlsInheritedProperties)
    b = create_schema_org_model(type_=WearableSizeGroupGirlsProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    WearableSizeGroupGirls.schema()


def AssignAction_test():
    from schorg.AssignAction import AssignActionInheritedProperties
    from schorg.AssignAction import AssignActionProperties
    from schorg.AssignAction import AllProperties
    from schorg.AssignAction import create_schema_org_model
    from schorg.AssignAction import AssignAction

    a = create_schema_org_model(type_=AssignActionInheritedProperties)
    b = create_schema_org_model(type_=AssignActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    AssignAction.schema()


def DigitalDocumentPermission_test():
    from schorg.DigitalDocumentPermission import DigitalDocumentPermissionInheritedProperties
    from schorg.DigitalDocumentPermission import DigitalDocumentPermissionProperties
    from schorg.DigitalDocumentPermission import AllProperties
    from schorg.DigitalDocumentPermission import create_schema_org_model
    from schorg.DigitalDocumentPermission import DigitalDocumentPermission

    a = create_schema_org_model(type_=DigitalDocumentPermissionInheritedProperties)
    b = create_schema_org_model(type_=DigitalDocumentPermissionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    DigitalDocumentPermission.schema()


def BookmarkAction_test():
    from schorg.BookmarkAction import BookmarkActionInheritedProperties
    from schorg.BookmarkAction import BookmarkActionProperties
    from schorg.BookmarkAction import AllProperties
    from schorg.BookmarkAction import create_schema_org_model
    from schorg.BookmarkAction import BookmarkAction

    a = create_schema_org_model(type_=BookmarkActionInheritedProperties)
    b = create_schema_org_model(type_=BookmarkActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    BookmarkAction.schema()


def BedDetails_test():
    from schorg.BedDetails import BedDetailsInheritedProperties
    from schorg.BedDetails import BedDetailsProperties
    from schorg.BedDetails import AllProperties
    from schorg.BedDetails import create_schema_org_model
    from schorg.BedDetails import BedDetails

    a = create_schema_org_model(type_=BedDetailsInheritedProperties)
    b = create_schema_org_model(type_=BedDetailsProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    BedDetails.schema()


def ReturnLabelCustomerResponsibility_test():
    from schorg.ReturnLabelCustomerResponsibility import ReturnLabelCustomerResponsibilityInheritedProperties
    from schorg.ReturnLabelCustomerResponsibility import ReturnLabelCustomerResponsibilityProperties
    from schorg.ReturnLabelCustomerResponsibility import AllProperties
    from schorg.ReturnLabelCustomerResponsibility import create_schema_org_model
    from schorg.ReturnLabelCustomerResponsibility import ReturnLabelCustomerResponsibility

    a = create_schema_org_model(type_=ReturnLabelCustomerResponsibilityInheritedProperties)
    b = create_schema_org_model(type_=ReturnLabelCustomerResponsibilityProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ReturnLabelCustomerResponsibility.schema()


def EventPostponed_test():
    from schorg.EventPostponed import EventPostponedInheritedProperties
    from schorg.EventPostponed import EventPostponedProperties
    from schorg.EventPostponed import AllProperties
    from schorg.EventPostponed import create_schema_org_model
    from schorg.EventPostponed import EventPostponed

    a = create_schema_org_model(type_=EventPostponedInheritedProperties)
    b = create_schema_org_model(type_=EventPostponedProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    EventPostponed.schema()


def Psychiatric_test():
    from schorg.Psychiatric import PsychiatricInheritedProperties
    from schorg.Psychiatric import PsychiatricProperties
    from schorg.Psychiatric import AllProperties
    from schorg.Psychiatric import create_schema_org_model
    from schorg.Psychiatric import Psychiatric

    a = create_schema_org_model(type_=PsychiatricInheritedProperties)
    b = create_schema_org_model(type_=PsychiatricProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Psychiatric.schema()


def Muscle_test():
    from schorg.Muscle import MuscleInheritedProperties
    from schorg.Muscle import MuscleProperties
    from schorg.Muscle import AllProperties
    from schorg.Muscle import create_schema_org_model
    from schorg.Muscle import Muscle

    a = create_schema_org_model(type_=MuscleInheritedProperties)
    b = create_schema_org_model(type_=MuscleProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Muscle.schema()


def Ultrasound_test():
    from schorg.Ultrasound import UltrasoundInheritedProperties
    from schorg.Ultrasound import UltrasoundProperties
    from schorg.Ultrasound import AllProperties
    from schorg.Ultrasound import create_schema_org_model
    from schorg.Ultrasound import Ultrasound

    a = create_schema_org_model(type_=UltrasoundInheritedProperties)
    b = create_schema_org_model(type_=UltrasoundProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Ultrasound.schema()


def BroadcastFrequencySpecification_test():
    from schorg.BroadcastFrequencySpecification import BroadcastFrequencySpecificationInheritedProperties
    from schorg.BroadcastFrequencySpecification import BroadcastFrequencySpecificationProperties
    from schorg.BroadcastFrequencySpecification import AllProperties
    from schorg.BroadcastFrequencySpecification import create_schema_org_model
    from schorg.BroadcastFrequencySpecification import BroadcastFrequencySpecification

    a = create_schema_org_model(type_=BroadcastFrequencySpecificationInheritedProperties)
    b = create_schema_org_model(type_=BroadcastFrequencySpecificationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    BroadcastFrequencySpecification.schema()


def TripleBlindedTrial_test():
    from schorg.TripleBlindedTrial import TripleBlindedTrialInheritedProperties
    from schorg.TripleBlindedTrial import TripleBlindedTrialProperties
    from schorg.TripleBlindedTrial import AllProperties
    from schorg.TripleBlindedTrial import create_schema_org_model
    from schorg.TripleBlindedTrial import TripleBlindedTrial

    a = create_schema_org_model(type_=TripleBlindedTrialInheritedProperties)
    b = create_schema_org_model(type_=TripleBlindedTrialProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    TripleBlindedTrial.schema()


def AllergiesHealthAspect_test():
    from schorg.AllergiesHealthAspect import AllergiesHealthAspectInheritedProperties
    from schorg.AllergiesHealthAspect import AllergiesHealthAspectProperties
    from schorg.AllergiesHealthAspect import AllProperties
    from schorg.AllergiesHealthAspect import create_schema_org_model
    from schorg.AllergiesHealthAspect import AllergiesHealthAspect

    a = create_schema_org_model(type_=AllergiesHealthAspectInheritedProperties)
    b = create_schema_org_model(type_=AllergiesHealthAspectProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    AllergiesHealthAspect.schema()


def OfflineTemporarily_test():
    from schorg.OfflineTemporarily import OfflineTemporarilyInheritedProperties
    from schorg.OfflineTemporarily import OfflineTemporarilyProperties
    from schorg.OfflineTemporarily import AllProperties
    from schorg.OfflineTemporarily import create_schema_org_model
    from schorg.OfflineTemporarily import OfflineTemporarily

    a = create_schema_org_model(type_=OfflineTemporarilyInheritedProperties)
    b = create_schema_org_model(type_=OfflineTemporarilyProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    OfflineTemporarily.schema()


def Nose_test():
    from schorg.Nose import NoseInheritedProperties
    from schorg.Nose import NoseProperties
    from schorg.Nose import AllProperties
    from schorg.Nose import create_schema_org_model
    from schorg.Nose import Nose

    a = create_schema_org_model(type_=NoseInheritedProperties)
    b = create_schema_org_model(type_=NoseProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Nose.schema()


def FundingAgency_test():
    from schorg.FundingAgency import FundingAgencyInheritedProperties
    from schorg.FundingAgency import FundingAgencyProperties
    from schorg.FundingAgency import AllProperties
    from schorg.FundingAgency import create_schema_org_model
    from schorg.FundingAgency import FundingAgency

    a = create_schema_org_model(type_=FundingAgencyInheritedProperties)
    b = create_schema_org_model(type_=FundingAgencyProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    FundingAgency.schema()


def CourseInstance_test():
    from schorg.CourseInstance import CourseInstanceInheritedProperties
    from schorg.CourseInstance import CourseInstanceProperties
    from schorg.CourseInstance import AllProperties
    from schorg.CourseInstance import create_schema_org_model
    from schorg.CourseInstance import CourseInstance

    a = create_schema_org_model(type_=CourseInstanceInheritedProperties)
    b = create_schema_org_model(type_=CourseInstanceProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    CourseInstance.schema()


def PlasticSurgery_test():
    from schorg.PlasticSurgery import PlasticSurgeryInheritedProperties
    from schorg.PlasticSurgery import PlasticSurgeryProperties
    from schorg.PlasticSurgery import AllProperties
    from schorg.PlasticSurgery import create_schema_org_model
    from schorg.PlasticSurgery import PlasticSurgery

    a = create_schema_org_model(type_=PlasticSurgeryInheritedProperties)
    b = create_schema_org_model(type_=PlasticSurgeryProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    PlasticSurgery.schema()


def Dentistry_test():
    from schorg.Dentistry import DentistryInheritedProperties
    from schorg.Dentistry import DentistryProperties
    from schorg.Dentistry import AllProperties
    from schorg.Dentistry import create_schema_org_model
    from schorg.Dentistry import Dentistry

    a = create_schema_org_model(type_=DentistryInheritedProperties)
    b = create_schema_org_model(type_=DentistryProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Dentistry.schema()


def ExchangeRateSpecification_test():
    from schorg.ExchangeRateSpecification import ExchangeRateSpecificationInheritedProperties
    from schorg.ExchangeRateSpecification import ExchangeRateSpecificationProperties
    from schorg.ExchangeRateSpecification import AllProperties
    from schorg.ExchangeRateSpecification import create_schema_org_model
    from schorg.ExchangeRateSpecification import ExchangeRateSpecification

    a = create_schema_org_model(type_=ExchangeRateSpecificationInheritedProperties)
    b = create_schema_org_model(type_=ExchangeRateSpecificationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ExchangeRateSpecification.schema()


def SportsEvent_test():
    from schorg.SportsEvent import SportsEventInheritedProperties
    from schorg.SportsEvent import SportsEventProperties
    from schorg.SportsEvent import AllProperties
    from schorg.SportsEvent import create_schema_org_model
    from schorg.SportsEvent import SportsEvent

    a = create_schema_org_model(type_=SportsEventInheritedProperties)
    b = create_schema_org_model(type_=SportsEventProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    SportsEvent.schema()


def Nonprofit501c17_test():
    from schorg.Nonprofit501c17 import Nonprofit501c17InheritedProperties
    from schorg.Nonprofit501c17 import Nonprofit501c17Properties
    from schorg.Nonprofit501c17 import AllProperties
    from schorg.Nonprofit501c17 import create_schema_org_model
    from schorg.Nonprofit501c17 import Nonprofit501c17

    a = create_schema_org_model(type_=Nonprofit501c17InheritedProperties)
    b = create_schema_org_model(type_=Nonprofit501c17Properties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Nonprofit501c17.schema()


def MedicalCause_test():
    from schorg.MedicalCause import MedicalCauseInheritedProperties
    from schorg.MedicalCause import MedicalCauseProperties
    from schorg.MedicalCause import AllProperties
    from schorg.MedicalCause import create_schema_org_model
    from schorg.MedicalCause import MedicalCause

    a = create_schema_org_model(type_=MedicalCauseInheritedProperties)
    b = create_schema_org_model(type_=MedicalCauseProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MedicalCause.schema()


def HealthPlanFormulary_test():
    from schorg.HealthPlanFormulary import HealthPlanFormularyInheritedProperties
    from schorg.HealthPlanFormulary import HealthPlanFormularyProperties
    from schorg.HealthPlanFormulary import AllProperties
    from schorg.HealthPlanFormulary import create_schema_org_model
    from schorg.HealthPlanFormulary import HealthPlanFormulary

    a = create_schema_org_model(type_=HealthPlanFormularyInheritedProperties)
    b = create_schema_org_model(type_=HealthPlanFormularyProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    HealthPlanFormulary.schema()


def SpokenWordAlbum_test():
    from schorg.SpokenWordAlbum import SpokenWordAlbumInheritedProperties
    from schorg.SpokenWordAlbum import SpokenWordAlbumProperties
    from schorg.SpokenWordAlbum import AllProperties
    from schorg.SpokenWordAlbum import create_schema_org_model
    from schorg.SpokenWordAlbum import SpokenWordAlbum

    a = create_schema_org_model(type_=SpokenWordAlbumInheritedProperties)
    b = create_schema_org_model(type_=SpokenWordAlbumProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    SpokenWordAlbum.schema()


def FilmAction_test():
    from schorg.FilmAction import FilmActionInheritedProperties
    from schorg.FilmAction import FilmActionProperties
    from schorg.FilmAction import AllProperties
    from schorg.FilmAction import create_schema_org_model
    from schorg.FilmAction import FilmAction

    a = create_schema_org_model(type_=FilmActionInheritedProperties)
    b = create_schema_org_model(type_=FilmActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    FilmAction.schema()


def SelfStorage_test():
    from schorg.SelfStorage import SelfStorageInheritedProperties
    from schorg.SelfStorage import SelfStorageProperties
    from schorg.SelfStorage import AllProperties
    from schorg.SelfStorage import create_schema_org_model
    from schorg.SelfStorage import SelfStorage

    a = create_schema_org_model(type_=SelfStorageInheritedProperties)
    b = create_schema_org_model(type_=SelfStorageProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    SelfStorage.schema()


def WPFooter_test():
    from schorg.WPFooter import WPFooterInheritedProperties
    from schorg.WPFooter import WPFooterProperties
    from schorg.WPFooter import AllProperties
    from schorg.WPFooter import create_schema_org_model
    from schorg.WPFooter import WPFooter

    a = create_schema_org_model(type_=WPFooterInheritedProperties)
    b = create_schema_org_model(type_=WPFooterProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    WPFooter.schema()


def DesktopWebPlatform_test():
    from schorg.DesktopWebPlatform import DesktopWebPlatformInheritedProperties
    from schorg.DesktopWebPlatform import DesktopWebPlatformProperties
    from schorg.DesktopWebPlatform import AllProperties
    from schorg.DesktopWebPlatform import create_schema_org_model
    from schorg.DesktopWebPlatform import DesktopWebPlatform

    a = create_schema_org_model(type_=DesktopWebPlatformInheritedProperties)
    b = create_schema_org_model(type_=DesktopWebPlatformProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    DesktopWebPlatform.schema()


def MulticellularParasite_test():
    from schorg.MulticellularParasite import MulticellularParasiteInheritedProperties
    from schorg.MulticellularParasite import MulticellularParasiteProperties
    from schorg.MulticellularParasite import AllProperties
    from schorg.MulticellularParasite import create_schema_org_model
    from schorg.MulticellularParasite import MulticellularParasite

    a = create_schema_org_model(type_=MulticellularParasiteInheritedProperties)
    b = create_schema_org_model(type_=MulticellularParasiteProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MulticellularParasite.schema()


def ViolenceConsideration_test():
    from schorg.ViolenceConsideration import ViolenceConsiderationInheritedProperties
    from schorg.ViolenceConsideration import ViolenceConsiderationProperties
    from schorg.ViolenceConsideration import AllProperties
    from schorg.ViolenceConsideration import create_schema_org_model
    from schorg.ViolenceConsideration import ViolenceConsideration

    a = create_schema_org_model(type_=ViolenceConsiderationInheritedProperties)
    b = create_schema_org_model(type_=ViolenceConsiderationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ViolenceConsideration.schema()


def BodyMeasurementChest_test():
    from schorg.BodyMeasurementChest import BodyMeasurementChestInheritedProperties
    from schorg.BodyMeasurementChest import BodyMeasurementChestProperties
    from schorg.BodyMeasurementChest import AllProperties
    from schorg.BodyMeasurementChest import create_schema_org_model
    from schorg.BodyMeasurementChest import BodyMeasurementChest

    a = create_schema_org_model(type_=BodyMeasurementChestInheritedProperties)
    b = create_schema_org_model(type_=BodyMeasurementChestProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    BodyMeasurementChest.schema()


def DataFeedItem_test():
    from schorg.DataFeedItem import DataFeedItemInheritedProperties
    from schorg.DataFeedItem import DataFeedItemProperties
    from schorg.DataFeedItem import AllProperties
    from schorg.DataFeedItem import create_schema_org_model
    from schorg.DataFeedItem import DataFeedItem

    a = create_schema_org_model(type_=DataFeedItemInheritedProperties)
    b = create_schema_org_model(type_=DataFeedItemProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    DataFeedItem.schema()


def Oncologic_test():
    from schorg.Oncologic import OncologicInheritedProperties
    from schorg.Oncologic import OncologicProperties
    from schorg.Oncologic import AllProperties
    from schorg.Oncologic import create_schema_org_model
    from schorg.Oncologic import Oncologic

    a = create_schema_org_model(type_=OncologicInheritedProperties)
    b = create_schema_org_model(type_=OncologicProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Oncologic.schema()


def CompoundPriceSpecification_test():
    from schorg.CompoundPriceSpecification import CompoundPriceSpecificationInheritedProperties
    from schorg.CompoundPriceSpecification import CompoundPriceSpecificationProperties
    from schorg.CompoundPriceSpecification import AllProperties
    from schorg.CompoundPriceSpecification import create_schema_org_model
    from schorg.CompoundPriceSpecification import CompoundPriceSpecification

    a = create_schema_org_model(type_=CompoundPriceSpecificationInheritedProperties)
    b = create_schema_org_model(type_=CompoundPriceSpecificationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    CompoundPriceSpecification.schema()


def AutoPartsStore_test():
    from schorg.AutoPartsStore import AutoPartsStoreInheritedProperties
    from schorg.AutoPartsStore import AutoPartsStoreProperties
    from schorg.AutoPartsStore import AllProperties
    from schorg.AutoPartsStore import create_schema_org_model
    from schorg.AutoPartsStore import AutoPartsStore

    a = create_schema_org_model(type_=AutoPartsStoreInheritedProperties)
    b = create_schema_org_model(type_=AutoPartsStoreProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    AutoPartsStore.schema()


def DatedMoneySpecification_test():
    from schorg.DatedMoneySpecification import DatedMoneySpecificationInheritedProperties
    from schorg.DatedMoneySpecification import DatedMoneySpecificationProperties
    from schorg.DatedMoneySpecification import AllProperties
    from schorg.DatedMoneySpecification import create_schema_org_model
    from schorg.DatedMoneySpecification import DatedMoneySpecification

    a = create_schema_org_model(type_=DatedMoneySpecificationInheritedProperties)
    b = create_schema_org_model(type_=DatedMoneySpecificationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    DatedMoneySpecification.schema()


def Hospital_test():
    from schorg.Hospital import HospitalInheritedProperties
    from schorg.Hospital import HospitalProperties
    from schorg.Hospital import AllProperties
    from schorg.Hospital import create_schema_org_model
    from schorg.Hospital import Hospital

    a = create_schema_org_model(type_=HospitalInheritedProperties)
    b = create_schema_org_model(type_=HospitalProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Hospital.schema()


def EndorseAction_test():
    from schorg.EndorseAction import EndorseActionInheritedProperties
    from schorg.EndorseAction import EndorseActionProperties
    from schorg.EndorseAction import AllProperties
    from schorg.EndorseAction import create_schema_org_model
    from schorg.EndorseAction import EndorseAction

    a = create_schema_org_model(type_=EndorseActionInheritedProperties)
    b = create_schema_org_model(type_=EndorseActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    EndorseAction.schema()


def RandomizedTrial_test():
    from schorg.RandomizedTrial import RandomizedTrialInheritedProperties
    from schorg.RandomizedTrial import RandomizedTrialProperties
    from schorg.RandomizedTrial import AllProperties
    from schorg.RandomizedTrial import create_schema_org_model
    from schorg.RandomizedTrial import RandomizedTrial

    a = create_schema_org_model(type_=RandomizedTrialInheritedProperties)
    b = create_schema_org_model(type_=RandomizedTrialProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    RandomizedTrial.schema()


def EUEnergyEfficiencyCategoryA2Plus_test():
    from schorg.EUEnergyEfficiencyCategoryA2Plus import EUEnergyEfficiencyCategoryA2PlusInheritedProperties
    from schorg.EUEnergyEfficiencyCategoryA2Plus import EUEnergyEfficiencyCategoryA2PlusProperties
    from schorg.EUEnergyEfficiencyCategoryA2Plus import AllProperties
    from schorg.EUEnergyEfficiencyCategoryA2Plus import create_schema_org_model
    from schorg.EUEnergyEfficiencyCategoryA2Plus import EUEnergyEfficiencyCategoryA2Plus

    a = create_schema_org_model(type_=EUEnergyEfficiencyCategoryA2PlusInheritedProperties)
    b = create_schema_org_model(type_=EUEnergyEfficiencyCategoryA2PlusProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    EUEnergyEfficiencyCategoryA2Plus.schema()


def Renal_test():
    from schorg.Renal import RenalInheritedProperties
    from schorg.Renal import RenalProperties
    from schorg.Renal import AllProperties
    from schorg.Renal import create_schema_org_model
    from schorg.Renal import Renal

    a = create_schema_org_model(type_=RenalInheritedProperties)
    b = create_schema_org_model(type_=RenalProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Renal.schema()


def BoatReservation_test():
    from schorg.BoatReservation import BoatReservationInheritedProperties
    from schorg.BoatReservation import BoatReservationProperties
    from schorg.BoatReservation import AllProperties
    from schorg.BoatReservation import create_schema_org_model
    from schorg.BoatReservation import BoatReservation

    a = create_schema_org_model(type_=BoatReservationInheritedProperties)
    b = create_schema_org_model(type_=BoatReservationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    BoatReservation.schema()


def SuperficialAnatomy_test():
    from schorg.SuperficialAnatomy import SuperficialAnatomyInheritedProperties
    from schorg.SuperficialAnatomy import SuperficialAnatomyProperties
    from schorg.SuperficialAnatomy import AllProperties
    from schorg.SuperficialAnatomy import create_schema_org_model
    from schorg.SuperficialAnatomy import SuperficialAnatomy

    a = create_schema_org_model(type_=SuperficialAnatomyInheritedProperties)
    b = create_schema_org_model(type_=SuperficialAnatomyProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    SuperficialAnatomy.schema()


def TheaterEvent_test():
    from schorg.TheaterEvent import TheaterEventInheritedProperties
    from schorg.TheaterEvent import TheaterEventProperties
    from schorg.TheaterEvent import AllProperties
    from schorg.TheaterEvent import create_schema_org_model
    from schorg.TheaterEvent import TheaterEvent

    a = create_schema_org_model(type_=TheaterEventInheritedProperties)
    b = create_schema_org_model(type_=TheaterEventProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    TheaterEvent.schema()


def InStoreOnly_test():
    from schorg.InStoreOnly import InStoreOnlyInheritedProperties
    from schorg.InStoreOnly import InStoreOnlyProperties
    from schorg.InStoreOnly import AllProperties
    from schorg.InStoreOnly import create_schema_org_model
    from schorg.InStoreOnly import InStoreOnly

    a = create_schema_org_model(type_=InStoreOnlyInheritedProperties)
    b = create_schema_org_model(type_=InStoreOnlyProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    InStoreOnly.schema()


def ReadAction_test():
    from schorg.ReadAction import ReadActionInheritedProperties
    from schorg.ReadAction import ReadActionProperties
    from schorg.ReadAction import AllProperties
    from schorg.ReadAction import create_schema_org_model
    from schorg.ReadAction import ReadAction

    a = create_schema_org_model(type_=ReadActionInheritedProperties)
    b = create_schema_org_model(type_=ReadActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ReadAction.schema()


def Answer_test():
    from schorg.Answer import AnswerInheritedProperties
    from schorg.Answer import AnswerProperties
    from schorg.Answer import AllProperties
    from schorg.Answer import create_schema_org_model
    from schorg.Answer import Answer

    a = create_schema_org_model(type_=AnswerInheritedProperties)
    b = create_schema_org_model(type_=AnswerProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Answer.schema()


def Registry_test():
    from schorg.Registry import RegistryInheritedProperties
    from schorg.Registry import RegistryProperties
    from schorg.Registry import AllProperties
    from schorg.Registry import create_schema_org_model
    from schorg.Registry import Registry

    a = create_schema_org_model(type_=RegistryInheritedProperties)
    b = create_schema_org_model(type_=RegistryProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Registry.schema()


def ActivationFee_test():
    from schorg.ActivationFee import ActivationFeeInheritedProperties
    from schorg.ActivationFee import ActivationFeeProperties
    from schorg.ActivationFee import AllProperties
    from schorg.ActivationFee import create_schema_org_model
    from schorg.ActivationFee import ActivationFee

    a = create_schema_org_model(type_=ActivationFeeInheritedProperties)
    b = create_schema_org_model(type_=ActivationFeeProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ActivationFee.schema()


def LaboratoryScience_test():
    from schorg.LaboratoryScience import LaboratoryScienceInheritedProperties
    from schorg.LaboratoryScience import LaboratoryScienceProperties
    from schorg.LaboratoryScience import AllProperties
    from schorg.LaboratoryScience import create_schema_org_model
    from schorg.LaboratoryScience import LaboratoryScience

    a = create_schema_org_model(type_=LaboratoryScienceInheritedProperties)
    b = create_schema_org_model(type_=LaboratoryScienceProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    LaboratoryScience.schema()


def SafetyHealthAspect_test():
    from schorg.SafetyHealthAspect import SafetyHealthAspectInheritedProperties
    from schorg.SafetyHealthAspect import SafetyHealthAspectProperties
    from schorg.SafetyHealthAspect import AllProperties
    from schorg.SafetyHealthAspect import create_schema_org_model
    from schorg.SafetyHealthAspect import SafetyHealthAspect

    a = create_schema_org_model(type_=SafetyHealthAspectInheritedProperties)
    b = create_schema_org_model(type_=SafetyHealthAspectProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    SafetyHealthAspect.schema()


def Map_test():
    from schorg.Map import MapInheritedProperties
    from schorg.Map import MapProperties
    from schorg.Map import AllProperties
    from schorg.Map import create_schema_org_model
    from schorg.Map import Map

    a = create_schema_org_model(type_=MapInheritedProperties)
    b = create_schema_org_model(type_=MapProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Map.schema()


def PostalAddress_test():
    from schorg.PostalAddress import PostalAddressInheritedProperties
    from schorg.PostalAddress import PostalAddressProperties
    from schorg.PostalAddress import AllProperties
    from schorg.PostalAddress import create_schema_org_model
    from schorg.PostalAddress import PostalAddress

    a = create_schema_org_model(type_=PostalAddressInheritedProperties)
    b = create_schema_org_model(type_=PostalAddressProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    PostalAddress.schema()


def JobPosting_test():
    from schorg.JobPosting import JobPostingInheritedProperties
    from schorg.JobPosting import JobPostingProperties
    from schorg.JobPosting import AllProperties
    from schorg.JobPosting import create_schema_org_model
    from schorg.JobPosting import JobPosting

    a = create_schema_org_model(type_=JobPostingInheritedProperties)
    b = create_schema_org_model(type_=JobPostingProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    JobPosting.schema()


def DonateAction_test():
    from schorg.DonateAction import DonateActionInheritedProperties
    from schorg.DonateAction import DonateActionProperties
    from schorg.DonateAction import AllProperties
    from schorg.DonateAction import create_schema_org_model
    from schorg.DonateAction import DonateAction

    a = create_schema_org_model(type_=DonateActionInheritedProperties)
    b = create_schema_org_model(type_=DonateActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    DonateAction.schema()


def GlutenFreeDiet_test():
    from schorg.GlutenFreeDiet import GlutenFreeDietInheritedProperties
    from schorg.GlutenFreeDiet import GlutenFreeDietProperties
    from schorg.GlutenFreeDiet import AllProperties
    from schorg.GlutenFreeDiet import create_schema_org_model
    from schorg.GlutenFreeDiet import GlutenFreeDiet

    a = create_schema_org_model(type_=GlutenFreeDietInheritedProperties)
    b = create_schema_org_model(type_=GlutenFreeDietProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    GlutenFreeDiet.schema()


def DrawAction_test():
    from schorg.DrawAction import DrawActionInheritedProperties
    from schorg.DrawAction import DrawActionProperties
    from schorg.DrawAction import AllProperties
    from schorg.DrawAction import create_schema_org_model
    from schorg.DrawAction import DrawAction

    a = create_schema_org_model(type_=DrawActionInheritedProperties)
    b = create_schema_org_model(type_=DrawActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    DrawAction.schema()


def OrderDelivered_test():
    from schorg.OrderDelivered import OrderDeliveredInheritedProperties
    from schorg.OrderDelivered import OrderDeliveredProperties
    from schorg.OrderDelivered import AllProperties
    from schorg.OrderDelivered import create_schema_org_model
    from schorg.OrderDelivered import OrderDelivered

    a = create_schema_org_model(type_=OrderDeliveredInheritedProperties)
    b = create_schema_org_model(type_=OrderDeliveredProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    OrderDelivered.schema()


def ExerciseGym_test():
    from schorg.ExerciseGym import ExerciseGymInheritedProperties
    from schorg.ExerciseGym import ExerciseGymProperties
    from schorg.ExerciseGym import AllProperties
    from schorg.ExerciseGym import create_schema_org_model
    from schorg.ExerciseGym import ExerciseGym

    a = create_schema_org_model(type_=ExerciseGymInheritedProperties)
    b = create_schema_org_model(type_=ExerciseGymProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ExerciseGym.schema()


def ReturnInStore_test():
    from schorg.ReturnInStore import ReturnInStoreInheritedProperties
    from schorg.ReturnInStore import ReturnInStoreProperties
    from schorg.ReturnInStore import AllProperties
    from schorg.ReturnInStore import create_schema_org_model
    from schorg.ReturnInStore import ReturnInStore

    a = create_schema_org_model(type_=ReturnInStoreInheritedProperties)
    b = create_schema_org_model(type_=ReturnInStoreProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ReturnInStore.schema()


def BenefitsHealthAspect_test():
    from schorg.BenefitsHealthAspect import BenefitsHealthAspectInheritedProperties
    from schorg.BenefitsHealthAspect import BenefitsHealthAspectProperties
    from schorg.BenefitsHealthAspect import AllProperties
    from schorg.BenefitsHealthAspect import create_schema_org_model
    from schorg.BenefitsHealthAspect import BenefitsHealthAspect

    a = create_schema_org_model(type_=BenefitsHealthAspectInheritedProperties)
    b = create_schema_org_model(type_=BenefitsHealthAspectProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    BenefitsHealthAspect.schema()


def Therapeutic_test():
    from schorg.Therapeutic import TherapeuticInheritedProperties
    from schorg.Therapeutic import TherapeuticProperties
    from schorg.Therapeutic import AllProperties
    from schorg.Therapeutic import create_schema_org_model
    from schorg.Therapeutic import Therapeutic

    a = create_schema_org_model(type_=TherapeuticInheritedProperties)
    b = create_schema_org_model(type_=TherapeuticProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Therapeutic.schema()


def LegislativeBuilding_test():
    from schorg.LegislativeBuilding import LegislativeBuildingInheritedProperties
    from schorg.LegislativeBuilding import LegislativeBuildingProperties
    from schorg.LegislativeBuilding import AllProperties
    from schorg.LegislativeBuilding import create_schema_org_model
    from schorg.LegislativeBuilding import LegislativeBuilding

    a = create_schema_org_model(type_=LegislativeBuildingInheritedProperties)
    b = create_schema_org_model(type_=LegislativeBuildingProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    LegislativeBuilding.schema()


def DefinitiveLegalValue_test():
    from schorg.DefinitiveLegalValue import DefinitiveLegalValueInheritedProperties
    from schorg.DefinitiveLegalValue import DefinitiveLegalValueProperties
    from schorg.DefinitiveLegalValue import AllProperties
    from schorg.DefinitiveLegalValue import create_schema_org_model
    from schorg.DefinitiveLegalValue import DefinitiveLegalValue

    a = create_schema_org_model(type_=DefinitiveLegalValueInheritedProperties)
    b = create_schema_org_model(type_=DefinitiveLegalValueProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    DefinitiveLegalValue.schema()


def ShoeStore_test():
    from schorg.ShoeStore import ShoeStoreInheritedProperties
    from schorg.ShoeStore import ShoeStoreProperties
    from schorg.ShoeStore import AllProperties
    from schorg.ShoeStore import create_schema_org_model
    from schorg.ShoeStore import ShoeStore

    a = create_schema_org_model(type_=ShoeStoreInheritedProperties)
    b = create_schema_org_model(type_=ShoeStoreProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ShoeStore.schema()


def FurnitureStore_test():
    from schorg.FurnitureStore import FurnitureStoreInheritedProperties
    from schorg.FurnitureStore import FurnitureStoreProperties
    from schorg.FurnitureStore import AllProperties
    from schorg.FurnitureStore import create_schema_org_model
    from schorg.FurnitureStore import FurnitureStore

    a = create_schema_org_model(type_=FurnitureStoreInheritedProperties)
    b = create_schema_org_model(type_=FurnitureStoreProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    FurnitureStore.schema()


def MusicVideoObject_test():
    from schorg.MusicVideoObject import MusicVideoObjectInheritedProperties
    from schorg.MusicVideoObject import MusicVideoObjectProperties
    from schorg.MusicVideoObject import AllProperties
    from schorg.MusicVideoObject import create_schema_org_model
    from schorg.MusicVideoObject import MusicVideoObject

    a = create_schema_org_model(type_=MusicVideoObjectInheritedProperties)
    b = create_schema_org_model(type_=MusicVideoObjectProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MusicVideoObject.schema()


def DrugLegalStatus_test():
    from schorg.DrugLegalStatus import DrugLegalStatusInheritedProperties
    from schorg.DrugLegalStatus import DrugLegalStatusProperties
    from schorg.DrugLegalStatus import AllProperties
    from schorg.DrugLegalStatus import create_schema_org_model
    from schorg.DrugLegalStatus import DrugLegalStatus

    a = create_schema_org_model(type_=DrugLegalStatusInheritedProperties)
    b = create_schema_org_model(type_=DrugLegalStatusProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    DrugLegalStatus.schema()


def TireShop_test():
    from schorg.TireShop import TireShopInheritedProperties
    from schorg.TireShop import TireShopProperties
    from schorg.TireShop import AllProperties
    from schorg.TireShop import create_schema_org_model
    from schorg.TireShop import TireShop

    a = create_schema_org_model(type_=TireShopInheritedProperties)
    b = create_schema_org_model(type_=TireShopProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    TireShop.schema()


def Obstetric_test():
    from schorg.Obstetric import ObstetricInheritedProperties
    from schorg.Obstetric import ObstetricProperties
    from schorg.Obstetric import AllProperties
    from schorg.Obstetric import create_schema_org_model
    from schorg.Obstetric import Obstetric

    a = create_schema_org_model(type_=ObstetricInheritedProperties)
    b = create_schema_org_model(type_=ObstetricProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Obstetric.schema()


def Nonprofit501c13_test():
    from schorg.Nonprofit501c13 import Nonprofit501c13InheritedProperties
    from schorg.Nonprofit501c13 import Nonprofit501c13Properties
    from schorg.Nonprofit501c13 import AllProperties
    from schorg.Nonprofit501c13 import create_schema_org_model
    from schorg.Nonprofit501c13 import Nonprofit501c13

    a = create_schema_org_model(type_=Nonprofit501c13InheritedProperties)
    b = create_schema_org_model(type_=Nonprofit501c13Properties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Nonprofit501c13.schema()


def Mountain_test():
    from schorg.Mountain import MountainInheritedProperties
    from schorg.Mountain import MountainProperties
    from schorg.Mountain import AllProperties
    from schorg.Mountain import create_schema_org_model
    from schorg.Mountain import Mountain

    a = create_schema_org_model(type_=MountainInheritedProperties)
    b = create_schema_org_model(type_=MountainProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Mountain.schema()


def Pediatric_test():
    from schorg.Pediatric import PediatricInheritedProperties
    from schorg.Pediatric import PediatricProperties
    from schorg.Pediatric import AllProperties
    from schorg.Pediatric import create_schema_org_model
    from schorg.Pediatric import Pediatric

    a = create_schema_org_model(type_=PediatricInheritedProperties)
    b = create_schema_org_model(type_=PediatricProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Pediatric.schema()


def Nonprofit501c14_test():
    from schorg.Nonprofit501c14 import Nonprofit501c14InheritedProperties
    from schorg.Nonprofit501c14 import Nonprofit501c14Properties
    from schorg.Nonprofit501c14 import AllProperties
    from schorg.Nonprofit501c14 import create_schema_org_model
    from schorg.Nonprofit501c14 import Nonprofit501c14

    a = create_schema_org_model(type_=Nonprofit501c14InheritedProperties)
    b = create_schema_org_model(type_=Nonprofit501c14Properties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Nonprofit501c14.schema()


def Corporation_test():
    from schorg.Corporation import CorporationInheritedProperties
    from schorg.Corporation import CorporationProperties
    from schorg.Corporation import AllProperties
    from schorg.Corporation import create_schema_org_model
    from schorg.Corporation import Corporation

    a = create_schema_org_model(type_=CorporationInheritedProperties)
    b = create_schema_org_model(type_=CorporationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Corporation.schema()


def RsvpAction_test():
    from schorg.RsvpAction import RsvpActionInheritedProperties
    from schorg.RsvpAction import RsvpActionProperties
    from schorg.RsvpAction import AllProperties
    from schorg.RsvpAction import create_schema_org_model
    from schorg.RsvpAction import RsvpAction

    a = create_schema_org_model(type_=RsvpActionInheritedProperties)
    b = create_schema_org_model(type_=RsvpActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    RsvpAction.schema()


def UserReview_test():
    from schorg.UserReview import UserReviewInheritedProperties
    from schorg.UserReview import UserReviewProperties
    from schorg.UserReview import AllProperties
    from schorg.UserReview import create_schema_org_model
    from schorg.UserReview import UserReview

    a = create_schema_org_model(type_=UserReviewInheritedProperties)
    b = create_schema_org_model(type_=UserReviewProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    UserReview.schema()


def DateTime_test():
    from schorg.DateTime import DateTimeInheritedProperties
    from schorg.DateTime import DateTimeProperties
    from schorg.DateTime import AllProperties
    from schorg.DateTime import create_schema_org_model
    from schorg.DateTime import DateTime

    a = create_schema_org_model(type_=DateTimeInheritedProperties)
    b = create_schema_org_model(type_=DateTimeProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    DateTime.schema()


def PaymentAutomaticallyApplied_test():
    from schorg.PaymentAutomaticallyApplied import PaymentAutomaticallyAppliedInheritedProperties
    from schorg.PaymentAutomaticallyApplied import PaymentAutomaticallyAppliedProperties
    from schorg.PaymentAutomaticallyApplied import AllProperties
    from schorg.PaymentAutomaticallyApplied import create_schema_org_model
    from schorg.PaymentAutomaticallyApplied import PaymentAutomaticallyApplied

    a = create_schema_org_model(type_=PaymentAutomaticallyAppliedInheritedProperties)
    b = create_schema_org_model(type_=PaymentAutomaticallyAppliedProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    PaymentAutomaticallyApplied.schema()


def Atlas_test():
    from schorg.Atlas import AtlasInheritedProperties
    from schorg.Atlas import AtlasProperties
    from schorg.Atlas import AllProperties
    from schorg.Atlas import create_schema_org_model
    from schorg.Atlas import Atlas

    a = create_schema_org_model(type_=AtlasInheritedProperties)
    b = create_schema_org_model(type_=AtlasProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Atlas.schema()


def PaintAction_test():
    from schorg.PaintAction import PaintActionInheritedProperties
    from schorg.PaintAction import PaintActionProperties
    from schorg.PaintAction import AllProperties
    from schorg.PaintAction import create_schema_org_model
    from schorg.PaintAction import PaintAction

    a = create_schema_org_model(type_=PaintActionInheritedProperties)
    b = create_schema_org_model(type_=PaintActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    PaintAction.schema()


def OrderAction_test():
    from schorg.OrderAction import OrderActionInheritedProperties
    from schorg.OrderAction import OrderActionProperties
    from schorg.OrderAction import AllProperties
    from schorg.OrderAction import create_schema_org_model
    from schorg.OrderAction import OrderAction

    a = create_schema_org_model(type_=OrderActionInheritedProperties)
    b = create_schema_org_model(type_=OrderActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    OrderAction.schema()


def WearableSizeSystemDE_test():
    from schorg.WearableSizeSystemDE import WearableSizeSystemDEInheritedProperties
    from schorg.WearableSizeSystemDE import WearableSizeSystemDEProperties
    from schorg.WearableSizeSystemDE import AllProperties
    from schorg.WearableSizeSystemDE import create_schema_org_model
    from schorg.WearableSizeSystemDE import WearableSizeSystemDE

    a = create_schema_org_model(type_=WearableSizeSystemDEInheritedProperties)
    b = create_schema_org_model(type_=WearableSizeSystemDEProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    WearableSizeSystemDE.schema()


def Newspaper_test():
    from schorg.Newspaper import NewspaperInheritedProperties
    from schorg.Newspaper import NewspaperProperties
    from schorg.Newspaper import AllProperties
    from schorg.Newspaper import create_schema_org_model
    from schorg.Newspaper import Newspaper

    a = create_schema_org_model(type_=NewspaperInheritedProperties)
    b = create_schema_org_model(type_=NewspaperProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Newspaper.schema()


def RiverBodyOfWater_test():
    from schorg.RiverBodyOfWater import RiverBodyOfWaterInheritedProperties
    from schorg.RiverBodyOfWater import RiverBodyOfWaterProperties
    from schorg.RiverBodyOfWater import AllProperties
    from schorg.RiverBodyOfWater import create_schema_org_model
    from schorg.RiverBodyOfWater import RiverBodyOfWater

    a = create_schema_org_model(type_=RiverBodyOfWaterInheritedProperties)
    b = create_schema_org_model(type_=RiverBodyOfWaterProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    RiverBodyOfWater.schema()


def Question_test():
    from schorg.Question import QuestionInheritedProperties
    from schorg.Question import QuestionProperties
    from schorg.Question import AllProperties
    from schorg.Question import create_schema_org_model
    from schorg.Question import Question

    a = create_schema_org_model(type_=QuestionInheritedProperties)
    b = create_schema_org_model(type_=QuestionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Question.schema()


def DiagnosticLab_test():
    from schorg.DiagnosticLab import DiagnosticLabInheritedProperties
    from schorg.DiagnosticLab import DiagnosticLabProperties
    from schorg.DiagnosticLab import AllProperties
    from schorg.DiagnosticLab import create_schema_org_model
    from schorg.DiagnosticLab import DiagnosticLab

    a = create_schema_org_model(type_=DiagnosticLabInheritedProperties)
    b = create_schema_org_model(type_=DiagnosticLabProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    DiagnosticLab.schema()


def Paperback_test():
    from schorg.Paperback import PaperbackInheritedProperties
    from schorg.Paperback import PaperbackProperties
    from schorg.Paperback import AllProperties
    from schorg.Paperback import create_schema_org_model
    from schorg.Paperback import Paperback

    a = create_schema_org_model(type_=PaperbackInheritedProperties)
    b = create_schema_org_model(type_=PaperbackProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Paperback.schema()


def LowCalorieDiet_test():
    from schorg.LowCalorieDiet import LowCalorieDietInheritedProperties
    from schorg.LowCalorieDiet import LowCalorieDietProperties
    from schorg.LowCalorieDiet import AllProperties
    from schorg.LowCalorieDiet import create_schema_org_model
    from schorg.LowCalorieDiet import LowCalorieDiet

    a = create_schema_org_model(type_=LowCalorieDietInheritedProperties)
    b = create_schema_org_model(type_=LowCalorieDietProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    LowCalorieDiet.schema()


def CheckoutPage_test():
    from schorg.CheckoutPage import CheckoutPageInheritedProperties
    from schorg.CheckoutPage import CheckoutPageProperties
    from schorg.CheckoutPage import AllProperties
    from schorg.CheckoutPage import create_schema_org_model
    from schorg.CheckoutPage import CheckoutPage

    a = create_schema_org_model(type_=CheckoutPageInheritedProperties)
    b = create_schema_org_model(type_=CheckoutPageProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    CheckoutPage.schema()


def DemoAlbum_test():
    from schorg.DemoAlbum import DemoAlbumInheritedProperties
    from schorg.DemoAlbum import DemoAlbumProperties
    from schorg.DemoAlbum import AllProperties
    from schorg.DemoAlbum import create_schema_org_model
    from schorg.DemoAlbum import DemoAlbum

    a = create_schema_org_model(type_=DemoAlbumInheritedProperties)
    b = create_schema_org_model(type_=DemoAlbumProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    DemoAlbum.schema()


def NewsMediaOrganization_test():
    from schorg.NewsMediaOrganization import NewsMediaOrganizationInheritedProperties
    from schorg.NewsMediaOrganization import NewsMediaOrganizationProperties
    from schorg.NewsMediaOrganization import AllProperties
    from schorg.NewsMediaOrganization import create_schema_org_model
    from schorg.NewsMediaOrganization import NewsMediaOrganization

    a = create_schema_org_model(type_=NewsMediaOrganizationInheritedProperties)
    b = create_schema_org_model(type_=NewsMediaOrganizationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    NewsMediaOrganization.schema()


def DefenceEstablishment_test():
    from schorg.DefenceEstablishment import DefenceEstablishmentInheritedProperties
    from schorg.DefenceEstablishment import DefenceEstablishmentProperties
    from schorg.DefenceEstablishment import AllProperties
    from schorg.DefenceEstablishment import create_schema_org_model
    from schorg.DefenceEstablishment import DefenceEstablishment

    a = create_schema_org_model(type_=DefenceEstablishmentInheritedProperties)
    b = create_schema_org_model(type_=DefenceEstablishmentProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    DefenceEstablishment.schema()


def MedicalGuidelineRecommendation_test():
    from schorg.MedicalGuidelineRecommendation import MedicalGuidelineRecommendationInheritedProperties
    from schorg.MedicalGuidelineRecommendation import MedicalGuidelineRecommendationProperties
    from schorg.MedicalGuidelineRecommendation import AllProperties
    from schorg.MedicalGuidelineRecommendation import create_schema_org_model
    from schorg.MedicalGuidelineRecommendation import MedicalGuidelineRecommendation

    a = create_schema_org_model(type_=MedicalGuidelineRecommendationInheritedProperties)
    b = create_schema_org_model(type_=MedicalGuidelineRecommendationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MedicalGuidelineRecommendation.schema()


def HotelRoom_test():
    from schorg.HotelRoom import HotelRoomInheritedProperties
    from schorg.HotelRoom import HotelRoomProperties
    from schorg.HotelRoom import AllProperties
    from schorg.HotelRoom import create_schema_org_model
    from schorg.HotelRoom import HotelRoom

    a = create_schema_org_model(type_=HotelRoomInheritedProperties)
    b = create_schema_org_model(type_=HotelRoomProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    HotelRoom.schema()


def Infectious_test():
    from schorg.Infectious import InfectiousInheritedProperties
    from schorg.Infectious import InfectiousProperties
    from schorg.Infectious import AllProperties
    from schorg.Infectious import create_schema_org_model
    from schorg.Infectious import Infectious

    a = create_schema_org_model(type_=InfectiousInheritedProperties)
    b = create_schema_org_model(type_=InfectiousProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Infectious.schema()


def WearableSizeGroupShort_test():
    from schorg.WearableSizeGroupShort import WearableSizeGroupShortInheritedProperties
    from schorg.WearableSizeGroupShort import WearableSizeGroupShortProperties
    from schorg.WearableSizeGroupShort import AllProperties
    from schorg.WearableSizeGroupShort import create_schema_org_model
    from schorg.WearableSizeGroupShort import WearableSizeGroupShort

    a = create_schema_org_model(type_=WearableSizeGroupShortInheritedProperties)
    b = create_schema_org_model(type_=WearableSizeGroupShortProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    WearableSizeGroupShort.schema()


def School_test():
    from schorg.School import SchoolInheritedProperties
    from schorg.School import SchoolProperties
    from schorg.School import AllProperties
    from schorg.School import create_schema_org_model
    from schorg.School import School

    a = create_schema_org_model(type_=SchoolInheritedProperties)
    b = create_schema_org_model(type_=SchoolProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    School.schema()


def AnalysisNewsArticle_test():
    from schorg.AnalysisNewsArticle import AnalysisNewsArticleInheritedProperties
    from schorg.AnalysisNewsArticle import AnalysisNewsArticleProperties
    from schorg.AnalysisNewsArticle import AllProperties
    from schorg.AnalysisNewsArticle import create_schema_org_model
    from schorg.AnalysisNewsArticle import AnalysisNewsArticle

    a = create_schema_org_model(type_=AnalysisNewsArticleInheritedProperties)
    b = create_schema_org_model(type_=AnalysisNewsArticleProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    AnalysisNewsArticle.schema()


def Installment_test():
    from schorg.Installment import InstallmentInheritedProperties
    from schorg.Installment import InstallmentProperties
    from schorg.Installment import AllProperties
    from schorg.Installment import create_schema_org_model
    from schorg.Installment import Installment

    a = create_schema_org_model(type_=InstallmentInheritedProperties)
    b = create_schema_org_model(type_=InstallmentProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Installment.schema()


def AnatomicalSystem_test():
    from schorg.AnatomicalSystem import AnatomicalSystemInheritedProperties
    from schorg.AnatomicalSystem import AnatomicalSystemProperties
    from schorg.AnatomicalSystem import AllProperties
    from schorg.AnatomicalSystem import create_schema_org_model
    from schorg.AnatomicalSystem import AnatomicalSystem

    a = create_schema_org_model(type_=AnatomicalSystemInheritedProperties)
    b = create_schema_org_model(type_=AnatomicalSystemProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    AnatomicalSystem.schema()


def MediaReview_test():
    from schorg.MediaReview import MediaReviewInheritedProperties
    from schorg.MediaReview import MediaReviewProperties
    from schorg.MediaReview import AllProperties
    from schorg.MediaReview import create_schema_org_model
    from schorg.MediaReview import MediaReview

    a = create_schema_org_model(type_=MediaReviewInheritedProperties)
    b = create_schema_org_model(type_=MediaReviewProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    MediaReview.schema()


def ExercisePlan_test():
    from schorg.ExercisePlan import ExercisePlanInheritedProperties
    from schorg.ExercisePlan import ExercisePlanProperties
    from schorg.ExercisePlan import AllProperties
    from schorg.ExercisePlan import create_schema_org_model
    from schorg.ExercisePlan import ExercisePlan

    a = create_schema_org_model(type_=ExercisePlanInheritedProperties)
    b = create_schema_org_model(type_=ExercisePlanProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ExercisePlan.schema()


def LowLactoseDiet_test():
    from schorg.LowLactoseDiet import LowLactoseDietInheritedProperties
    from schorg.LowLactoseDiet import LowLactoseDietProperties
    from schorg.LowLactoseDiet import AllProperties
    from schorg.LowLactoseDiet import create_schema_org_model
    from schorg.LowLactoseDiet import LowLactoseDiet

    a = create_schema_org_model(type_=LowLactoseDietInheritedProperties)
    b = create_schema_org_model(type_=LowLactoseDietProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    LowLactoseDiet.schema()


def Quotation_test():
    from schorg.Quotation import QuotationInheritedProperties
    from schorg.Quotation import QuotationProperties
    from schorg.Quotation import AllProperties
    from schorg.Quotation import create_schema_org_model
    from schorg.Quotation import Quotation

    a = create_schema_org_model(type_=QuotationInheritedProperties)
    b = create_schema_org_model(type_=QuotationProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Quotation.schema()


def DisagreeAction_test():
    from schorg.DisagreeAction import DisagreeActionInheritedProperties
    from schorg.DisagreeAction import DisagreeActionProperties
    from schorg.DisagreeAction import AllProperties
    from schorg.DisagreeAction import create_schema_org_model
    from schorg.DisagreeAction import DisagreeAction

    a = create_schema_org_model(type_=DisagreeActionInheritedProperties)
    b = create_schema_org_model(type_=DisagreeActionProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    DisagreeAction.schema()


def OnlineOnly_test():
    from schorg.OnlineOnly import OnlineOnlyInheritedProperties
    from schorg.OnlineOnly import OnlineOnlyProperties
    from schorg.OnlineOnly import AllProperties
    from schorg.OnlineOnly import create_schema_org_model
    from schorg.OnlineOnly import OnlineOnly

    a = create_schema_org_model(type_=OnlineOnlyInheritedProperties)
    b = create_schema_org_model(type_=OnlineOnlyProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    OnlineOnly.schema()


def WearableSizeSystemUK_test():
    from schorg.WearableSizeSystemUK import WearableSizeSystemUKInheritedProperties
    from schorg.WearableSizeSystemUK import WearableSizeSystemUKProperties
    from schorg.WearableSizeSystemUK import AllProperties
    from schorg.WearableSizeSystemUK import create_schema_org_model
    from schorg.WearableSizeSystemUK import WearableSizeSystemUK

    a = create_schema_org_model(type_=WearableSizeSystemUKInheritedProperties)
    b = create_schema_org_model(type_=WearableSizeSystemUKProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    WearableSizeSystemUK.schema()


def ReturnLabelDownloadAndPrint_test():
    from schorg.ReturnLabelDownloadAndPrint import ReturnLabelDownloadAndPrintInheritedProperties
    from schorg.ReturnLabelDownloadAndPrint import ReturnLabelDownloadAndPrintProperties
    from schorg.ReturnLabelDownloadAndPrint import AllProperties
    from schorg.ReturnLabelDownloadAndPrint import create_schema_org_model
    from schorg.ReturnLabelDownloadAndPrint import ReturnLabelDownloadAndPrint

    a = create_schema_org_model(type_=ReturnLabelDownloadAndPrintInheritedProperties)
    b = create_schema_org_model(type_=ReturnLabelDownloadAndPrintProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ReturnLabelDownloadAndPrint.schema()


def Wholesale_test():
    from schorg.Wholesale import WholesaleInheritedProperties
    from schorg.Wholesale import WholesaleProperties
    from schorg.Wholesale import AllProperties
    from schorg.Wholesale import create_schema_org_model
    from schorg.Wholesale import Wholesale

    a = create_schema_org_model(type_=WholesaleInheritedProperties)
    b = create_schema_org_model(type_=WholesaleProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Wholesale.schema()


def ItemPage_test():
    from schorg.ItemPage import ItemPageInheritedProperties
    from schorg.ItemPage import ItemPageProperties
    from schorg.ItemPage import AllProperties
    from schorg.ItemPage import create_schema_org_model
    from schorg.ItemPage import ItemPage

    a = create_schema_org_model(type_=ItemPageInheritedProperties)
    b = create_schema_org_model(type_=ItemPageProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    ItemPage.schema()


def EUEnergyEfficiencyCategoryA1Plus_test():
    from schorg.EUEnergyEfficiencyCategoryA1Plus import EUEnergyEfficiencyCategoryA1PlusInheritedProperties
    from schorg.EUEnergyEfficiencyCategoryA1Plus import EUEnergyEfficiencyCategoryA1PlusProperties
    from schorg.EUEnergyEfficiencyCategoryA1Plus import AllProperties
    from schorg.EUEnergyEfficiencyCategoryA1Plus import create_schema_org_model
    from schorg.EUEnergyEfficiencyCategoryA1Plus import EUEnergyEfficiencyCategoryA1Plus

    a = create_schema_org_model(type_=EUEnergyEfficiencyCategoryA1PlusInheritedProperties)
    b = create_schema_org_model(type_=EUEnergyEfficiencyCategoryA1PlusProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    EUEnergyEfficiencyCategoryA1Plus.schema()


def Reservoir_test():
    from schorg.Reservoir import ReservoirInheritedProperties
    from schorg.Reservoir import ReservoirProperties
    from schorg.Reservoir import AllProperties
    from schorg.Reservoir import create_schema_org_model
    from schorg.Reservoir import Reservoir

    a = create_schema_org_model(type_=ReservoirInheritedProperties)
    b = create_schema_org_model(type_=ReservoirProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Reservoir.schema()


def EBook_test():
    from schorg.EBook import EBookInheritedProperties
    from schorg.EBook import EBookProperties
    from schorg.EBook import AllProperties
    from schorg.EBook import create_schema_org_model
    from schorg.EBook import EBook

    a = create_schema_org_model(type_=EBookInheritedProperties)
    b = create_schema_org_model(type_=EBookProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    EBook.schema()


def SelfCareHealthAspect_test():
    from schorg.SelfCareHealthAspect import SelfCareHealthAspectInheritedProperties
    from schorg.SelfCareHealthAspect import SelfCareHealthAspectProperties
    from schorg.SelfCareHealthAspect import AllProperties
    from schorg.SelfCareHealthAspect import create_schema_org_model
    from schorg.SelfCareHealthAspect import SelfCareHealthAspect

    a = create_schema_org_model(type_=SelfCareHealthAspectInheritedProperties)
    b = create_schema_org_model(type_=SelfCareHealthAspectProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    SelfCareHealthAspect.schema()


def RisksOrComplicationsHealthAspect_test():
    from schorg.RisksOrComplicationsHealthAspect import RisksOrComplicationsHealthAspectInheritedProperties
    from schorg.RisksOrComplicationsHealthAspect import RisksOrComplicationsHealthAspectProperties
    from schorg.RisksOrComplicationsHealthAspect import AllProperties
    from schorg.RisksOrComplicationsHealthAspect import create_schema_org_model
    from schorg.RisksOrComplicationsHealthAspect import RisksOrComplicationsHealthAspect

    a = create_schema_org_model(type_=RisksOrComplicationsHealthAspectInheritedProperties)
    b = create_schema_org_model(type_=RisksOrComplicationsHealthAspectProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    RisksOrComplicationsHealthAspect.schema()


def Movie_test():
    from schorg.Movie import MovieInheritedProperties
    from schorg.Movie import MovieProperties
    from schorg.Movie import AllProperties
    from schorg.Movie import create_schema_org_model
    from schorg.Movie import Movie

    a = create_schema_org_model(type_=MovieInheritedProperties)
    b = create_schema_org_model(type_=MovieProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Movie.schema()


def False__test():
    from schorg.False_ import False_InheritedProperties
    from schorg.False_ import False_Properties
    from schorg.False_ import AllProperties
    from schorg.False_ import create_schema_org_model
    from schorg.False_ import False_

    a = create_schema_org_model(type_=False_InheritedProperties)
    b = create_schema_org_model(type_=False_Properties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    False_.schema()


def OfflineEventAttendanceMode_test():
    from schorg.OfflineEventAttendanceMode import OfflineEventAttendanceModeInheritedProperties
    from schorg.OfflineEventAttendanceMode import OfflineEventAttendanceModeProperties
    from schorg.OfflineEventAttendanceMode import AllProperties
    from schorg.OfflineEventAttendanceMode import create_schema_org_model
    from schorg.OfflineEventAttendanceMode import OfflineEventAttendanceMode

    a = create_schema_org_model(type_=OfflineEventAttendanceModeInheritedProperties)
    b = create_schema_org_model(type_=OfflineEventAttendanceModeProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    OfflineEventAttendanceMode.schema()


def Integer_test():
    from schorg.Integer import IntegerInheritedProperties
    from schorg.Integer import IntegerProperties
    from schorg.Integer import AllProperties
    from schorg.Integer import create_schema_org_model
    from schorg.Integer import Integer

    a = create_schema_org_model(type_=IntegerInheritedProperties)
    b = create_schema_org_model(type_=IntegerProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Integer.schema()


def OrderItem_test():
    from schorg.OrderItem import OrderItemInheritedProperties
    from schorg.OrderItem import OrderItemProperties
    from schorg.OrderItem import AllProperties
    from schorg.OrderItem import create_schema_org_model
    from schorg.OrderItem import OrderItem

    a = create_schema_org_model(type_=OrderItemInheritedProperties)
    b = create_schema_org_model(type_=OrderItemProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    OrderItem.schema()


def CaseSeries_test():
    from schorg.CaseSeries import CaseSeriesInheritedProperties
    from schorg.CaseSeries import CaseSeriesProperties
    from schorg.CaseSeries import AllProperties
    from schorg.CaseSeries import create_schema_org_model
    from schorg.CaseSeries import CaseSeries

    a = create_schema_org_model(type_=CaseSeriesInheritedProperties)
    b = create_schema_org_model(type_=CaseSeriesProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    CaseSeries.schema()


def Preschool_test():
    from schorg.Preschool import PreschoolInheritedProperties
    from schorg.Preschool import PreschoolProperties
    from schorg.Preschool import AllProperties
    from schorg.Preschool import create_schema_org_model
    from schorg.Preschool import Preschool

    a = create_schema_org_model(type_=PreschoolInheritedProperties)
    b = create_schema_org_model(type_=PreschoolProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    Preschool.schema()


def BodyMeasurementWaist_test():
    from schorg.BodyMeasurementWaist import BodyMeasurementWaistInheritedProperties
    from schorg.BodyMeasurementWaist import BodyMeasurementWaistProperties
    from schorg.BodyMeasurementWaist import AllProperties
    from schorg.BodyMeasurementWaist import create_schema_org_model
    from schorg.BodyMeasurementWaist import BodyMeasurementWaist

    a = create_schema_org_model(type_=BodyMeasurementWaistInheritedProperties)
    b = create_schema_org_model(type_=BodyMeasurementWaistProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    BodyMeasurementWaist.schema()


def NotYetRecruiting_test():
    from schorg.NotYetRecruiting import NotYetRecruitingInheritedProperties
    from schorg.NotYetRecruiting import NotYetRecruitingProperties
    from schorg.NotYetRecruiting import AllProperties
    from schorg.NotYetRecruiting import create_schema_org_model
    from schorg.NotYetRecruiting import NotYetRecruiting

    a = create_schema_org_model(type_=NotYetRecruitingInheritedProperties)
    b = create_schema_org_model(type_=NotYetRecruitingProperties)
    c = create_schema_org_model(type_=AllProperties)
    a.schema()
    b.schema()
    c.schema()
    NotYetRecruiting.schema()



def run_all():
    print("running Thing_test")
    Thing_test()
    print("running Intangible_test")
    Intangible_test()
    print("running StructuredValue_test")
    StructuredValue_test()
    print("running GeoShape_test")
    GeoShape_test()
    print("running Enumeration_test")
    Enumeration_test()
    print("running SizeGroupEnumeration_test")
    SizeGroupEnumeration_test()
    print("running WearableSizeGroupEnumeration_test")
    WearableSizeGroupEnumeration_test()
    print("running WearableSizeGroupMens_test")
    WearableSizeGroupMens_test()
    print("running QualitativeValue_test")
    QualitativeValue_test()
    print("running DriveWheelConfigurationValue_test")
    DriveWheelConfigurationValue_test()
    print("running FrontWheelDriveConfiguration_test")
    FrontWheelDriveConfiguration_test()
    print("running QuantitativeValueDistribution_test")
    QuantitativeValueDistribution_test()
    print("running MonetaryAmountDistribution_test")
    MonetaryAmountDistribution_test()
    print("running Organization_test")
    Organization_test()
    print("running WorkersUnion_test")
    WorkersUnion_test()
    print("running Place_test")
    Place_test()
    print("running CivicStructure_test")
    CivicStructure_test()
    print("running Park_test")
    Park_test()
    print("running LocalBusiness_test")
    LocalBusiness_test()
    print("running Store_test")
    Store_test()
    print("running PetStore_test")
    PetStore_test()
    print("running MedicalEntity_test")
    MedicalEntity_test()
    print("running MedicalIntangible_test")
    MedicalIntangible_test()
    print("running DDxElement_test")
    DDxElement_test()
    print("running ReturnFeesEnumeration_test")
    ReturnFeesEnumeration_test()
    print("running ReturnShippingFees_test")
    ReturnShippingFees_test()
    print("running Florist_test")
    Florist_test()
    print("running AnatomicalStructure_test")
    AnatomicalStructure_test()
    print("running SizeSystemEnumeration_test")
    SizeSystemEnumeration_test()
    print("running WearableSizeSystemEnumeration_test")
    WearableSizeSystemEnumeration_test()
    print("running WearableSizeSystemBR_test")
    WearableSizeSystemBR_test()
    print("running NonprofitType_test")
    NonprofitType_test()
    print("running NLNonprofitType_test")
    NLNonprofitType_test()
    print("running NonprofitSBBI_test")
    NonprofitSBBI_test()
    print("running CreativeWork_test")
    CreativeWork_test()
    print("running DataCatalog_test")
    DataCatalog_test()
    print("running WebPageElement_test")
    WebPageElement_test()
    print("running Accommodation_test")
    Accommodation_test()
    print("running Apartment_test")
    Apartment_test()
    print("running Event_test")
    Event_test()
    print("running LiteraryEvent_test")
    LiteraryEvent_test()
    print("running Clip_test")
    Clip_test()
    print("running MovieClip_test")
    MovieClip_test()
    print("running EducationEvent_test")
    EducationEvent_test()
    print("running MedicalProcedure_test")
    MedicalProcedure_test()
    print("running MedicalEnumeration_test")
    MedicalEnumeration_test()
    print("running PhysicalExam_test")
    PhysicalExam_test()
    print("running Abdomen_test")
    Abdomen_test()
    print("running SocialEvent_test")
    SocialEvent_test()
    print("running MedicalTest_test")
    MedicalTest_test()
    print("running ImagingTest_test")
    ImagingTest_test()
    print("running InteractionCounter_test")
    InteractionCounter_test()
    print("running Audience_test")
    Audience_test()
    print("running PeopleAudience_test")
    PeopleAudience_test()
    print("running ParentAudience_test")
    ParentAudience_test()
    print("running Product_test")
    Product_test()
    print("running ProductModel_test")
    ProductModel_test()
    print("running MedicalTrialDesign_test")
    MedicalTrialDesign_test()
    print("running PlaceboControlledTrial_test")
    PlaceboControlledTrial_test()
    print("running Action_test")
    Action_test()
    print("running CreateAction_test")
    CreateAction_test()
    print("running PhotographAction_test")
    PhotographAction_test()
    print("running USNonprofitType_test")
    USNonprofitType_test()
    print("running Nonprofit501c4_test")
    Nonprofit501c4_test()
    print("running MeasurementTypeEnumeration_test")
    MeasurementTypeEnumeration_test()
    print("running BodyMeasurementTypeEnumeration_test")
    BodyMeasurementTypeEnumeration_test()
    print("running BodyMeasurementWeight_test")
    BodyMeasurementWeight_test()
    print("running Reservation_test")
    Reservation_test()
    print("running FlightReservation_test")
    FlightReservation_test()
    print("running Grant_test")
    Grant_test()
    print("running MonetaryGrant_test")
    MonetaryGrant_test()
    print("running MedicalIndication_test")
    MedicalIndication_test()
    print("running TreatmentIndication_test")
    TreatmentIndication_test()
    print("running Cemetery_test")
    Cemetery_test()
    print("running EnergyEfficiencyEnumeration_test")
    EnergyEfficiencyEnumeration_test()
    print("running EUEnergyEfficiencyEnumeration_test")
    EUEnergyEfficiencyEnumeration_test()
    print("running EUEnergyEfficiencyCategoryA3Plus_test")
    EUEnergyEfficiencyCategoryA3Plus_test()
    print("running DigitalPlatformEnumeration_test")
    DigitalPlatformEnumeration_test()
    print("running MedicalBusiness_test")
    MedicalBusiness_test()
    print("running Specialty_test")
    Specialty_test()
    print("running MedicalSpecialty_test")
    MedicalSpecialty_test()
    print("running PublicHealth_test")
    PublicHealth_test()
    print("running WearableSizeSystemEN13402_test")
    WearableSizeSystemEN13402_test()
    print("running InteractAction_test")
    InteractAction_test()
    print("running CommunicateAction_test")
    CommunicateAction_test()
    print("running CheckInAction_test")
    CheckInAction_test()
    print("running PriceComponentTypeEnumeration_test")
    PriceComponentTypeEnumeration_test()
    print("running DistanceFee_test")
    DistanceFee_test()
    print("running WearableSizeGroupExtraShort_test")
    WearableSizeGroupExtraShort_test()
    print("running EventAttendanceModeEnumeration_test")
    EventAttendanceModeEnumeration_test()
    print("running WearableSizeSystemJP_test")
    WearableSizeSystemJP_test()
    print("running StatusEnumeration_test")
    StatusEnumeration_test()
    print("running OrderStatus_test")
    OrderStatus_test()
    print("running OrderCancelled_test")
    OrderCancelled_test()
    print("running PhysicalActivityCategory_test")
    PhysicalActivityCategory_test()
    print("running StrengthTraining_test")
    StrengthTraining_test()
    print("running FoodEstablishmentReservation_test")
    FoodEstablishmentReservation_test()
    print("running VisualArtwork_test")
    VisualArtwork_test()
    print("running CoverArt_test")
    CoverArt_test()
    print("running MedicineSystem_test")
    MedicineSystem_test()
    print("running Osteopathic_test")
    Osteopathic_test()
    print("running MusicReleaseFormatType_test")
    MusicReleaseFormatType_test()
    print("running DigitalAudioTapeFormat_test")
    DigitalAudioTapeFormat_test()
    print("running HealthInsurancePlan_test")
    HealthInsurancePlan_test()
    print("running SportsOrganization_test")
    SportsOrganization_test()
    print("running AutomotiveBusiness_test")
    AutomotiveBusiness_test()
    print("running AutoRepair_test")
    AutoRepair_test()
    print("running OnlineBusiness_test")
    OnlineBusiness_test()
    print("running MedicalStudyStatus_test")
    MedicalStudyStatus_test()
    print("running ResultsAvailable_test")
    ResultsAvailable_test()
    print("running Suite_test")
    Suite_test()
    print("running EUEnergyEfficiencyCategoryG_test")
    EUEnergyEfficiencyCategoryG_test()
    print("running DeliveryMethod_test")
    DeliveryMethod_test()
    print("running ParcelService_test")
    ParcelService_test()
    print("running TradeAction_test")
    TradeAction_test()
    print("running TipAction_test")
    TipAction_test()
    print("running LearningResource_test")
    LearningResource_test()
    print("running MedicalAudienceType_test")
    MedicalAudienceType_test()
    print("running LodgingBusiness_test")
    LodgingBusiness_test()
    print("running BedAndBreakfast_test")
    BedAndBreakfast_test()
    print("running EngineSpecification_test")
    EngineSpecification_test()
    print("running Bridge_test")
    Bridge_test()
    print("running OnlineStore_test")
    OnlineStore_test()
    print("running ReservationStatusType_test")
    ReservationStatusType_test()
    print("running ReservationCancelled_test")
    ReservationCancelled_test()
    print("running Thesis_test")
    Thesis_test()
    print("running BusinessAudience_test")
    BusinessAudience_test()
    print("running Service_test")
    Service_test()
    print("running FinancialProduct_test")
    FinancialProduct_test()
    print("running InvestmentOrDeposit_test")
    InvestmentOrDeposit_test()
    print("running BrokerageAccount_test")
    BrokerageAccount_test()
    print("running FinancialService_test")
    FinancialService_test()
    print("running AutomatedTeller_test")
    AutomatedTeller_test()
    print("running DayOfWeek_test")
    DayOfWeek_test()
    print("running Thursday_test")
    Thursday_test()
    print("running Crematorium_test")
    Crematorium_test()
    print("running MedicalConditionStage_test")
    MedicalConditionStage_test()
    print("running DietNutrition_test")
    DietNutrition_test()
    print("running Rheumatologic_test")
    Rheumatologic_test()
    print("running AssessAction_test")
    AssessAction_test()
    print("running EmergencyService_test")
    EmergencyService_test()
    print("running FireStation_test")
    FireStation_test()
    print("running Class_test")
    Class_test()
    print("running DataType_test")
    DataType_test()
    print("running Text_test")
    Text_test()
    print("running CssSelectorType_test")
    CssSelectorType_test()
    print("running LaserDiscFormat_test")
    LaserDiscFormat_test()
    print("running Ticket_test")
    Ticket_test()
    print("running OfferItemCondition_test")
    OfferItemCondition_test()
    print("running UsedCondition_test")
    UsedCondition_test()
    print("running WebPage_test")
    WebPage_test()
    print("running CollectionPage_test")
    CollectionPage_test()
    print("running LifestyleModification_test")
    LifestyleModification_test()
    print("running PhysicalActivity_test")
    PhysicalActivity_test()
    print("running LiquorStore_test")
    LiquorStore_test()
    print("running DrugPregnancyCategory_test")
    DrugPregnancyCategory_test()
    print("running FDAcategoryX_test")
    FDAcategoryX_test()
    print("running EducationalOrganization_test")
    EducationalOrganization_test()
    print("running Series_test")
    Series_test()
    print("running EventSeries_test")
    EventSeries_test()
    print("running WearableSizeGroupPetite_test")
    WearableSizeGroupPetite_test()
    print("running HealthAspectEnumeration_test")
    HealthAspectEnumeration_test()
    print("running PrognosisHealthAspect_test")
    PrognosisHealthAspect_test()
    print("running LegalForceStatus_test")
    LegalForceStatus_test()
    print("running PartiallyInForce_test")
    PartiallyInForce_test()
    print("running RestockingFees_test")
    RestockingFees_test()
    print("running WearableMeasurementTypeEnumeration_test")
    WearableMeasurementTypeEnumeration_test()
    print("running WearableMeasurementHips_test")
    WearableMeasurementHips_test()
    print("running UserInteraction_test")
    UserInteraction_test()
    print("running UserPageVisits_test")
    UserPageVisits_test()
    print("running DigitalDocumentPermissionType_test")
    DigitalDocumentPermissionType_test()
    print("running CommentPermission_test")
    CommentPermission_test()
    print("running MediaManipulationRatingEnumeration_test")
    MediaManipulationRatingEnumeration_test()
    print("running OriginalMediaContent_test")
    OriginalMediaContent_test()
    print("running DVDFormat_test")
    DVDFormat_test()
    print("running UserDownloads_test")
    UserDownloads_test()
    print("running TrainReservation_test")
    TrainReservation_test()
    print("running MusicPlaylist_test")
    MusicPlaylist_test()
    print("running VirtualLocation_test")
    VirtualLocation_test()
    print("running EntertainmentBusiness_test")
    EntertainmentBusiness_test()
    print("running AdultEntertainment_test")
    AdultEntertainment_test()
    print("running Review_test")
    Review_test()
    print("running Recommendation_test")
    Recommendation_test()
    print("running MediaObject_test")
    MediaObject_test()
    print("running AudioObject_test")
    AudioObject_test()
    print("running Book_test")
    Book_test()
    print("running Audiobook_test")
    Audiobook_test()
    print("running Person_test")
    Person_test()
    print("running MedicalAudience_test")
    MedicalAudience_test()
    print("running Patient_test")
    Patient_test()
    print("running GovernmentBenefitsType_test")
    GovernmentBenefitsType_test()
    print("running BusinessSupport_test")
    BusinessSupport_test()
    print("running SatireOrParodyContent_test")
    SatireOrParodyContent_test()
    print("running Genitourinary_test")
    Genitourinary_test()
    print("running Collection_test")
    Collection_test()
    print("running ProductCollection_test")
    ProductCollection_test()
    print("running Role_test")
    Role_test()
    print("running OrganizationRole_test")
    OrganizationRole_test()
    print("running FindAction_test")
    FindAction_test()
    print("running GeoCircle_test")
    GeoCircle_test()
    print("running SportsActivityLocation_test")
    SportsActivityLocation_test()
    print("running Room_test")
    Room_test()
    print("running MeetingRoom_test")
    MeetingRoom_test()
    print("running UKNonprofitType_test")
    UKNonprofitType_test()
    print("running Trip_test")
    Trip_test()
    print("running BoatTrip_test")
    BoatTrip_test()
    print("running EmployeeRole_test")
    EmployeeRole_test()
    print("running BookStore_test")
    BookStore_test()
    print("running Gastroenterologic_test")
    Gastroenterologic_test()
    print("running UpdateAction_test")
    UpdateAction_test()
    print("running SoftwareApplication_test")
    SoftwareApplication_test()
    print("running MobileApplication_test")
    MobileApplication_test()
    print("running DiagnosticProcedure_test")
    DiagnosticProcedure_test()
    print("running LegalService_test")
    LegalService_test()
    print("running Attorney_test")
    Attorney_test()
    print("running EUEnergyEfficiencyCategoryA_test")
    EUEnergyEfficiencyCategoryA_test()
    print("running BloodTest_test")
    BloodTest_test()
    print("running RadioStation_test")
    RadioStation_test()
    print("running ComputerStore_test")
    ComputerStore_test()
    print("running RentalCarReservation_test")
    RentalCarReservation_test()
    print("running ItemList_test")
    ItemList_test()
    print("running CausesHealthAspect_test")
    CausesHealthAspect_test()
    print("running RestrictedDiet_test")
    RestrictedDiet_test()
    print("running VegetarianDiet_test")
    VegetarianDiet_test()
    print("running MerchantReturnPolicySeasonalOverride_test")
    MerchantReturnPolicySeasonalOverride_test()
    print("running RearWheelDriveConfiguration_test")
    RearWheelDriveConfiguration_test()
    print("running ContactPointOption_test")
    ContactPointOption_test()
    print("running IgnoreAction_test")
    IgnoreAction_test()
    print("running UserCheckins_test")
    UserCheckins_test()
    print("running MoveAction_test")
    MoveAction_test()
    print("running ArriveAction_test")
    ArriveAction_test()
    print("running RecyclingCenter_test")
    RecyclingCenter_test()
    print("running HomeAndConstructionBusiness_test")
    HomeAndConstructionBusiness_test()
    print("running RoofingContractor_test")
    RoofingContractor_test()
    print("running WearableMeasurementLength_test")
    WearableMeasurementLength_test()
    print("running ReservationConfirmed_test")
    ReservationConfirmed_test()
    print("running EUEnergyEfficiencyCategoryC_test")
    EUEnergyEfficiencyCategoryC_test()
    print("running GeoCoordinates_test")
    GeoCoordinates_test()
    print("running PriceTypeEnumeration_test")
    PriceTypeEnumeration_test()
    print("running SRP_test")
    SRP_test()
    print("running TaxiStand_test")
    TaxiStand_test()
    print("running Nonprofit501c2_test")
    Nonprofit501c2_test()
    print("running ClothingStore_test")
    ClothingStore_test()
    print("running VideoObject_test")
    VideoObject_test()
    print("running VideoObjectSnapshot_test")
    VideoObjectSnapshot_test()
    print("running OverviewHealthAspect_test")
    OverviewHealthAspect_test()
    print("running Guide_test")
    Guide_test()
    print("running TransferAction_test")
    TransferAction_test()
    print("running MoneyTransfer_test")
    MoneyTransfer_test()
    print("running Festival_test")
    Festival_test()
    print("running Endocrine_test")
    Endocrine_test()
    print("running WearableMeasurementOutsideLeg_test")
    WearableMeasurementOutsideLeg_test()
    print("running MusicAlbum_test")
    MusicAlbum_test()
    print("running Article_test")
    Article_test()
    print("running NewsArticle_test")
    NewsArticle_test()
    print("running AskPublicNewsArticle_test")
    AskPublicNewsArticle_test()
    print("running ServiceChannel_test")
    ServiceChannel_test()
    print("running Saturday_test")
    Saturday_test()
    print("running OccupationalExperienceRequirements_test")
    OccupationalExperienceRequirements_test()
    print("running HealthPlanNetwork_test")
    HealthPlanNetwork_test()
    print("running TouristTrip_test")
    TouristTrip_test()
    print("running SymptomsHealthAspect_test")
    SymptomsHealthAspect_test()
    print("running Neuro_test")
    Neuro_test()
    print("running HobbyShop_test")
    HobbyShop_test()
    print("running BodyMeasurementFoot_test")
    BodyMeasurementFoot_test()
    print("running Casino_test")
    Casino_test()
    print("running SoftwareSourceCode_test")
    SoftwareSourceCode_test()
    print("running MultiCenterTrial_test")
    MultiCenterTrial_test()
    print("running ItemAvailability_test")
    ItemAvailability_test()
    print("running BackOrder_test")
    BackOrder_test()
    print("running CreativeWorkSeason_test")
    CreativeWorkSeason_test()
    print("running PodcastSeason_test")
    PodcastSeason_test()
    print("running EventReservation_test")
    EventReservation_test()
    print("running MedicalProcedureType_test")
    MedicalProcedureType_test()
    print("running Rating_test")
    Rating_test()
    print("running AggregateRating_test")
    AggregateRating_test()
    print("running DataDownload_test")
    DataDownload_test()
    print("running MerchantReturnEnumeration_test")
    MerchantReturnEnumeration_test()
    print("running MerchantReturnUnlimitedWindow_test")
    MerchantReturnUnlimitedWindow_test()
    print("running CreativeWorkSeries_test")
    CreativeWorkSeries_test()
    print("running Periodical_test")
    Periodical_test()
    print("running ComicSeries_test")
    ComicSeries_test()
    print("running AdultOrientedEnumeration_test")
    AdultOrientedEnumeration_test()
    print("running SexualContentConsideration_test")
    SexualContentConsideration_test()
    print("running GovernmentService_test")
    GovernmentService_test()
    print("running Landform_test")
    Landform_test()
    print("running Continent_test")
    Continent_test()
    print("running EducationalOccupationalCredential_test")
    EducationalOccupationalCredential_test()
    print("running MedicalCondition_test")
    MedicalCondition_test()
    print("running InfectiousDisease_test")
    InfectiousDisease_test()
    print("running ReturnMethodEnumeration_test")
    ReturnMethodEnumeration_test()
    print("running ReturnByMail_test")
    ReturnByMail_test()
    print("running InfectiousAgentClass_test")
    InfectiousAgentClass_test()
    print("running Prion_test")
    Prion_test()
    print("running PerformingGroup_test")
    PerformingGroup_test()
    print("running MusicGroup_test")
    MusicGroup_test()
    print("running SingleCenterTrial_test")
    SingleCenterTrial_test()
    print("running Nonprofit501c10_test")
    Nonprofit501c10_test()
    print("running MedicalTestPanel_test")
    MedicalTestPanel_test()
    print("running DrugStrength_test")
    DrugStrength_test()
    print("running TypeAndQuantityNode_test")
    TypeAndQuantityNode_test()
    print("running MediaSubscription_test")
    MediaSubscription_test()
    print("running DrugCostCategory_test")
    DrugCostCategory_test()
    print("running Retail_test")
    Retail_test()
    print("running WearableSizeGroupHusky_test")
    WearableSizeGroupHusky_test()
    print("running DiabeticDiet_test")
    DiabeticDiet_test()
    print("running MedicalImagingTechnique_test")
    MedicalImagingTechnique_test()
    print("running XRay_test")
    XRay_test()
    print("running WearableMeasurementInseam_test")
    WearableMeasurementInseam_test()
    print("running SeeDoctorHealthAspect_test")
    SeeDoctorHealthAspect_test()
    print("running MusicEvent_test")
    MusicEvent_test()
    print("running MixedEventAttendanceMode_test")
    MixedEventAttendanceMode_test()
    print("running Dermatology_test")
    Dermatology_test()
    print("running TherapeuticProcedure_test")
    TherapeuticProcedure_test()
    print("running MedicalTherapy_test")
    MedicalTherapy_test()
    print("running Episode_test")
    Episode_test()
    print("running RadioEpisode_test")
    RadioEpisode_test()
    print("running MedicalSignOrSymptom_test")
    MedicalSignOrSymptom_test()
    print("running BodyMeasurementArm_test")
    BodyMeasurementArm_test()
    print("running ChooseAction_test")
    ChooseAction_test()
    print("running VoteAction_test")
    VoteAction_test()
    print("running WPSideBar_test")
    WPSideBar_test()
    print("running Residence_test")
    Residence_test()
    print("running ApartmentComplex_test")
    ApartmentComplex_test()
    print("running Sculpture_test")
    Sculpture_test()
    print("running Surgical_test")
    Surgical_test()
    print("running Terminated_test")
    Terminated_test()
    print("running EnergyStarEnergyEfficiencyEnumeration_test")
    EnergyStarEnergyEfficiencyEnumeration_test()
    print("running BankAccount_test")
    BankAccount_test()
    print("running DepositAccount_test")
    DepositAccount_test()
    print("running MovingCompany_test")
    MovingCompany_test()
    print("running Offer_test")
    Offer_test()
    print("running AggregateOffer_test")
    AggregateOffer_test()
    print("running WearableSizeSystemGS1_test")
    WearableSizeSystemGS1_test()
    print("running EmploymentAgency_test")
    EmploymentAgency_test()
    print("running Ligament_test")
    Ligament_test()
    print("running FDAcategoryC_test")
    FDAcategoryC_test()
    print("running Optometric_test")
    Optometric_test()
    print("running OutletStore_test")
    OutletStore_test()
    print("running RefundTypeEnumeration_test")
    RefundTypeEnumeration_test()
    print("running StoreCreditRefund_test")
    StoreCreditRefund_test()
    print("running InternetCafe_test")
    InternetCafe_test()
    print("running AdministrativeArea_test")
    AdministrativeArea_test()
    print("running GameServerStatus_test")
    GameServerStatus_test()
    print("running OnlineFull_test")
    OnlineFull_test()
    print("running ConsumeAction_test")
    ConsumeAction_test()
    print("running ListenAction_test")
    ListenAction_test()
    print("running SocialMediaPosting_test")
    SocialMediaPosting_test()
    print("running MusicVenue_test")
    MusicVenue_test()
    print("running Genetic_test")
    Genetic_test()
    print("running Head_test")
    Head_test()
    print("running MSRP_test")
    MSRP_test()
    print("running PoliceStation_test")
    PoliceStation_test()
    print("running Friday_test")
    Friday_test()
    print("running PaymentStatusType_test")
    PaymentStatusType_test()
    print("running PaymentComplete_test")
    PaymentComplete_test()
    print("running CableOrSatelliteService_test")
    CableOrSatelliteService_test()
    print("running PayAction_test")
    PayAction_test()
    print("running DeliveryTimeSettings_test")
    DeliveryTimeSettings_test()
    print("running WarrantyPromise_test")
    WarrantyPromise_test()
    print("running MobilePhoneStore_test")
    MobilePhoneStore_test()
    print("running Nonprofit501q_test")
    Nonprofit501q_test()
    print("running DrugCost_test")
    DrugCost_test()
    print("running ReadPermission_test")
    ReadPermission_test()
    print("running WearableSizeSystemContinental_test")
    WearableSizeSystemContinental_test()
    print("running RentAction_test")
    RentAction_test()
    print("running ShortStory_test")
    ShortStory_test()
    print("running BreadcrumbList_test")
    BreadcrumbList_test()
    print("running MedicalObservationalStudyDesign_test")
    MedicalObservationalStudyDesign_test()
    print("running Observational_test")
    Observational_test()
    print("running LandmarksOrHistoricalBuildings_test")
    LandmarksOrHistoricalBuildings_test()
    print("running Seat_test")
    Seat_test()
    print("running PaymentService_test")
    PaymentService_test()
    print("running PercutaneousProcedure_test")
    PercutaneousProcedure_test()
    print("running OpenTrial_test")
    OpenTrial_test()
    print("running PaymentDeclined_test")
    PaymentDeclined_test()
    print("running MusicAlbumProductionType_test")
    MusicAlbumProductionType_test()
    print("running Museum_test")
    Museum_test()
    print("running Taxi_test")
    Taxi_test()
    print("running TrainTrip_test")
    TrainTrip_test()
    print("running GeospatialGeometry_test")
    GeospatialGeometry_test()
    print("running HealthAndBeautyBusiness_test")
    HealthAndBeautyBusiness_test()
    print("running Nonprofit501c24_test")
    Nonprofit501c24_test()
    print("running Vessel_test")
    Vessel_test()
    print("running Vein_test")
    Vein_test()
    print("running ItemListOrderType_test")
    ItemListOrderType_test()
    print("running ItemListOrderDescending_test")
    ItemListOrderDescending_test()
    print("running MedicalEvidenceLevel_test")
    MedicalEvidenceLevel_test()
    print("running EvidenceLevelC_test")
    EvidenceLevelC_test()
    print("running Artery_test")
    Artery_test()
    print("running NoninvasiveProcedure_test")
    NoninvasiveProcedure_test()
    print("running SiteNavigationElement_test")
    SiteNavigationElement_test()
    print("running Neck_test")
    Neck_test()
    print("running DoseSchedule_test")
    DoseSchedule_test()
    print("running ReturnLabelSourceEnumeration_test")
    ReturnLabelSourceEnumeration_test()
    print("running ReturnLabelInBox_test")
    ReturnLabelInBox_test()
    print("running HealthcareConsideration_test")
    HealthcareConsideration_test()
    print("running InformAction_test")
    InformAction_test()
    print("running ConfirmAction_test")
    ConfirmAction_test()
    print("running FoodService_test")
    FoodService_test()
    print("running ControlAction_test")
    ControlAction_test()
    print("running DeactivateAction_test")
    DeactivateAction_test()
    print("running TheaterGroup_test")
    TheaterGroup_test()
    print("running OrderPaymentDue_test")
    OrderPaymentDue_test()
    print("running AutoRental_test")
    AutoRental_test()
    print("running DigitalFormat_test")
    DigitalFormat_test()
    print("running InviteAction_test")
    InviteAction_test()
    print("running PodcastSeries_test")
    PodcastSeries_test()
    print("running SizeSpecification_test")
    SizeSpecification_test()
    print("running WebContent_test")
    WebContent_test()
    print("running HealthTopicContent_test")
    HealthTopicContent_test()
    print("running CriticReview_test")
    CriticReview_test()
    print("running CleaningFee_test")
    CleaningFee_test()
    print("running Aquarium_test")
    Aquarium_test()
    print("running WearableSizeSystemIT_test")
    WearableSizeSystemIT_test()
    print("running PublicSwimmingPool_test")
    PublicSwimmingPool_test()
    print("running WearableSizeGroupPlus_test")
    WearableSizeGroupPlus_test()
    print("running PodcastEpisode_test")
    PodcastEpisode_test()
    print("running Dataset_test")
    Dataset_test()
    print("running Conversation_test")
    Conversation_test()
    print("running MedicalOrganization_test")
    MedicalOrganization_test()
    print("running MedicalClinic_test")
    MedicalClinic_test()
    print("running CovidTestingFacility_test")
    CovidTestingFacility_test()
    print("running OutOfStock_test")
    OutOfStock_test()
    print("running PostalCodeRangeSpecification_test")
    PostalCodeRangeSpecification_test()
    print("running Nonprofit501c18_test")
    Nonprofit501c18_test()
    print("running ReactAction_test")
    ReactAction_test()
    print("running WantAction_test")
    WantAction_test()
    print("running MixtapeAlbum_test")
    MixtapeAlbum_test()
    print("running Nonprofit501c20_test")
    Nonprofit501c20_test()
    print("running Nonprofit501c15_test")
    Nonprofit501c15_test()
    print("running BookFormatType_test")
    BookFormatType_test()
    print("running GraphicNovel_test")
    GraphicNovel_test()
    print("running TaxiReservation_test")
    TaxiReservation_test()
    print("running Bacteria_test")
    Bacteria_test()
    print("running NightClub_test")
    NightClub_test()
    print("running OrganizeAction_test")
    OrganizeAction_test()
    print("running PlanAction_test")
    PlanAction_test()
    print("running ScheduleAction_test")
    ScheduleAction_test()
    print("running ScholarlyArticle_test")
    ScholarlyArticle_test()
    print("running PlaceOfWorship_test")
    PlaceOfWorship_test()
    print("running BuddhistTemple_test")
    BuddhistTemple_test()
    print("running SatiricalArticle_test")
    SatiricalArticle_test()
    print("running FoodEstablishment_test")
    FoodEstablishment_test()
    print("running MarryAction_test")
    MarryAction_test()
    print("running ProfilePage_test")
    ProfilePage_test()
    print("running AmusementPark_test")
    AmusementPark_test()
    print("running BowlingAlley_test")
    BowlingAlley_test()
    print("running Sunday_test")
    Sunday_test()
    print("running ScreeningHealthAspect_test")
    ScreeningHealthAspect_test()
    print("running PaymentMethod_test")
    PaymentMethod_test()
    print("running PaymentCard_test")
    PaymentCard_test()
    print("running RespiratoryTherapy_test")
    RespiratoryTherapy_test()
    print("running DataFeed_test")
    DataFeed_test()
    print("running CarUsageType_test")
    CarUsageType_test()
    print("running TaxiVehicleUsage_test")
    TaxiVehicleUsage_test()
    print("running ElectronicsStore_test")
    ElectronicsStore_test()
    print("running Toxicologic_test")
    Toxicologic_test()
    print("running CDFormat_test")
    CDFormat_test()
    print("running VideoGameClip_test")
    VideoGameClip_test()
    print("running AchieveAction_test")
    AchieveAction_test()
    print("running TieAction_test")
    TieAction_test()
    print("running AllWheelDriveConfiguration_test")
    AllWheelDriveConfiguration_test()
    print("running Bone_test")
    Bone_test()
    print("running BroadcastChannel_test")
    BroadcastChannel_test()
    print("running RadioChannel_test")
    RadioChannel_test()
    print("running AMRadioChannel_test")
    AMRadioChannel_test()
    print("running PET_test")
    PET_test()
    print("running MusicAlbumReleaseType_test")
    MusicAlbumReleaseType_test()
    print("running Nonprofit501n_test")
    Nonprofit501n_test()
    print("running Project_test")
    Project_test()
    print("running ResearchProject_test")
    ResearchProject_test()
    print("running DislikeAction_test")
    DislikeAction_test()
    print("running Schedule_test")
    Schedule_test()
    print("running ContactPage_test")
    ContactPage_test()
    print("running AlignmentObject_test")
    AlignmentObject_test()
    print("running PriceSpecification_test")
    PriceSpecification_test()
    print("running PaymentChargeSpecification_test")
    PaymentChargeSpecification_test()
    print("running WebAPI_test")
    WebAPI_test()
    print("running TVClip_test")
    TVClip_test()
    print("running Quantity_test")
    Quantity_test()
    print("running Mass_test")
    Mass_test()
    print("running GenderType_test")
    GenderType_test()
    print("running Male_test")
    Male_test()
    print("running DangerousGoodConsideration_test")
    DangerousGoodConsideration_test()
    print("running HyperToc_test")
    HyperToc_test()
    print("running Restaurant_test")
    Restaurant_test()
    print("running Permit_test")
    Permit_test()
    print("running GovernmentPermit_test")
    GovernmentPermit_test()
    print("running SportsClub_test")
    SportsClub_test()
    print("running PublicationEvent_test")
    PublicationEvent_test()
    print("running TravelAgency_test")
    TravelAgency_test()
    print("running NailSalon_test")
    NailSalon_test()
    print("running RefurbishedCondition_test")
    RefurbishedCondition_test()
    print("running Plumber_test")
    Plumber_test()
    print("running TouristInformationCenter_test")
    TouristInformationCenter_test()
    print("running QuoteAction_test")
    QuoteAction_test()
    print("running WearableSizeGroupBoys_test")
    WearableSizeGroupBoys_test()
    print("running ActionStatusType_test")
    ActionStatusType_test()
    print("running CompletedActionStatus_test")
    CompletedActionStatus_test()
    print("running BodyOfWater_test")
    BodyOfWater_test()
    print("running OceanBodyOfWater_test")
    OceanBodyOfWater_test()
    print("running PlayGameAction_test")
    PlayGameAction_test()
    print("running ActivateAction_test")
    ActivateAction_test()
    print("running MenuSection_test")
    MenuSection_test()
    print("running MovieRentalStore_test")
    MovieRentalStore_test()
    print("running Chapter_test")
    Chapter_test()
    print("running BodyMeasurementUnderbust_test")
    BodyMeasurementUnderbust_test()
    print("running Order_test")
    Order_test()
    print("running ArtGallery_test")
    ArtGallery_test()
    print("running Nonprofit501c8_test")
    Nonprofit501c8_test()
    print("running SteeringPositionValue_test")
    SteeringPositionValue_test()
    print("running LeftHandDriving_test")
    LeftHandDriving_test()
    print("running ComicStory_test")
    ComicStory_test()
    print("running ComicCoverArt_test")
    ComicCoverArt_test()
    print("running LikeAction_test")
    LikeAction_test()
    print("running WearableMeasurementCollar_test")
    WearableMeasurementCollar_test()
    print("running ItemListUnordered_test")
    ItemListUnordered_test()
    print("running GameAvailabilityEnumeration_test")
    GameAvailabilityEnumeration_test()
    print("running DemoGameAvailability_test")
    DemoGameAvailability_test()
    print("running Canal_test")
    Canal_test()
    print("running SideEffectsHealthAspect_test")
    SideEffectsHealthAspect_test()
    print("running AudiobookFormat_test")
    AudiobookFormat_test()
    print("running MathSolver_test")
    MathSolver_test()
    print("running EUEnergyEfficiencyCategoryB_test")
    EUEnergyEfficiencyCategoryB_test()
    print("running PlayAction_test")
    PlayAction_test()
    print("running ExerciseAction_test")
    ExerciseAction_test()
    print("running BioChemEntity_test")
    BioChemEntity_test()
    print("running Gene_test")
    Gene_test()
    print("running Downpayment_test")
    Downpayment_test()
    print("running Invoice_test")
    Invoice_test()
    print("running GovernmentOffice_test")
    GovernmentOffice_test()
    print("running PostOffice_test")
    PostOffice_test()
    print("running DigitalDocument_test")
    DigitalDocument_test()
    print("running TextDigitalDocument_test")
    TextDigitalDocument_test()
    print("running Flight_test")
    Flight_test()
    print("running DecontextualizedContent_test")
    DecontextualizedContent_test()
    print("running BedType_test")
    BedType_test()
    print("running BlogPosting_test")
    BlogPosting_test()
    print("running Distance_test")
    Distance_test()
    print("running ReservationPending_test")
    ReservationPending_test()
    print("running LodgingReservation_test")
    LodgingReservation_test()
    print("running SearchResultsPage_test")
    SearchResultsPage_test()
    print("running TennisComplex_test")
    TennisComplex_test()
    print("running GovernmentBuilding_test")
    GovernmentBuilding_test()
    print("running Embassy_test")
    Embassy_test()
    print("running DamagedCondition_test")
    DamagedCondition_test()
    print("running LegalValueLevel_test")
    LegalValueLevel_test()
    print("running UnofficialLegalValue_test")
    UnofficialLegalValue_test()
    print("running MedicalGuideline_test")
    MedicalGuideline_test()
    print("running CampingPitch_test")
    CampingPitch_test()
    print("running LoseAction_test")
    LoseAction_test()
    print("running WearableSizeGroupTall_test")
    WearableSizeGroupTall_test()
    print("running KosherDiet_test")
    KosherDiet_test()
    print("running FDAcategoryB_test")
    FDAcategoryB_test()
    print("running WearableSizeGroupJuniors_test")
    WearableSizeGroupJuniors_test()
    print("running ElementarySchool_test")
    ElementarySchool_test()
    print("running Message_test")
    Message_test()
    print("running EmailMessage_test")
    EmailMessage_test()
    print("running SaleEvent_test")
    SaleEvent_test()
    print("running MediaReviewItem_test")
    MediaReviewItem_test()
    print("running ImageObject_test")
    ImageObject_test()
    print("running ImageObjectSnapshot_test")
    ImageObjectSnapshot_test()
    print("running Pharmacy_test")
    Pharmacy_test()
    print("running ContactPoint_test")
    ContactPoint_test()
    print("running PublicHolidays_test")
    PublicHolidays_test()
    print("running BusTrip_test")
    BusTrip_test()
    print("running Physician_test")
    Physician_test()
    print("running EventStatusType_test")
    EventStatusType_test()
    print("running EventCancelled_test")
    EventCancelled_test()
    print("running ResultsNotAvailable_test")
    ResultsNotAvailable_test()
    print("running Campground_test")
    Campground_test()
    print("running Joint_test")
    Joint_test()
    print("running MerchantReturnPolicy_test")
    MerchantReturnPolicy_test()
    print("running CompleteDataFeed_test")
    CompleteDataFeed_test()
    print("running PrimaryCare_test")
    PrimaryCare_test()
    print("running City_test")
    City_test()
    print("running HealthPlanCostSharingSpecification_test")
    HealthPlanCostSharingSpecification_test()
    print("running MedicalStudy_test")
    MedicalStudy_test()
    print("running MedicalObservationalStudy_test")
    MedicalObservationalStudy_test()
    print("running LockerDelivery_test")
    LockerDelivery_test()
    print("running ItemListOrderAscending_test")
    ItemListOrderAscending_test()
    print("running AudioObjectSnapshot_test")
    AudioObjectSnapshot_test()
    print("running Statement_test")
    Statement_test()
    print("running WearableMeasurementWaist_test")
    WearableMeasurementWaist_test()
    print("running WearableMeasurementBack_test")
    WearableMeasurementBack_test()
    print("running AnaerobicActivity_test")
    AnaerobicActivity_test()
    print("running ReducedRelevanceForChildrenConsideration_test")
    ReducedRelevanceForChildrenConsideration_test()
    print("running ResearchOrganization_test")
    ResearchOrganization_test()
    print("running Eye_test")
    Eye_test()
    print("running QAPage_test")
    QAPage_test()
    print("running Playground_test")
    Playground_test()
    print("running ChemicalSubstance_test")
    ChemicalSubstance_test()
    print("running WearableSizeGroupRegular_test")
    WearableSizeGroupRegular_test()
    print("running SubwayStation_test")
    SubwayStation_test()
    print("running SomeProducts_test")
    SomeProducts_test()
    print("running MonetaryAmount_test")
    MonetaryAmount_test()
    print("running AddAction_test")
    AddAction_test()
    print("running InsertAction_test")
    InsertAction_test()
    print("running ProductGroup_test")
    ProductGroup_test()
    print("running LivingWithHealthAspect_test")
    LivingWithHealthAspect_test()
    print("running RecommendedDoseSchedule_test")
    RecommendedDoseSchedule_test()
    print("running ActionAccessSpecification_test")
    ActionAccessSpecification_test()
    print("running Beach_test")
    Beach_test()
    print("running OccupationalActivity_test")
    OccupationalActivity_test()
    print("running FDAcategoryD_test")
    FDAcategoryD_test()
    print("running Podiatric_test")
    Podiatric_test()
    print("running MedicalScholarlyArticle_test")
    MedicalScholarlyArticle_test()
    print("running OfferForLease_test")
    OfferForLease_test()
    print("running Church_test")
    Church_test()
    print("running CatholicChurch_test")
    CatholicChurch_test()
    print("running ReservationHold_test")
    ReservationHold_test()
    print("running Nonprofit501c6_test")
    Nonprofit501c6_test()
    print("running Midwifery_test")
    Midwifery_test()
    print("running LiveAlbum_test")
    LiveAlbum_test()
    print("running ExhibitionEvent_test")
    ExhibitionEvent_test()
    print("running FullGameAvailability_test")
    FullGameAvailability_test()
    print("running ResumeAction_test")
    ResumeAction_test()
    print("running ProgramMembership_test")
    ProgramMembership_test()
    print("running DiscoverAction_test")
    DiscoverAction_test()
    print("running OfflinePermanently_test")
    OfflinePermanently_test()
    print("running CafeOrCoffeeShop_test")
    CafeOrCoffeeShop_test()
    print("running ReimbursementCap_test")
    ReimbursementCap_test()
    print("running DryCleaningOrLaundry_test")
    DryCleaningOrLaundry_test()
    print("running ContagiousnessHealthAspect_test")
    ContagiousnessHealthAspect_test()
    print("running RVPark_test")
    RVPark_test()
    print("running LymphaticVessel_test")
    LymphaticVessel_test()
    print("running ExchangeRefund_test")
    ExchangeRefund_test()
    print("running CharitableIncorporatedOrganization_test")
    CharitableIncorporatedOrganization_test()
    print("running Discontinued_test")
    Discontinued_test()
    print("running BodyMeasurementNeck_test")
    BodyMeasurementNeck_test()
    print("running EvidenceLevelA_test")
    EvidenceLevelA_test()
    print("running SpeechPathology_test")
    SpeechPathology_test()
    print("running OpeningHoursSpecification_test")
    OpeningHoursSpecification_test()
    print("running PresentationDigitalDocument_test")
    PresentationDigitalDocument_test()
    print("running ProfessionalService_test")
    ProfessionalService_test()
    print("running BankOrCreditUnion_test")
    BankOrCreditUnion_test()
    print("running IngredientsHealthAspect_test")
    IngredientsHealthAspect_test()
    print("running PhysicalTherapy_test")
    PhysicalTherapy_test()
    print("running Substance_test")
    Substance_test()
    print("running Drug_test")
    Drug_test()
    print("running Season_test")
    Season_test()
    print("running EventVenue_test")
    EventVenue_test()
    print("running EPRelease_test")
    EPRelease_test()
    print("running ReservationPackage_test")
    ReservationPackage_test()
    print("running AutoBodyShop_test")
    AutoBodyShop_test()
    print("running TypesHealthAspect_test")
    TypesHealthAspect_test()
    print("running CheckAction_test")
    CheckAction_test()
    print("running StudioAlbum_test")
    StudioAlbum_test()
    print("running DisabilitySupport_test")
    DisabilitySupport_test()
    print("running StagesHealthAspect_test")
    StagesHealthAspect_test()
    print("running Legislation_test")
    Legislation_test()
    print("running LegislationObject_test")
    LegislationObject_test()
    print("running Airport_test")
    Airport_test()
    print("running UserLikes_test")
    UserLikes_test()
    print("running AmpStory_test")
    AmpStory_test()
    print("running CookAction_test")
    CookAction_test()
    print("running MedicalWebPage_test")
    MedicalWebPage_test()
    print("running Throat_test")
    Throat_test()
    print("running Urologic_test")
    Urologic_test()
    print("running StadiumOrArena_test")
    StadiumOrArena_test()
    print("running FDAnotEvaluated_test")
    FDAnotEvaluated_test()
    print("running Cardiovascular_test")
    Cardiovascular_test()
    print("running UserComments_test")
    UserComments_test()
    print("running Lung_test")
    Lung_test()
    print("running ReserveAction_test")
    ReserveAction_test()
    print("running OrderInTransit_test")
    OrderInTransit_test()
    print("running BusinessEvent_test")
    BusinessEvent_test()
    print("running MusicComposition_test")
    MusicComposition_test()
    print("running WinAction_test")
    WinAction_test()
    print("running SalePrice_test")
    SalePrice_test()
    print("running ListItem_test")
    ListItem_test()
    print("running HowToTip_test")
    HowToTip_test()
    print("running Longitudinal_test")
    Longitudinal_test()
    print("running Hackathon_test")
    Hackathon_test()
    print("running StatisticalPopulation_test")
    StatisticalPopulation_test()
    print("running WriteAction_test")
    WriteAction_test()
    print("running HowToSection_test")
    HowToSection_test()
    print("running HVACBusiness_test")
    HVACBusiness_test()
    print("running RepaymentSpecification_test")
    RepaymentSpecification_test()
    print("running RelatedTopicsHealthAspect_test")
    RelatedTopicsHealthAspect_test()
    print("running UserPlusOnes_test")
    UserPlusOnes_test()
    print("running Gynecologic_test")
    Gynecologic_test()
    print("running MerchantReturnNotPermitted_test")
    MerchantReturnNotPermitted_test()
    print("running OrderPickupAvailable_test")
    OrderPickupAvailable_test()
    print("running DeliveryEvent_test")
    DeliveryEvent_test()
    print("running LimitedByGuaranteeCharity_test")
    LimitedByGuaranteeCharity_test()
    print("running ComputerLanguage_test")
    ComputerLanguage_test()
    print("running WearableMeasurementCup_test")
    WearableMeasurementCup_test()
    print("running ReportedDoseSchedule_test")
    ReportedDoseSchedule_test()
    print("running Vehicle_test")
    Vehicle_test()
    print("running Motorcycle_test")
    Motorcycle_test()
    print("running Nonprofit501c21_test")
    Nonprofit501c21_test()
    print("running FollowAction_test")
    FollowAction_test()
    print("running Game_test")
    Game_test()
    print("running VideoGame_test")
    VideoGame_test()
    print("running OpinionNewsArticle_test")
    OpinionNewsArticle_test()
    print("running MapCategoryType_test")
    MapCategoryType_test()
    print("running NGO_test")
    NGO_test()
    print("running BusStation_test")
    BusStation_test()
    print("running TrainStation_test")
    TrainStation_test()
    print("running SportingGoodsStore_test")
    SportingGoodsStore_test()
    print("running UnRegisterAction_test")
    UnRegisterAction_test()
    print("running DoubleBlindedTrial_test")
    DoubleBlindedTrial_test()
    print("running ToyStore_test")
    ToyStore_test()
    print("running UnemploymentSupport_test")
    UnemploymentSupport_test()
    print("running MedicalSign_test")
    MedicalSign_test()
    print("running MovieSeries_test")
    MovieSeries_test()
    print("running Car_test")
    Car_test()
    print("running SoldOut_test")
    SoldOut_test()
    print("running Physiotherapy_test")
    Physiotherapy_test()
    print("running Pond_test")
    Pond_test()
    print("running PropertyValueSpecification_test")
    PropertyValueSpecification_test()
    print("running BorrowAction_test")
    BorrowAction_test()
    print("running HinduDiet_test")
    HinduDiet_test()
    print("running Hematologic_test")
    Hematologic_test()
    print("running LowSaltDiet_test")
    LowSaltDiet_test()
    print("running XPathType_test")
    XPathType_test()
    print("running SingleBlindedTrial_test")
    SingleBlindedTrial_test()
    print("running SingleRelease_test")
    SingleRelease_test()
    print("running WearableSizeSystemAU_test")
    WearableSizeSystemAU_test()
    print("running UKTrust_test")
    UKTrust_test()
    print("running PaidLeave_test")
    PaidLeave_test()
    print("running EditedOrCroppedContent_test")
    EditedOrCroppedContent_test()
    print("running Nonprofit501c12_test")
    Nonprofit501c12_test()
    print("running VitalSign_test")
    VitalSign_test()
    print("running WearableSizeSystemMX_test")
    WearableSizeSystemMX_test()
    print("running GardenStore_test")
    GardenStore_test()
    print("running SearchRescueOrganization_test")
    SearchRescueOrganization_test()
    print("running BrainStructure_test")
    BrainStructure_test()
    print("running TreatmentsHealthAspect_test")
    TreatmentsHealthAspect_test()
    print("running HowTo_test")
    HowTo_test()
    print("running Recipe_test")
    Recipe_test()
    print("running WearableSizeGroupMaternity_test")
    WearableSizeGroupMaternity_test()
    print("running ReplaceAction_test")
    ReplaceAction_test()
    print("running Code_test")
    Code_test()
    print("running Nonprofit501c16_test")
    Nonprofit501c16_test()
    print("running SizeSystemMetric_test")
    SizeSystemMetric_test()
    print("running ChildCare_test")
    ChildCare_test()
    print("running PropertyValue_test")
    PropertyValue_test()
    print("running LocationFeatureSpecification_test")
    LocationFeatureSpecification_test()
    print("running RemixAlbum_test")
    RemixAlbum_test()
    print("running Date_test")
    Date_test()
    print("running DrugPrescriptionStatus_test")
    DrugPrescriptionStatus_test()
    print("running OTC_test")
    OTC_test()
    print("running Taxon_test")
    Taxon_test()
    print("running AccountingService_test")
    AccountingService_test()
    print("running EventScheduled_test")
    EventScheduled_test()
    print("running WearableMeasurementSleeve_test")
    WearableMeasurementSleeve_test()
    print("running ListPrice_test")
    ListPrice_test()
    print("running WebApplication_test")
    WebApplication_test()
    print("running Suspended_test")
    Suspended_test()
    print("running Subscription_test")
    Subscription_test()
    print("running FreeReturn_test")
    FreeReturn_test()
    print("running HowToItem_test")
    HowToItem_test()
    print("running HowToTool_test")
    HowToTool_test()
    print("running InvestmentFund_test")
    InvestmentFund_test()
    print("running FailedActionStatus_test")
    FailedActionStatus_test()
    print("running RealEstateAgent_test")
    RealEstateAgent_test()
    print("running AdvertiserContentArticle_test")
    AdvertiserContentArticle_test()
    print("running Drawing_test")
    Drawing_test()
    print("running RegisterAction_test")
    RegisterAction_test()
    print("running CommunityHealth_test")
    CommunityHealth_test()
    print("running LoanOrCredit_test")
    LoanOrCredit_test()
    print("running MortgageLoan_test")
    MortgageLoan_test()
    print("running Comment_test")
    Comment_test()
    print("running CorrectionComment_test")
    CorrectionComment_test()
    print("running BusStop_test")
    BusStop_test()
    print("running OfficeEquipmentStore_test")
    OfficeEquipmentStore_test()
    print("running MisconceptionsHealthAspect_test")
    MisconceptionsHealthAspect_test()
    print("running WearableMeasurementHeight_test")
    WearableMeasurementHeight_test()
    print("running PrependAction_test")
    PrependAction_test()
    print("running Appearance_test")
    Appearance_test()
    print("running Resort_test")
    Resort_test()
    print("running SkiResort_test")
    SkiResort_test()
    print("running MedicalTrial_test")
    MedicalTrial_test()
    print("running Nonprofit501c7_test")
    Nonprofit501c7_test()
    print("running DanceGroup_test")
    DanceGroup_test()
    print("running Photograph_test")
    Photograph_test()
    print("running HousePainter_test")
    HousePainter_test()
    print("running OrderProblem_test")
    OrderProblem_test()
    print("running Nonprofit501a_test")
    Nonprofit501a_test()
    print("running DiscussionForumPosting_test")
    DiscussionForumPosting_test()
    print("running CohortStudy_test")
    CohortStudy_test()
    print("running Wednesday_test")
    Wednesday_test()
    print("running UnclassifiedAdultConsideration_test")
    UnclassifiedAdultConsideration_test()
    print("running TransitMap_test")
    TransitMap_test()
    print("running RealEstateListing_test")
    RealEstateListing_test()
    print("running SellAction_test")
    SellAction_test()
    print("running ShareAction_test")
    ShareAction_test()
    print("running Bakery_test")
    Bakery_test()
    print("running WholesaleStore_test")
    WholesaleStore_test()
    print("running AllocateAction_test")
    AllocateAction_test()
    print("running RejectAction_test")
    RejectAction_test()
    print("running WarrantyScope_test")
    WarrantyScope_test()
    print("running SpeakableSpecification_test")
    SpeakableSpecification_test()
    print("running DepartmentStore_test")
    DepartmentStore_test()
    print("running GasStation_test")
    GasStation_test()
    print("running MotorcycleDealer_test")
    MotorcycleDealer_test()
    print("running OfferCatalog_test")
    OfferCatalog_test()
    print("running GeneralContractor_test")
    GeneralContractor_test()
    print("running Online_test")
    Online_test()
    print("running Observation_test")
    Observation_test()
    print("running DefinedTerm_test")
    DefinedTerm_test()
    print("running CategoryCode_test")
    CategoryCode_test()
    print("running DrinkAction_test")
    DrinkAction_test()
    print("running Nonprofit501c28_test")
    Nonprofit501c28_test()
    print("running Report_test")
    Report_test()
    print("running OriginalShippingFees_test")
    OriginalShippingFees_test()
    print("running DaySpa_test")
    DaySpa_test()
    print("running Geriatric_test")
    Geriatric_test()
    print("running AppendAction_test")
    AppendAction_test()
    print("running WearableSizeGroupWomens_test")
    WearableSizeGroupWomens_test()
    print("running Occupation_test")
    Occupation_test()
    print("running RadiationTherapy_test")
    RadiationTherapy_test()
    print("running BodyMeasurementHeight_test")
    BodyMeasurementHeight_test()
    print("running OfferShippingDetails_test")
    OfferShippingDetails_test()
    print("running Nonprofit501c5_test")
    Nonprofit501c5_test()
    print("running Nonprofit501c25_test")
    Nonprofit501c25_test()
    print("running MedicalResearcher_test")
    MedicalResearcher_test()
    print("running RadioSeries_test")
    RadioSeries_test()
    print("running MedicalSymptom_test")
    MedicalSymptom_test()
    print("running Nonprofit501c1_test")
    Nonprofit501c1_test()
    print("running TechArticle_test")
    TechArticle_test()
    print("running APIReference_test")
    APIReference_test()
    print("running Fungus_test")
    Fungus_test()
    print("running MedicalRiskEstimator_test")
    MedicalRiskEstimator_test()
    print("running MedicalRiskScore_test")
    MedicalRiskScore_test()
    print("running Hotel_test")
    Hotel_test()
    print("running AskAction_test")
    AskAction_test()
    print("running MediaGallery_test")
    MediaGallery_test()
    print("running BodyMeasurementHand_test")
    BodyMeasurementHand_test()
    print("running SchoolDistrict_test")
    SchoolDistrict_test()
    print("running LinkRole_test")
    LinkRole_test()
    print("running TVEpisode_test")
    TVEpisode_test()
    print("running FMRadioChannel_test")
    FMRadioChannel_test()
    print("running WritePermission_test")
    WritePermission_test()
    print("running Menu_test")
    Menu_test()
    print("running DownloadAction_test")
    DownloadAction_test()
    print("running UserTweets_test")
    UserTweets_test()
    print("running Anesthesia_test")
    Anesthesia_test()
    print("running WearableSizeSystemCN_test")
    WearableSizeSystemCN_test()
    print("running VinylFormat_test")
    VinylFormat_test()
    print("running FourWheelDriveConfiguration_test")
    FourWheelDriveConfiguration_test()
    print("running PerformingArtsTheater_test")
    PerformingArtsTheater_test()
    print("running MedicalDevicePurpose_test")
    MedicalDevicePurpose_test()
    print("running Zoo_test")
    Zoo_test()
    print("running BasicIncome_test")
    BasicIncome_test()
    print("running Flexibility_test")
    Flexibility_test()
    print("running JoinAction_test")
    JoinAction_test()
    print("running IceCreamShop_test")
    IceCreamShop_test()
    print("running HinduTemple_test")
    HinduTemple_test()
    print("running NarcoticConsideration_test")
    NarcoticConsideration_test()
    print("running CancelAction_test")
    CancelAction_test()
    print("running RadioSeason_test")
    RadioSeason_test()
    print("running Dentist_test")
    Dentist_test()
    print("running Nonprofit501c11_test")
    Nonprofit501c11_test()
    print("running DrugClass_test")
    DrugClass_test()
    print("running Musculoskeletal_test")
    Musculoskeletal_test()
    print("running CityHall_test")
    CityHall_test()
    print("running PharmacySpecialty_test")
    PharmacySpecialty_test()
    print("running HowToDirection_test")
    HowToDirection_test()
    print("running BuyAction_test")
    BuyAction_test()
    print("running Nonprofit501e_test")
    Nonprofit501e_test()
    print("running HearingImpairedSupported_test")
    HearingImpairedSupported_test()
    print("running Nonprofit501c3_test")
    Nonprofit501c3_test()
    print("running Manuscript_test")
    Manuscript_test()
    print("running CompilationAlbum_test")
    CompilationAlbum_test()
    print("running BookSeries_test")
    BookSeries_test()
    print("running ReturnAtKiosk_test")
    ReturnAtKiosk_test()
    print("running TouristDestination_test")
    TouristDestination_test()
    print("running RsvpResponseType_test")
    RsvpResponseType_test()
    print("running BroadcastService_test")
    BroadcastService_test()
    print("running RadioBroadcastService_test")
    RadioBroadcastService_test()
    print("running MusicStore_test")
    MusicStore_test()
    print("running InstallAction_test")
    InstallAction_test()
    print("running Nursing_test")
    Nursing_test()
    print("running BarOrPub_test")
    BarOrPub_test()
    print("running IndividualProduct_test")
    IndividualProduct_test()
    print("running SportsTeam_test")
    SportsTeam_test()
    print("running HairSalon_test")
    HairSalon_test()
    print("running UseAction_test")
    UseAction_test()
    print("running SoundtrackAlbum_test")
    SoundtrackAlbum_test()
    print("running HowToStep_test")
    HowToStep_test()
    print("running HardwareStore_test")
    HardwareStore_test()
    print("running Virus_test")
    Virus_test()
    print("running EndorsementRating_test")
    EndorsementRating_test()
    print("running Brewery_test")
    Brewery_test()
    print("running Country_test")
    Country_test()
    print("running BoatTerminal_test")
    BoatTerminal_test()
    print("running Play_test")
    Play_test()
    print("running ParkingFacility_test")
    ParkingFacility_test()
    print("running MedicalDevice_test")
    MedicalDevice_test()
    print("running Winery_test")
    Winery_test()
    print("running CheckOutAction_test")
    CheckOutAction_test()
    print("running ArchiveOrganization_test")
    ArchiveOrganization_test()
    print("running PaymentPastDue_test")
    PaymentPastDue_test()
    print("running GroceryStore_test")
    GroceryStore_test()
    print("running EffectivenessHealthAspect_test")
    EffectivenessHealthAspect_test()
    print("running OccupationalTherapy_test")
    OccupationalTherapy_test()
    print("running VenueMap_test")
    VenueMap_test()
    print("running EventMovedOnline_test")
    EventMovedOnline_test()
    print("running Barcode_test")
    Barcode_test()
    print("running VeterinaryCare_test")
    VeterinaryCare_test()
    print("running BeautySalon_test")
    BeautySalon_test()
    print("running WebSite_test")
    WebSite_test()
    print("running Electrician_test")
    Electrician_test()
    print("running EUEnergyEfficiencyCategoryE_test")
    EUEnergyEfficiencyCategoryE_test()
    print("running BusinessEntityType_test")
    BusinessEntityType_test()
    print("running ReturnAction_test")
    ReturnAction_test()
    print("running PerformanceRole_test")
    PerformanceRole_test()
    print("running Protein_test")
    Protein_test()
    print("running TrackAction_test")
    TrackAction_test()
    print("running DeliveryChargeSpecification_test")
    DeliveryChargeSpecification_test()
    print("running PublicationIssue_test")
    PublicationIssue_test()
    print("running ComicIssue_test")
    ComicIssue_test()
    print("running AgreeAction_test")
    AgreeAction_test()
    print("running ActiveNotRecruiting_test")
    ActiveNotRecruiting_test()
    print("running Tuesday_test")
    Tuesday_test()
    print("running Protozoa_test")
    Protozoa_test()
    print("running LeisureTimeActivity_test")
    LeisureTimeActivity_test()
    print("running AcceptAction_test")
    AcceptAction_test()
    print("running Nonprofit501c27_test")
    Nonprofit501c27_test()
    print("running AlcoholConsideration_test")
    AlcoholConsideration_test()
    print("running CDCPMDRecord_test")
    CDCPMDRecord_test()
    print("running MensClothingStore_test")
    MensClothingStore_test()
    print("running CollegeOrUniversity_test")
    CollegeOrUniversity_test()
    print("running SheetMusic_test")
    SheetMusic_test()
    print("running WPAdBlock_test")
    WPAdBlock_test()
    print("running UserBlocks_test")
    UserBlocks_test()
    print("running SeaBodyOfWater_test")
    SeaBodyOfWater_test()
    print("running WearableMeasurementWidth_test")
    WearableMeasurementWidth_test()
    print("running VisualArtsEvent_test")
    VisualArtsEvent_test()
    print("running Language_test")
    Language_test()
    print("running TollFree_test")
    TollFree_test()
    print("running PathologyTest_test")
    PathologyTest_test()
    print("running DrivingSchoolVehicleUsage_test")
    DrivingSchoolVehicleUsage_test()
    print("running VideoGameSeries_test")
    VideoGameSeries_test()
    print("running OnDemandEvent_test")
    OnDemandEvent_test()
    print("running Pulmonary_test")
    Pulmonary_test()
    print("running HealthClub_test")
    HealthClub_test()
    print("running StagedContent_test")
    StagedContent_test()
    print("running Nonprofit501c9_test")
    Nonprofit501c9_test()
    print("running FastFoodRestaurant_test")
    FastFoodRestaurant_test()
    print("running BusinessFunction_test")
    BusinessFunction_test()
    print("running Dermatologic_test")
    Dermatologic_test()
    print("running PaymentDue_test")
    PaymentDue_test()
    print("running DJMixAlbum_test")
    DJMixAlbum_test()
    print("running URL_test")
    URL_test()
    print("running EducationalAudience_test")
    EducationalAudience_test()
    print("running GamePlayMode_test")
    GamePlayMode_test()
    print("running SinglePlayer_test")
    SinglePlayer_test()
    print("running HealthCare_test")
    HealthCare_test()
    print("running PreventionHealthAspect_test")
    PreventionHealthAspect_test()
    print("running DepartAction_test")
    DepartAction_test()
    print("running EnergyConsumptionDetails_test")
    EnergyConsumptionDetails_test()
    print("running Painting_test")
    Painting_test()
    print("running MultiPlayer_test")
    MultiPlayer_test()
    print("running CreditCard_test")
    CreditCard_test()
    print("running LimitedAvailability_test")
    LimitedAvailability_test()
    print("running VeganDiet_test")
    VeganDiet_test()
    print("running ApplyAction_test")
    ApplyAction_test()
    print("running ParkingMap_test")
    ParkingMap_test()
    print("running GiveAction_test")
    GiveAction_test()
    print("running Ayurvedic_test")
    Ayurvedic_test()
    print("running WearableSizeGroupExtraTall_test")
    WearableSizeGroupExtraTall_test()
    print("running TVSeries_test")
    TVSeries_test()
    print("running FloorPlan_test")
    FloorPlan_test()
    print("running NotInForce_test")
    NotInForce_test()
    print("running Radiography_test")
    Radiography_test()
    print("running CoOp_test")
    CoOp_test()
    print("running _3DModel_test")
    _3DModel_test()
    print("running BackgroundNewsArticle_test")
    BackgroundNewsArticle_test()
    print("running Diet_test")
    Diet_test()
    print("running House_test")
    House_test()
    print("running Course_test")
    Course_test()
    print("running InStock_test")
    InStock_test()
    print("running SolveMathAction_test")
    SolveMathAction_test()
    print("running Volcano_test")
    Volcano_test()
    print("running RentalVehicleUsage_test")
    RentalVehicleUsage_test()
    print("running ViewAction_test")
    ViewAction_test()
    print("running NonprofitANBI_test")
    NonprofitANBI_test()
    print("running Nonprofit501c22_test")
    Nonprofit501c22_test()
    print("running Clinician_test")
    Clinician_test()
    print("running PawnShop_test")
    PawnShop_test()
    print("running DanceEvent_test")
    DanceEvent_test()
    print("running DefinedTermSet_test")
    DefinedTermSet_test()
    print("running CategoryCodeSet_test")
    CategoryCodeSet_test()
    print("running Nonprofit501k_test")
    Nonprofit501k_test()
    print("running PregnancyHealthAspect_test")
    PregnancyHealthAspect_test()
    print("running MobileWebPlatform_test")
    MobileWebPlatform_test()
    print("running ApprovedIndication_test")
    ApprovedIndication_test()
    print("running MedicalGuidelineContraindication_test")
    MedicalGuidelineContraindication_test()
    print("running GolfCourse_test")
    GolfCourse_test()
    print("running BefriendAction_test")
    BefriendAction_test()
    print("running Motel_test")
    Motel_test()
    print("running EatAction_test")
    EatAction_test()
    print("running OrderProcessing_test")
    OrderProcessing_test()
    print("running FullRefund_test")
    FullRefund_test()
    print("running PreventionIndication_test")
    PreventionIndication_test()
    print("running MolecularEntity_test")
    MolecularEntity_test()
    print("running FAQPage_test")
    FAQPage_test()
    print("running BodyMeasurementInsideLeg_test")
    BodyMeasurementInsideLeg_test()
    print("running ReportageNewsArticle_test")
    ReportageNewsArticle_test()
    print("running EUEnergyEfficiencyCategoryF_test")
    EUEnergyEfficiencyCategoryF_test()
    print("running TobaccoNicotineConsideration_test")
    TobaccoNicotineConsideration_test()
    print("running MinimumAdvertisedPrice_test")
    MinimumAdvertisedPrice_test()
    print("running CardiovascularExam_test")
    CardiovascularExam_test()
    print("running QuantitativeValue_test")
    QuantitativeValue_test()
    print("running WearableSizeSystemEurope_test")
    WearableSizeSystemEurope_test()
    print("running Blog_test")
    Blog_test()
    print("running DeleteAction_test")
    DeleteAction_test()
    print("running BoardingPolicyType_test")
    BoardingPolicyType_test()
    print("running GroupBoardingPolicy_test")
    GroupBoardingPolicy_test()
    print("running BikeStore_test")
    BikeStore_test()
    print("running OnSitePickup_test")
    OnSitePickup_test()
    print("running HighSchool_test")
    HighSchool_test()
    print("running Synagogue_test")
    Synagogue_test()
    print("running PalliativeProcedure_test")
    PalliativeProcedure_test()
    print("running Optician_test")
    Optician_test()
    print("running TelevisionChannel_test")
    TelevisionChannel_test()
    print("running GenericWebPlatform_test")
    GenericWebPlatform_test()
    print("running PublicationVolume_test")
    PublicationVolume_test()
    print("running ShippingDeliveryTime_test")
    ShippingDeliveryTime_test()
    print("running UnitPriceSpecification_test")
    UnitPriceSpecification_test()
    print("running RadioClip_test")
    RadioClip_test()
    print("running Nonprofit501d_test")
    Nonprofit501d_test()
    print("running HowOrWhereHealthAspect_test")
    HowOrWhereHealthAspect_test()
    print("running Otolaryngologic_test")
    Otolaryngologic_test()
    print("running PreSale_test")
    PreSale_test()
    print("running Hostel_test")
    Hostel_test()
    print("running PsychologicalTreatment_test")
    PsychologicalTreatment_test()
    print("running PerformAction_test")
    PerformAction_test()
    print("running PreOrder_test")
    PreOrder_test()
    print("running ChildrensEvent_test")
    ChildrensEvent_test()
    print("running AuthoritativeLegalValue_test")
    AuthoritativeLegalValue_test()
    print("running WearableSizeSystemFR_test")
    WearableSizeSystemFR_test()
    print("running BroadcastRelease_test")
    BroadcastRelease_test()
    print("running TaxiService_test")
    TaxiService_test()
    print("running TattooParlor_test")
    TattooParlor_test()
    print("running EnergyStarCertified_test")
    EnergyStarCertified_test()
    print("running SendAction_test")
    SendAction_test()
    print("running Demand_test")
    Demand_test()
    print("running SubscribeAction_test")
    SubscribeAction_test()
    print("running Number_test")
    Number_test()
    print("running Waterfall_test")
    Waterfall_test()
    print("running TakeAction_test")
    TakeAction_test()
    print("running State_test")
    State_test()
    print("running ReturnFeesCustomerResponsibility_test")
    ReturnFeesCustomerResponsibility_test()
    print("running NewCondition_test")
    NewCondition_test()
    print("running LeaveAction_test")
    LeaveAction_test()
    print("running WearableMeasurementChestOrBust_test")
    WearableMeasurementChestOrBust_test()
    print("running Property_test")
    Property_test()
    print("running TVSeason_test")
    TVSeason_test()
    print("running WPHeader_test")
    WPHeader_test()
    print("running Nonprofit501c26_test")
    Nonprofit501c26_test()
    print("running ShoppingCenter_test")
    ShoppingCenter_test()
    print("running MedicalCode_test")
    MedicalCode_test()
    print("running PronounceableText_test")
    PronounceableText_test()
    print("running TransformedContent_test")
    TransformedContent_test()
    print("running MotorcycleRepair_test")
    MotorcycleRepair_test()
    print("running ActiveActionStatus_test")
    ActiveActionStatus_test()
    print("running EducationalOccupationalProgram_test")
    EducationalOccupationalProgram_test()
    print("running WorkBasedProgram_test")
    WorkBasedProgram_test()
    print("running DefinedRegion_test")
    DefinedRegion_test()
    print("running Distillery_test")
    Distillery_test()
    print("running BusOrCoach_test")
    BusOrCoach_test()
    print("running BodyMeasurementHips_test")
    BodyMeasurementHips_test()
    print("running Researcher_test")
    Researcher_test()
    print("running IOSPlatform_test")
    IOSPlatform_test()
    print("running Quiz_test")
    Quiz_test()
    print("running LowFatDiet_test")
    LowFatDiet_test()
    print("running Airline_test")
    Airline_test()
    print("running Chiropractic_test")
    Chiropractic_test()
    print("running WesternConventional_test")
    WesternConventional_test()
    print("running MerchantReturnUnspecified_test")
    MerchantReturnUnspecified_test()
    print("running ReceiveAction_test")
    ReceiveAction_test()
    print("running ReplyAction_test")
    ReplyAction_test()
    print("running RightHandDriving_test")
    RightHandDriving_test()
    print("running SearchAction_test")
    SearchAction_test()
    print("running InternationalTrial_test")
    InternationalTrial_test()
    print("running MedicalRiskCalculator_test")
    MedicalRiskCalculator_test()
    print("running MovieTheater_test")
    MovieTheater_test()
    print("running ShippingRateSettings_test")
    ShippingRateSettings_test()
    print("running RsvpResponseMaybe_test")
    RsvpResponseMaybe_test()
    print("running Ear_test")
    Ear_test()
    print("running WearAction_test")
    WearAction_test()
    print("running BusReservation_test")
    BusReservation_test()
    print("running ArchiveComponent_test")
    ArchiveComponent_test()
    print("running Library_test")
    Library_test()
    print("running MerchantReturnFiniteReturnWindow_test")
    MerchantReturnFiniteReturnWindow_test()
    print("running SpecialAnnouncement_test")
    SpecialAnnouncement_test()
    print("running EmployerReview_test")
    EmployerReview_test()
    print("running RsvpResponseNo_test")
    RsvpResponseNo_test()
    print("running HyperTocEntry_test")
    HyperTocEntry_test()
    print("running SurgicalProcedure_test")
    SurgicalProcedure_test()
    print("running GettingAccessHealthAspect_test")
    GettingAccessHealthAspect_test()
    print("running VideoGallery_test")
    VideoGallery_test()
    print("running ScreeningEvent_test")
    ScreeningEvent_test()
    print("running AndroidPlatform_test")
    AndroidPlatform_test()
    print("running Claim_test")
    Claim_test()
    print("running Mosque_test")
    Mosque_test()
    print("running LibrarySystem_test")
    LibrarySystem_test()
    print("running Nerve_test")
    Nerve_test()
    print("running Notary_test")
    Notary_test()
    print("running WatchAction_test")
    WatchAction_test()
    print("running AutoWash_test")
    AutoWash_test()
    print("running UsageOrScheduleHealthAspect_test")
    UsageOrScheduleHealthAspect_test()
    print("running CommentAction_test")
    CommentAction_test()
    print("running JewelryStore_test")
    JewelryStore_test()
    print("running Skin_test")
    Skin_test()
    print("running ReviewAction_test")
    ReviewAction_test()
    print("running WearableSizeGroupMisses_test")
    WearableSizeGroupMisses_test()
    print("running MusculoskeletalExam_test")
    MusculoskeletalExam_test()
    print("running AnimalShelter_test")
    AnimalShelter_test()
    print("running Emergency_test")
    Emergency_test()
    print("running ImageGallery_test")
    ImageGallery_test()
    print("running LiveBlogPosting_test")
    LiveBlogPosting_test()
    print("running WearableSizeGroupInfants_test")
    WearableSizeGroupInfants_test()
    print("running PublicToilet_test")
    PublicToilet_test()
    print("running FDAcategoryA_test")
    FDAcategoryA_test()
    print("running MedicalContraindication_test")
    MedicalContraindication_test()
    print("running ComedyEvent_test")
    ComedyEvent_test()
    print("running SuspendAction_test")
    SuspendAction_test()
    print("running Pathology_test")
    Pathology_test()
    print("running ParentalSupport_test")
    ParentalSupport_test()
    print("running LendAction_test")
    LendAction_test()
    print("running Hardcover_test")
    Hardcover_test()
    print("running FundingScheme_test")
    FundingScheme_test()
    print("running PatientExperienceHealthAspect_test")
    PatientExperienceHealthAspect_test()
    print("running TelevisionStation_test")
    TelevisionStation_test()
    print("running MRI_test")
    MRI_test()
    print("running MotorizedBicycle_test")
    MotorizedBicycle_test()
    print("running Poster_test")
    Poster_test()
    print("running RsvpResponseYes_test")
    RsvpResponseYes_test()
    print("running EventRescheduled_test")
    EventRescheduled_test()
    print("running BodyMeasurementHead_test")
    BodyMeasurementHead_test()
    print("running UserPlays_test")
    UserPlays_test()
    print("running MiddleSchool_test")
    MiddleSchool_test()
    print("running LakeBodyOfWater_test")
    LakeBodyOfWater_test()
    print("running Monday_test")
    Monday_test()
    print("running AboutPage_test")
    AboutPage_test()
    print("running GameServer_test")
    GameServer_test()
    print("running PreOrderAction_test")
    PreOrderAction_test()
    print("running Duration_test")
    Duration_test()
    print("running BroadcastEvent_test")
    BroadcastEvent_test()
    print("running MedicalRiskFactor_test")
    MedicalRiskFactor_test()
    print("running ConvenienceStore_test")
    ConvenienceStore_test()
    print("running AlbumRelease_test")
    AlbumRelease_test()
    print("running SingleFamilyResidence_test")
    SingleFamilyResidence_test()
    print("running MusicRelease_test")
    MusicRelease_test()
    print("running EmployerAggregateRating_test")
    EmployerAggregateRating_test()
    print("running Female_test")
    Female_test()
    print("running ReviewNewsArticle_test")
    ReviewNewsArticle_test()
    print("running SeatingMap_test")
    SeatingMap_test()
    print("running EvidenceLevelB_test")
    EvidenceLevelB_test()
    print("running BodyMeasurementBust_test")
    BodyMeasurementBust_test()
    print("running HomeGoodsStore_test")
    HomeGoodsStore_test()
    print("running ClaimReview_test")
    ClaimReview_test()
    print("running NutritionInformation_test")
    NutritionInformation_test()
    print("running CT_test")
    CT_test()
    print("running Nonprofit527_test")
    Nonprofit527_test()
    print("running MenuItem_test")
    MenuItem_test()
    print("running OnlineEventAttendanceMode_test")
    OnlineEventAttendanceMode_test()
    print("running SizeSystemImperial_test")
    SizeSystemImperial_test()
    print("running Recruiting_test")
    Recruiting_test()
    print("running Nonprofit501c23_test")
    Nonprofit501c23_test()
    print("running PotentialActionStatus_test")
    PotentialActionStatus_test()
    print("running OneTimePayments_test")
    OneTimePayments_test()
    print("running TravelAction_test")
    TravelAction_test()
    print("running EUEnergyEfficiencyCategoryD_test")
    EUEnergyEfficiencyCategoryD_test()
    print("running MaximumDoseSchedule_test")
    MaximumDoseSchedule_test()
    print("running Brand_test")
    Brand_test()
    print("running HowToSupply_test")
    HowToSupply_test()
    print("running ZoneBoardingPolicy_test")
    ZoneBoardingPolicy_test()
    print("running Nonprofit501f_test")
    Nonprofit501f_test()
    print("running ParcelDelivery_test")
    ParcelDelivery_test()
    print("running SeekToAction_test")
    SeekToAction_test()
    print("running Balance_test")
    Balance_test()
    print("running InForce_test")
    InForce_test()
    print("running AuthorizeAction_test")
    AuthorizeAction_test()
    print("running InvoicePrice_test")
    InvoicePrice_test()
    print("running Neurologic_test")
    Neurologic_test()
    print("running CassetteFormat_test")
    CassetteFormat_test()
    print("running TraditionalChinese_test")
    TraditionalChinese_test()
    print("running Homeopathic_test")
    Homeopathic_test()
    print("running TouristAttraction_test")
    TouristAttraction_test()
    print("running Energy_test")
    Energy_test()
    print("running Nonprofit501c19_test")
    Nonprofit501c19_test()
    print("running OfferForPurchase_test")
    OfferForPurchase_test()
    print("running EntryPoint_test")
    EntryPoint_test()
    print("running OfficialLegalValue_test")
    OfficialLegalValue_test()
    print("running HowItWorksHealthAspect_test")
    HowItWorksHealthAspect_test()
    print("running Table_test")
    Table_test()
    print("running EnrollingByInvitation_test")
    EnrollingByInvitation_test()
    print("running MayTreatHealthAspect_test")
    MayTreatHealthAspect_test()
    print("running OrderReturned_test")
    OrderReturned_test()
    print("running FoodEvent_test")
    FoodEvent_test()
    print("running CrossSectional_test")
    CrossSectional_test()
    print("running AutoDealer_test")
    AutoDealer_test()
    print("running InsuranceAgency_test")
    InsuranceAgency_test()
    print("running MusicRecording_test")
    MusicRecording_test()
    print("running HalalDiet_test")
    HalalDiet_test()
    print("running Time_test")
    Time_test()
    print("running WearableSizeGroupBig_test")
    WearableSizeGroupBig_test()
    print("running GatedResidenceCommunity_test")
    GatedResidenceCommunity_test()
    print("running Diagnostic_test")
    Diagnostic_test()
    print("running Courthouse_test")
    Courthouse_test()
    print("running ComedyClub_test")
    ComedyClub_test()
    print("running AerobicActivity_test")
    AerobicActivity_test()
    print("running SpreadsheetDigitalDocument_test")
    SpreadsheetDigitalDocument_test()
    print("running Locksmith_test")
    Locksmith_test()
    print("running Boolean_test")
    Boolean_test()
    print("running True__test")
    True__test()
    print("running DietarySupplement_test")
    DietarySupplement_test()
    print("running WeaponConsideration_test")
    WeaponConsideration_test()
    print("running WearableSizeSystemUS_test")
    WearableSizeSystemUS_test()
    print("running Withdrawn_test")
    Withdrawn_test()
    print("running OwnershipInfo_test")
    OwnershipInfo_test()
    print("running Completed_test")
    Completed_test()
    print("running NoteDigitalDocument_test")
    NoteDigitalDocument_test()
    print("running Float_test")
    Float_test()
    print("running Consortium_test")
    Consortium_test()
    print("running PrescriptionOnly_test")
    PrescriptionOnly_test()
    print("running GovernmentOrganization_test")
    GovernmentOrganization_test()
    print("running CurrencyConversionService_test")
    CurrencyConversionService_test()
    print("running UnincorporatedAssociationCharity_test")
    UnincorporatedAssociationCharity_test()
    print("running WearableSizeGroupGirls_test")
    WearableSizeGroupGirls_test()
    print("running AssignAction_test")
    AssignAction_test()
    print("running DigitalDocumentPermission_test")
    DigitalDocumentPermission_test()
    print("running BookmarkAction_test")
    BookmarkAction_test()
    print("running BedDetails_test")
    BedDetails_test()
    print("running ReturnLabelCustomerResponsibility_test")
    ReturnLabelCustomerResponsibility_test()
    print("running EventPostponed_test")
    EventPostponed_test()
    print("running Psychiatric_test")
    Psychiatric_test()
    print("running Muscle_test")
    Muscle_test()
    print("running Ultrasound_test")
    Ultrasound_test()
    print("running BroadcastFrequencySpecification_test")
    BroadcastFrequencySpecification_test()
    print("running TripleBlindedTrial_test")
    TripleBlindedTrial_test()
    print("running AllergiesHealthAspect_test")
    AllergiesHealthAspect_test()
    print("running OfflineTemporarily_test")
    OfflineTemporarily_test()
    print("running Nose_test")
    Nose_test()
    print("running FundingAgency_test")
    FundingAgency_test()
    print("running CourseInstance_test")
    CourseInstance_test()
    print("running PlasticSurgery_test")
    PlasticSurgery_test()
    print("running Dentistry_test")
    Dentistry_test()
    print("running ExchangeRateSpecification_test")
    ExchangeRateSpecification_test()
    print("running SportsEvent_test")
    SportsEvent_test()
    print("running Nonprofit501c17_test")
    Nonprofit501c17_test()
    print("running MedicalCause_test")
    MedicalCause_test()
    print("running HealthPlanFormulary_test")
    HealthPlanFormulary_test()
    print("running SpokenWordAlbum_test")
    SpokenWordAlbum_test()
    print("running FilmAction_test")
    FilmAction_test()
    print("running SelfStorage_test")
    SelfStorage_test()
    print("running WPFooter_test")
    WPFooter_test()
    print("running DesktopWebPlatform_test")
    DesktopWebPlatform_test()
    print("running MulticellularParasite_test")
    MulticellularParasite_test()
    print("running ViolenceConsideration_test")
    ViolenceConsideration_test()
    print("running BodyMeasurementChest_test")
    BodyMeasurementChest_test()
    print("running DataFeedItem_test")
    DataFeedItem_test()
    print("running Oncologic_test")
    Oncologic_test()
    print("running CompoundPriceSpecification_test")
    CompoundPriceSpecification_test()
    print("running AutoPartsStore_test")
    AutoPartsStore_test()
    print("running DatedMoneySpecification_test")
    DatedMoneySpecification_test()
    print("running Hospital_test")
    Hospital_test()
    print("running EndorseAction_test")
    EndorseAction_test()
    print("running RandomizedTrial_test")
    RandomizedTrial_test()
    print("running EUEnergyEfficiencyCategoryA2Plus_test")
    EUEnergyEfficiencyCategoryA2Plus_test()
    print("running Renal_test")
    Renal_test()
    print("running BoatReservation_test")
    BoatReservation_test()
    print("running SuperficialAnatomy_test")
    SuperficialAnatomy_test()
    print("running TheaterEvent_test")
    TheaterEvent_test()
    print("running InStoreOnly_test")
    InStoreOnly_test()
    print("running ReadAction_test")
    ReadAction_test()
    print("running Answer_test")
    Answer_test()
    print("running Registry_test")
    Registry_test()
    print("running ActivationFee_test")
    ActivationFee_test()
    print("running LaboratoryScience_test")
    LaboratoryScience_test()
    print("running SafetyHealthAspect_test")
    SafetyHealthAspect_test()
    print("running Map_test")
    Map_test()
    print("running PostalAddress_test")
    PostalAddress_test()
    print("running JobPosting_test")
    JobPosting_test()
    print("running DonateAction_test")
    DonateAction_test()
    print("running GlutenFreeDiet_test")
    GlutenFreeDiet_test()
    print("running DrawAction_test")
    DrawAction_test()
    print("running OrderDelivered_test")
    OrderDelivered_test()
    print("running ExerciseGym_test")
    ExerciseGym_test()
    print("running ReturnInStore_test")
    ReturnInStore_test()
    print("running BenefitsHealthAspect_test")
    BenefitsHealthAspect_test()
    print("running Therapeutic_test")
    Therapeutic_test()
    print("running LegislativeBuilding_test")
    LegislativeBuilding_test()
    print("running DefinitiveLegalValue_test")
    DefinitiveLegalValue_test()
    print("running ShoeStore_test")
    ShoeStore_test()
    print("running FurnitureStore_test")
    FurnitureStore_test()
    print("running MusicVideoObject_test")
    MusicVideoObject_test()
    print("running DrugLegalStatus_test")
    DrugLegalStatus_test()
    print("running TireShop_test")
    TireShop_test()
    print("running Obstetric_test")
    Obstetric_test()
    print("running Nonprofit501c13_test")
    Nonprofit501c13_test()
    print("running Mountain_test")
    Mountain_test()
    print("running Pediatric_test")
    Pediatric_test()
    print("running Nonprofit501c14_test")
    Nonprofit501c14_test()
    print("running Corporation_test")
    Corporation_test()
    print("running RsvpAction_test")
    RsvpAction_test()
    print("running UserReview_test")
    UserReview_test()
    print("running DateTime_test")
    DateTime_test()
    print("running PaymentAutomaticallyApplied_test")
    PaymentAutomaticallyApplied_test()
    print("running Atlas_test")
    Atlas_test()
    print("running PaintAction_test")
    PaintAction_test()
    print("running OrderAction_test")
    OrderAction_test()
    print("running WearableSizeSystemDE_test")
    WearableSizeSystemDE_test()
    print("running Newspaper_test")
    Newspaper_test()
    print("running RiverBodyOfWater_test")
    RiverBodyOfWater_test()
    print("running Question_test")
    Question_test()
    print("running DiagnosticLab_test")
    DiagnosticLab_test()
    print("running Paperback_test")
    Paperback_test()
    print("running LowCalorieDiet_test")
    LowCalorieDiet_test()
    print("running CheckoutPage_test")
    CheckoutPage_test()
    print("running DemoAlbum_test")
    DemoAlbum_test()
    print("running NewsMediaOrganization_test")
    NewsMediaOrganization_test()
    print("running DefenceEstablishment_test")
    DefenceEstablishment_test()
    print("running MedicalGuidelineRecommendation_test")
    MedicalGuidelineRecommendation_test()
    print("running HotelRoom_test")
    HotelRoom_test()
    print("running Infectious_test")
    Infectious_test()
    print("running WearableSizeGroupShort_test")
    WearableSizeGroupShort_test()
    print("running School_test")
    School_test()
    print("running AnalysisNewsArticle_test")
    AnalysisNewsArticle_test()
    print("running Installment_test")
    Installment_test()
    print("running AnatomicalSystem_test")
    AnatomicalSystem_test()
    print("running MediaReview_test")
    MediaReview_test()
    print("running ExercisePlan_test")
    ExercisePlan_test()
    print("running LowLactoseDiet_test")
    LowLactoseDiet_test()
    print("running Quotation_test")
    Quotation_test()
    print("running DisagreeAction_test")
    DisagreeAction_test()
    print("running OnlineOnly_test")
    OnlineOnly_test()
    print("running WearableSizeSystemUK_test")
    WearableSizeSystemUK_test()
    print("running ReturnLabelDownloadAndPrint_test")
    ReturnLabelDownloadAndPrint_test()
    print("running Wholesale_test")
    Wholesale_test()
    print("running ItemPage_test")
    ItemPage_test()
    print("running EUEnergyEfficiencyCategoryA1Plus_test")
    EUEnergyEfficiencyCategoryA1Plus_test()
    print("running Reservoir_test")
    Reservoir_test()
    print("running EBook_test")
    EBook_test()
    print("running SelfCareHealthAspect_test")
    SelfCareHealthAspect_test()
    print("running RisksOrComplicationsHealthAspect_test")
    RisksOrComplicationsHealthAspect_test()
    print("running Movie_test")
    Movie_test()
    print("running False__test")
    False__test()
    print("running OfflineEventAttendanceMode_test")
    OfflineEventAttendanceMode_test()
    print("running Integer_test")
    Integer_test()
    print("running OrderItem_test")
    OrderItem_test()
    print("running CaseSeries_test")
    CaseSeries_test()
    print("running Preschool_test")
    Preschool_test()
    print("running BodyMeasurementWaist_test")
    BodyMeasurementWaist_test()
    print("running NotYetRecruiting_test")
    NotYetRecruiting_test()

if __name__ == "__main__":
    run_all()