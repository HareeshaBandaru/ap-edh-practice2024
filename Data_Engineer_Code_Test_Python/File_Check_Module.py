import os
import shutil

#create a function with three parameters sourcefile_path, targetfile_path, badfile_path
def File_Check_Module(sourcefile_path=None, targetfile_path=None, badfile_path=None):
    for (dir, _, files) in os.walk(sourcefile_path):
        files_tobeprocessed=[]
        target_list = os.listdir(targetfile_path)
        for filename in files:
            file_path = os.path.join(dir, filename)
            # check if the file is already in processed folder
            # check if the file extension is .csv
            if ('.csv' in filename) and (filename not in target_list):
                #check if the file size is empty
                if os.path.getsize(file_path) != 0:
                    #then process the file to target folder
                    files_tobeprocessed.append(filename)
                else:
                    # else move it to bad folder
                    shutil.move(file_path, badfile_path)
            else:
                # else move it to bad folder
                shutil.move(file_path, badfile_path)
        print(files_tobeprocessed)
sourcefile_path = "C:\\Users\hareesha.bandaru\Documents\GitHub\\ap-edh-practice2024\source_folder"
targetfile_path = "C:\\Users\hareesha.bandaru\Documents\GitHub\\ap-edh-practice2024\\target_folder"
badfile_path = "C:\\Users\hareesha.bandaru\Documents\GitHub\\ap-edh-practice2024\\bad_folder"
File_Check_Module(sourcefile_path, targetfile_path, badfile_path)
