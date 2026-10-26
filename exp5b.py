import matplotlib.pyplot as plt

# Data
labels = ['Python', 'Java', 'C++', 'JavaScript', 'C']
sizes = [35, 25, 20, 15, 5]

# Create pie chart
plt.pie(
    sizes,
    labels=labels,
    autopct='%1.1f%%',
    startangle=90
)

# Add title
plt.title('Programming Language Usage')

# Ensure the pie chart is circular
plt.axis('equal')

# Display the chart
plt.show()
