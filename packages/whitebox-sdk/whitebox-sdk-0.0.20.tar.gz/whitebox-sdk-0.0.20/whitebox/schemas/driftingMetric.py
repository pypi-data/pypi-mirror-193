from datetime import datetime
from typing import Dict, List, Union
from pydantic import BaseModel
from whitebox.schemas.base import ItemBase


class ColumnDataDriftMetrics(BaseModel):
    """One column drift metrics"""

    column_name: str
    column_type: str
    stattest_name: str
    drift_score: float
    drift_detected: bool
    threshold: float


class DataDriftTable(BaseModel):
    number_of_columns: int
    number_of_drifted_columns: int
    share_of_drifted_columns: float
    dataset_drift: bool
    drift_by_columns: Dict[str, ColumnDataDriftMetrics]


class CramerV(BaseModel):
    """CramerV statistics"""

    column_name: str
    kind: str
    values: Dict[str, List[str]]


class ColumnConceptDriftCorrelationMetrics(BaseModel):
    """One column concept drift correlation metrics"""

    column_name: str
    current: Dict[str, CramerV]
    reference: Dict[str, CramerV]


class ColumnConceptDriftMetrics(BaseModel):
    """One column concept drift metrics"""

    column_name: str
    column_type: str
    stattest_name: str
    drift_score: float
    drift_detected: bool
    stattest_threshold: float


class ConceptDriftTable(BaseModel):
    """Concept drift Table metrics"""

    concept_drift_summary: ColumnConceptDriftMetrics
    column_correlation: ColumnConceptDriftCorrelationMetrics


class DriftingMetricBase(ItemBase):
    model_id: str
    timestamp: Union[str, datetime]
    concept_drift_summary: ConceptDriftTable
    data_drift_summary: DataDriftTable


class DriftingMetric(DriftingMetricBase, ItemBase):
    pass
