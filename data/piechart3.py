
#/ of medal position: 3
#/ of population: 625
#/ of sports: 6
import matplotlib.pyplot as plt

values = values = [3, 625, 6]
labels = ["Medal position", "population", "sports"]
colors = ["green", "grey", "skyblue"]
explode = (0, 0.1, 0.2)

plt.pie(values, labels=labels, colors=colors, explode=explode, autopct = '%2.1f%%')
plt.show()