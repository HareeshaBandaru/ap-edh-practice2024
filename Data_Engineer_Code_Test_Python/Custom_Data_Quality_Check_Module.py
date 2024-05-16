#duplicate records check
import os
import pandas as pd

def Data_Quality_Check_Module(sourcefile_path=None):
    for (dir, _, files) in os.walk(sourcefile_path):
        for filename in files:
            file_path = os.path.join(dir, filename)
            # Load data
            print(file_path)
            df = pd.read_csv(file_path)
            duplicate_in_file = df.duplicated(subset=['name'])
            if duplicate_in_file.any():
                print(df.loc[~duplicate_in_file], end='\n\n')

sourcefile_path = "C:\\Users\hareesha.bandaru\Documents\GitHub\\ap-edh-practice2024\source_folder"
Data_Quality_Check_Module(sourcefile_path)