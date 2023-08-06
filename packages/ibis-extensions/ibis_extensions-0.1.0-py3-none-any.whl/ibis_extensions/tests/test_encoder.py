from datetime import date

import ibis
import pandas as pd
from ibis.backends.duckdb import Backend as DuckDBBackend

from ibis_extensions import OneHotEncoder, pivot, dedup

ibis.set_backend(ibis.duckdb.connect("database.ddb", threads=4, memory_limit="1GB"))


def test_col():
    df = pd.DataFrame({'id': [1, 2, 3, 4, 5], 'type': ['A', 'A', 'B', 'B', 'C']})
    table = ibis.memtable(df)
    ohc = OneHotEncoder(table.type)
    ohc.fit(table)
    trnsformed = ohc.transform(table)

    print(trnsformed.columns)


def test_col():
    be: DuckDBBackend = ibis.duckdb.connect("database.ddb", threads=4, memory_limit="1GB")
    df = pd.DataFrame({'id': [1, 2, 1, 1, 5], 'type': ['A', 'A', 'B', 'B', 'C']})
    table = ibis.memtable(df).mutate(value=1)
    pv = pivot(table, table.id, table.type, table.value)
    print(pv.execute())


def test_col():
    be: DuckDBBackend = ibis.duckdb.connect("database.ddb", threads=4, memory_limit="1GB")
    df = pd.DataFrame({'id': [1, 2, 1, 1, 5], 'type': ['A', 'A', 'B', 'B', 'C']})
    table = ibis.memtable(df)
    pv = dedup(table, [table.id], order_by=table.type.asc())
    print(be.compile(pv))


def test_col():
    be: DuckDBBackend = ibis.duckdb.connect("database.ddb", threads=4, memory_limit="1GB")
    df = pd.DataFrame({'id': [1, 2, 1, 1, 5], 'type': ['A', 'A', 'B', 'B', 'C']})
    df['start_date'] = date(2022, 1, 1)
    df['end_date'] = date(2022, 4, 1)
    table = ibis.memtable(df)
    pv = table.select(
        row_number=ibis.row_number().over(ibis.window(order_by=[table.type, table.start_date, table.end_date])),
        previous_end_date=table.end_date.max().over(
            ibis.window(group_by=table.type, order_by=[table.start_date, table.end_date], preceding=(None, 1))
            ))
    print(be.compile(pv))
