import pandas as pd
from app.pipeline.transform import transform_data


def test_union_dataframes():
    """
    Test that the function returns a single DataFrame with all the data from the input DataFrames
    """
    data_frame_list = [pd.DataFrame({"A": [1, 2], "B": [3, 4]}), pd.DataFrame({"A": [5, 6], "B": [7, 8]})]
    result = transform_data(data_frame_list)
    expected = pd.DataFrame({"A": [1, 2, 5, 6], "B": [3, 4, 7, 8]})
    pd.testing.assert_frame_equal(result, expected)