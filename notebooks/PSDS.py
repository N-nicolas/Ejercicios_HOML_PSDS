# %% Cell 0
from pathlib import Path
import pandas as pd
import numpy as np
from scipy import stats
from sklearn.utils import resample

import seaborn as sns
import matplotlib.pyplot as plt

# %% Cell 1
DATA = Path('..') / 'data'
LOANS_INCOME_CSV = DATA / 'loans_income.csv'
SP500_DATA_CSV = DATA / 'sp500_data.csv.gz'


# %% Cell 2
df = pd.read_csv(LOANS_INCOME_CSV)
df.head()


# %% Cell 3
sample_data = pd.DataFrame({
    'income': df.sample(1000).x,
    'type': 'Data',
})

mean_5 = pd.DataFrame({
    'income': [df.sample(5).x.mean() for _ in range(1000)],
    'type': 'mean 5'
})

mean_20 = pd.DataFrame({
    'income': [df.sample(20).x.mean() for _ in range(1000)],
    'type': 'mean 20'
})

results = pd.concat([sample_data, mean_5, mean_20])

g = sns.FacetGrid(results, col='type', col_wrap=1,
                  height=2, aspect=2)
g.map(plt.hist, 'income', bins=20)
g.set_axis_labels('Income', 'Count')
g.set_titles('{col_name}')

plt.tight_layout()
plt.show()
