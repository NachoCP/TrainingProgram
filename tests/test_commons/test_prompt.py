import os

import pytest

from commons.prompts.prompt_template import PromptTemplate


# Test valid input for generating the prompt
def test_valid_prompt():
    path = os.path.dirname(os.path.abspath(__file__))
    template = PromptTemplate(f"{path}/prompt.txt")

    # Generate the prompt with valid input
    output = template.text(competencies="Leadership, Communication", courses="Course A, Course B")

    # Expected result
    expected_output = "You are an expert in analyzing courses and identifying the relevant competencies they target.\n\nCompetencies:\nLeadership, Communication\n\nCourses:\nCourse A, Course B"
    print(output.strip())
    print("----")
    print(expected_output.strip())
    assert output.strip() == expected_output.strip()


def test_missing_variable():
    path = os.path.dirname(os.path.abspath(__file__))
    template = PromptTemplate(f"{path}/prompt.txt")

    with pytest.raises(AttributeError, match=r"Missing the following variable"):
        template.text(competencies="Leadership, Communication")


# Test invalid file path for the prompt template
def test_invalid_file_path(monkeypatch):
    def mock_exists(path):
        return False

    monkeypatch.setattr(os.path, "exists", mock_exists)

    with pytest.raises(ValueError, match=r"File does not exist"):
        PromptTemplate('invalid_path.txt')
