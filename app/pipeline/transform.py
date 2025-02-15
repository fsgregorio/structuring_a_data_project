"""Module to transform the data extracted from the source into a single DataFrame."""

from typing import List

import pandas as pd


def transform_data(data_frame_list: List[pd.DataFrame]) -> pd.DataFrame:
    """
    Transform the data from the extracted DataFrames and returns a single DataFrame.

    args:
    data_frame_list(List[pd.DataFrame]): List of DataFrames to be transformed.
    """
    return pd.concat(data_frame_list, ignore_index=True)
