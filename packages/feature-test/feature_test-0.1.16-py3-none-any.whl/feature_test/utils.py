import pandas as pd
from typing import List


class Utils:
    def __init__(self):
        self.get_columns()
        self.exclude_columns()

    @classmethod
    def get_columns(self, X: pd.DataFrame) -> List:
        """
        Returns a list of column names.
        """
        return list(X.columns)

    @classmethod
    def exclude_columns(self, X: pd.DataFrame, columns: List) -> pd.DataFrame:
        """
        Exclude a list of columns from a dataframe.
        """
        return X.drop(columns, axis=1)
