import pandas as pd

data_frame = pd.read_parquet("data/raw/yellow_tripdata_2024-01.parquet")
data_frame.info(show_counts=True)
data_frame.describe()
data_frame.isna().mean()
data_frame.memory_usage(deep=True).sum() / 1e6

print("Missing Passenger count: ", data_frame.passenger_count.isna().sum())
print("Negative fares: ", (data_frame.fare_amount < 0).sum())

pickup = data_frame.tpep_pickup_datetime
print(
    "Pickups outside the January: ",
    ((pickup < "2024-01-01") | (pickup >= "2024-02-01")).sum(),
)

cols = [
    "VendorID",
    "RatecodeID",
    "payment_type",
    "PULocationID",
    "DOLocationID",
    "store_and_fwd_flag",
]
data_frame[cols] = data_frame[cols].astype("category")

print("Memory after type category: ", data_frame.memory_usage(deep=True).sum() / 1e6)
print(data_frame.dtypes)
