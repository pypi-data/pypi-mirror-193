import regex_cleansing.functions.functions as regex_fun
import regex_cleansing.interface.regex_manager as regex_manager
from pathlib import Path


def regex_library_clean(input_data: Path,
                        output_directory: Path,
                        field_mapping_document: Path,
                        field_column: str,
                        field_category_column: str,
                        mode: str = 'Snowflake',
                        client_id: str = None,
                        no_general_terms: bool = False):
    output = regex_fun.run_regex_cleansing(mode=mode,
                                           client_id=client_id,
                                           no_general_terms=no_general_terms,
                                           field_mapping_input=field_mapping_document,
                                           field_mapping_field_column=field_column,
                                           field_mapping_cleaning_category=field_category_column,
                                           input_file=input_data,
                                           output_location=output_directory)
    return output


def example_object_test(output_directory: Path,
                        mode: str = 'Snowflake',
                        client_id: str = None,
                        no_general_terms: str = None):

    output = regex_fun.run_example_output_checks(mode=mode,
                                                 client_id=client_id,
                                                 no_general_terms=no_general_terms,
                                                 output_location=output_directory)
    return output


def run_regex_library_manager():
    app = regex_manager.RegexManagerApp()
    app.mainloop()
