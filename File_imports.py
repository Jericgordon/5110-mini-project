import sqlite3 as sql #for reading sql db
import pandas as pd #for everything else




# auto detects filetype and returns a pandas df converted of that file
def read_file(file_name:str,**kwargs):
    valid_file_formats = ["json","csv","xlsx","db"]
    file_extension = file_name.split(".")[-1] #extract the extension from the string
    if file_extension not in valid_file_formats: #check to make sure program can handle the extension
         print("Cannot handle that type of file")
         return
    
    match file_extension:
        case "csv":
            df = pd.read_csv(file_name)
            return df
        case "json":
            df = pd.read_json(file_name)
            return df
        case "db":
            try:
                conn = sql.connect(file_name)
                df = pd.read_sql(f'SELECT * FROM {kwargs["table_name"]}',conn)
                return df
            except KeyError:
                print("Please add the table name")

            return df
        case "xlsx":
            df = pd.read_excel(file_name)
            return df
        
    
       



def main():
    #This is just some preliminary testing. Feel free to move around or ignore
    df = read_file("./Data/noisy_data.db",table_name = "noisy_table")
    df = read_file("./Data/noisy_data.csv")
    #print(df.head())
    df = read_file("./Data/noisy_data.json")
    #print(df.head())
    df = read_file("./Data/api_noisy_data.json")
 
    df = read_file("./Data/noisy_data.xlsx")






if __name__ == '__main__':
    main()
