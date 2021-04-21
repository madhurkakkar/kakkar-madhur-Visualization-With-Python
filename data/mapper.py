import matplotlib.pyplot as plt

Games = ['Ice hockey', 'Relay', 'Curling', 'Individuals']
Medals = [76, 16, 10, 6]

plt.plot(Games, Medals, color=(0/255, 100/255, 100/255), linewidth=3.0)

plt.ylabel("Type Of Games")

plt.xlabel("Medals Won By Canada")

plt.title("Medals Won In Different Games", pad="20")

plt.show()