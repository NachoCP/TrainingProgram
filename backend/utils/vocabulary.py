from enum import Enum


class RoleEnum(str, Enum):
    manager = "Manager"
    worker = "Worker"

class TypeEnum(str, Enum):
    global_level = "Global"
    team_level = "Team"

class RequiredLevelEnum(str, Enum):
    # Enum for the competency levels
    basic = "Basic"  # Entry-level knowledge
    intermediate = "Intermediate"  # Mid-level competency
    advanced = "Advanced"  # Proficient with advanced understanding
    expert = "Expert"  # Mastery in the competency
