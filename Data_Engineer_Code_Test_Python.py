import os
import glob
def File_Check_Module(file_path=None):
    for (dir, _, files) in os.walk(file_path):
        for filename in files: # Generate file path
            file_path = os.path.join(dir, filename)
            # Check if it is file and empty (size = 0) --------
            if os.path.getsize(file_path) == 0:
                print(file_path)

File_Check_Module("C:\\Users\hareesha.bandaru\Documents\GitHub\\ap-edh-practice2024\\files_folder\*")

#
# files = glob.glob(file_path)
#     # print(files)
#     for path in files:
#         if os.path.getsize(path) != 0 and :
#             print("empty", path)
#         # Check if the path is a file and empty (size = 0)
#         # if (
#         #         os.path.isfile(path) and
#         #         os.path.getsize(path) == 0
#         # ):
#         #     print("path", path)
#     # # Get the list of all files and directories
#     # dir_list = os.listdir(file_path)
#     # print("Files and directories in '", file_path, "' :")
#     # # prints all files
#     # print(dir_list)
#     # for i in dir_list:
#     #     if i.split(".")[1] == "csv":
#     #         if os.stat(i[0]).st_size != 0:
#     #             print(i)
