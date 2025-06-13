import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.declarations import build_function_declarations
from functions.call_functions import call_function

def main():
  if len(sys.argv) < 2:
    print("Usage: python main.py <prompt>")
    sys.exit(1)
    
  flags = []
  if len(sys.argv) > 2:
    flags = sys.argv[2:]
  if flags:
    print(f"Flags provided: {', '.join(flags)}")
  
  verbose = "--verbose" in flags
    
  prompt = sys.argv[1]
  if not prompt:
    print("Prompt cannot be empty.")
    sys.exit(1)
  
  load_dotenv()
  api_key = os.environ.get("GEMINI_API_KEY")
  model_name = os.environ.get("MODEL_NAME", "gemini-2.0-flash-001")
  system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""

  client = genai.Client(api_key=api_key)
  
  messages = [
    types.Content(
      role="user",
      parts=[
        types.Part(
          text=prompt
        )
      ]
    )
  ]
  
  available_functions = types.Tool(
    function_declarations=build_function_declarations()
  )
  
  response = client.models.generate_content(
    model="gemini-2.0-flash-001",
    contents=messages,
    config=types.GenerateContentConfig(
      tools=[available_functions],
      system_instruction=system_prompt
    )
  )
  
  if response.function_calls:
    for call in response.function_calls:
      result = call_function(call, verbose=verbose)
      if not result.parts[0].function_response.response:
        raise Exception(f"Function {call.name} returned no response.")
      if verbose:
        print(f"-> {result.parts[0].function_response.response}")
  else:
    print(response.text)
  
  if verbose:
    print(f"User prompt: {prompt}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

if __name__ == "__main__":
  main()
  sys.exit(0)