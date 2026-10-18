"""Download the public datasets used across the workbook into data/raw/."""

import urllib.request
import zipfile
from pathlib import Path

import truststore

truststore.inject_into_ssl()  # trust the OS certificates (corporate TLS)

RAW = Path("data/raw")
RAW.mkdir(parents=True, exist_ok=True)
TLC = "https://d37ci6vzurychx.cloudfront.net"
FILES = {
    f"yellow_tripdata_2024-{m:02d}.parquet": f"{TLC}/trip-data/yellow_tripdata_2024-{m:02d}.parquet"
    for m in (1, 2, 3)
}

FILES["taxi_zone_lookup.csv"] = f"{TLC}/misc/taxi_zone_lookup.csv"
BEIR = "https://public.ukp.informatik.tu-darmstadt.de/thakur/BEIR/datasets"
FILES["scifact.zip"] = f"{BEIR}/scifact.zip"

for name, url in FILES.items():
    if (RAW / name).exists():
        continue
    print("downloading", name)
    urllib.request.urlretrieve(url, RAW / name)

with zipfile.ZipFile(RAW / "scifact.zip") as z:
    z.extractall(RAW)
