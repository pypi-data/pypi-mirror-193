from __future__ import annotations

from datetime import datetime, date
from typing import List, Optional

from pydantic import BaseModel


class Topic(BaseModel):
    name: str
    vocabulary: str


class TimePeriod(BaseModel):
    start: str
    end: str


class GeographicUnit(BaseModel):
    name: str
    code: str


class LicenseItem(BaseModel):
    name: str
    uri: str


class Link(BaseModel):
    type: str
    description: str
    uri: str


class ApiDocumentationItem(BaseModel):
    description: str
    uri: str


class Source(BaseModel):
    name: str


class Note(BaseModel):
    note: str


class Producer(BaseModel):
    name: str
    abbr: str
    affiliation: str
    role: str


class MetadataCreation(BaseModel):
    producers: Optional[List[Producer]] = None
    prod_date: Optional[date] = None
    version: Optional[str] = None


class SeriesDescription(BaseModel):
    idno: str
    doi: Optional[str] = None
    name: str
    database_id: Optional[str] = None
    # aliases
    # alternate_identifiers
    measurement_unit: Optional[str] = None
    # dimensions
    periodicity: Optional[str] = None
    base_period: Optional[str] = None
    definition_short: Optional[str] = None
    definition_long: Optional[str] = None
    # statistical_concept
    # concepts
    methodology: Optional[str] = None
    # imputation
    # missing
    # quality_checks
    # quality_note
    # sources_discrepancies
    # series_break
    limitation: Optional[str] = None
    # themes
    topics: Optional[List[Topic]] = None
    # disciplines
    relevance: Optional[str] = None
    time_periods: Optional[List[TimePeriod]] = None
    # ref_country
    geographic_units: Optional[List[GeographicUnit]] = None
    aggregation_method: Optional[str] = None
    # disaggregation
    license: Optional[List[LicenseItem]] = None
    # confidentiality
    # confidentiality_status
    links: Optional[List[Link]] = None
    api_documentation: Optional[List[ApiDocumentationItem]] = None
    # authoring_entity
    sources: Optional[List[Source]] = None
    sources_note: Optional[str] = None
    keywords: Optional[List] = None
    # acronyms
    notes: Optional[List[Note]] = None
    # related_indicators
    # compliance
    # framework
    # lda_topics
    # embeddings
    # series_groups



class Indicators(BaseModel):
    metadata_creation: Optional[MetadataCreation] = None
    series_description: SeriesDescription
    schematype: str
