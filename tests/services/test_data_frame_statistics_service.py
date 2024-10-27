from typing import List, Tuple

import pandas as pd
import pytest
from pytest import LogCaptureFixture

from src.services.data_frame_statistics_service import DataFrameStatisticsService


def test_check_duplicates_invalid_column_input_raises_value_error(data_frame: pd.DataFrame) -> None:
    missing_column_name = "col_missing_column_name"
    with pytest.raises(KeyError):
        DataFrameStatisticsService.check_duplicates(data_frame, [missing_column_name])


@pytest.mark.parametrize(
    "columns, expected_count, expected_samples_shape",
    [
        (["col_1"], 2, (2, 2)),
        (["col_1", "col_2"], 1, (1, 3)),
        (["col_1", "col_2", "col_3"], 0, (0, 4)),
    ],
)
def test_check_duplicates_valid_cases(
    data_frame: pd.DataFrame, columns: List[str], expected_count: int, expected_samples_shape: Tuple[int, int]
) -> None:
    result = DataFrameStatisticsService.check_duplicates(data_frame, columns)
    assert result["count"] == expected_count
    assert result["samples"].shape == expected_samples_shape  # type: ignore[union-attr]


def test_empty_dataframe() -> None:
    df_empty = pd.DataFrame(columns=["col_1", "col_2", "col_3"])
    result = DataFrameStatisticsService.check_duplicates(df_empty, ["col_1"])
    assert result["count"] == 0
    assert result["samples"].shape == (0, 2)  # type: ignore[union-attr]


def test_empty_column_list(data_frame: pd.DataFrame, caplog: LogCaptureFixture) -> None:
    with pytest.raises(KeyError):
        DataFrameStatisticsService.check_duplicates(data_frame, [])

    assert "Column list is empty" in caplog.text
