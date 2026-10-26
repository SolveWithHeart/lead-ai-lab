from collections import Counter
from collections.abc import Iterable
from dataclasses import dataclass
from datetime import datetime
from functools import reduce
from typing import Any

from pydantic import BaseModel, Field, ValidationError, model_validator


@dataclass(frozen=True)
class Trip:
    distance: int
    fare: int
    tip: float | None = None


class TripIn(BaseModel):
    pickup: datetime
    dropoff: datetime
    passenger_count: int = Field(ge=1, le=6)
    fare_amount: float = Field(ge=0)

    @model_validator(mode="after")
    def dropoff_after_pickup(self) -> "TripIn":
        if self.dropoff <= self.pickup:
            raise ValueError("dropff must be after pickup")
        return self


def avg_tip_of_long_trips(trips, min_miles=5.0) -> float:
    long = [t for t in trips if t.distance > 5]
    avgTip = reduce(lambda avg, trip: avg + (trip.tip or 0), long, 0) / len(long)

    return avgTip


def count_validation_errors(rows: Iterable[dict[str, Any]]) -> Counter[str]:
    errors: Counter[str] = Counter()
    for row in rows:
        try:
            TripIn(**row)
        except ValidationError as e:
            errors.update(
                ".".join(map(str, err["loc"])) or "model" for err in e.errors()
            )

    return errors
