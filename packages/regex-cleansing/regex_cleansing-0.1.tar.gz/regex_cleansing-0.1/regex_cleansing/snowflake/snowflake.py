import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas
import config
import pandas as pd
from datetime import datetime
import os


def create_snowflake_connection():
    ctx = snowflake.connector.connect(user=config.sf_user,
                                      password=config.sf_password,
                                      account=config.sf_account,
                                      database=config.sf_database,
                                      warehouse=config.sf_warehouse,
                                      schema=config.sf_schema)
    return ctx


def create_snowflake_connection_with_cursor():
    ctx = snowflake.connector.connect(user=config.sf_user,
                                      password=config.sf_password,
                                      account=config.sf_account,
                                      database=config.sf_database,
                                      warehouse=config.sf_warehouse,
                                      schema=config.sf_schema)
    cs = ctx.cursor()
    return cs


def create_test_snowflake_connection():
    print('Attempting Snowflake connection test.')
    ctx = create_snowflake_connection()
    cs = ctx.cursor()
    try:
        cs.execute("SELECT current_version()")
        one_row = cs.fetchone()
        if '7.4.4' in one_row[0]:
            print('Snowflake connection established.')
        else:
            print('Snowflake connection error. Check connection status and connection version. Returned version = '
                  , str(one_row[0]))
    finally:
        cs.close()
        ctx.close()


def open_regex_terms_to_dataframe(input_file):
    regex_terms_df = pd.read_excel(input_file)
    return regex_terms_df


def open_regex_categories_to_dataframe(input_file):
    regex_categories = pd.read_excel(input_file)
    return regex_categories


def rename_regex_terms_dataframe_to_snowflake(regex_terms_df):
    #regex_terms_df['IS_CASESENSITIVE'] = regex_terms_df['IS_CASESENSITIVE'].apply(lambda x: True if 1 else False)
    #regex_terms_df['IS_FROM_START_OF_STRING'] = regex_terms_df['IS_FROM_START_OF_STRING'].apply(lambda x: True if 1 else False)
    #regex_terms_df['IS_FROM_END_OF_STRING'] = regex_terms_df['IS_FROM_END_OF_STRING'].apply(lambda x: True if 1 else False)
    #regex_terms_df['IS_PATTERN'] = regex_terms_df['IS_PATTERN'].apply(lambda x: True if 1 else False)
    #regex_terms_df['IS_ENCODING_ISSUE'] = regex_terms_df['IS_ENCODING_ISSUE'].apply(lambda x: True if 1 else False)
    # regex_terms_df['IS_CATEGORISATION_ONLY'] = regex_terms_df['IS_CATEGORISATION_ONLY'].apply(lambda x: True if 1 else False)
    return regex_terms_df


def query_snowflake_regex_terms():
    ctx = create_snowflake_connection()
    cs = ctx.cursor()
    try:
        sql = "select * from REGEX_TERMS"
        cs.execute(sql)
        snowflake_terms = cs.fetch_pandas_all()
    finally:
        cs.close()
    ctx.close()
    return snowflake_terms


def determine_new_regex_terms(input_file):
    regex_terms_df = open_regex_terms_to_dataframe(input_file)
    regex_terms_df = rename_regex_terms_dataframe_to_snowflake(regex_terms_df)
    snowflake_terms = query_snowflake_regex_terms()
    new_terms = regex_terms_df[~regex_terms_df['ID'].isin(snowflake_terms['ID'])]
    return new_terms


def determine_existing_regex_terms(input_file):
    regex_terms = open_regex_terms_to_dataframe(input_file)
    regex_terms = rename_regex_terms_dataframe_to_snowflake(regex_terms)
    snowflake_terms = query_snowflake_regex_terms()
    existing_terms = regex_terms[regex_terms['ID'].isin(snowflake_terms['ID'])]
    return existing_terms


def upload_new_regex_terms_to_snowflake(input_file):
    new_terms = determine_new_regex_terms(input_file)
    new_terms['DATE_ADDED'] = datetime.today().strftime('%Y-%m-%d')
    new_terms['LAST_UPDATED'] = datetime.today().strftime('%Y-%m-%d')
    ctx = create_snowflake_connection()
    cs = ctx.cursor()
    try:
        if len(new_terms) == 0:
            response = 'No New Regex Terms to populated to Snowflake Library.'
        else:
            response = write_pandas(ctx, new_terms, 'REGEX_TERMS')
    finally:
        cs.close()
    ctx.close()
    print(response)


def existing_regex_terms_in_snowflake(input_file):
    existing_terms = determine_existing_regex_terms(input_file)
    existing_terms['DATE_MODIFIED'] = datetime.today().strftime('%Y-%m-%d')
    existing_terms['LAST_UPDATED'] = datetime.today().strftime('%Y-%m-%d')


def upsert_regex_terms_to_snowflake(input_file):
    ctx = create_snowflake_connection()
    cs = ctx.cursor()

    regex_terms = open_regex_terms_to_dataframe(input_file)
    regex_terms = rename_regex_terms_dataframe_to_snowflake(regex_terms)

    #Update DATE for new
    snowflake_terms = query_snowflake_regex_terms()
    new_terms = regex_terms[~regex_terms['ID'].isin(snowflake_terms['ID'])]
    new_terms['DATE_ADDED'] = datetime.today().strftime('%Y-%m-%d')
    new_terms['LAST_UPDATED'] = datetime.today().strftime('%Y-%m-%d')
    new_terms = new_terms.drop(columns=['DATE_MODIFIED', 'DATE_REMOVED'])
    print("New Terms being inserted: " + str(len(new_terms)))
    #Update DATE for existing
    existing_terms = regex_terms[regex_terms['ID'].isin(snowflake_terms['ID'])]
    existing_terms['DATE_MODIFIED'] = datetime.today().strftime('%Y-%m-%d')
    existing_terms['LAST_UPDATED'] = datetime.today().strftime('%Y-%m-%d')
    existing_terms = existing_terms.drop(columns=['DATE_ADDED', 'DATE_REMOVED'])
    print("Existing Terms being inserted: " +str(len(existing_terms)))
    regex_terms = pd.concat([new_terms, existing_terms])
    #prepare json file for upload to staging
    filename = 'terms_staging.json'
    regex_terms.to_json(filename, orient='records', lines=True, date_unit='s')
    filepath = os.path.abspath(filename)
    #prepare sql for merging staging to production
    stage = 'REGEX_TERMS_STAGE'
    table = 'REGEX_TERMS'
    header_string = ','.join([f'$1:{col} as {col}' for col in regex_terms.columns])
    header_from_string = f'@{stage}/{filename}'
    on_string = f't.ID = {table}.ID'
    matched_field_string = ','.join(f'{col} = t.{col}' for col in regex_terms.columns.drop('DATE_ADDED'))
    not_matched_insert_string = ','.join(f'{col}' for col in regex_terms.columns)
    not_matched_values_string = ','.join(f't.{col}' for col in regex_terms.columns)
    #execute upload of json to staging and merging
    cs.execute(f"put file://{filepath} @{stage} overwrite=true;")
    merge_sql = f'MERGE INTO {table} USING (SELECT {header_string} FROM {header_from_string}) t ON {on_string} ' \
                f'WHEN MATCHED THEN UPDATE SET {matched_field_string} ' \
                f'WHEN NOT MATCHED THEN INSERT ({not_matched_insert_string}) VALUES ({not_matched_values_string});'
    cs.execute(merge_sql)
    #cleanup
    cs.execute(f'remove @{stage}/{filename};')
    os.remove(filename)
    cs.close()
    ctx.close()


def query_snowflake_regex_categories():
    ctx = create_snowflake_connection()
    cs = ctx.cursor()
    try:
        sql = "select * from REGEX_CATEGORY"
        cs.execute(sql)
        snowflake_terms = cs.fetch_pandas_all()
    finally:
        cs.close()
    ctx.close()
    return snowflake_terms


def upsert_regex_categories_to_snowflake(input_file):
    ctx = create_snowflake_connection()
    cs = ctx.cursor()
    regex_categories = open_regex_categories_to_dataframe(input_file)

    snowflake_categories = query_snowflake_regex_categories()
    #Update DATE for new
    new_categories = regex_categories[~regex_categories['ID'].isin(snowflake_categories['ID'])]
    new_categories['DATE_ADDED'] = datetime.today().strftime('%Y-%m-%d')
    new_categories['LAST_UPDATED'] = datetime.today().strftime('%Y-%m-%d')
    new_categories = new_categories.drop(columns=['DATE_MODIFIED', 'DATE_REMOVED'])
    print("New Terms being inserted: " + str(len(new_categories)))
    #Update DATE for existing
    existing_categories = regex_categories[regex_categories['ID'].isin(snowflake_categories['ID'])]
    existing_categories['DATE_MODIFIED'] = datetime.today().strftime('%Y-%m-%d')
    existing_categories['LAST_UPDATED'] = datetime.today().strftime('%Y-%m-%d')
    existing_categories = existing_categories.drop(columns=['DATE_ADDED', 'DATE_REMOVED'])
    print("Existing Terms being inserted: " + str(len(existing_categories)))
    regex_categories = pd.concat([new_categories, existing_categories])
    #prepare json file for upload to staging
    filename = 'categories_staging.json'
    regex_categories.to_json(filename, orient='records', lines=True, date_unit='s')
    filepath = os.path.abspath(filename)
    stage = 'REGEX_CATEGORY_STAGE'
    table = 'REGEX_CATEGORY'
    header_string = ','.join([f'$1:{col} as {col}' for col in regex_categories.columns])
    header_from_string = f'@{stage}/{filename}'
    on_string = f't.ID = {table}.ID'
    matched_field_string = ','.join(f'{col} = t.{col}' for col in regex_categories.columns.drop('DATE_ADDED'))
    not_matched_insert_string = ','.join(f'{col}' for col in regex_categories.columns)
    not_matched_values_string = ','.join(f't.{col}' for col in regex_categories.columns)
    #excute upload of json to staging and merging into production
    cs.execute(f"put file://{filepath} @{stage} overwrite=true;")
    merge_sql = f'MERGE INTO {table} USING (SELECT {header_string} FROM {header_from_string}) t ON {on_string} ' \
                f'WHEN MATCHED THEN UPDATE SET {matched_field_string} ' \
                f'WHEN NOT MATCHED THEN INSERT ({not_matched_insert_string}) VALUES ({not_matched_values_string});'
    print(merge_sql)
    cs.execute(merge_sql)
    # cleanup
    cs.execute(f'remove @{stage}/{filename};')
    os.remove(filename)
    cs.close()
    ctx.close()

    # -- add deleting terms

    # - import terms to delete
    # - create snowflake connection
    # - identify existing terms
    # - label identified terms with a deleted date

    # -- add deleting categories


def open_example_outputs_to_dataframe(input_file):
    example_outputs = pd.read_excel(input_file)
    return example_outputs


def query_snowflake_example_outputs():
    ctx = create_snowflake_connection()
    cs = ctx.cursor()
    try:
        sql = "select * from EXAMPLE_OUTPUTS"
        cs.execute(sql)
        snowflake_terms = cs.fetch_pandas_all()
    finally:
        cs.close()
    ctx.close()
    return snowflake_terms


def upsert_example_outputs_to_snowflake(input_file):
    ctx = create_snowflake_connection()
    cs = ctx.cursor()
    example_outputs = open_example_outputs_to_dataframe(input_file)

    snowflake_example_outputs = query_snowflake_example_outputs()
    #Update Date for new
    new_example_outputs = example_outputs[~example_outputs['ID'].isin(snowflake_example_outputs['ID'])]
    new_example_outputs['DATE_ADDED'] = datetime.today().strftime('%Y-%m-%d')
    new_example_outputs['LAST_UPDATED'] = datetime.today().strftime('%Y-%m-%d')
    new_example_outputs = new_example_outputs.drop(columns=['DATE_MODIFIED', 'DATE_REMOVED'])
    print("New Terms being inserted: " + str(len(new_example_outputs)))
    #Update DATE for existing
    existing_example_outputs = example_outputs[example_outputs['ID'].isin(snowflake_example_outputs['ID'])]
    existing_example_outputs['DATE_MODIFIED'] = datetime.today().strftime('%Y-%m-%d')
    existing_example_outputs['LAST_UPDATED'] = datetime.today().strftime('%Y-%m-%d')
    existing_example_outputs = existing_example_outputs.drop(columns=['DATE_ADDED', 'DATE_REMOVED'])
    print("Existing Terms being inserted: " + str(len(existing_example_outputs)))
    example_outputs = pd.concat([new_example_outputs, existing_example_outputs])
    #prepare json file for upload to staging
    filename = 'example_output_staging.json'
    example_outputs.to_json(filename, orient='records', lines=True, date_unit='s')
    filepath = os.path.abspath(filename)
    stage = 'EXAMPLE_OUTPUTS_STAGE'
    table = 'EXAMPLE_OUTPUTS'
    header_string = ','.join([f'$1:{col} as {col}' for col in example_outputs.columns])
    header_from_string = f'@{stage}/{filename}'
    on_string = f't.ID = {table}.ID'
    matched_field_string = ','.join(f'{col} = t.{col}' for col in example_outputs.columns.drop('DATE_ADDED'))
    not_matched_insert_string = ','.join(f'{col}' for col in example_outputs.columns)
    not_matched_values_string = ','.join(f't.{col}' for col in example_outputs.columns)
    # excute upload of json to staging and merging into production
    cs.execute(f"put file://{filepath} @{stage} overwrite=true;")
    merge_sql = f'MERGE INTO {table} USING (SELECT {header_string} FROM {header_from_string}) t ON {on_string} ' \
                f'WHEN MATCHED THEN UPDATE SET {matched_field_string} ' \
                f'WHEN NOT MATCHED THEN INSERT ({not_matched_insert_string}) VALUES ({not_matched_values_string});'
    print(merge_sql)
    cs.execute(merge_sql)
    # cleanup
    cs.execute(f'remove @{stage}/{filename};')
    os.remove(filename)
    cs.close()
    ctx.close()
