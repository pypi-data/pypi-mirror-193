import os
import posixpath
from typing import List, Optional

from pydantic import BaseModel, Field, validator

from elementary.utils.time import convert_partial_iso_format_to_full_iso_format


class ArtifactSchema(BaseModel):
    name: str
    unique_id: str
    owners: Optional[str]
    tags: Optional[str]
    package_name: Optional[str]
    description: Optional[str]
    full_path: str

    @validator("full_path", pre=True)
    def format_full_path_sep(cls, full_path: str) -> str:
        return _format_path_sep(full_path)


class ModelSchema(ArtifactSchema):
    database_name: str = None
    schema_name: str
    table_name: str


class SourceSchema(ArtifactSchema):
    database_name: str = None
    schema_name: str
    table_name: str


class ExposureSchema(ArtifactSchema):
    url: Optional[str]
    type: Optional[str]
    maturity: Optional[str]
    owner_email: Optional[str]


class NormalizedArtifactSchema(BaseModel):
    owners: Optional[List[str]] = []
    tags: Optional[List[str]] = []
    # Should be changed to artifact_name.
    # Currently its model_name to match the CLI UI.
    model_name: str
    normalized_full_path: str

    @validator("owners", pre=True, always=True)
    def set_owners(cls, owners):
        return owners or []

    @validator("tags", pre=True, always=True)
    def set_tags(cls, tags):
        return tags or []

    @validator("normalized_full_path", pre=True)
    def format_normalized_full_path_sep(cls, normalized_full_path: str) -> str:
        return _format_path_sep(normalized_full_path)


# NormalizedArtifactSchema must be first in the inheritance order
class NormalizedModelSchema(NormalizedArtifactSchema, ModelSchema):
    artifact_type: str = Field("model", const=True)


# NormalizedArtifactSchema must be first in the inheritance order
class NormalizedSourceSchema(NormalizedArtifactSchema, SourceSchema):
    artifact_type: str = Field("source", const=True)


# NormalizedArtifactSchema must be first in the inheritance order
class NormalizedExposureSchema(NormalizedArtifactSchema, ExposureSchema):
    artifact_type: str = Field("exposure", const=True)


class ModelCoverageSchema(BaseModel):
    table_tests: int
    column_tests: int


class ModelRunSchema(BaseModel):
    id: str
    time_utc: str
    status: str
    full_refresh: bool
    materialization: str
    execution_time: float

    @validator("time_utc", pre=True)
    def format_time_utc(cls, time_utc):
        return convert_partial_iso_format_to_full_iso_format(time_utc)


class TotalsModelRunsSchema(BaseModel):
    errors: Optional[int] = 0
    success: Optional[int] = 0


class ModelRunsSchema(BaseModel):
    unique_id: str
    # schema is a saved name, so we use alias
    schema_name: str = Field(alias="schema")
    name: str
    status: str
    last_exec_time: float
    median_exec_time: float
    exec_time_change_rate: float
    totals: TotalsModelRunsSchema
    runs: List[ModelRunSchema]


def _format_path_sep(path: str) -> str:
    return posixpath.sep.join(path.split(os.path.sep))
