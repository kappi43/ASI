import pandas as pd

df = pd.read_csv('data/HotelReservations.csv')
df.drop('Booking_ID', axis=1, inplace=True)
obj_df = df.select_dtypes(include=['object']).copy()
for column in obj_df.keys():
    df[column] = df[column].astype('category')
    df[column + '_cat'] = df[column].cat.codes
    df.drop(column, axis=1, inplace=True)
df=df.fillna(value = df.mean(numeric_only=True))
df.to_pickle("data_preprocessed\\preprocessed")