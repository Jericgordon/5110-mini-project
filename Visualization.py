from User_prompt import read_file
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np






#Handles the merging of all data
def merge_all_files():
    #Process dfr
    dfr = read_file("./Data/noisy_data.xlsx") #originally df 5
    dfr.set_index("ID")
    dfr["Salary"] = dfr["Salary"].astype("float64") 
    #There were some challenges in converting the other 
    #Salary fields to at float because of N/A fields. Because I dont' want to do data processing
    #At the stage where null values can still be filled in by others, I've chosen to convert to the more
    #general format.

    #Process Json API data
    df4 = read_file("./Data/api_noisy_data.json") #Add in df4
    df4.set_index("ID")
    df4["Salary"].replace("N/A",np.nan,inplace=True)
    df4["City"].replace("",np.nan,inplace=True)
    dfr = pd.merge(dfr,df4,how='outer',on=None)    
    #print(dfr)


    #Process db
    df1 = read_file("./Data/noisy_data.db",table_name = "noisy_table")
    df1.set_index("ID")
    df1["Salary"].replace("N/A",np.nan,inplace=True)
    df1["Salary"] = df1["Salary"].astype("float64")
    df1["City"].replace("",np.nan,inplace=True)
    dfr = pd.merge(dfr,df1,how='outer',on=None)    
    #print(dfr)

    
    #Process csv
    df2 = read_file("./Data/noisy_data.csv")
    df2["Salary"].replace("N/A",np.nan,inplace=True)
    df2["Salary"] = df2["Salary"].astype('float64')
    df2["City"] = df2["City"].astype("string")
    df2["Name"] = df2["Name"].astype("string")
    
    df2["JoinDate"].replace("unknown",np.nan,inplace=True)
    df2["JoinDate"] = pd.to_datetime(df2["JoinDate"])
    df2.set_index("ID")
    df2 = pd.merge(df2,df2,how='outer',on=None)
   



    #Check dfr dtypes
    dfr["City"] = dfr["City"].astype("string")
    dfr["Name"] = dfr["Name"].astype("string")
    #print("Debug",dfr.dtypes)

    dfr["JoinDate"].replace("unknown",np.nan,inplace=True)
    dfr["JoinDate"] = pd.to_datetime(dfr["JoinDate"])

    #Process
    df3 = read_file("./Data/noisy_data.json")
    #clarify column types
    df3["Salary"].replace("N/A",np.nan,inplace=True)
    df3["Salary"] = df3["Salary"].astype('float64')
    df3["City"] = df3["City"].astype("string")
    df3["Name"] = df3["Name"].astype("string")
    
    df3["JoinDate"].replace("unknown",np.nan,inplace=True)
    df3["JoinDate"] = pd.to_datetime(df3["JoinDate"])



    df3.set_index("ID")
    dfr = pd.merge(dfr,df3,how='outer',on=None)    



   
    # print(dfr.dtypes)
    dfr = dfr.drop_duplicates()
    # print(dfr.loc[dfr.duplicated(subset="ID")])
    # print(dfr.loc[dfr["ID"] == 84])
    # print(dfr.iloc[83])
    # print(dfr.iloc[3078])
    # print(dfr.iloc[83].compare(dfr.iloc[83]))
    print("Data")
    print(dfr)
    print(dfr.dtypes)
    #Deal with duplicates
    dfr = dfr.drop_duplicates(keep="first") #We merge on ID because it's non-repeatable 
    
    return dfr


def agg_func(df):
    #print(df)
    pass



def main():
    df = merge_all_files()
    #print(df.columns)
    #groupby = df.groupby('ID')
    #print(groupby.aggregate(agg_func))
    # print(df.loc[df.duplicated(subset="ID")])
    # print(df.loc[df["ID"] == 84])


if __name__ == '__main__':
    main()
