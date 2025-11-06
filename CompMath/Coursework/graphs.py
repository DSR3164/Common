import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("output.txt", sep=r"\s+", engine="python")
variables = ["S", "E", "I", "R", "D"]
variables = [x for x in reversed(variables)] 
titles = {"S": "Susceptible (Восприимчивые)","E": "Exposed (Подвергшиеся воздействию)","I": "Infectious (Инфицированные)","R": "Recovered (Выздоровевшие)","D": "Dead (Умершие)"}

for var in variables:
    plt.figure(figsize=(12.453544, 4.151181))
    plt.plot(df["t"], df[var], linewidth=2)
    plt.title(f"{titles[var]}")
    plt.xlabel("Time (days)")
    plt.ylabel("Population")
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.tight_layout()  

plt.show()