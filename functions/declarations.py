from google.genai import types

def decl_get_files_info():
  schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
      type=types.Type.OBJECT,
      properties={
        "directory": types.Schema(
          type=types.Type.STRING,
          description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
        ),
      },
    ),
  )
  return schema_get_files_info

def decl_get_file_contents():
  schema_get_file_contents = types.FunctionDeclaration(
    name="get_file_contents",
    description="Retrieves the contents of a specified file, constrained to the working directory. Returns a maximum of 10000 characters.",
    parameters=types.Schema(
      type=types.Type.OBJECT,
      properties={
        "file_path": types.Schema(
          type=types.Type.STRING,
          description="The path to the file to read, relative to the working directory.",
        )
      }
    )
  )
  return schema_get_file_contents

def decl_run_python_file():
  schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a Python file in the working directory. Returns the output of the execution, including stdout and stderr.",
    parameters=types.Schema(
      type=types.Type.OBJECT,
      properties={
        "file_path": types.Schema(
          type=types.Type.STRING,
          description="The path to the Python file to execute, relative to the working directory.",
        )
      }
    )
  )
  return schema_run_python_file

def decl_write_file():
  schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes or overwrites a file with the provided content in the working directory.",
    parameters=types.Schema(
      type=types.Type.OBJECT,
      properties={
        "file_path": types.Schema(
          type=types.Type.STRING,
          description="The path to the file to write, relative to the working directory.",
        ),
        "content": types.Schema(
          type=types.Type.STRING,
          description="The content to write to the file.",
        )
      }
    )
  )
  return schema_write_file

def build_function_declarations():
  function_declarations = []
  function_declarations.append(decl_get_files_info())
  function_declarations.append(decl_get_file_contents())
  function_declarations.append(decl_run_python_file())
  function_declarations.append(decl_write_file())
  
  return function_declarations