Functions provided:
fix_NaN - Replaces NaN values
read_file - Reads Files


Data pre-processing choices made
fix_NaN function replaced the NaN values in columns with specific numbers and strings 
    Column "Name" NaN values replaced with "Name_0"
    Column "Age" NaN values replaced with "0"
    Column "Salary" NaN values replaced with "0"
    Column "City" NaN values replaced with "City_101"
    Column "JoinDate" NaN values replaced with "1900-01-01"


merge_files_and_format()
    Parameters - List of DF
    Returns -> merged DF

    This fuction enforces a strict typcasting to help pd.merge work effectively.
    Types are as follows.

    ID                   int64
    Name        string[python]
    Age                float64
    City        string[python]
    Salary             float64
    JoinDate    datetime64[ns]

    At the end of this process, true duplicates are dropped.


