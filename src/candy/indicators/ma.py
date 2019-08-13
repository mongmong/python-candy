import collections
import numpy as np
import pandas as pd

from . import columns_to_transform, transform_ta



def moving_min(df, columns, window = '365d', win_type = None, append = False, trans_methods = None):
    columns = columns_to_transform(df, columns)

    tmp0 = df[columns]
    tmp = tmp0.rolling(window, win_type = win_type).min()

    ta_suffix = '_SMMIN;' + str(window)
    transformed = transform_ta(tmp0, tmp, ta_suffix, methods = None)
    if append:
        return df.join(transformed)

    return transformed

def moving_max(df, columns, window = '365d', win_type = None, append = False, trans_methods = None):
    columns = columns_to_transform(df, columns)

    tmp0 = df[columns]
    tmp = tmp0.rolling(window, win_type = win_type).max()

    ta_suffix = '_SMMAX;' + str(window)
    transformed = transform_ta(tmp0, tmp, ta_suffix, methods = None)
    if append:
        return df.join(transformed)

    return transformed

def moving_average(df, columns, window = 10, win_type = None, append = False, trans_methods = None):
    columns = columns_to_transform(df, columns)

    tmp0 = df[columns]
    tmp = tmp0.rolling(window, win_type = win_type).mean()

    ta_suffix = '_SMA;' + str(window)
    transformed = transform_ta(tmp0, tmp, ta_suffix, trans_methods)
    if append:
        return df.join(transformed)

    return transformed

def moving_standard_deviation(df, columns, window = 10, win_type = None, append = False, trans_methods = None):
    columns = columns_to_transform(df, columns)

    tmp0 = df[columns]
    tmp = tmp0.rolling(window, win_type = win_type).std()

    ta_suffix = '_SMSTD;' + str(window)
    transformed = transform_ta(tmp0, tmp, ta_suffix, trans_methods)
    if append:
        return df.join(transformed)

    return transformed

def exponential_moving_average(df, columns, window = 10, append = False, trans_methods = None):
    columns = columns_to_transform(df, columns)

    tmp0 = df[columns]
    tmp = tmp0.ewm(span = window, adjust = False).mean()

    ta_suffix = '_EMA;' + str(window)
    transformed = transform_ta(tmp0, tmp, ta_suffix, trans_methods)
    if append:
        return df.join(transformed)

    return transformed

def exponential_standard_deviation(df, columns, window = 10, append = False, trans_methods = None):
    columns = columns_to_transform(df, columns)

    tmp0 = df[columns]
    tmp = tmp0.ewm(span = window, adjust = False).std()

    ta_suffix = '_EMSTD;' + str(window)
    transformed = transform_ta(tmp0, tmp, ta_suffix, trans_methods)
    if append:
        return df.join(transformed)

    return transformed

def weighted_moving_average(df, columns, window = 10, win_type = None, append = False, trans_methods = None):
    columns = columns_to_transform(df, columns)

    tmp0 = df[columns]
    weights = range(1, window + 1)
    sum_weights = np.sum(weights)
    tmp = tmp0.rolling(window, win_type = win_type).aggregate(lambda x: np.dot(x, weights) / sum_weights)

    ta_suffix = '_WMA;' + str(window)
    transformed = transform_ta(tmp0, tmp, ta_suffix, trans_methods)
    if append:
        return df.join(transformed)

    return transformed

