from File_imports import read_file
from Data_Preprocessing import merge_files_and_format
from matplotlib import pyplot as plt
from NaN import fix_NaN


def main():
    df1 = read_file("./Data/noisy_data.db",table_name = "noisy_table")
    df2 = read_file("./Data/noisy_data.csv")
    df3 = read_file("./Data/noisy_data.json")
    df4 = read_file("./Data/api_noisy_data.json")
    df5 = read_file("./Data/noisy_data.xlsx")

    df_list = [df1,df2,df3,df4,df5]
    df_merge = merge_files_and_format(df_list)
    df = fix_NaN(df_merge)
    



if __name__ == '__main__':
    main()