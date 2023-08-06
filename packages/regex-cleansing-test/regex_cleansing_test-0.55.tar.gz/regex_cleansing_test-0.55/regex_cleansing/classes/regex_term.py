from dataclasses import dataclass
from datetime import datetime
import re
import pandas as pd


@dataclass
class RegexTerm:
    id: int
    source_field: str
    term: str
    case_sensitive: bool
    from_start_of_string: bool
    from_end_of_string: bool
    is_pattern: bool
    is_encoding_issue: bool
    is_categorisation_only: bool
    match_output_value: str
    pattern_output_value: str
    date_added: datetime
    date_modified: datetime
    date_removed: datetime
    last_updated: datetime
    project_owner: str

    def describe_self(self):
        print(f'\nRegexID: {self.id}'
              f'\nSource Field: {self.source_field}'
              f'\nRegex Term: {self.term}'
              f'\nCase Sensitive: {self.case_sensitive}'
              f'\nFrom Start of String: {self.from_start_of_string}'
              f'\nFrom End of String: {self.from_end_of_string}'
              f'\nIs Pattern Term: {self.is_pattern}'
              f'\nIs Encoding Issue: {self.is_encoding_issue}'
              f'\nIs Categorisation only: {self.is_categorisation_only}'
              f'\nMatch Output Value: {self.match_output_value}'
              f'\nPattern Output Value: {self.pattern_output_value}'
              f'\nDate Added: {self.date_added} '
              f'\nDate Modified: {self.date_modified} '
              f'\nDate Removed:  {self.date_removed} '
              f'\nLast Updated: {self.last_updated} '
              f'\nProject Owner: {self.project_owner} '
              )