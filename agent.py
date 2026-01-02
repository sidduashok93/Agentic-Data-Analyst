def code_agent(step):
    if "Convert Date" in step:
        return """
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df = df.sort_values('Date')
"""

    if "Plot trends" in step:
        return """
df.set_index('Date').plot(figsize=(10,5))
plt.title('Trends Over Time')
plt.show()
"""

    if "anomalies" in step:
        return """
from scipy.stats import zscore
df['sales_z'] = zscore(df['Sales'])
anomalies = df[np.abs(df['sales_z']) > 3]
print(anomalies)
"""

    if "summary statistics" in step:
        return """
print(df.describe())
"""

    return ""
