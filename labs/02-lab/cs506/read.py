import sys
import subprocess
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pandas'])

import csv
import pandas as pd
def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    # with open(csv_file_path, 'r') as read_obj:
    #     csv_reader = csv.reader(read_obj)
    #     list_of_csv = list(csv_reader)
    #     return list_of_csv
    
    df = pd.read_csv(csv_file_path, delimiter=',')
    list_of_rows = [list(row) for row in df.values]
    return list_of_rows
