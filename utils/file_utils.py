import os
import pandas as pd
import uuid


def read_file(file, **kwargs):
    read_map = {'xls': pd.read_excel, 'xlsx': pd.read_excel, 'csv': pd.read_csv,
                'gz': pd.read_csv, 'pkl': pd.read_pickle}

    ext = os.path.splitext(file.name)[1].lower()[1:]

    if ext not in read_map:
        raise Exception(f"Input file not in correct format, must be xls, xlsx, csv, csv.gz, pkl; current format '{ext}'")

    df = read_map[ext](file, **kwargs)
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')
    return df


def get_table_name(file):
    filename = os.path.splitext(file.name)[0].lower()
    return "%s_%s" % (filename, uuid.uuid4().hex)
