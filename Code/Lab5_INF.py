def AdditionalTask15():
    import pandas as pd
    import matplotlib.pyplot as plt

    data = pd.read_csv("AdditionalTask13.csv", delimiter=";", encoding='utf-8')
    data.boxplot()
    plt.xticks(rotation=90)
    plt.show()


AdditionalTask15()
