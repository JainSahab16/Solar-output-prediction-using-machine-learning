import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder

# Load data
weather = pd.read_csv("daily-weather-dataset_chronological-order.csv")
solar = pd.read_csv("solar-data-daily.csv")

# Drop unnecessary columns
solar.drop(columns=["New.Nexus.1272.Meter", "Site.Performance.Estimate"], inplace=True)
solar.rename(columns={"Date": "Date"}, inplace=True)

# Merge datasets on Date
all_data = pd.merge(solar, weather, on="Date")
all_data.dropna(inplace=True)  # Remove rows with missing values

# Convert categorical columns to numeric
for col in ["Inverters", "Cloud.coverage"]:
    all_data[col] = pd.to_numeric(all_data[col], errors='coerce')

# Drop any additional unwanted columns
if "X.Inverters." in all_data.columns:
    all_data.drop(columns=["X.Inverters."], inplace=True)

# Load correlation data
all_corr = pd.read_pickle("all.corr.Rda")  # Assuming it's stored in a pickle format

# Mapping variables
var_map = {
    "alt": "Altimeter",
    "wind": "Wind speed",
    "hum": "Relative humidity",
    "dew": "Dew point",
    "cloud": "Cloud coverage",
    "vis": "Visibility"
}
all_corr["variable"] = all_corr["variable"].replace(var_map)

# Mapping months
month_map = {
    "1": "January", "2": "February", "3": "March", "4": "April", "5": "May", "6": "June",
    "7": "July", "8": "August", "9": "September", "10": "October", "11": "November", "12": "December"
}
all_corr["Month"] = all_corr["Month"].astype(str).replace(month_map)

# Categorize correlation values
all_corr["type"] = np.where((all_corr["COR"] > 0.5) | (all_corr["COR"] < -0.5), "h1", "l")

# Plot correlations
plt.figure(figsize=(8, 5))
sns.barplot(data=all_corr, x="Month", y="COR", hue="type", palette={"h1": "firebrick2", "l": "grey80"})
plt.xlabel("Month")
plt.ylabel("Correlation")
plt.title("Correlation by Month and Variable")
plt.xticks(rotation=45)
plt.legend(title="Type", loc="upper right")
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()

# Save the figure
plt.savefig("corr-v1.pdf", format="pdf", dpi=300)
plt.show()
