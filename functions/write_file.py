import os

def write_file(working_directory, file_path, content):
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
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        
        # If the file doesn't exist, create the necessary directories
        if not os.path.isfile(file_path_abs):
            os.makedirs(os.path.dirname(file_path_abs), exist_ok=True)
        
        # Overwrite the file with the provided content
        with open(file_path_abs, 'w', encoding='utf-8') as file:
            file.write(content)

        # Return success message
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f'Error: {str(e)}'