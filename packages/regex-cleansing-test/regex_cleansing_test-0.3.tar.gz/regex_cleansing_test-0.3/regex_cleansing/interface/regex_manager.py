import tkinter as tk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from regex_cleansing.snowflake import manager_functions as mf
import pandas
import filepaths as fpath
from datetime import datetime


class RegexManagerApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage,
                  RetrieveLibrary,
                  BulkUpsert,
                  UploadTerms,
                  UploadCategories,
                  UploadExamples,
                  SingletonMenu,
                  SingletonTerm,
                  SingletonCategory,
                  SingletonExample):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky='nsew')
        self.show_frame("StartPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text='Welcome to the Regex Library Manager. Please select an option from below to get'
                                    'started')
        label.pack(side="top", fill="x", pady=10)
        button_retrieve = tk.Button(self, text="Retrieve Library from Snowflake",
                                    command=lambda: controller.show_frame("RetrieveLibrary"))
        button_bulk_upsert = tk.Button(self, text="Bulk upsert to Snowflake",
                                       command=lambda: controller.show_frame("BulkUpsert"))
        button_singleton_upsert = tk.Button(self, text="Singleton upserts",
                                            command=lambda: controller.show_frame("SingletonMenu"))
        button_retrieve.pack()
        button_bulk_upsert.pack()
        button_singleton_upsert.pack()


class RetrieveLibrary(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text='RetrieveLibrary')
        label.pack(side="top", fill="x", pady=10)
        retrieval_directory = tk.StringVar()
        directory_selection_button = tk.Button(self, text='Select an Output Directory',
                                               command=lambda: retrieval_directory.set(self.retrieval_directory_selection(directory_selection_label)))
        directory_selection_label = tk.Label(self, text='None')
        execute_retrieval_button = tk.Button(self, text='Execute Retrieval',
                                             command=lambda: self.execute_retrieval(retrieval_directory))
        back_button = tk.Button(self, text='Back',
                                command=lambda: controller.show_frame("StartPage"))
        directory_selection_button.pack()
        directory_selection_label.pack()
        execute_retrieval_button.pack()
        back_button.pack()

    def execute_retrieval(self, retrieval_directory):
        directory = retrieval_directory.get()
        mf.retrieve_snowflake_library(directory)

    def retrieval_directory_selection(self, label):
        directory = fd.askdirectory()
        showinfo(title='Selected Directory:',
                 message=directory)
        label.configure(text=directory)
        print(directory)
        print(str(directory))
        return directory


class BulkUpsert(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text='Select a table to upsert to')
        label.pack(side="top", fill="x", pady=10)

        button_terms = tk.Button(self, text='Regex Terms',
                                 command=lambda: controller.show_frame("UploadTerms"))
        button_categories = tk.Button(self, text='Regex Categories',
                                      command=lambda: controller.show_frame("UploadCategories"))
        button_examples = tk.Button(self, text='Example Outputs',
                                    command=lambda: controller.show_frame("UploadExamples"))
        back_button = tk.Button(self, text='Back',
                                command=lambda: controller.show_frame("StartPage"))
        button_terms.pack()
        button_categories.pack()
        button_examples.pack()
        back_button.pack()


class UploadTerms(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text='Upserting Regex Terms')
        label.pack(side="top", fill="x", pady=10)
        file_name = tk.StringVar()
        file_selection_button = tk.Button(self, text='Select a Regex Terms file for upsert',
                                          command=lambda: self.select_file_for_upsert(file_label,
                                                                                      file_upsert_button,
                                                                                      file_name))
        file_label = tk.Label(self, text='None')
        file_upsert_button = tk.Button(self, text='Upsert', state=tk.DISABLED,
                                       command=lambda: self.upsert_file(file_name))
        back_button = tk.Button(self, text='Back',
                                command=lambda: controller.show_frame("BulkUpsert"))
        file_selection_button.pack()
        file_label.pack()
        file_upsert_button.pack()
        back_button.pack()

    def select_file_for_upsert(self, label, upsert_button, file_name_var):
        file = fd.askopenfilename(
            title='Select a file',
            initialdir='/')
        showinfo(title='File Selected:',
                 message=file)
        label.configure(text=file)
        file_name_var.set(file)
        upsert_button['state'] = tk.NORMAL
        return file

    def upsert_file(self, file_name_var):
        mf.upsert_regex_terms_to_snowflake(file_name_var.get())
        print("Upserted Regex Term File")


class UploadCategories(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text='Upserting Regex Categories')
        label.pack(side="top", fill="x", pady=10)
        file_name = tk.StringVar()
        file_selection_button = tk.Button(self, text='Select a Regex Categories file for upsert',
                                          command=lambda: self.select_file_for_upsert(file_label,
                                                                                      file_upsert_button,
                                                                                      file_name))
        file_label = tk.Label(self, text='None')
        file_upsert_button = tk.Button(self, text='Upsert', state=tk.DISABLED,
                                       command=lambda: self.upsert_file(file_name))
        back_button = tk.Button(self, text='Back',
                                command=lambda: controller.show_frame("BulkUpsert"))
        file_selection_button.pack()
        file_label.pack()
        file_upsert_button.pack()
        back_button.pack()

    def select_file_for_upsert(self, label, upsert_button, file_name_var):
        file = fd.askopenfilename(
            title='Select a file',
            initialdir='/')
        showinfo(title='File Selected:',
                 message=file)
        label.configure(text=file)
        file_name_var.set(file)
        upsert_button['state'] = tk.NORMAL
        return file

    def upsert_file(self, file_name_var):
        mf.upsert_regex_categories_to_snowflake(file_name_var.get())
        print("Upserted Regex Categories File")


class UploadExamples(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text='Upserting Example Outputs')
        label.pack(side="top", fill="x", pady=10)
        file_name = tk.StringVar()
        file_selection_button = tk.Button(self, text='Select an Example Output file for upsert',
                                          command=lambda: self.select_file_for_upsert(file_label,
                                                                                      file_upsert_button,
                                                                                      file_name))
        file_label = tk.Label(self, text='None')
        file_upsert_button = tk.Button(self, text='Upsert', state=tk.DISABLED,
                                       command=lambda: self.upsert_file(file_name))

        back_button = tk.Button(self, text='Back',
                                command=lambda: controller.show_frame("BulkUpsert"))
        file_selection_button.pack()
        file_label.pack()
        file_upsert_button.pack()
        back_button.pack()

    def select_file_for_upsert(self, label, upsert_button, file_name_var):
        file = fd.askopenfilename(
            title='Select a file',
            initialdir='/')
        showinfo(title='File Selected:',
                 message=file)
        label.configure(text=file)
        file_name_var.set(file)
        upsert_button['state'] = tk.NORMAL
        return file

    def upsert_file(self, file_name_var):
        mf.upsert_example_outputs_to_snowflake(file_name_var.get())
        print("Upserted Example Outputs File")


class SingletonMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text='Select an library object type')
        label.pack(side="top", fill="x", pady=10)
        button_terms = tk.Button(self, text='Regex Terms',
                                 command=lambda: controller.show_frame("SingletonTerm"))
        button_categories = tk.Button(self, text='Regex Categories',
                                      command=lambda: controller.show_frame("SingletonCategory"))
        button_examples = tk.Button(self, text='Example Outputs',
                                    command=lambda: controller.show_frame("SingletonExample"))
        back_button = tk.Button(self, text='Back',
                                command=lambda: controller.show_frame("StartPage"))
        button_terms.pack()
        button_categories.pack()
        button_examples.pack()
        back_button.pack()


class SingletonTerm(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text='Upserting a single change')
        label.pack(side="top", fill="x", pady=10)
        row_max_value = tk.IntVar()
        source_field_value = tk.StringVar()
        search_term_value = tk.StringVar()
        match_output_value = tk.StringVar()
        pattern_match_value = tk.StringVar()
        project_owner_value = tk.StringVar()
        regex_categories_value = tk.StringVar()
        is_case_sensitive_value = tk.IntVar()
        is_categorisation_value = tk.IntVar()
        is_encoding_value = tk.IntVar()
        is_from_start_of_string_value = tk.IntVar()
        is_from_end_of_string_value = tk.IntVar()
        is_pattern_check_value = tk.IntVar()
        source_field_label = tk.Label(self, text='Source Field')
        source_field_entry = tk.Entry(self, textvariable=source_field_value)
        search_term_label = tk.Label(self, text='Search Term')
        search_term_entry = tk.Entry(self, textvariable=search_term_value)
        match_output_label = tk.Label(self, text='Match Output Value')
        match_output_entry = tk.Entry(self, textvariable=match_output_value)
        pattern_match_label = tk.Label(self, text='Pattern Match Value')
        pattern_match_entry = tk.Entry(self, textvariable=pattern_match_value)
        project_owner_label = tk.Label(self, text='Project Owner')
        project_owner_entry = tk.Entry(self, textvariable=project_owner_value)
        is_case_sensitive_checkbox = tk.Checkbutton(self, text='Is Case Sensitive',
                                                    onvalue=1, offvalue=0,
                                                    variable=is_case_sensitive_value)
        is_categorisation_checkbox = tk.Checkbutton(self, text='Is Categorisation', onvalue=1, offvalue=0,
                                                    variable=is_categorisation_value)
        is_encoding_issue_checkbox = tk.Checkbutton(self, text='Is Encoding Issue', onvalue=1, offvalue=0,
                                                    variable=is_encoding_value)
        is_from_start_of_string_checkbox = tk.Checkbutton(self, text='From Start of String', onvalue=1, offvalue=0,
                                                          variable=is_from_start_of_string_value)
        is_from_end_of_string_checkbox = tk.Checkbutton(self, text='From End of String', onvalue=1, offvalue=0,
                                                        variable=is_from_end_of_string_value)
        is_pattern_check_checkbox = tk.Checkbutton(self, text='Is Pattern Check', onvalue=1, offvalue=0,
                                                   variable=is_pattern_check_value)
        regex_category_label = tk.Label(self, text='Regex Categories (list)')
        regex_category_entry = tk.Entry(self, textvariable=regex_categories_value)
        back_button = tk.Button(self, text='Back',
                                command=lambda: controller.show_frame("SingletonMenu"))
        check_term_button = tk.Button(self, text='Check Term',
                                      command=lambda: self.check_regex_term(create_term_button,
                                                                            upsert_term_button,
                                                                            reactivate_term_button,
                                                                            delete_button,
                                                                            search_term_value,
                                                                            row_max_value))
        create_term_button = tk.Button(self, text='Create Term', state=tk.DISABLED,
                                       command=lambda: self.upsert_regex_term(source_field_value,
                                                                              search_term_value,
                                                                              match_output_value,
                                                                              pattern_match_value,
                                                                              project_owner_value,
                                                                              is_case_sensitive_value,
                                                                              is_categorisation_value,
                                                                              is_encoding_value,
                                                                              is_from_start_of_string_value,
                                                                              is_from_end_of_string_value,
                                                                              is_pattern_check_value,
                                                                              row_max_value))
        upsert_term_button = tk.Button(self, text='Upsert Term', state=tk.DISABLED,
                                       command=lambda: self.upsert_regex_term(source_field_value,
                                                                              search_term_value,
                                                                              match_output_value,
                                                                              pattern_match_value,
                                                                              project_owner_value,
                                                                              is_case_sensitive_value,
                                                                              is_categorisation_value,
                                                                              is_encoding_value,
                                                                              is_from_start_of_string_value,
                                                                              is_from_end_of_string_value,
                                                                              is_pattern_check_value,
                                                                              row_max_value))
        reactivate_term_button = tk.Button(self, text='Re-activate Term', state=tk.DISABLED,
                                           command=lambda: self.reactivate_regex_term(source_field_value,
                                                                              search_term_value,
                                                                              match_output_value,
                                                                              pattern_match_value,
                                                                              project_owner_value,
                                                                              is_case_sensitive_value,
                                                                              is_categorisation_value,
                                                                              is_encoding_value,
                                                                              is_from_start_of_string_value,
                                                                              is_from_end_of_string_value,
                                                                              is_pattern_check_value,
                                                                              row_max_value))
        delete_button = tk.Button(self, text='Delete Term', state=tk.DISABLED,
                                  command=lambda: self.delete_regex_term(source_field_value,
                                                                              search_term_value,
                                                                              match_output_value,
                                                                              pattern_match_value,
                                                                              project_owner_value,
                                                                              is_case_sensitive_value,
                                                                              is_categorisation_value,
                                                                              is_encoding_value,
                                                                              is_from_start_of_string_value,
                                                                              is_from_end_of_string_value,
                                                                              is_pattern_check_value,
                                                                              row_max_value))
        source_field_label.pack()
        source_field_entry.pack()
        search_term_label.pack()
        search_term_entry.pack()
        match_output_label.pack()
        match_output_entry.pack()
        pattern_match_label.pack()
        pattern_match_entry.pack()
        project_owner_label.pack()
        project_owner_entry.pack()
        is_case_sensitive_checkbox.pack()
        is_categorisation_checkbox.pack()
        is_encoding_issue_checkbox.pack()
        is_from_start_of_string_checkbox.pack()
        is_from_end_of_string_checkbox.pack()
        is_pattern_check_checkbox.pack()
        regex_category_label.pack()
        regex_category_entry.pack()
        back_button.pack()
        check_term_button.pack()
        create_term_button.pack()
        upsert_term_button.pack()
        reactivate_term_button.pack()
        delete_button.pack()

    def check_regex_term(self, create_button, upsert_button, reactivation_button, delete_button, term_var, max_var):
        create_button['state'] = tk.DISABLED
        upsert_button['state'] = tk.DISABLED
        reactivation_button['state'] = tk.DISABLED
        delete_button['state'] = tk.DISABLED
        existing_terms = mf.check_snowflake_terms(term_var.get())
        if len(existing_terms) == 0:
            create_button['state'] = tk.NORMAL
            print("No existing term found - create?")
            max_var.set(mf.get_max_row_id_regex_terms() + 1)
        elif len(existing_terms.loc[existing_terms['DATE_REMOVED'].notnull()]) != 0:
            print(existing_terms.loc[existing_terms['DATE_REMOVED'].notnull()])
            reactivation_button['state'] = tk.NORMAL
            print("Matching deactivated term found - reactivate?")
            max_var.set(existing_terms['ID'].max())
            print(f"Matched Rule ID: {max_var.get()}")
        else:
            upsert_button['state'] = tk.NORMAL
            delete_button['state'] = tk.NORMAL
            print("Existing term found - upsert?")
            max_var.set(existing_terms['ID'].max())
            print(f"Matched Rule ID: {max_var.get()}")

    def upsert_regex_term(self, source_field_var, search_term_var, match_output_var, pattern_match_var,
                          project_owner_var, is_case_sensitive_checkbox, is_categorisation_checkbox,
                          is_encoding_issue_checkbox,
                          is_from_start_of_string_checkbox, is_from_end_of_string_checkbox,
                          is_pattern_check_checkbox, max_row_var):
        print("This should upsert regex term from snowflake database.")
        upsert_data = [[source_field_var.get(), search_term_var.get(), match_output_var.get(), pattern_match_var.get(),
                       project_owner_var.get(), is_case_sensitive_checkbox.get(),
                       is_categorisation_checkbox.get(),
                       is_encoding_issue_checkbox.get(), is_from_start_of_string_checkbox.get(),
                       is_from_end_of_string_checkbox.get(), is_pattern_check_checkbox.get(),
                       max_row_var.get()]]
        print(upsert_data)
        upsert_df = pandas.DataFrame(upsert_data, columns=['SOURCE_FIELD', 'SEARCH_TERM', 'MATCH_OUTPUT_VALUE',
                                                           'PATTERN_OUTPUT_VALUE', 'PROJECT_OWNER', 'IS_CASESENSITIVE',
                                                           'IS_CATEGORISATION_ONLY',
                                                           'IS_ENCODING_ISSUE', 'IS_FROM_START_OF_STRING',
                                                           'IS_FROM_END_OF_STRING', 'IS_PATTERN', 'ID'])
        upsert_df['DATE_ADDED'] = None
        upsert_df['DATE_MODIFIED'] = None
        upsert_df['DATE_REMOVED'] = None
        upsert_df['LAST_UPDATED'] = None
        upsert_df['IS_CASESENSITIVE'] = upsert_df['IS_CASESENSITIVE'].apply(lambda x: True if x == 1 else False)
        upsert_df['IS_CATEGORISATION_ONLY'] = upsert_df['IS_CATEGORISATION_ONLY'].apply(lambda x: True if x == 1 else False)
        upsert_df['IS_ENCODING_ISSUE'] = upsert_df['IS_ENCODING_ISSUE'].apply(lambda x: True if x == 1 else False)
        upsert_df['IS_FROM_START_OF_STRING'] = upsert_df['IS_FROM_START_OF_STRING'].apply(lambda x: True if x == 1 else False)
        upsert_df['IS_FROM_END_OF_STRING'] = upsert_df['IS_FROM_END_OF_STRING'].apply(lambda x: True if x == 1 else False)
        upsert_df['IS_PATTERN'] = upsert_df['IS_PATTERN'].apply(lambda x: True if x == 1 else False)
        mf.singleton_upsert_regex_terms_to_snowflake(upsert_df, deletion=False, reactivation=False)


    def delete_regex_term(self, source_field_var, search_term_var, match_output_var, pattern_match_var,
                          project_owner_var, is_case_sensitive_checkbox, is_categorisation_checkbox,
                          is_encoding_issue_checkbox,
                          is_from_start_of_string_checkbox, is_from_end_of_string_checkbox,
                          is_pattern_check_checkbox, max_row_var):
        print("This should upsert regex term from snowflake database.")
        upsert_data = [[source_field_var.get(), search_term_var.get(), match_output_var.get(), pattern_match_var.get(),
                       project_owner_var.get(), is_case_sensitive_checkbox.get(),
                       is_categorisation_checkbox.get(),
                       is_encoding_issue_checkbox.get(), is_from_start_of_string_checkbox.get(),
                       is_from_end_of_string_checkbox.get(), is_pattern_check_checkbox.get(),
                       max_row_var.get()]]
        print(upsert_data)
        upsert_df = pandas.DataFrame(upsert_data, columns=['SOURCE_FIELD', 'SEARCH_TERM', 'MATCH_OUTPUT_VALUE',
                                                           'PATTERN_OUTPUT_VALUE', 'PROJECT_OWNER', 'IS_CASESENSITIVE',
                                                           'IS_CATEGORISATION_ONLY',
                                                           'IS_ENCODING_ISSUE', 'IS_FROM_START_OF_STRING',
                                                           'IS_FROM_END_OF_STRING', 'IS_PATTERN', 'ID'])
        upsert_df['DATE_ADDED'] = None
        upsert_df['DATE_MODIFIED'] = None
        upsert_df['DATE_REMOVED'] = datetime.today().strftime('%Y-%m-%d')
        upsert_df['LAST_UPDATED'] = None
        upsert_df['IS_CASESENSITIVE'] = upsert_df['IS_CASESENSITIVE'].apply(lambda x: True if x == 1 else False)
        upsert_df['IS_CATEGORISATION_ONLY'] = upsert_df['IS_CATEGORISATION_ONLY'].apply(lambda x: True if x == 1 else False)
        upsert_df['IS_ENCODING_ISSUE'] = upsert_df['IS_ENCODING_ISSUE'].apply(lambda x: True if x == 1 else False)
        upsert_df['IS_FROM_START_OF_STRING'] = upsert_df['IS_FROM_START_OF_STRING'].apply(lambda x: True if x == 1 else False)
        upsert_df['IS_FROM_END_OF_STRING'] = upsert_df['IS_FROM_END_OF_STRING'].apply(lambda x: True if x == 1 else False)
        upsert_df['IS_PATTERN'] = upsert_df['IS_PATTERN'].apply(lambda x: True if x == 1 else False)
        mf.singleton_upsert_regex_terms_to_snowflake(upsert_df, deletion=True, reactivation=False)


    def reactivate_regex_term(self, source_field_var, search_term_var, match_output_var, pattern_match_var,
                              project_owner_var, is_case_sensitive_checkbox, is_categorisation_checkbox,
                              is_encoding_issue_checkbox,
                              is_from_start_of_string_checkbox, is_from_end_of_string_checkbox,
                              is_pattern_check_checkbox, max_row_var):
        print("This should upsert regex term from snowflake database.")
        upsert_data = [[source_field_var.get(), search_term_var.get(), match_output_var.get(), pattern_match_var.get(),
                       project_owner_var.get(), is_case_sensitive_checkbox.get(),
                       is_categorisation_checkbox.get(),
                       is_encoding_issue_checkbox.get(), is_from_start_of_string_checkbox.get(),
                       is_from_end_of_string_checkbox.get(), is_pattern_check_checkbox.get(),
                       max_row_var.get()]]
        print(upsert_data)
        upsert_df = pandas.DataFrame(upsert_data, columns=['SOURCE_FIELD', 'SEARCH_TERM', 'MATCH_OUTPUT_VALUE',
                                                           'PATTERN_OUTPUT_VALUE', 'PROJECT_OWNER', 'IS_CASESENSITIVE',
                                                           'IS_CATEGORISATION_ONLY',
                                                           'IS_ENCODING_ISSUE', 'IS_FROM_START_OF_STRING',
                                                           'IS_FROM_END_OF_STRING', 'IS_PATTERN', 'ID'])
        upsert_df['DATE_ADDED'] = None
        upsert_df['DATE_MODIFIED'] = None
        upsert_df['DATE_REMOVED'] = datetime.today().strftime('%Y-%m-%d')
        upsert_df['LAST_UPDATED'] = None
        upsert_df['IS_CASESENSITIVE'] = upsert_df['IS_CASESENSITIVE'].apply(lambda x: True if x == 1 else False)
        upsert_df['IS_CATEGORISATION_ONLY'] = upsert_df['IS_CATEGORISATION_ONLY'].apply(lambda x: True if x == 1 else False)
        upsert_df['IS_ENCODING_ISSUE'] = upsert_df['IS_ENCODING_ISSUE'].apply(lambda x: True if x == 1 else False)
        upsert_df['IS_FROM_START_OF_STRING'] = upsert_df['IS_FROM_START_OF_STRING'].apply(lambda x: True if x == 1 else False)
        upsert_df['IS_FROM_END_OF_STRING'] = upsert_df['IS_FROM_END_OF_STRING'].apply(lambda x: True if x == 1 else False)
        upsert_df['IS_PATTERN'] = upsert_df['IS_PATTERN'].apply(lambda x: True if x == 1 else False)
        mf.singleton_upsert_regex_terms_to_snowflake(upsert_df, deletion=False, reactivation=True)


class SingletonCategory(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text='Upserting a single change')
        label.pack(side="top", fill="x", pady=10)
        category_entry_value = tk.StringVar()
        client_entry_value = tk.StringVar()
        regex_terms_value = tk.StringVar()
        project_owner_value = tk.StringVar()
        row_max_id = tk.IntVar()
        category_label = tk.Label(self, text='Category')
        category_entry = tk.Entry(self, textvariable=category_entry_value)
        client_id_label = tk.Label(self, text='Client ID')
        client_id_entry = tk.Entry(self, textvariable=client_entry_value)
        regex_terms_label = tk.Label(self, text='Regex Terms (List)')
        regex_terms_entry = tk.Entry(self, textvariable=regex_terms_value)
        project_owner_label = tk.Label(self, text='Project Owner')
        project_owner_entry = tk.Entry(self, textvariable=project_owner_value)
        back_button = tk.Button(self, text='Back',
                                command=lambda: controller.show_frame("SingletonMenu"))
        check_button = tk.Button(self, text='Check',
                                command=lambda: self.check_regex_category(create_button,
                                                                          upsert_button,
                                                                          reactivate_button,
                                                                          delete_button,
                                                                          category_entry_value,
                                                                          row_max_id))
        create_button = tk.Button(self, text='Create', state=tk.DISABLED,
                                  command=lambda: self.create_regex_category)
        upsert_button = tk.Button(self, text='Upsert', state=tk.DISABLED,
                                  command=lambda: self.upsert_regex_category)
        reactivate_button = tk.Button(self, text='Reactivate', state=tk.DISABLED,
                                      command=lambda: self.reactivate_regex_category)
        delete_button = tk.Button(self, text='Delete', state=tk.DISABLED,
                                  command=lambda: self.delete_regex_category)
        category_label.pack()
        category_entry.pack()
        client_id_label.pack()
        client_id_entry.pack()
        regex_terms_label.pack()
        regex_terms_entry.pack()
        project_owner_label.pack()
        project_owner_entry.pack()
        back_button.pack()
        check_button.pack()

    def check_regex_category(self, create_button, upsert_button, reactivation_button, delete_button, category, max_var):
        create_button['state'] = tk.DISABLED
        upsert_button['state'] = tk.DISABLED
        reactivation_button['state'] = tk.DISABLED
        delete_button['state'] = tk.DISABLED
        existing_categories = mf.check_snowflake_categories(category.get())
        if len(existing_categories) == 0:
            create_button['state'] = tk.NORMAL
            print("No existing term found - create?")
            max_var.set(mf.get_max_row_id_regex_category() + 1)
        elif len(existing_categories.loc[existing_categories['DATE_REMOVED'].notnull()]) != 0:
            print(existing_categories.loc[existing_categories['DATE_REMOVED'].notnull()])
            reactivation_button['state'] = tk.NORMAL
            print("Matching deactivated term found - reactivate?")
            max_var.set(existing_categories['ID'].max())
            print(f"Matched Rule ID: {max_var.get()}")
        else:
            upsert_button['state'] = tk.NORMAL
            delete_button['state'] = tk.NORMAL
            print("Existing term found - upsert?")
            max_var.set(existing_categories['ID'].max())
            print(f"Matched Rule ID: {max_var.get()}")


    def create_regex_category(self):
        pass
    def upsert_regex_category(self):
        pass
    def reactivate_regex_category(self):
        pass
    def delete_regex_category(self):
        pass


class SingletonExample(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text='Upserting a single change')
        label.pack(side="top", fill="x", pady=10)


if __name__ == "__main__":
    app = RegexManagerApp()
    app.mainloop()
