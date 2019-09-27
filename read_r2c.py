import pandas as pd
import argparse
import os


def read_excel(excel_path):
    """
    Get excel and return a dataframe
    @excel_path: path to excel file
    """
    df = pd.ExcelFile(excel_path)
    return pd.read_excel(df, '1-Source')

#xls = pd.ExcelFile('path_to_file.xls')
#df1 = pd.read_excel(xls, 'Sheet1')
#df2 = pd.read_excel(xls, 'Sheet2')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="later bois", formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("-f", "--file", metavar="EXCEL_FILE", type=str, help="Full path of excel file")
    agrs = parser.parse_args()
    if agrs.file :
        print(read_excel(str(agrs.file)))
    else:
        print("BOO!")
