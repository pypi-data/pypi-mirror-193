from dataclasses import dataclass


@dataclass
class FieldValue:
    field: str
    value: str
    row_id: int

    def describe_self(self):
        print(f'\nField: {self.field}'
              f'\nValue: {self.value}'
              f'\nRow ID: {self.row_id}')
