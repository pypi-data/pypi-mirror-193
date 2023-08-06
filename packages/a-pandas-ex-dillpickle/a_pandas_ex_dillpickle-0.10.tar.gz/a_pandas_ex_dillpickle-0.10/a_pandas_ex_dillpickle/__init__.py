import os
from touchtouch import touch
from dill import dumps, loads

import pandas as pd
from pandas.core.frame import DataFrame, Series

def to_pickle_dill(df, path):
    dumped = dumps(df)
    touch(path)
    with open(path, mode='wb') as f:
        f.write(dumped)


def read_pickle_dill(pkl):
    if isinstance(pkl,str):
        if os.path.exists(pkl):
            with open(pkl, mode='rb') as f:
                pkl =f.read()
    return loads(pkl)

def pd_add_dillpickle():
    DataFrame.to_dillpickle = to_pickle_dill
    Series.to_dillpickle = to_pickle_dill
    pd.read_dillpickle = read_pickle_dill


