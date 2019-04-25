import matplotlib
matplotlib.use('Agg')
import pandas as pd
import seaborn as sns
import numpy as np


def boostrap(sample, sample_size, iterations):
    # <---INSERT YOUR CODE HERE--->
    sample_data = np.random.choice(sample, size=(iterations, sample_size))

    data_mean = np.mean(sample_data)
    lower = np.percentile(sample_data, 2.5)
    upper = np.percentile(sample_data, 97.5)
    return data_mean, lower, upper


if __name__ == "__main__":
    df = pd.read_csv('./vehicles.csv')

    data = df.values.T[0]
    boots = []
    for i in range(100, 100000, 1000):
        boot = boostrap(data, data.shape[0], i)
        boots.append([i, boot[0], "mean"])
        boots.append([i, boot[1], "lower"])
        boots.append([i, boot[2], "upper"])

    df_boot = pd.DataFrame(boots, columns=['Boostrap Iterations', 'Mean', "Value"])
    sns_plot = sns.lmplot(df_boot.columns[0], df_boot.columns[1], data=df_boot, fit_reg=False, hue="Value")

    sns_plot.axes[0, 0].set_ylim(0,)
    sns_plot.axes[0, 0].set_xlim(0, 100000)

    sns_plot.savefig("bootstrap_current_fleet.png", bbox_inches='tight')
    sns_plot.savefig("bootstrap_current_fleet.pdf", bbox_inches='tight')

    data1 = df.values.T[2]

    bootnew = []
    for i in range(100, 100000, 1000):
        bootnew = boostrap(data1, data1.shape[0], i)
        bootnew.append([i, boot[0], "mean"])
        bootnew.append([i, boot[1], "lower"])
        bootnew.append([i, boot[2], "upper"])

    df_bootnew = pd.DataFrame(bootnew, columns=['Boostrap Iterations', 'Mean', "Value"])
    sns_plot = sns.lmplot(df_bootnew.columns[0], df_bootnew.columns[1], data=df_bootnew, fit_reg=False, hue="Value")

    sns_plot.axes[0, 0].set_ylim(0,)
    sns_plot.axes[0, 0].set_xlim(0, 100000)

    sns_plot.savefig("bootstrap_new_fleet.png", bbox_inches='tight')
    sns_plot.savefig("bootstrap_new_fleet.pdf", bbox_inches='tight')



    #print ("Mean: %f")%(np.mean(data))
    #print ("Var: %f")%(np.var(data))