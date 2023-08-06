from dataclasses import dataclass
import re


@dataclass
class CleaningAction:
    id: int
    field: str
    field_value: list
    field_mapping: list
    regex_categories: list = None
    regex_terms: list = None
    working_value: str = ''
    regex_flag: int = 0
    pattern_match_output: str = ''
    pattern_term_matches: str = ''
    matched: str = ''
    matched_terms: str = ''
    cleaned_value: str = ''
    prepared_term: str = ''
    example_output_expected_result: str = ''
    example_output_test_result: str = ''

    def describe_self(self):
        print(f'\nID: {self.id}'
              f'\nField: {self.field}'
              f'\nField Value: {self.field_value}'
              f'\nField Mapping: {self.field_mapping}'
              f'\nRegex Categories: {self.regex_categories}'
              f'\nRegex Terms: {self.regex_terms}'
              f'\nWorking Value: {self.working_value}'
              f'\nPattern Match Output: {self.pattern_match_output}'
              f'\nPattern Term Matches: {self.pattern_term_matches}'
              f'\nMatched: {self.matched}'
              f'\nMatched Terms: {self.matched_terms}'
              f'\n Example Output Expected Result: {self.example_output_expected_result}')

    def _set_working_value(self):
        if self.working_value == '':
            self.working_value = self.field_value

    def _set_pattern_matching_output(self, value):
        if self.pattern_match_output == '':
            self.pattern_match_output = value
        else:
            self.pattern_match_output = self.pattern_match_output + ", " + value

    def _set_pattern_term_matches(self, value):
        if self.pattern_term_matches == '':
            self.pattern_term_matches = value
        else:
            self.pattern_term_matches = self.pattern_term_matches + ", " + value

    def _set_matched_terms(self, value):
        if self.matched_terms == '':
            self.matched_terms = r'(' + value + r')'
        else:
            self.matched_terms = self.matched_terms + ", " + r'(' + value + r')'

    def _set_cleaned_value_to_working_value(self):
        self.cleaned_value = self.working_value

    def _special_character_escape(self, term):
        special_character_escape_list = ['!', '"', '%', "'", ',', '/', ':', ';', '<', '=', '>', '@',
                                         "`"]
        for special in special_character_escape_list:
            term = term.replace(special, "\\" + special)
        return term

    def _adjust_term_for_conditions(self, term, regex_term):
        if regex_term.from_start_of_string == True:
            term = '^' + term
        if regex_term.from_end_of_string == True:
            term = term + "$"
        if regex_term.case_sensitive == False:
            self.regex_flag = re.IGNORECASE
        return term

    def _prepare_regex_term(self, regex_term):
        term = regex_term.term
        term = self._special_character_escape(term)
        self.prepared_term = term

    def _encoding_term(self, regex_term):
        term = self.prepared_term
        if regex_term.is_encoding_issue == True:
            term = bytes(term, 'UTF-8')
            byte_value = bytes(self.working_value, 'UTF-8')
            term = re.escape(term)
            if re.search(term, byte_value):
                self._set_pattern_matching_output(regex_term.pattern_output_value)

    def _pattern_term(self, regex_term):
        term = self.prepared_term
        if regex_term.is_pattern == True:
            if re.search(term, self.working_value):
                self._set_pattern_matching_output(regex_term.pattern_output_value)
                self._set_pattern_term_matches(term)

    def _substitution_term(self, regex_term):
        term = self.prepared_term
        term = self._adjust_term_for_conditions(term, regex_term)
        if regex_term.is_categorisation_only == False:
            if re.search(term, self.working_value):
                regex_output = re.sub(term,
                                      str(regex_term.match_output_value),
                                      str(self.working_value),
                                      flags=self.regex_flag)
                self.working_value = regex_output
                self.matched = "Matched"
                self._set_matched_terms(term)
            else:
                if self.matched != 'Matched':
                    self.matched = 'Unmatched'

    def execute_cleaning_functions(self):
        self._set_working_value()
        for RegexCategory in self.regex_categories:
            for RegexTerm in RegexCategory.regex_terms:
                self._prepare_regex_term(RegexTerm)
                self._encoding_term(RegexTerm)
                self._pattern_term(RegexTerm)
        for RegexCategory in self.regex_categories:
            for RegexTerm in RegexCategory.regex_terms:
                self._prepare_regex_term(RegexTerm)
                self._substitution_term(RegexTerm)
                self._set_cleaned_value_to_working_value()

    def values_to_dict(self):
        return {
            'CleaningAction ID': self.id,
            'Field': self.field,
            'Field Value': self.field_value,
            'Field Mapping': self.field_mapping,
            'Pattern Match Output': self.pattern_match_output,
            'Pattern Term Matches': self.pattern_term_matches,
            'Matched': self.matched,
            'Matched Terms': self.matched_terms,
            'Cleaned Value': self.cleaned_value,
            'Expected Result': self.example_output_expected_result,
            'Test Result': self.example_output_test_result
        }

