"""
Main script to run the data processing pipeline.

This script extracts data from Excel files, transforms the extracted data,
and then saves the final DataFrame as an Excel file in the output directory.

Steps:
1. Extract Excel files from 'data/input' directory.
2. Transform the extracted data using the transformation function.
3. Save the transformed data as an Excel file in 'data/output' directory.
"""

from pipeline.extract import extract_excel
from pipeline.load import save_to_excel
from pipeline.transform import transform_data

if __name__ == '__main__':
    listas_de_dataframes = extract_excel('data/input')
    print('Files Extracted 🔄')
    data_frame = transform_data(listas_de_dataframes)
    print('Data Transformed ⛏️')
    save_to_excel(data_frame, 'data/output', 'output')
    print('File Saved 💾')
