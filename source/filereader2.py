def read_text_file(filename):
  """
  Reads the contents of a text file.

  Args:
      filename: The path to the text file.

  Returns:
      A string containing the entire content of the file, or None if an error occurs.
  """
  try:
    with open(filename, "r") as file:
      content = file.read()
      return content
  except FileNotFoundError:
    print("Error: File not found!")
  except PermissionError:
    print("Error: Insufficient permissions to access the file!")
  except Exception as e:
    print(f"An error occurred: {e}")
  return None

# Example usage
filename = "source/title1.txt"  # Replace with your actual file path
content = read_text_file(filename)

if content:
  print("File contents:")
  print(content)
else:
  print("Failed to read the file.")