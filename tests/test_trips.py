from lab.trips import Trip, avg_tip_of_long_trips, count_validation_errors


def test_avg_tip_counts_missing_tip_as_zero():
    trips = [Trip(2, 10), Trip(6, 20, 4.0), Trip(8, 30)]
    assert avg_tip_of_long_trips(trips) == 2.0


def test_count_errors_by_fields():
    ok = {
        "pickup": "2024-01-01T10:00",
        "dropoff": "2024-01-01T10:20",
        "fare_amount": 12.5,
        "passenger_count": 1,
    }
    rows = [
        ok,
        {**ok, "passenger_count": 0},
        {**ok, "dropoff": "2024-01-01T09:00"},
        {**ok, "fare_amount": -3},
    ]
    assert count_validation_errors(rows) == {
        "passenger_count": 1,
        "fare_amount": 1,
        "model": 1,
    }
