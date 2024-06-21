import pandas as pd
import numpy as np

def fix_NaN(merge_list):
    merge_list[['Name']] = merge_list[['Name']].fillna('Name_0')
    merge_list[['Age', 'Salary']] = merge_list[['Age', 'Salary']].fillna(0)
    merge_list[['City']] = merge_list[['City']].fillna('City_101')
    merge_list[['JoinDate']] = merge_list[['JoinDate']].fillna('1900-01-01')

    return merge_list

    