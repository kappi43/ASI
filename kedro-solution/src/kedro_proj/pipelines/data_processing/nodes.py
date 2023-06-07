import pandas as pd

def encode_object_type_columns_categorical(reservations: pd.DataFrame) -> pd.DataFrame:
    obj_df = reservations.select_dtypes(include=['object']).copy()
    for column in obj_df.keys():
        reservations[column] = reservations[column].astype('category')
        reservations[column + '_cat'] = reservations[column].cat.codes
        reservations.drop(column, axis=1, inplace=True)
    return reservations

def preprocess_reservations(reservations: pd.DataFrame) -> pd.DataFrame:
    reservations.drop("Booking_ID", axis=1, inplace=True)
    reservations = encode_object_type_columns_categorical(reservations)
    reservations.fillna(value = reservations.mean(numeric_only=True), inplace=True)
    return reservations