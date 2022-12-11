def AdditionalTask15():
    import matplotlib.pyplot as plt
    import pandas as pd

    data = pd.read_csv('AdditionalTask13.csv', sep=';')
    data.boxplot()
    plt.show()


AdditionalTask15()
