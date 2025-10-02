import openpyxl
import os

def get_test_data(file_name="Test_Data.xlsx"):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(base_dir, "data", file_name)

    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active

    data = []
    for row in sheet.iter_rows(min_row=2, values_only=True):
        # Only keep rows where at least one cell is non-empty
        if any(row):
            data.append(row)
    return data
