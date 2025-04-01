import os

import duckdb

# Paths to your CSV files
clicks_csv = 'raw/clicks.csv'
orders_csv = 'raw/orders.csv'

# Connect to DuckDB (in-memory or to a file)
con = duckdb.connect('dbt_project/dev.duckdb')

# Create schema and tables
con.execute("""
CREATE SCHEMA IF NOT EXISTS raw;

CREATE OR REPLACE TABLE raw.clicks (
    click_id INTEGER,
    session_id INTEGER,
    campaign_id INTEGER,
    click_date DATE
);

CREATE OR REPLACE TABLE raw.orders (
    order_id INTEGER,
    session_id INTEGER,
    user_id INTEGER,
    order_date DATE,
    total_price INTEGER
);
""")

# Load CSV data into the tables
con.execute(f"""
COPY raw.clicks
FROM '{os.path.abspath(clicks_csv)}'
WITH (HEADER TRUE, DELIM ',', AUTO_DETECT TRUE);
""")

con.execute(f"""
COPY raw.orders
FROM '{os.path.abspath(orders_csv)}'
WITH (HEADER TRUE, DELIM ',', AUTO_DETECT TRUE);
""")

print("Data successfully inserted into DuckDB!")
