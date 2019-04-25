import inline as inline
import matplotlib
matplotlib.use('Agg')
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np








if __name__ == "__main__":
    data = pd.read_csv('./vehicles.csv')
    print (data.columns)
    sns_plot = sns.lmplot(data.columns[0], data.columns[1], data=data, fit_reg=False)
    sns_plot.axes[0,0].set_ylim(0,)
    sns_plot.axes[0,0].set_xlim(0,)
    sns_plot.savefig("CFScatterPlot.png", bbox_inches='tight')

    sns1plot = sns.distplot(data.values.T[0], bins=20, kde=False, rug=True, axlabel="Current Fleet").get_figure()
    sns1plot.savefig("currentfleethistogram.png", bbox_inches='tight')
    plt.hist(data.values.T[1], bins=22, density=7, color="Red")
    plt.title("Proposed Fleet")
    plt.savefig("ProposedFleet.png")

























