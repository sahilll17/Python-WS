import matplotlib.pyplot as plt

# Data
subjects = ["Math", "Science", "English", "Computer"]
marks = [85, 78, 90, 95]

# Create bar graph
plt.bar(subjects, marks)

# Labels and title
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Marks by Subject")

# Display graph
plt.show()
