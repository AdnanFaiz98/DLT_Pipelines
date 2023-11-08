import dlt

pipeline = dlt.pipeline(destination="duckdb", dataset_name="countries_ds")

data = [
    {'country': 'USA', 'population': 331449281, 'capital': 'Washington, D.C.'},
    {'country': 'Canada', 'population': 38005238, 'capital': 'Ottawa'},
    {'country': 'Germany', 'population': 83019200, 'capital': 'Berlin'}
]

info = pipeline.run(data, table_name="countries_tbl")

print(info)