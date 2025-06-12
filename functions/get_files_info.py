import os

def get_files_info(working_directory, directory=None):
  try:
    # Get the path to the working directory
    working_dir_abs = os.path.abspath(working_directory)
    if directory is None:
      directory = working_dir_abs
    else:
      directory = os.path.abspath(os.path.join(working_dir_abs, directory))
    
    # Check that the given directory is a subdirectory of the working directory
    if not directory.startswith(working_dir_abs):
      return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
      
    # Check if the directory path is a directory
    if not os.path.isdir(directory):
      return f'Error: "{directory}" is not a directory.'
    
    # Build string represetation of the directory contents.
    file_info_lines = []
    files = os.listdir(directory)
    for file in files:
      name = file
      path = os.path.join(directory, file)
      is_dir = os.path.isdir(path)
      size = os.path.getsize(path)
      file_info_lines.append(f'- {name}: file_size={size} bytes, is_dir={is_dir}')
      
    return '\n'.join(file_info_lines) if file_info_lines else 'Error: Nothing found in the directory.'
  except Exception as e:
    return f'Error: {str(e)}'