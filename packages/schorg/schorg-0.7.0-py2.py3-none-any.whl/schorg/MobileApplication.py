"""
A software application designed specifically to work well on a mobile device such as a telephone.

https://schema.org/MobileApplication
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MobileApplicationInheritedProperties(TypedDict):
    """A software application designed specifically to work well on a mobile device such as a telephone.

    References:
        https://schema.org/MobileApplication
    Note:
        Model Depth 4
    Attributes:
        screenshot: (Optional[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]): A link to a screenshot image of the app.
        permissions: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Permission(s) required to run the app (for example, a mobile app may require full internet access or may run only on wifi).
        requirements: (Optional[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]): Component dependency requirements for application. This includes runtime environments and shared libraries that are not included in the application distribution package, but required to run the application (examples: DirectX, Java or .NET runtime).
        storageRequirements: (Optional[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]): Storage requirements (free space required).
        softwareRequirements: (Optional[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]): Component dependency requirements for application. This includes runtime environments and shared libraries that are not included in the application distribution package, but required to run the application (examples: DirectX, Java or .NET runtime).
        applicationCategory: (Optional[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]): Type of software application, e.g. 'Game, Multimedia'.
        device: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Device required to run the application. Used in cases where a specific make/model is required to run the application.
        fileSize: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Size of the application / package (e.g. 18MB). In the absence of a unit (MB, KB etc.), KB will be assumed.
        countriesNotSupported: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Countries for which the application is not supported. You can also provide the two-letter ISO 3166-1 alpha-2 country code.
        operatingSystem: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Operating systems supported (Windows 7, OS X 10.6, Android 1.6).
        featureList: (Optional[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]): Features or modules provided by this application (and possibly required by other applications).
        applicationSuite: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The name of the application suite to which the application belongs (e.g. Excel belongs to Office).
        applicationSubCategory: (Optional[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]): Subcategory of the application, e.g. 'Arcade Game'.
        releaseNotes: (Optional[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]): Description of what changed in this version.
        softwareHelp: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Software application help.
        supportingData: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Supporting data for a SoftwareApplication.
        countriesSupported: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Countries for which the application is supported. You can also provide the two-letter ISO 3166-1 alpha-2 country code.
        availableOnDevice: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Device required to run the application. Used in cases where a specific make/model is required to run the application.
        softwareVersion: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Version of the software instance.
        installUrl: (Optional[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]): URL at which the app may be installed, if different from the URL of the item.
        memoryRequirements: (Optional[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]): Minimum memory requirements.
        processorRequirements: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Processor architecture required to run the application (e.g. IA64).
        softwareAddOn: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Additional content for a software application.
        downloadUrl: (Optional[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]): If the file can be downloaded, URL to download the binary.
    """

    screenshot: NotRequired[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]
    permissions: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    requirements: NotRequired[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]
    storageRequirements: NotRequired[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]
    softwareRequirements: NotRequired[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]
    applicationCategory: NotRequired[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]
    device: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    fileSize: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    countriesNotSupported: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    operatingSystem: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    featureList: NotRequired[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]
    applicationSuite: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    applicationSubCategory: NotRequired[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]
    releaseNotes: NotRequired[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]
    softwareHelp: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    supportingData: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    countriesSupported: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    availableOnDevice: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    softwareVersion: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    installUrl: NotRequired[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]
    memoryRequirements: NotRequired[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]
    processorRequirements: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    softwareAddOn: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    downloadUrl: NotRequired[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]
    


class MobileApplicationProperties(TypedDict):
    """A software application designed specifically to work well on a mobile device such as a telephone.

    References:
        https://schema.org/MobileApplication
    Note:
        Model Depth 4
    Attributes:
        carrierRequirements: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Specifies specific carrier(s) requirements for the application (e.g. an application may only work on a specific carrier network).
    """

    carrierRequirements: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    


class AllProperties(MobileApplicationInheritedProperties , MobileApplicationProperties, TypedDict):
    pass


class MobileApplicationBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="MobileApplication",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'screenshot': {'exclude': True}}
        fields = {'permissions': {'exclude': True}}
        fields = {'requirements': {'exclude': True}}
        fields = {'storageRequirements': {'exclude': True}}
        fields = {'softwareRequirements': {'exclude': True}}
        fields = {'applicationCategory': {'exclude': True}}
        fields = {'device': {'exclude': True}}
        fields = {'fileSize': {'exclude': True}}
        fields = {'countriesNotSupported': {'exclude': True}}
        fields = {'operatingSystem': {'exclude': True}}
        fields = {'featureList': {'exclude': True}}
        fields = {'applicationSuite': {'exclude': True}}
        fields = {'applicationSubCategory': {'exclude': True}}
        fields = {'releaseNotes': {'exclude': True}}
        fields = {'softwareHelp': {'exclude': True}}
        fields = {'supportingData': {'exclude': True}}
        fields = {'countriesSupported': {'exclude': True}}
        fields = {'availableOnDevice': {'exclude': True}}
        fields = {'softwareVersion': {'exclude': True}}
        fields = {'installUrl': {'exclude': True}}
        fields = {'memoryRequirements': {'exclude': True}}
        fields = {'processorRequirements': {'exclude': True}}
        fields = {'softwareAddOn': {'exclude': True}}
        fields = {'downloadUrl': {'exclude': True}}
        fields = {'carrierRequirements': {'exclude': True}}
        


def create_schema_org_model(type_: Union[MobileApplicationProperties, MobileApplicationInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MobileApplication"
    return model
    

MobileApplication = create_schema_org_model()


def create_mobileapplication_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_mobileapplication_model(model=model)
    return pydantic_type(model).schema_json()


