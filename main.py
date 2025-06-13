import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

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
  system_prompt = os.environ.get("SYSTEM_PROMPT")

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
  
  response = client.models.generate_content(
    model="gemini-2.0-flash-001",
    contents=messages,
    config=types.GenerateContentConfig(
      system_instruction=system_prompt
    )
  )
  print(response.text)
  
  if verbose:
    print(f"User prompt: {prompt}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

if __name__ == "__main__":
  main()
  sys.exit(0)