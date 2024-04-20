import os
import tkinter as tk
from tkinter import filedialog

def rename_files(event=None):
    # Get selected folder and rename type
    selected_folder = folder_var.get()
    rename_type = rename_type_var.get()

    if selected_folder and rename_type:
        folder_path = os.path.join(base_directory, selected_folder)
        ds_store_path = os.path.join(folder_path, ".DS_Store")
        if os.path.exists(ds_store_path):
            os.remove(ds_store_path)
            log_text.insert(tk.END, "Deleted .DS_Store file.\n")

        files = os.listdir(folder_path)
        files.sort()

        log_text.delete(1.0, tk.END)

        for index, file_name in enumerate(files):
            file_extension = os.path.splitext(file_name)[-1]
            new_file_name = f'{index+1}{file_extension}'

            new_file_path = os.path.join(folder_path, new_file_name)

            # Check if the file already exists
            if os.path.exists(new_file_path):
                log_text.insert(tk.END, f"File '{new_file_name}' already exists in folder '{selected_folder}'\n")
            else:
                os.rename(os.path.join(folder_path, file_name), new_file_path)
                log_text.insert(tk.END, f"Renamed file '{file_name}' to '{new_file_name}'\n")

        log_text.insert(tk.END, 'Files renamed successfully.\n')

def select_next_folder(event):
    current_index = folders.index(folder_var.get())
    next_index = (current_index + 1) % len(folders)
    folder_var.set(folders[next_index])

def select_previous_folder(event):
    current_index = folders.index(folder_var.get())
    previous_index = (current_index - 1) % len(folders)
    folder_var.set(folders[previous_index])

# Initialize Tkinter window
window = tk.Tk()
window.title("File Renamer")
window.geometry("400x300")

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

# Bind arrow up and down keys to change folder selection
window.bind("<Up>", select_previous_folder)
window.bind("<Down>", select_next_folder)

# Button to rename files
rename_button = tk.Button(window, text="Rename Files", command=rename_files)
rename_button.grid(row=2, column=0, columnspan=2)

# Text widget to display log
log_text = tk.Text(window, height=10, width=40)
log_text.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Bind Enter key to rename files
window.bind("<Return>", rename_files)

# Run the Tkinter event loop
window.mainloop()
