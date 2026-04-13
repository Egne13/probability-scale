import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/events.csv")

# sortime väiksemast suuremani
df = df.sort_values("probability")

plt.figure(figsize=(10,6))

plt.barh(df["event"], df["probability"])

plt.xscale("log")

plt.xlabel("Probability (log scale)")
plt.title("Probability Scale of Real-World Events")

plt.tight_layout()
plt.show()

plt.grid(True, which="both", linestyle="--", alpha=0.3)