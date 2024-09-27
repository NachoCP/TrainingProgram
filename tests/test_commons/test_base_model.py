from commons.models.base_dynamic_model import BaseDynamicModel


class TestModel(BaseDynamicModel):
    name: str
    age: int


def test_set_dynamic_example_for_name():
    TestModel.set_dynamic_example("name", ["Alice", "Bob", "Charlie"])

    assert "name" in TestModel.Config.json_schema_extra["example"]
    assert TestModel.Config.json_schema_extra["example"]["name"] == ["Alice", "Bob", "Charlie"]


def test_set_dynamic_example_for_age():
    TestModel.set_dynamic_example("age", ["25", "30", "40"])

    assert "age" in TestModel.Config.json_schema_extra["example"]
    assert TestModel.Config.json_schema_extra["example"]["age"] == ["25", "30", "40"]
