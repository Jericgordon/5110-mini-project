import pandas as pd
import numpy as np


"""
When Dataframes are not strictly formatted, it becomes increasingly difficult for Pandas to accurately Join
Dataframes. As such, enforcing rigid typeing leads to fewer, and easier to detect duplicates. The type
formatting is as follows:

ID                   int64
Name        string[python]
Age                float64
City        string[python]
Salary             float64
JoinDate    datetime64[ns]

Parameters: 
df -> Pandas Dataframe

Returns
-> Single formatted pandas dataframe

"""
def format_df(df):
    df["Salary"] = df["Salary"].replace("N/A",np.nan)
    df["Salary"] = df["Salary"].astype('float64')
    df["City"] = df["City"].astype("string")
    df["City"] = df["City"].fillna("")
    df["Name"] = df["Name"].astype("string")
    df["JoinDate"] = df["JoinDate"].replace("unknown","")
    df["JoinDate"] = pd.to_datetime(df["JoinDate"])
    df.set_index("ID")
    return df
    


"""
Parameters
List_of_DF  -> List of all desired dataframes to concatinate

Returns
Singer merge Dataframe


This function formats, and then merges all Dataframes passed to it.
"""

def merge_files_and_format(list_of_DF):
    #Define a return DF
    rdf = format_df(list_of_DF[0]) 

    #Handle the first one so that that DF is populated
    for index in range(len(list_of_DF) - 1): #Format and Join DF to the return DF
        df = format_df(list_of_DF[index + 1])
        rdf = pd.merge(rdf,df,how='outer',on=None)   

    #Drop any complete Duplicates
    rdf.drop_duplicates()
    return rdf

