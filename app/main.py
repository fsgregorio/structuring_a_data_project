from pipeline.extract import extract_excel
from pipeline.transform import transform_data
from pipeline.load import save_to_excel


if __name__ == "__main__":
    listas_de_dataframes = extract_excel("data/input")
    print("Files Extracted 🔄")
    data_frame = transform_data(listas_de_dataframes)
    print("Data Transformed ⛏️")
    save_to_excel(data_frame, "data/output", "output")
    print("File Saved 💾")



