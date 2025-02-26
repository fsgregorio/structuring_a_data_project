"""Extracts data from the folder data/input and returns a DataFrame."""

import glob
import os
from typing import List

import openpyxl
import pandas as pd

path = 'data/input'


def extract_excel(path: str) -> List[pd.DataFrame]:
    """
    Extract data from the folder data/input and returns a DataFrame.

    args:
    path(str): path to the folder containing the data files

    returns:
    df(DataFrame): DataFrame containing the data from the files.
    """
    all_files = glob.glob(os.path.join(path, '*.xlsx'))

    data_frame_list = []
    for file in all_files:
        data_frame_list.append(pd.read_excel(file))

    return data_frame_list
