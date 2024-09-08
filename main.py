# import os
# import shutil
# path =r'C:\Users\upendar parvatham\Downloads\unorganized'
# print(shutil.disk_usage(path))
# list_of_file=os.listdir(path)
# print(list_of_file)
# for file in list_of_file:
#     name,extension=os.path.splitext(file)
#     print(name,extension)
#     extension=extension[1:]

#     if os.path.exists(path+'/'+extension):
#         shutil.move(path+'/'+file,path+'/'+extension+'/'+file)
#     else:
#         os.makedirs(path+'/'+extension)
#         shutil.move(path+'/'+file,path+'/'+extension+'/'+file)
import os
import shutil

# Prompt the user to enter the path
path = input("Enter the path to the directory you want to organize: ").strip()

# Check if the provided path exists
if not os.path.exists(path):
    print("The provided path does not exist.")
else:
    # Print disk usage of the given path
    print(shutil.disk_usage(path))
    
    # List all files and directories in the provided path
    list_of_file = os.listdir(path)
    print(list_of_file)
    
    # Organize files based on their extensions
    for file in list_of_file:
        name, extension = os.path.splitext(file)
        print(name, extension)
        extension = extension[1:]  # Remove the dot from the extension

        # Construct the folder path for the extension
        folder_path = os.path.join(path, extension)
        
        if os.path.exists(folder_path):
            # Move the file into the existing folder
            shutil.move(os.path.join(path, file), os.path.join(folder_path, file))
        else:
            # Create the folder and move the file into it
            os.makedirs(folder_path)
            shutil.move(os.path.join(path, file), os.path.join(folder_path, file))
