import pandas as pd

from lab.trips import count_validation_errors

data_frame = pd.read_parquet("data/raw/yellow_tripdata_2024-01.parquet")
sample = data_frame.sample(100_000, random_state=0).rename(
    columns={"tpep_pickup_datetime": "pickup", "tpep_dropoff_datetime": "dropoff"}
)

cols = ["pickup", "dropoff", "passenger_count", "fare_amount"]
print(count_validation_errors(sample[cols].to_dict("records")))
