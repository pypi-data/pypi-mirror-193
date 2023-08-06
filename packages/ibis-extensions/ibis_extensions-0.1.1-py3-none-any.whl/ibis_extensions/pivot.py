import ibis
from ibis.expr.types import Table, Column


def _get_categories(df: Table, cat_col: Column):
    return df.select(cat_col).distinct().execute().iloc[:, 0].tolist()


def pivot(table: Table, id_column: Column, pivot_column: Column, value_column: Column) -> Table:
    categories = _get_categories(table, pivot_column)

    terms = {}
    for category in categories:
        terms[f"{category}"] = (
            ibis.case().when(table[pivot_column.get_name()] == category, table[value_column.get_name()]).end().sum()
        )
    return table.group_by(id_column).aggregate(**terms)
