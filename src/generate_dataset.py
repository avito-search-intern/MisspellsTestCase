'''
Этим скриптом были сгенерированы данные для задания
python src/generate_dataset.py
'''
import numpy as np
import pandas as pd

df = pd.read_csv('data/misspell.tsv', '\t')
df['INPUT:diff1'] = df['INPUT:diff1'].fillna('nan')

rs = np.random.RandomState(0)
df['holdout'] = rs.uniform(0, 1, size=len(df)) < 0.2
df.loc[df['GOLDEN:result'].notnull(), 'holdout'] = True

df.loc[~df['holdout'], [
    'INPUT:diff1', 'INPUT:diff2', 'INPUT:query1', 'INPUT:query2',
    'OUTPUT:result', 'CONFIDENCE:result',
]].to_csv('data/dataset.tsv', '\t', index=False)

df.loc[df['holdout'], [
    'INPUT:diff1', 'INPUT:diff2', 'INPUT:query1', 'INPUT:query2',
]].to_csv('data/holdout.tsv', '\t', index=False)
