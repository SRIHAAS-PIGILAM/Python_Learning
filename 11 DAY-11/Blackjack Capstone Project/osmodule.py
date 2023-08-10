"""The `os` module in Python is a built-in module that provides a way to interact with the operating system. It allows you to perform various tasks related to file management, directory operations, and more. Here are some of the commonly used functions and features of the `os` module:

1. **Working with Files and Directories:**
   - `os.getcwd()`: Returns the current working directory.
   - `os.chdir(path)`: Changes the current working directory to the specified path.
   - `os.listdir(path)`: Returns a list of files and directories in the specified path.
   - `os.mkdir(path)`: Creates a new directory at the specified path.
   - `os.rmdir(path)`: Removes an empty directory at the specified path.
   - `os.remove(path)`: Deletes a file at the specified path.
   - `os.path.exists(path)`: Checks if a path (file or directory) exists.

2. **Running System Commands:**
   - `os.system(command)`: Executes a shell command as a subprocess.
   - `os.popen(command)`: Opens a pipe to or from a command.

3. **File Information and Manipulation:**
   - `os.path.join(path, *paths)`: Joins one or more path components intelligently.
   - `os.path.basename(path)`: Returns the base name of a file path.
   - `os.path.dirname(path)`: Returns the directory name of a file path.
   - `os.path.isfile(path)`: Checks if the specified path points to a file.
   - `os.path.isdir(path)`: Checks if the specified path points to a directory.
   - `os.path.getsize(path)`: Returns the size of a file in bytes.

4. **Environment Variables:**
   - `os.environ`: A dictionary-like object that contains environment variables.

5. **Clearing the Screen:**
   - `os.system('clear')`: Clears the terminal screen (works on Unix-like systems).
   - `os.system('cls')`: Clears the terminal screen (works on Windows).

6. **Miscellaneous:**
   - `os.name`: Returns the name of the operating system dependent module.
   - `os.pathsep`: Returns the string used to separate entries in the `PATH` environment variable.

The `os` module is powerful and versatile, allowing you to interact with the file system and perform various system-related tasks within your Python programs. Keep in mind that some functions might behave differently on different operating systems, so it's a good practice to check the documentation for any platform-specific behavior.
"""
# 1. **Working with Files and Directories:**


import os

# Get current working directory
current_dir = os.getcwd()
print("Current working directory:", current_dir)

# Change working directory
new_dir = "/path/to/new/directory"
os.chdir(new_dir)
print("Changed working directory to:", new_dir)

# List files and directories in a directory
files_and_dirs = os.listdir(current_dir)
print("Files and directories:", files_and_dirs)

# Create a new directory
new_directory = "/path/to/new/directory"
os.mkdir(new_directory)
print("New directory created:", new_directory)

# Remove an empty directory
directory_to_remove = "/path/to/directory/to/remove"
os.rmdir(directory_to_remove)
print("Directory removed:", directory_to_remove)

# Delete a file
file_to_delete = "/path/to/file/to/delete.txt"
os.remove(file_to_delete)
print("File deleted:", file_to_delete)

# Check if a path exists
path_to_check = "/path/to/check"
if os.path.exists(path_to_check):
    print("Path exists:", path_to_check)
else:
    print("Path does not exist:", path_to_check)


# 2. **Running System Commands:**


# Execute a shell command
os.system("ls -l")

# Open a pipe to a command and read output
command_output = os.popen("ls -l").read()
print("Command output:", command_output)


# 3. **File Information and Manipulation:**


# Join path components
path1 = "/path/to"
path2 = "file.txt"
full_path = os.path.join(path1, path2)
print("Full path:", full_path)

# Get base name and directory name
file_path = "/path/to/file.txt"
print("Base name:", os.path.basename(file_path))
print("Directory name:", os.path.dirname(file_path))

# Check if a path points to a file or directory
print("Is file:", os.path.isfile(file_path))
print("Is directory:", os.path.isdir(path1))

# Get file size
file_size = os.path.getsize(file_path)
print("File size (bytes):", file_size)


# 4. **Environment Variables:**


# Access environment variables
user_home = os.environ['HOME']
print("User's home directory:", user_home)

# Print all environment variables
for key, value in os.environ.items():
    print(f"{key}: {value}")


# 5. **Clearing the Screen:**


# Clear terminal screen (works on Unix-like systems)
os.system("clear")

# Clear terminal screen (works on Windows)
os.system("cls")


# 6. **Miscellaneous:**


# Get the name of the operating system module
os_module_name = os.name
print("OS module name:", os_module_name)

# Get the path separator used in the system
path_separator = os.pathsep
print("Path separator:", path_separator)

"""
These code snippets demonstrate how to use various functionalities of the `os` module in Python. Remember to replace the placeholder paths with actual paths relevant to your system.
"""


#7. **Copying and Moving Files:**

#You can use the `shutil` module, which is often used in conjunction with the `os` module, to copy and move files and directories.


import shutil

# Copy a file
source_file = "source.txt"
destination_file = "destination.txt"
shutil.copy(source_file, destination_file)
print("File copied successfully.")

# Move a file
source_file = "source.txt"
destination_path = "/path/to/destination"
shutil.move(source_file, destination_path)
print("File moved successfully.")


#8. **Getting and Setting File Permissions:**

#You can use the `os` module to get and set file permissions on Unix-like systems using octal values.


import os

# Get file permissions (Unix-like systems)
file_path = "file.txt"
permissions = oct(os.stat(file_path).st_mode)[-3:]
print("File permissions:", permissions)

# Set file permissions (Unix-like systems)
new_permissions = "755"  # Example: Read, write, execute for owner, read and execute for others
os.chmod(file_path, int(new_permissions, 8))
print("File permissions changed.")


#9. **Executing Programs with Arguments:**

#You can use the `subprocess` module to execute external programs with arguments.


import subprocess

# Run a command and capture output
result = subprocess.run(["ls", "-l"], stdout=subprocess.PIPE, text=True)
print("Command output:", result.stdout)


#10. **Working with Paths:**

#The `os.path` submodule provides functions for path manipulation and analysis.


import os

# Check if a path is absolute
path = "/path/to/file.txt"
is_absolute = os.path.isabs(path)
print("Is absolute path:", is_absolute)

# Split a path into directory and file parts
dir_name, file_name = os.path.split(path)
print("Directory name:", dir_name)
print("File name:", file_name)

# Get the file extension
file_extension = os.path.splitext(file_name)[1]
print("File extension:", file_extension)


#11. **Creating Directories Recursively:**

#You can create directories and their parent directories recursively using the `os.makedirs()` function.


import os

# Create a directory and its parent directories if they don't exist
new_directory = "/path/to/new/directory"
os.makedirs(new_directory, exist_ok=True)
print("Directories created.")

"""
These additional code snippets demonstrate more functionalities of the `os` module, from copying files to manipulating paths and working with permissions. Remember to adapt these examples to your specific use cases and system. If you have any further questions or need more assistance, feel free to ask!
"""