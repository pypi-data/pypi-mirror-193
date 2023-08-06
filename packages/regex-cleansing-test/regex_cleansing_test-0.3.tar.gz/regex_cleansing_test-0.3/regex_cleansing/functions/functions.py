import regex_cleansing.classes.regex_term as regex_term
import regex_cleansing.classes.regex_category as reg_category
import regex_cleansing.classes.field_mapping as field_mapping
import regex_cleansing.classes.field as field
import regex_cleansing.classes.cleaning_action as cleaning_action
import regex_cleansing.classes.example_output as example_output
import regex_cleansing.snowflake.snowflake as snowflake
import pandas
import filepaths as fpath


def _import_regex_terms_from_excel():
    regex_terms = (pandas.read_excel(fpath.regex_terms)).fillna('')
    return regex_terms


def _import_regex_terms_from_snowflake():
    regex_terms = snowflake.query_snowflake_regex_terms()
    regex_terms = regex_terms.fillna('')
    return regex_terms


def import_regex_terms(mode: str):
    if mode == 'Excel':
        regex_terms = _import_regex_terms_from_excel()
    elif mode == 'Snowflake':
        regex_terms = _import_regex_terms_from_snowflake()
    else:
        print("Select Valid mode: Excel or Snowflake")
    regex_terms.to_csv(fpath.output_directory / "regex_terms_import_test.csv", index=False)
    return regex_terms


def create_regex_term_objects(regex_terms: pandas.DataFrame):
    regex_terms_list = []
    for index, row in regex_terms.iterrows():
        regex_term_object = regex_term.RegexTerm(id=row['ID'],
                                                 source_field=row['SOURCE_FIELD'],
                                                 term=row['SEARCH_TERM'],
                                                 case_sensitive=row['IS_CASESENSITIVE'],
                                                 from_start_of_string=row['IS_FROM_START_OF_STRING'],
                                                 from_end_of_string=row['IS_FROM_END_OF_STRING'],
                                                 is_pattern=row['IS_PATTERN'],
                                                 is_encoding_issue=row['IS_ENCODING_ISSUE'],
                                                 is_categorisation_only=row['IS_CATEGORISATION_ONLY'],
                                                 match_output_value=row['MATCH_OUTPUT_VALUE'],
                                                 pattern_output_value=row['PATTERN_OUTPUT_VALUE'],
                                                 date_added=row['DATE_ADDED'],
                                                 date_modified=row['DATE_MODIFIED'],
                                                 date_removed=row['DATE_REMOVED'],
                                                 last_updated=row['LAST_UPDATED'],
                                                 project_owner=row['PROJECT_OWNER']
                                                 )
        regex_terms_list.append(regex_term_object)
    return regex_terms_list


def _import_regex_categories_from_excel():
    regex_categories = (pandas.read_excel(fpath.regex_categories)).fillna('')
    return regex_categories


def _import_regex_categories_from_snowflake():
    regex_categories = snowflake.query_snowflake_regex_categories()
    regex_categories = regex_categories.fillna('')
    return regex_categories


def import_regex_categories(mode: str):
    if mode == 'Excel':
        regex_categories = _import_regex_categories_from_excel()
    elif mode == 'Snowflake':
        regex_categories = _import_regex_categories_from_snowflake()
    else:
        print("Select Valid mode: Excel or Snowflake")
    return regex_categories


def create_regex_categories(regex_categories, client_id, no_general_terms: bool, regex_term_list):
    if no_general_terms:
        regex_categories = regex_categories.loc[(regex_categories['CLIENT_ID'] == client_id)]
    else:
        if client_id is not None:
            regex_categories = regex_categories.loc[
                (regex_categories['CLIENT_ID'] == 'General') | (regex_categories['CLIENT_ID'] == client_id)]
        else:
            regex_categories = regex_categories.loc[(regex_categories['CLIENT_ID'] == 'General')]
    regex_categories_list = []
    print(regex_categories)
    for index, row in regex_categories.iterrows():
        regex_category = reg_category.RegexCategory(id=row['REGEX_TERM'],
                                                    category=row['CATEGORY'],
                                                    client_id=row['CLIENT_ID'],
                                                    date_added=row['DATE_ADDED'],
                                                    date_modified=row['DATE_MODIFIED'],
                                                    date_removed=row['DATE_REMOVED'],
                                                    last_updated=row['LAST_UPDATED'],
                                                    project_owner=row['PROJECT_OWNER'],
                                                    regex_terms=[x for x in regex_term_list if
                                                                 x.id == row['REGEX_TERM']]
                                                    )
        regex_categories_list.append(regex_category)
    return regex_categories_list


def generate_regex_categories(mode: str, client_id: str, no_general_terms: bool, regex_term_list):
    regex_categories = import_regex_categories(mode)
    regex_categories_list = create_regex_categories(regex_categories, client_id, no_general_terms, regex_term_list)
    return regex_categories_list


def import_field_mapping(mapping_file, field_name, field_cleaning_category):
    fields = [field_name, field_cleaning_category]
    # rename fields to be looked up later
    field_mapping_df = pandas.read_excel(mapping_file, usecols=fields)
    return field_mapping_df


def create_field_mapping_objects(field_mapping_df, field_name, field_cleaning_category):
    field_mapping_item_list = []
    for index, row in field_mapping_df.iterrows():
        field_mapping_item = field_mapping.FieldMapping(field_name=row[field_name],
                                                        cleaning_category=row[field_cleaning_category])
        field_mapping_item_list.append(field_mapping_item)
    return field_mapping_item_list


def generate_field_mapping_objects(mapping_file, field_name, field_cleaning_category):
    field_mapping_df = import_field_mapping(mapping_file, field_name, field_cleaning_category)
    field_mapping_list = create_field_mapping_objects(field_mapping_df, field_name, field_cleaning_category)
    return field_mapping_list


def import_field_value_inputs(input_file):
    field_value_df = pandas.read_excel(input_file)
    field_value_df['Row ID'] = field_value_df.index + 1
    return field_value_df


def create_field_value_objects(field_value_df):
    field_value_list = []
    for column in field_value_df:
        for index, row in field_value_df.iterrows():
            field_value_item = field.FieldValue(field=column,
                                                value=row[column],
                                                row_id=row['Row ID'])
            field_value_list.append(field_value_item)
    return field_value_list


def generate_field_value_objects(input_file):
    field_value_df = import_field_value_inputs(input_file)
    field_value_list = create_field_value_objects(field_value_df)
    return field_value_list


def generate_cleaning_action_objects(field_value_list, field_mapping_list, regex_categories_list):
    id_ticker = 1
    cleaning_action_object_list = []
    for FieldValue in field_value_list:
        cleaning_action_object = cleaning_action.CleaningAction(id=id_ticker,
                                                                field=FieldValue.field,
                                                                field_value=FieldValue.value,
                                                                field_mapping=[x for x in field_mapping_list
                                                                               if x.field_name == FieldValue.field])
        for FieldMapping in cleaning_action_object.field_mapping:
            cleaning_action_object.regex_categories = [x for x in regex_categories_list
                                                       if x.category == FieldMapping.cleaning_category]
        id_ticker = id_ticker + 1
        cleaning_action_object_list.append(cleaning_action_object)
    return cleaning_action_object_list


def execute_cleaning_actions(cleaning_action_object_list, example_output: bool):
    output_df = pandas.DataFrame(columns=['CleaningAction ID'])
    for CleaningAction in cleaning_action_object_list:
        if CleaningAction.regex_categories is not None:
            CleaningAction.execute_cleaning_functions()
            if CleaningAction.example_output_expected_result is not None:
                if str(CleaningAction.example_output_expected_result) == str(CleaningAction.cleaned_value):
                    CleaningAction.example_output_test_result = "PASS"
                else:
                    CleaningAction.example_output_test_result = "FAIL"
            df_cleaning_action = pandas.DataFrame.from_records(CleaningAction.values_to_dict(), index=[0])
            output_df = pandas.concat([output_df, df_cleaning_action])
    if not example_output:
        output_df = output_df.drop(columns=['Expected Result', 'Test Result'])
    output_df = (output_df.reset_index()).drop(columns=['index'])
    return output_df


def run_regex_cleansing(mode,
                        client_id,
                        no_general_terms: bool,
                        field_mapping_input,
                        field_mapping_field_column,
                        field_mapping_cleaning_category,
                        input_file,
                        output_location):
    regex_terms = import_regex_terms(mode)
    regex_term_list = create_regex_term_objects(regex_terms)
    print("--RegexTerms objects created--\n" + str(regex_term_list))
    regex_category_list = generate_regex_categories(mode,
                                                    client_id,
                                                    no_general_terms,
                                                    regex_term_list)
    print("--RegexCategories objects created--\n" + str(regex_category_list))
    field_mapping_list = generate_field_mapping_objects(field_mapping_input,
                                                        field_mapping_field_column,
                                                        field_mapping_cleaning_category)
    print("--FieldMapping objects created--\n" + str(field_mapping_list))
    field_value_list = generate_field_value_objects(input_file)
    print("--FieldValue objects creates--\n" + str(field_value_list))
    cleaning_object_list = generate_cleaning_action_objects(field_value_list,
                                                            field_mapping_list,
                                                            regex_category_list)
    print("--CleaningAction objects created--\n" + str(cleaning_object_list))
    output = execute_cleaning_actions(cleaning_object_list, False)
    output.to_csv(output_location / "regex_clean_output.csv", index=False)
    print("--CleaningActions executed. Dataframe of output generated--")
    print(output)
    return output


def _import_example_outputs_from_excel():
    example_outputs = (pandas.read_excel(fpath.example_outputs)).fillna('')
    return example_outputs


def _import_example_outputs_from_snowflake():
    example_outputs = snowflake.query_snowflake_example_outputs()
    example_outputs = example_outputs.fillna('')
    return example_outputs


def import_example_outputs(mode: str):
    if mode == 'Excel':
        example_outputs = _import_example_outputs_from_excel()
    elif mode == 'Snowflake':
        example_outputs = _import_example_outputs_from_snowflake()
    else:
        print("Select Valid mode: Excel or Snowflake")
    return example_outputs


def create_example_output_objects(example_outputs: pandas.DataFrame):
    example_output_list = []
    for index, row in example_outputs.iterrows():
        example_output_item = example_output.ExampleOutput(example_id=row['ID'],
                                                           field=row['FIELD_NAME'],
                                                           category=row['CATEGORY'],
                                                           input_value=row['INPUT_VALUE'],
                                                           expected_result=row['EXPECTED_RESULT'],
                                                           client_id=row['CLIENT_ID'],
                                                           project_owner=row['PROJECT_OWNER'])
        example_output_list.append(example_output_item)
    return example_output_list


def create_example_cleaning_action_objects(example_output_list, regex_categories_list):
    id_ticker = 1
    cleaning_action_object_list = []
    for ExampleOutput in example_output_list:
        cleaning_action_object = cleaning_action.CleaningAction(id=id_ticker,
                                                                field=ExampleOutput.field,
                                                                field_value=ExampleOutput.input_value,
                                                                field_mapping='Example_Output_Test',
                                                                regex_categories=[x for x in regex_categories_list
                                                                                  if x.category == ExampleOutput.category],
                                                                example_output_expected_result=ExampleOutput.expected_result)
        cleaning_action_object_list.append(cleaning_action_object)
    return cleaning_action_object_list


def run_example_output_checks(mode, client_id, no_general_terms, output_location):
    regex_terms = import_regex_terms(mode)
    regex_terms_list = create_regex_term_objects(regex_terms)
    print(f"-- RegexTerms objects created--\n {regex_terms_list}")
    regex_category_list = generate_regex_categories(mode,
                                                    client_id,
                                                    no_general_terms,
                                                    regex_terms_list)
    print(f"-- Regex Categories objects created--\n {regex_category_list}")
    example_outputs = import_example_outputs(mode)
    example_output_list = create_example_output_objects(example_outputs)
    print(f"-- Example output objects created--\n {example_output_list}")
    cleaning_action_object_list = create_example_cleaning_action_objects(example_output_list, regex_category_list)
    print(f"-- Cleaning Action objects created -- \n {cleaning_action_object_list}")
    print(cleaning_action_object_list)
    output = execute_cleaning_actions(cleaning_action_object_list, True)
    print(f"-- Cleaning executed, output dataframe returned--\n")
    print(output)
    output.to_csv(output_location / "example_output_test.csv", index=False)
    total_example_outputs = len(output)
    print(f"Total example output checks: {total_example_outputs}")
    total_passes = len(output.loc[output['Test Result'] == "PASS"])
    print(f"Total PASS checks: {total_passes}")
    total_fails = len(output.loc[output['Test Result'] == "FAIL"])
    print(f"Total FAIL checks: {total_fails}")
    return output

