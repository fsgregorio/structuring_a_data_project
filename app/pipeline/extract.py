import os
import glob

import pandas as pd
from typing import List
import openpyxl

"""
Extracts data from the folder data/input and returns a DataFrame

args: path(str): path to the folder containing the data files
returns: df(DataFrame): DataFrame containing the data from the files

"""
path = "data/input"

def extract_excel(path: str) -> List[pd.DataFrame]:
    all_files = glob.glob(os.path.join(path, "*.xlsx"))
    
    data_frame_list = []
    for file in all_files:
        data_frame_list.append(pd.read_excel(file))

    return data_frame_list
    

if __name__ == "__main__":
    data_frame_list = extract_excel(path)
    print(data_frame_list)

