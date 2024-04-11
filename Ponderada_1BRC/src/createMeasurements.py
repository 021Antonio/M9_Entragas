import argparse
import time

import numpy as np
import polars as pl
from tqdm import tqdm

from stations_data import STATIONS

class CreateMeasurement:
    stations = pl.DataFrame(STATIONS, ("names", "means"))

    def __init__(self):
        self.rng = np.random.default_rng()

    def generate_batch(
            self,
            std_dev: float = 10,
            records: int = 10_000_000
    ) -> pl.DataFrame:
        batch = self.stations.sample(
            records,
            with_replacement=True,
            shuffle=True,
            seed=self.rng.integers(np.iinfo(np.int64).max)
        )
        batch = batch.with_columns(temperature=self.rng.normal(batch["means"], std_dev))
        return batch.drop("means")

    def generate_measurement_file(
            self,
            file_name: str = "measurements.txt",
            records: int = 1_000_000_000,
            sep: str = ";",
            std_dev: float = 10,
    ) -> None:
        print(
            f"Creating measurement file '{file_name}' with {records:,} measurements..."
        )
        start = time.time()
        batches = max(records // 10_000_000, 1)
        batch_ends = np.linspace(0, records, batches + 1).astype(int)

        with open(file_name, "w") as f:
            for i in tqdm(range(batches)):
                from_, to = batch_ends[i], batch_ends[i + 1]
                data = self.generate_batch(std_dev, to - from_)
                data.write_csv(f, separator=sep, float_precision=1, include_header=False)

            print(
                f"Created file '{file_name}' with {to:,} measurements in {time.time() - start:.2f} seconds"
            )


if __name__ == "__main__":

    def min_records(records: str) -> int:
        try:
            value = int(records)
        except Exception:
            raise argparse.ArgumentTypeError(f"invalid int value: '{records}'")
        else:
            if value < 1:
                raise argparse.ArgumentTypeError(
                    "Minimum number of records to be created is 1"
                )
            else:
                return value


    parser = argparse.ArgumentParser(description="Create measurement file")
    parser.add_argument(
        "-o",
        "--output",
        dest="output",
        type=str,
        help='Measurement file name (default is "measurements.txt")',
        default="measurements.txt",
    )
    parser.add_argument(
        "-r",
        "--records",
        help="Number of records to create (default is 1_000_000_000)",
        dest="records",
        type=min_records,
        default=1_000_000_000,
    )

    args = parser.parse_args()

    measurement = CreateMeasurement()
    measurement.generate_measurement_file(
        file_name=args.output,
        records=args.records,
    )


    