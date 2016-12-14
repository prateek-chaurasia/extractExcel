import json
import os
import pandas as pd

with open('config.json', 'rU') as data_file:
	data = json.loads(data_file.read())

FILE_DIR = data.get('FILE_DIR')
LOGS_DIR = data.get('ERROR_LOG_DIR')
EMP_TABLE_COLS = data.get('DB_COLUMN_MAPPING').keys()

FILE_PATH = os.path.join(FILE_DIR, 'data_dump.csv')

emp_records = pd.read_csv(FILE_PATH, sep=",", names=EMP_TABLE_COLS, encoding='UTF-8')
