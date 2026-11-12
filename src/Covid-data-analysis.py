# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# I/O paths
BASE_DIR = Path(__file__).resolve().parent.parent
file = BASE_DIR / "data" / "covid_sample.csv"

output_dir = BASE_DIR / "outputs"
output_dir.mkdir(exist_ok=True)

# Read file and filter to Italy
f1 = pd.read_csv(file)

cols = ["location", "date", "total_cases", "new_cases", "population"]
data = f1[cols]

data["date"] = pd.to_datetime(data["date"])
italy = data[data["location"] == "Italy"]

print("\nItaly Statistics:")
print(italy.describe())

# Graphs
plt.figure(figsize=(10,5))
sns.lineplot(data=italy, x="date", y="new_cases")
plt.title("Trend of cases in Italy")
plt.xlabel("Data")
plt.ylabel("Daily Cases")

# Output png
plt.savefig(
    output_dir / "Covid_trend_italy.png",
    dpi = 300,
    bbox_inches = "tight"
)

plt.show()

