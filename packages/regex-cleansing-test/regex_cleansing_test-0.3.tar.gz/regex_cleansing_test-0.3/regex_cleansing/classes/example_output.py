from dataclasses import dataclass


@dataclass
class ExampleOutput:
    example_id: int
    field: str
    category: str
    input_value: str
    expected_result: str
    client_id: str
    project_owner: str

    def describe_self(self):
        print(f'\nExample ID: {self.example_id}'
              f'\nField: {self.field}'
              f'\nCategory: {self.category}'
              f'\nInput Value: {self.input_value}'
              f'\nExpected Result: {self.expected_result}'
              f'\nClient ID: {self.client_id}'
              f'\nProject Owner: {self.project_owner}')
