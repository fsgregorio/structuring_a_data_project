import pandas as pd
from typing import List

def transform_data(data_frame_list: List[pd.DataFrame]) -> pd.DataFrame:
    """
    Transforms the data from the extracted DataFrames and returns a single DataFrame
   
    args: 
    data_frame_list(List[pd.DataFrame]): List of DataFrames to be transformed
    """
    return pd.concat(data_frame_list, ignore_index=True)



