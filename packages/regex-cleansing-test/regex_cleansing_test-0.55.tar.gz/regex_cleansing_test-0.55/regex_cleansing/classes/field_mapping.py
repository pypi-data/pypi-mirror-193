from dataclasses import dataclass


@dataclass
class FieldMapping:
    field_name: str
    cleaning_category: str

    def describe_self(self):
        print(f'\nField: {self.field_name}'
              f'\nCleaning Category: {self.cleaning_category}')