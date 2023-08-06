from ibis import _
import ibis
from ibis.expr.types import Table, Column, Value


def dedup(table: Table, keys: list[Column], order_by: Value) -> Table:
    return table.mutate(keep_row=ibis.row_number().over(ibis.window(group_by=keys, order_by=order_by))) \
        .filter(_.keep_row == 0) \
        .drop("keep_row")


