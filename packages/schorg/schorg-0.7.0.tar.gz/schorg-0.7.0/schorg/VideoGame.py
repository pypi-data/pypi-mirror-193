"""
A video game is an electronic game that involves human interaction with a user interface to generate visual feedback on a video device.

https://schema.org/VideoGame
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class VideoGameInheritedProperties(TypedDict):
    """A video game is an electronic game that involves human interaction with a user interface to generate visual feedback on a video device.

    References:
        https://schema.org/VideoGame
    Note:
        Model Depth 4
    Attributes:
        characterAttribute: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A piece of data that represents a particular aspect of a fictional character (skill, power, character points, advantage, disadvantage).
        gameLocation: (Optional[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]): Real or fictional location of the game (or part of game).
        numberOfPlayers: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Indicate how many people can play this game (minimum, maximum, or range).
        gameItem: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): An item is an object within the game world that can be collected by a player or, occasionally, a non-player character.
        quest: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The task that a player-controlled character, or group of characters may complete in order to gain a reward.
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

    characterAttribute: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    gameLocation: NotRequired[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]
    numberOfPlayers: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    gameItem: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    quest: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
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
    


class VideoGameProperties(TypedDict):
    """A video game is an electronic game that involves human interaction with a user interface to generate visual feedback on a video device.

    References:
        https://schema.org/VideoGame
    Note:
        Model Depth 4
    Attributes:
        actors: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): An actor, e.g. in TV, radio, movie, video games etc. Actors can be associated with individual items or with a series, episode, clip.
        actor: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): An actor, e.g. in TV, radio, movie, video games etc., or in an event. Actors can be associated with individual items or with a series, episode, clip.
        cheatCode: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Cheat codes to the game.
        gameServer: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The server on which  it is possible to play the game.
        trailer: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The trailer of a movie or TV/radio series, season, episode, etc.
        gameEdition: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The edition of a video game.
        gamePlatform: (Optional[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]): The electronic systems used to play <a href="http://en.wikipedia.org/wiki/Category:Video_game_platforms">video games</a>.
        director: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A director of e.g. TV, radio, movie, video gaming etc. content, or of an event. Directors can be associated with individual items or with a series, episode, clip.
        directors: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A director of e.g. TV, radio, movie, video games etc. content. Directors can be associated with individual items or with a series, episode, clip.
        musicBy: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The composer of the soundtrack.
        gameTip: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Links to tips, tactics, etc.
        playMode: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Indicates whether this game is multi-player, co-op or single-player.  The game can be marked as multi-player, co-op and single-player at the same time.
    """

    actors: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    actor: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    cheatCode: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    gameServer: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    trailer: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    gameEdition: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    gamePlatform: NotRequired[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]
    director: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    directors: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    musicBy: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    gameTip: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    playMode: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    


class AllProperties(VideoGameInheritedProperties , VideoGameProperties, TypedDict):
    pass


class VideoGameBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="VideoGame",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'characterAttribute': {'exclude': True}}
        fields = {'gameLocation': {'exclude': True}}
        fields = {'numberOfPlayers': {'exclude': True}}
        fields = {'gameItem': {'exclude': True}}
        fields = {'quest': {'exclude': True}}
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
        fields = {'actors': {'exclude': True}}
        fields = {'actor': {'exclude': True}}
        fields = {'cheatCode': {'exclude': True}}
        fields = {'gameServer': {'exclude': True}}
        fields = {'trailer': {'exclude': True}}
        fields = {'gameEdition': {'exclude': True}}
        fields = {'gamePlatform': {'exclude': True}}
        fields = {'director': {'exclude': True}}
        fields = {'directors': {'exclude': True}}
        fields = {'musicBy': {'exclude': True}}
        fields = {'gameTip': {'exclude': True}}
        fields = {'playMode': {'exclude': True}}
        


def create_schema_org_model(type_: Union[VideoGameProperties, VideoGameInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "VideoGame"
    return model
    

VideoGame = create_schema_org_model()


def create_videogame_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_videogame_model(model=model)
    return pydantic_type(model).schema_json()


