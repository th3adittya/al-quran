import os
import tkinter as tk
from tkinter import filedialog

def rename_files():
    # Get selected folder and rename type
    selected_folder = folder_var.get()
    rename_type = rename_type_var.get()

    if selected_folder and rename_type:
        folder_path = os.path.join(base_directory, selected_folder)
        files = os.listdir(folder_path)

        for index, file_name in enumerate(files):
            file_extension = os.path.splitext(file_name)[-1]
            new_file_name = ''

            if rename_type == 'Numeric':
                new_file_name = f'{index+1}{file_extension}'
            elif rename_type == 'Alphabetic':
                new_file_name = f'{chr(97 + index)}{file_extension}'

            os.rename(os.path.join(folder_path, file_name), os.path.join(folder_path, new_file_name))

        print('Files renamed successfully.')

# Initialize Tkinter window
window = tk.Tk()
window.title("File Renamer")

# Get the directory of the Python script
base_directory = os.path.dirname(__file__)

# Get the list of folders in the base directory and sort them numerically
folders = [folder for folder in os.listdir(base_directory) if os.path.isdir(os.path.join(base_directory, folder))]
folders.sort(key=lambda x: int(x))

# Dropdown for selecting folder
folder_label = tk.Label(window, text="Select Folder:")
folder_label.grid(row=0, column=0)
folder_var = tk.StringVar()
folder_dropdown = tk.OptionMenu(window, folder_var, *folders)
folder_dropdown.grid(row=0, column=1)

# Dropdown for selecting rename type
rename_type_label = tk.Label(window, text="Select Rename Type:")
rename_type_label.grid(row=1, column=0)
rename_type_var = tk.StringVar()
rename_type_dropdown = tk.OptionMenu(window, rename_type_var, "Numeric", "Alphabetic")
rename_type_dropdown.grid(row=1, column=1)

# Button to rename files
rename_button = tk.Button(window, text="Rename Files", command=rename_files)
rename_button.grid(row=2, column=0, columnspan=2)

# Run the Tkinter event loop
window.mainloop()
