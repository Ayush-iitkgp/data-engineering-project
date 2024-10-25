from typing import List, Union

import pandas as pd


class DataFrameStatisticsService:
    @classmethod
    def check_duplicates(cls, df: pd.DataFrame, columns: List[str]) -> dict[str, Union[int, pd.DataFrame]]:
        """
        Checks for duplicates in a DataFrame based on specified columns.

        Parameters:
            df (pd.DataFrame): The input dataframe.
            columns (list): List of column names to check for duplicates.

        Returns:
            dict: A dictionary containing:
                - 'count': Number of distinct cases where duplicates occur.
                - 'samples': DataFrame with group count of duplicate rows for the given columns,
                             e.g.: col_1, col_2, number_of_duplicates.

        Raises:
            KeyError: If any column in 'columns' is not present in the dataframe.
        """
        df_columns = df.columns
        missing_columns = [col for col in columns if col not in df_columns]
        if missing_columns:
            raise KeyError(f"Columns {missing_columns} are not present in the dataframe.")

        grouped_df = df.groupby(columns).size().reset_index(name="number_of_duplicates")
        duplicate_cases = grouped_df[grouped_df["number_of_duplicates"] > 1]
        count = duplicate_cases.shape[0]
        return {"count": count, "samples": duplicate_cases}
