import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import os

os.makedirs("visualizations", exist_ok=True)

df = pd.read_csv("data/sales_data.csv")
df["Date"] = pd.to_datetime(df["Date"])

sns.set_theme(style="whitegrid", palette="Set2")

# Box Plot
sns.boxplot(x="Category", y="Price", data=df)
plt.title("Price Distribution by Category")
plt.savefig("visualizations/boxplot_category.png")
plt.show()

# Violin Plot
sns.violinplot(x="Region", y="Sales", data=df)
plt.title("Sales Distribution by Region")
plt.savefig("visualizations/violin_region.png")
plt.show()

# Heatmap
corr = df[["Sales", "Price"]].corr()
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.savefig("visualizations/correlation_heatmap.png")
plt.show()

# Bar Chart
df.groupby("Product")["Sales"].sum().plot(kind="bar")
plt.title("Product Performance")
plt.savefig("visualizations/product_sales_bar.png")
plt.show()

# Interactive Plot
fig = px.line(df, x="Date", y="Sales", color="Category", title="Interactive Sales Trend")
fig.write_html("visualizations/interactive_dashboard.html")
fig.show()
