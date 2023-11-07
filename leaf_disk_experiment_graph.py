import matplotlib.pyplot as plt

# Summary: Python script for generating a line graph of the Leaf Disk Photosynthesis Experiment
# Data represents the number of leaves floating under high light, low light, and control conditions over 1-20 minutes.

# Data for the experiment
time = list(range(1, 21))  # Time from 1 to 20 minutes

high_light = [
    1, 4, 6, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10
]

low_light = [
    0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1
]

control = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
]

# Create the line graph
plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
plt.plot(time, high_light, label='High Light', marker='o')
plt.plot(time, low_light, label='Low Light', marker='o')
plt.plot(time, control, label='Control', marker='o')

# Customize the graph
plt.xlabel('Time (minutes)')
plt.ylabel('Number of Leaves Floating')
plt.title('Leaf Disk Photosynthesis Experiment')
plt.legend()

# Save the graph as a PNG
plt.savefig('leaf_disk_experiment_graph.png', dpi=300, bbox_inches='tight')  # Adjust the filename and DPI as needed
plt.show()

