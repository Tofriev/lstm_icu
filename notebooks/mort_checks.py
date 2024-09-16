#%%
import os
import sys
import pandas as pd


project_root = os.path.abspath(os.path.join(os.getcwd(), ".."))
sys.path.append(project_root)

m = pd.read_csv(os.path.join(project_root, 'data/raw/mimiciv/mort_new.csv'))
m2 = pd.read_csv(os.path.join(project_root, 'data/raw/mimiciv/mort2.csv'))

#%%
print(f'length of data: {len(m)}')
m.drop_duplicates(inplace=True)
print(f'length of data after dropping duplicates: {len(m)}')

print(f'length of data: {len(m2)}')
m2.drop_duplicates(inplace=True)
print(f'length of data after dropping duplicates: {len(m2)}')