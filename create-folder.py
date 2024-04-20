import os

# Get the directory of the Python script
base_directory = os.path.dirname(__file__)

# Specify the range of folder names you want to create
start_range = 1
end_range = 114

# Loop through the range and create folders
for folder_number in range(start_range, end_range + 1):
    folder_name = f'{folder_number}'
    folder_path = os.path.join(base_directory, folder_name)
    
    # Check if the folder already exists
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f'Created folder: {folder_path}')
    else:
        print(f'Folder already exists: {folder_path}')
