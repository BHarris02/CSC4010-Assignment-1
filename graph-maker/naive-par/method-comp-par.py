import matplotlib.pyplot as plt
import numpy as np

# Data for wall clock times at 16 threads for different dataset and pattern combinations
execution_time_data = {
    'data1-1MB + pattern1': {'Method A': 0.08, 'Method B': 0.06},
    'data1-1MB + pattern2': {'Method A': 0.03, 'Method B': 0.07},
    'data1-100MB + pattern1': {'Method A': 0.46, 'Method B': 0.47},
    'data1-100MB + pattern2': {'Method A': 0.52, 'Method B': 0.43},
    'data1-1GB + pattern1': {'Method A': 3.83, 'Method B': 3.43},
    'data1-1GB + pattern2': {'Method A': 3.74, 'Method B': 3.41}
}

# Extract dataset and pattern labels, Method A and B times for each
labels = list(execution_time_data.keys())
method_a_times = [execution_time_data[label]['Method A'] for label in labels]
method_b_times = [execution_time_data[label]['Method B'] for label in labels]

# Set the position of bars on the x-axis
x = np.arange(len(labels))

# Width of the bars
width = 0.35

# Plotting
plt.figure(figsize=(12, 8))
plt.bar(x - width/2, method_a_times, width, label='Method A', color='skyblue')
plt.bar(x + width/2, method_b_times, width, label='Method B', color='salmon')

# Adding labels and title
plt.xlabel('Dataset and Pattern Combinations')
plt.ylabel('Wall Clock Time (s)')
plt.title('Wall Clock Time Comparison at 16 Threads for Each Dataset and Pattern Combination')
plt.xticks(x, labels, rotation=45, ha='right')
plt.legend()
plt.tight_layout()

# Save the plot as an image file
plt.savefig('wall_clock_time_comparison_bar_chart.png')
plt.show()
