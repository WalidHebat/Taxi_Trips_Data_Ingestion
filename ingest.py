import pandas as pd

from sqlalchemy import create_engine


dtype_mapping = {
    'column1': 'float',
    'column2': 'str',
    'column3': 'str',
    'column4': 'float',
    'column5': 'float',
    'column6': 'float',
    'column7': 'str',
    'column8': 'int',
    'column9': 'int',
    'column10': 'float',
    'column11': 'float',
    'column12': 'float',
    'column13': 'float',
    'column14': 'float',
    'column15': 'float',
    'column16': 'float',
    'column17': 'float',
    'column18': 'float',
}

# Read the CSV file with explicit data types
df = pd.read_csv('yellow_tripdata_2021_jan.csv', dtype=dtype_mapping, low_memory=False)


engine = create_engine('postgresql://root:root@pgdatabase:5432/big_data')

if(engine.connect()):
	print('connected succesfully')
else:
	print('failed to connect')


df.to_sql(name = 'trips',con = engine,if_exists='replace')

