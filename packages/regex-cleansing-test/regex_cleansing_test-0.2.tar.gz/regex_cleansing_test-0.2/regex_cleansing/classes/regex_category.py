from dataclasses import dataclass
import pandas
from datetime import datetime
import re


@dataclass
class RegexCategory:
    id: str
    category: str
    client_id: str
    date_added: datetime
    date_modified: datetime
    date_removed: datetime
    last_updated: datetime
    project_owner: str
    regex_terms: list

    def describe_self(self):
        print(f'\nRegex ID: {self.id}'
              f'\nCategory: {self.category}'
              f'\nClient ID: {self.client_id}'
              f'\nDate Added: {self.date_added}'
              f'\nDate Modified: {self.date_modified}'
              f'\nDate Removed: {self.date_removed}'
              f'\nLast Updated: {self.last_updated}'
              f'\nProject Owner: {self.project_owner}'
              f'\nRegex Terms: {self.regex_terms}'
              )
