import ibis
from ibis.expr.types import Table, Column

def merge_timeframes(dataframe: Table, start: Column, end: Column, keys: list[any]) -> Table:
    grouping = dataframe \
        .mutate(row_number=ibis.row_number()
                .over(ibis.window(order_by=keys + [start, end])),
                previous_end_date=end.max()
                .over(ibis.window(group_by=keys, order_by=[start, end], preceding=(None, 1))))

    islands = grouping \
        .mutate(
            island_start_ind=ibis.case().when(grouping.previous_end_date >= start, 0).else_(1).end(),
            island_id=(ibis.case()
                       .when(grouping.previous_end_date >= start, 0).else_(1).end()
                       ).sum().over(ibis.window(order_by=grouping.row_number)))

    return islands.groupby(keys + [islands.island_id]) \
        .aggregate(start_date=start.min(), end_date=end.max()) \
        .order_by(keys).drop("island_id")

