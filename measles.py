import pandas as pd
import matplotlib.pyplot as plt

print("Reading data from measles.csv...")

# Attempt to read the CSV file
try:
    df = pd.read_csv("measles.csv", names=["Country", "Income_Level", "Percent_Vaccinated"], header=None, skiprows=1)
except FileNotFoundError:
    print("Error: Unable to open 'measles.csv'. Please make sure the file exists.")
    exit(1)

# Plot 1: Scatter plot of Percent Vaccinated vs. Income Level
plt.figure(figsize=(12, 8))
plt.scatter(df['Income_Level'], df['Percent_Vaccinated'], color='purple', alpha=0.5)
plt.title('Percentage of Children Vaccinated Against Measles by Country Income Level')
plt.xlabel('Income Level')
plt.ylabel('Percent Vaccinated')
plt.grid(True)
plt.xticks(rotation=45)

# Adjust axes limits
plt.xlim(-1, len(df['Country']))
plt.ylim(df['Percent_Vaccinated'].min() - 5, 150)  # Limit y-axis to 150

plt.tight_layout()

# Save the plot 1 to an image file (e.g., PNG)
plt.savefig('scatter_plot_income_vs_vaccination.png')

# Print a message to indicate that plot 1 has been saved
print("Plot 1 saved as 'scatter_plot_income_vs_vaccination.png'")

# Plot 2: Scatter plot of Percent Vaccinated vs. Country
plt.figure(figsize=(12, 8))
plt.scatter(df['Country'], df['Percent_Vaccinated'], color='blue', alpha=0.5)
plt.title('Percentage of Children Vaccinated Against Measles by Country')
plt.xlabel('Country')
plt.ylabel('Percent Vaccinated')
plt.grid(True)
plt.xticks(rotation=90)

# Adjust axes limits
plt.xlim(-1, len(df['Country']))
plt.ylim(df['Percent_Vaccinated'].min() - 5, 150)  # Limit y-axis to 150

plt.tight_layout()

# Save the plot 2 to an image file (e.g., PNG)
plt.savefig('scatter_plot_country_vs_vaccination.png')

# Print a message to indicate that plot 2 has been saved
print("Plot 2 saved as 'scatter_plot_country_vs_vaccination.png'")

# Plot 3: Line graph of Total Percent Vaccinated by Income Level
total_percent_vaccinated_income = df.groupby('Income_Level')['Percent_Vaccinated'].sum()
plt.figure(figsize=(10, 6))
total_percent_vaccinated_income.plot(color='skyblue', marker='o', linestyle='-')
plt.title('Total Percentage of Children Vaccinated Against Measles by Income Level')
plt.xlabel('Income Level')
plt.ylabel('Total Percent Vaccinated')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()

# Save the plot 1 to an image file (e.g., PNG)
plt.savefig('line_graph_total_vaccinated_by_income.png')

# Print a message to indicate that plot 1 has been saved
print("Plot 3 saved as 'line_graph_total_vaccinated_by_income.png'")

# Plot 4: Line graph of Total Percent Vaccinated by Country
total_percent_vaccinated_country = df.groupby('Country')['Percent_Vaccinated'].sum()
plt.figure(figsize=(10, 6))
total_percent_vaccinated_country.plot(color='red', marker='o', linestyle='-')
plt.title('Total Percentage of Children Vaccinated Against Measles by Country')
plt.xlabel('Country')
plt.ylabel('Total Percent Vaccinated')
plt.xticks(rotation=90)  # Rotate x-axis labels for better readability
plt.grid(True)
plt.tight_layout()

# Save the plot 2 to an image file (e.g., PNG)
plt.savefig('line_graph_total_vaccinated_by_country.png')

# Print a message to indicate that plot 2 has been saved
print("Plot 4 saved as 'line_graph_total_vaccinated_by_country.png'")

# Show the plots
plt.show()
