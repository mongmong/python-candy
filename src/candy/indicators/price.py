import collections
import numpy as np
import pandas as pd

from . import columns_to_transform, transform_ta

#
# indicators
#
def log_return(df, columns, window = 1, append = False, trans_methods = None):
    columns = columns_to_transform(df, columns)

    tmp0 = df[columns]
    tmp = np.log(tmp0 / tmp0.shift(window))

    ta_suffix = '_LOGRET;' + str(window)
    transformed = transform_ta(tmp0, tmp, ta_suffix, trans_methods)
    if append:
        return df.join(transformed)

    return transformed

def simple_return(df, columns, window = 1, append = False, trans_methods = None):
    columns = columns_to_transform(df, columns)

    tmp0 = df[columns]
    tmp = tmp0 / tmp0.shift(window) - 1

    ta_suffix = '_RET;' + str(window)
    transformed = transform_ta(tmp0, tmp, ta_suffix, trans_methods)
    if append:
        return df.join(transformed)

    return transformed

def price_rank(df, columns, window = '365d', win_type = None, append = False, trans_methods = None):
    columns = columns_to_transform(df, columns)

    tmp0 = df[columns]
    rolling = tmp0.rolling(window, win_type = win_type)
    rolling_min = rolling.min()
    rolling_max = rolling.max()
    tmp = (tmp0 - rolling_min) / (rolling_max - rolling_min)

    ta_suffix = '_PRANK;' + str(window)
    transformed = transform_ta(tmp0, tmp, ta_suffix, methods = None)
    if append:
        return df.join(transformed)

    return transformed

def price_percentile(df, columns, window = '365d', win_type = None, append = False, trans_methods = None):
    columns = columns_to_transform(df, columns)

    tmp0 = df[columns]
    # tmp = tmp0.rolling(window, win_type = win_type).aggregate(lambda x: len([e for e in x if e <= x[-1]]) / len(x))
    tmp = tmp0.rolling(window, win_type = win_type).aggregate(lambda x: np.sum(x <= x[-1]) / len(x))

    ta_suffix = '_PPCT;' + str(window)
    transformed = transform_ta(tmp0, tmp, ta_suffix, methods = None)
    if append:
        return df.join(transformed)

    return transformed
