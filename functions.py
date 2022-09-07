# Helper Functions
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sb

def univ_plot(kind, series, bins = None, figsize = (7, 5), title = None, xlabel = None, ylabel = None, labels = None, order = None, legend = False):
    """ A helper function for univariate plots"""
    
    plt.figure(figsize = figsize);
    color = sb.color_palette()[0]
    if kind == "bar":
        sb.countplot(x = series, order = order, color = color);
    
    elif kind == "barh":
        sb.countplot(y = series, order = order, color = color);
        
    elif kind == "donut":
        plt.pie(series, labels=labels, autopct='%1.1f%%');

        #draw a circle at the center of pie to make it look like a donut
        centre_circle = plt.Circle((0,0),0.75,color='white', fc='white',linewidth=1)
        fig = plt.gcf()
        fig.gca().add_artist(centre_circle)

        # Set aspect ratio to be equal so that pie is drawn as a circle.
        plt.axis('equal')
        
    elif kind == "hist":
        plt.hist(series, bins);
        
    plt.title(title);
    plt.xlabel(xlabel);
    plt.ylabel(ylabel);
    
    if legend:
        plt.legend();
    
def bin_gen(series, bin_size, log = False):
    """This function helps to generate bins for visualizations"""
    if log:
        out = 10 ** np.arange(round(np.log10(series.min())), round(np.log10(series.max()))+1, 1)
    else:
        out = np.arange(series.min(), series.max()+bin_size, bin_size)
    return out

def bi_plot(kind, df, x, y, bins = None, figsize = (7, 5), title = None, xlabel = None, ylabel = None, labels = None, order = None, legend = False):
    """ A helper function for bivariate plots"""
    
    plt.figure(figsize = figsize);
    color = sb.color_palette()[0]
        
    if kind == "bar":
        sb.barplot(data = df, x = x, y = y, ci = 'sd', color = color, order = order);
        
    elif kind == "heat":
        plt.hist2d(data = df, x = x, y = y, bins = bins, cmap = 'viridis_r', cmin = 500);
        plt.colorbar();
        
    elif kind == "scatter":
        sb.regplot(data = df, x = x, y = y, x_jitter=0.04, scatter_kws={'alpha':1/10}, fit_reg=False);
     
    plt.title(title);
    plt.xlabel(xlabel);
    plt.ylabel(ylabel);
    
    if legend:
        plt.legend();