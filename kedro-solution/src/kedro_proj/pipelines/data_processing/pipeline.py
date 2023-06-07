from kedro.pipeline import Pipeline, node, pipeline
from .nodes import preprocess_reservations

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=preprocess_reservations,
                inputs="hotelReservations",
                outputs="preprocessed_reservations",
                name="preprocess_reservations_node",
            )
        ]
    )