import pandas as pd
from typing import List

"""
  Transforms the data from the extracted DataFrames and returns a single DataFrame
  Args:
    data_frame_list(List[pd.DataFrame]): List of DataFrames to be transformed
"""

def transform_data(data_frame_list: List[pd.DataFrame]) -> pd.DataFrame:
    return pd.concat(data_frame_list, ignore_index=True)



