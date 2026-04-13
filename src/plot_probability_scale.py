import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("data/events.csv")

# Create figure
plt.figure(figsize=(10,5))

# Scatter plot
plt.scatter(df["probability"], df["event"])

# Log scale for probabilities
plt.xscale("log")

# Labels
plt.xlabel("Probability (log scale)")
plt.ylabel("Events")
plt.title("Probability Scale of Real-World Events")

plt.grid(True)

plt.show()
