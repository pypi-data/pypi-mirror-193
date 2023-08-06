from typing import NewType, Any, Optional

from pydantic import BaseModel, Field


class SchemaOrgBase(BaseModel):
    #JSON-LD fields
    reverse_ : Optional[Any] = Field(default=None,alias='@reverse')
    id_ : Optional[Any] = Field(default=None,alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')


SchemaOrgObj =  NewType("SchemaOrgObj", Any)
