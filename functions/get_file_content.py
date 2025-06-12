import os

def get_file_content(working_directory, file_path):
  try:
    # Get the path to the working directory
    working_dir_abs = os.path.abspath(working_directory)
    
    # Check if the file_path is None or empty
    if file_path is None or file_path.strip() == '':
      return f'Error: No file specified. Please provide a valid file path.'
    
    # Resolve the absolute path of the file
    file_path_abs = os.path.abspath(os.path.join(working_dir_abs, file_path))
    
    # Check that the given file path is inside the working directory
    if not file_path_abs.startswith(working_dir_abs):
      return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    # Check that the file is a file and exists
    if not os.path.isfile(file_path_abs):
      return f'Error: File not found or is not a regular file: "{file_path}"'
    
    # Read the first 10000 characters of the file
    MAX_CHARS = 10000
    with open(file_path_abs, 'r', encoding='utf-8') as file:
      content = file.read(MAX_CHARS)
    if len(content) == MAX_CHARS:
      content += f'\n\n...File "{file_path}" truncated at 10000 characters'
      
    return content
  except Exception as e:
    return f'Error: {str(e)}'