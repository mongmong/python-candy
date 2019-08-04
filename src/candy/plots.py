
import numpy as np
import pandas as pd

def format_plot(fig, **kwargs):
    if 'title' in kwargs and kwargs['title']:
        fig.set_title(kwargs['title'])
    if 'ylabel' in kwargs and kwargs['ylabel']:
        fig.set_ylabel(kwargs['ylabel'])
    if 'xlabel' in kwargs and kwargs['xlabel']:
        fig.set_xlabel(kwargs['xlabel'])
    if 'legend' in kwargs and kwargs['legend']:
        fig.legend(kwargs['legend'])

    fig.set_axisbelow(True)
    fig.minorticks_on()
    fig.grid(which = 'minor', linestyle = ':', linewidth = 0.5)
    fig.grid(which = 'major')
    
def columns_to_plot(df, columns = None):
    if isinstance(columns, str):
        columns = [columns]
    columns = columns or list(df.select_dtypes(include = np.number).columns)

    return columns

def lines(df, columns = None, title = None, xlabel = None, ylabel = None, **kwargs):
    columns = columns_to_plot(df, columns)

    if 'figsize' not in kwargs:
        kwargs['figsize'] = (8, 5)

    fig = df[columns].plot.line(**kwargs)
    format_plot(fig, title = title, xlabel = xlabel, ylabel = ylabel, legend = columns)

    return fig

def bars(df, columns, title = None, xlabel = None, ylabel = None, **kwargs):
    columns = columns_to_plot(df, columns)

    if 'figsize' not in kwargs:
        kwargs['figsize'] = (8, 5)

    fig = df[columns].plot.bar(**kwargs)
    format_plot(fig, title = title, xlabel = xlabel, ylabel = ylabel, legend = columns)

    return fig