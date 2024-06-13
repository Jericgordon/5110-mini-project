

# auto detects filetype and returns a pandas df converted of that file
def read_file(file_name:str):
    valid_file_formats = ["json","csv"]
    file_extension = file_name.split(".")[-1]
    if file_extension not in valid_file_formats:
         print("Cannot handle that type of file")
         return

    match file_extension:
        case "csv":
            print("csv")
        case "json":
            print("json")
        case "db":
            print("db")
        case "xlsx":
            print("xlsx")
    
       


def main():
    read_file("file.json")
    read_file("fila.csv")
    read_file("file.txt")



if __name__ == '__main__':
    main()