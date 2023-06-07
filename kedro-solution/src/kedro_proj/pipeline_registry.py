"""Project pipelines."""
from typing import Dict

from kedro.framework.project import find_pipelines
from kedro.pipeline import Pipeline
from .pipelines.data_processing.pipeline import create_pipeline as data_processing_pipeline
from .pipelines.data_science.pipeline import create_pipeline as data_science_pipeline


def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from pipeline names to ``Pipeline`` objects.
    """
    pipelines = find_pipelines()
    pipelines["__default__"] = data_processing_pipeline() + data_science_pipeline()
    return pipelines
