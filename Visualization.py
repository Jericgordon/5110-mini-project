from User_prompt import read_file
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np



#returns a DF that is formated in the documented format
def format_df(df):
    df["Salary"].replace("N/A",np.nan,inplace=True)
    df["Salary"] = df["Salary"].astype('float64')
    df["City"] = df["City"].astype("string")
    df["City"] = df["City"].fillna("")
    df["Name"] = df["Name"].astype("string")
    df["JoinDate"].replace("unknown",np.nan,inplace=True)
    df["JoinDate"] = pd.to_datetime(df["JoinDate"])
    df.set_index("ID")
    return df
    


#Handles the merging of all data
def merge_files_and_format(list_of_DF):
    #Define a return DF
    rdf = format_df(list_of_DF[0]) 

    #Handle the first one so that that DF is populated
    for index in range(len(list_of_DF) - 1): #Format and Join DF to the return DF
        df = format_df(list_of_DF[index])
        rdf = pd.merge(rdf,df,how='outer',on=None)   

    #Drop any complete Duplicates
    rdf.drop_duplicates()
    return rdf




def main():
    df1 = read_file("./Data/noisy_data.db",table_name = "noisy_table")
    df2 = read_file("./Data/noisy_data.csv")
    df3 = read_file("./Data/noisy_data.json")
    df4 = read_file("./Data/api_noisy_data.json")
    df5 = read_file("./Data/noisy_data.xlsx")

    df_list = [df1,df2,df3,df4,df5]
    df = merge_files_and_format(df_list)
    print(df.loc[df.duplicated("ID")])
    print(df)
    #print(df.columns)
    #groupby = df.groupby('ID')
    #print(groupby.aggregate(agg_func))
    # print(df.loc[df.duplicated(subset="ID")])
  #  print(df.loc[df["ID"] == 84])


if __name__ == '__main__':
    main()
