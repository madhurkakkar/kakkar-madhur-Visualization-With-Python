# # of silver medals: 66
# # of gold medals: 193
# # of bronze medals: 128
import matplotlib.pyplot as plt

values = values = [ 193, 66, 128]
labels = ["Gold Medal", "Silver Medal", "Bronze Medal"]
colors = ["Gold", "Silver", "brown"]
explode = (0, 0.1, 0.2)

plt.pie(values, labels=labels, colors=colors, explode=explode, autopct = '%2.1f%%')
plt.show()