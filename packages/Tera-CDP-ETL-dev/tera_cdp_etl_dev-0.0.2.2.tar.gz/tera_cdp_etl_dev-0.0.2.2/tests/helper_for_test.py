import os
import tera_etl

def delete_file(path):
    if os.path.exists(path):
        os.remove(path)


def output_file_path():
    return f'{tera_etl.root}/tera_etl/output'


def test_data_folder():
    return f'{tera_etl.root}/tests/data'