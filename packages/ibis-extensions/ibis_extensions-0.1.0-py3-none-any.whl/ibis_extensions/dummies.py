from typing import Optional
import ibis
from ibis import Expr
from ibis.expr.types import Table, Column


def _get_categories(df: Table, cat_col: Column):
    return df.select(cat_col).distinct().execute().iloc[:, 0].tolist()


class OneHotEncoder:
    def __init__(
            self,
            input_col: Optional[str] = None,
            categories: Optional[list[str]] = None,
    ):

        self._fitted_values = []
        self.input_col: Column = input_col
        self.categories = categories

    def fit(self, df: Expr) -> "OneHotEncoder":
        if not self.categories:
            self._fitted_values = _get_categories(df, self.input_col)
        else:
            self._fitted_values = self.categories

        return self

    def transform(self, df: Expr) -> Expr:
        terms = {}
        orig_columns = df.columns
        for column in orig_columns:
            if column != self.input_col.get_name():
                terms[column] = df[column]
            else:
                for category in self._fitted_values:
                    terms[f"{self.input_col.get_name()}_{category}"] = (
                        ibis.case().when(df[self.input_col.get_name()] == category, 1).else_(0).end()
                    )
        return df.select(**terms)

    def fit_transform(self, df: Expr) -> Expr:
        return self.fit(df).transform(df)


def get_dummies(df: Expr) -> Expr:
    ohc = OneHotEncoder()
    return ohc.fit_transform(df)
