import polars as pl

# Read data file
df = pl.scan_csv(
    "measurements.txt",
    separator=";",
    has_header=False,
    with_column_names=lambda cols: ["station_name", "measurement"],
)

# Group data
grouped = (
    df.group_by("station_name")
    .agg(
        pl.min("measurement").alias("min_measurement"),
        pl.mean("measurement").alias("mean_measurement"),
        pl.max("measurement").alias("max_measurement"),
    )
    .sort("station_name")
    .collect(streaming=True)
)

# Abrindo um arquivo para escrita
with open("resultados.txt", "w") as file:
    for data in grouped.iter_rows():
        file.write(
            f"{data[0]}={data[1]:.1f}/{data[2]:.1f}/{data[3]:.1f}\n"
        )

