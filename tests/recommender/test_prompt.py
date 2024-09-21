import os

import pytest

from recommender.prompts.prompt_template import PromptTemplate


# Mock for reading a file
@pytest.fixture
def mock_read_text_file(monkeypatch):
    def mock_read(path):
        return """
        You are an expert in analyzing courses and identifying the relevant competencies they target.

        Competencies:
        {competencies}

        Courses:
        {courses}
        """
    monkeypatch.setattr("recommender.utils.read_text_file", mock_read)

# Mock for identifying prompt variables
@pytest.fixture
def mock_identify_prompt_variables(monkeypatch):
    def mock_identify(text):
        return ['competencies', 'courses']
    monkeypatch.setattr("recommender.utils.identify_prompt_variables", mock_identify)

# Test valid input for generating the prompt
def test_valid_prompt(mock_read_text_file, mock_identify_prompt_variables):
    template = PromptTemplate('template.txt')

    # Generate the prompt with valid input
    output = template.text(competencies="Leadership, Communication", courses="Course A, Course B")

    # Expected result
    expected_output = """
    You are an expert in analyzing courses and identifying the relevant competencies they target.

    Competencies:
    Leadership, Communication

    Courses:
    Course A, Course B
    """

    assert output.strip() == expected_output.strip()

# Test missing variable in the kwargs
def test_missing_variable(mock_read_text_file, mock_identify_prompt_variables):
    template = PromptTemplate('template.txt')

    # Attempt to generate prompt without the required 'courses' variable
    with pytest.raises(AttributeError, match=r"Missing the following variable"):
        template.text(competencies="Leadership, Communication")  # 'courses' is missing

# Test invalid file path for the prompt template
def test_invalid_file_path(monkeypatch):
    def mock_exists(path):
        return False  # Mock os.path.exists to return False

    monkeypatch.setattr(os.path, "exists", mock_exists)

    with pytest.raises(ValueError, match=r"File does not exist"):
        PromptTemplate('invalid_path.txt')

