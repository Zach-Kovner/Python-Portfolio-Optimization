from Monte_Carlo import sims
import matplotlib.pyplot as plt
import seaborn as sns


print(sims.head())
x = sims.Volatility
y = sims['Exp Return']

sns.scatterplot(x=x, y=y, s=2)
plt.xlabel('Risk')
plt.ylabel('Return')
plt.title('The Efficient Frontier')

plt.show()
