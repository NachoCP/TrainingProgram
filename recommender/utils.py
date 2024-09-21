import re
from pathlib import Path


def read_text_file(path: str) -> str:
    """Helper function to read a prompt file based on the type."""
    return Path(path).read_text()

def identify_prompt_variables(text: str) -> list[str]:
    matches = re.findall(r'\{(.*?)\}', text)
    return matches
