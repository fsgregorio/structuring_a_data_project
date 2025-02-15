import pandas as pd
import os


def save_to_excel(df: pd.DataFrame, output_path: str, file_name: str) -> str:
    """
    Receive a DataFrame and save as a XLSX file
    
    args:
    df(DataFrame): DataFrame to be saved
    output_path(str): path to save the file
    file_name(str): name of the file to be saved
    
    If the path does not exist, it will be created
    """
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    file_path = os.path.join(output_path, f"{file_name}.xlsx")
    df.to_excel(file_path, index=False)
    