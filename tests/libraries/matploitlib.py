import matplotlib.pyplot as plt
import pandas as pd


# Sample data
#x = [0, 1, 2, 3, 4, 5]
#y = [0, 1, 4, 9, 16, 25]

df = pd.read_csv('pp.csv')
print(df.columns)
print(df[['x', 'y']])

x = df['x']
y = df['y']

# Create a plot
plt.plot(x, y)

# Add title and labels
plt.title("Simple Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

# Show the plot

#plt.savefig("line_plot.png")
plt.show()

