import os

import pandas as pd
def Data_Quality_Check_Module(sourcefile_path=None):
    for (dir, _, files) in os.walk(sourcefile_path):
        for filename in files:
            file_path = os.path.join(dir, filename)
            # Load data
            print(file_path)
            df = pd.read_csv(file_path)
            
            bad_df =df[df['name'].isnull() | df['location'].isnull() | df['phone'].isnull()]
            bad_df.to_csv("C:\\Users\hareesha.bandaru\Documents\GitHub\\ap-edh-practice2024\\bad_folder\\{}".format(filename), header=True, index=False, sep=' ', mode='a')
            # filtering data
            # displaying data only with team = NaN
            
            df = df[~df['name'].isnull() |~df['location'].isnull() |~df['phone'].isnull()]
            df['phone'] = df['phone'].str.replace('\W', '', regex=True)
            df['address'] = df['address'].str.replace('\W', '', regex=True)
            # print(df)
            
            df.to_csv("C:\\Users\hareesha.bandaru\Documents\GitHub\\ap-edh-practice2024\\target_folder\\{}".format(filename), header=True, index=False, sep=' ', mode='a')

sourcefile_path = "C:\\Users\hareesha.bandaru\Documents\GitHub\\ap-edh-practice2024\source_folder"

Data_Quality_Check_Module(sourcefile_path)