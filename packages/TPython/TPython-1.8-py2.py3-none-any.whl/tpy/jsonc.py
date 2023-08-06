# Import Libs
import json
import re

# Parser
def parse(filepath: str) -> dict:
    # Define the regular expression to match both comment styles
    comment_pattern = r'(\/\/[^\n]*)|(/\*[\s\S]*?\*/)'

    # Read the contents of the file into a string
    with open(filepath, 'r', encoding='utf-8') as f:
        contents = f.read()

    # Remove the comments from the string
    json_dict = json.loads(re.sub(comment_pattern, '', contents))
    return json_dict