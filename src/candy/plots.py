
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def format_plot(func):

    def decorator(df, columns = None, *args, **kwargs):

        columns = columns_to_plot(df, columns)

        if kwargs.get('subplots', False):
            raise Exception('Argument [subplots] equals to [True] is not supported.')
        if 'figsize' not in kwargs and 'ax' not in kwargs:
            kwargs['figsize'] = (8, 5)

        fig = func(df, columns, *args, **kwargs)

        if 'title' in kwargs and kwargs['title']:
            fig.set_title(kwargs['title'])
        else:
            fig.set_title(', '.join(columns))
        if 'ylabel' in kwargs and kwargs['ylabel']:
            fig.set_ylabel(kwargs['ylabel'])
        if 'xlabel' in kwargs and kwargs['xlabel']:
            fig.set_xlabel(kwargs['xlabel'])
        # if 'legend' in kwargs and kwargs['legend']:
        #     fig.legend(kwargs['legend'])

        fig.set_axisbelow(True)
        fig.minorticks_on()
        fig.grid(which = 'minor', linestyle = ':', linewidth = 0.5)
        fig.grid(which = 'major')
    
    return decorator

def columns_to_plot(df, columns = None):
    if isinstance(columns, str):
        columns = [columns]
    columns = columns or list(df.select_dtypes(include = np.number).columns)

    return columns

@format_plot
def lines(df, columns = None, title = None, xlabel = None, ylabel = None, shifts = [], **kwargs):
    colors = plt.rcParams['axes.prop_cycle'].by_key()['color']
    n_colors = len(colors)
    fig = None
    kwargs_shift = dict(kwargs)
    legends0 = kwargs.get('legend', list(columns))
    legends0 = [legends0] if isinstance(legends0, str) else legends0
    legends = []
    #xticks = None
    for i, col in enumerate(columns):
        
        fig = df[col].plot.line(**kwargs)
        #if not xticks:
        #    xticks = fig.get_xticks()
        legends.append(legends0[i])

        alpha = kwargs.get('alpha', 1.0)
        linewidth = kwargs.get('linewidth', 1.0)
        color = kwargs.get('color', colors[i % n_colors])
        for shift in shifts:
            kwargs_shift['linestyle'] = '-.'
            kwargs_shift['linewidth'] = linewidth
            alpha = alpha * 0.8
            kwargs_shift['alpha'] = alpha
            kwargs_shift['color'] = color
            
            fig = df[col].shift(shift).plot.line(**kwargs_shift)
            legends.append('%s [%d]' % (legends0[i], shift))

    fig.legend(legends)
    #fig.set_xticks(xticks)
    # print(xticks)

    return fig

def bars(df, columns, title = None, xlabel = None, ylabel = None, **kwargs):
    columns = columns_to_plot(df, columns)

    if 'figsize' not in kwargs:
        kwargs['figsize'] = (8, 5)

    fig = df[columns].plot.bar(**kwargs)
    format_plot(fig, title = title, xlabel = xlabel, ylabel = ylabel, legend = columns)

    return fig