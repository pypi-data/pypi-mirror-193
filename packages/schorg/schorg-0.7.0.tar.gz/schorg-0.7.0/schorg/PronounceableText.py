"""
Data type: PronounceableText.

https://schema.org/PronounceableText
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class PronounceableTextInheritedProperties(TypedDict):
    """Data type: PronounceableText.

    References:
        https://schema.org/PronounceableText
    Note:
        Model Depth 6
    Attributes:
    """

    


class PronounceableTextProperties(TypedDict):
    """Data type: PronounceableText.

    References:
        https://schema.org/PronounceableText
    Note:
        Model Depth 6
    Attributes:
        textValue: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Text value being annotated.
        phoneticText: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Representation of a text [[textValue]] using the specified [[speechToTextMarkup]]. For example the city name of Houston in IPA: /ˈhjuːstən/.
        inLanguage: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The language of the content or performance or used in an action. Please use one of the language codes from the [IETF BCP 47 standard](http://tools.ietf.org/html/bcp47). See also [[availableLanguage]].
        speechToTextMarkup: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Form of markup used. eg. [SSML](https://www.w3.org/TR/speech-synthesis11) or [IPA](https://www.wikidata.org/wiki/Property:P898).
    """

    textValue: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    phoneticText: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    inLanguage: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    speechToTextMarkup: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    


class AllProperties(PronounceableTextInheritedProperties , PronounceableTextProperties, TypedDict):
    pass


class PronounceableTextBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="PronounceableText",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'textValue': {'exclude': True}}
        fields = {'phoneticText': {'exclude': True}}
        fields = {'inLanguage': {'exclude': True}}
        fields = {'speechToTextMarkup': {'exclude': True}}
        


def create_schema_org_model(type_: Union[PronounceableTextProperties, PronounceableTextInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "PronounceableText"
    return model
    

PronounceableText = create_schema_org_model()


def create_pronounceabletext_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_pronounceabletext_model(model=model)
    return pydantic_type(model).schema_json()


