import os
import subprocess

def run_python_file(working_directory, file_path):
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
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        
        # If the file doesn't exist, create the necessary directories
        if not os.path.isfile(file_path_abs):
            return f'Error: File "{file_path}" not found.'
        
        # If the file is not a Python file, return an error
        if not file_path_abs.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file.'
        
        # Execute the Python file with a timeout of 30s.
        try:
            result = subprocess.run(
                ['python3', file_path_abs],
                cwd=working_dir_abs,
                capture_output=True,
                text=True,
                timeout=30
            )
            response = []
            if result.stdout:
                response.append(f'STDOUT:\n{result.stdout.strip()}')
            if result.stderr:
                response.append(f'STDERR:\n{result.stderr.strip()}')
            if result.returncode != 0:
                response.append(f'Process exited with code {result.returncode}')
            
            return '\n'.join(response) if response else 'No output produced.'

        except Exception as e:
            return f"Error: executing Python file: {e}"

    except Exception as e:
        return f'Error: {str(e)}'