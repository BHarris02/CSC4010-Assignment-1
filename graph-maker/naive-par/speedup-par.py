import matplotlib.pyplot as plt
import numpy as np

# Data structure for execution times (replace with actual data as necessary)
threads = [1, 2, 4, 8, 16]
execution_time_data = {
    'small': {
        'data1-1MB + pattern1': {'Method A': [0.03, 0.02, 0.03, 0.09, 0.08], 'Method B': [0.03, 0.02, 0.02, 0.03, 0.06]},
        'data1-1MB + pattern2': {'Method A': [0.02, 0.01, 0.02, 0.03, 0.03], 'Method B': [0.02, 0.01, 0.01, 0.02, 0.07]}
    },
    'medium': {
        'data1-100MB + pattern1': {'Method A': [3.14, 1.66, 1.76, 1.58, 0.46], 'Method B': [3.07, 1.63, 0.91, 0.63, 0.47]},
        'data1-100MB + pattern2': {'Method A': [2.27, 1.42, 0.80, 0.49, 0.52], 'Method B': [2.29, 1.36, 0.66, 0.40, 0.43]}
    },
    'large': {
        'data1-1GB + pattern1': {'Method A': [26.31, 13.42, 7.89, 5.50, 3.83], 'Method B': [25.82, 13.65, 7.41, 5.11, 3.43]},
        'data1-1GB + pattern2': {'Method A': [19.31, 11.77, 6.05, 3.62, 3.74], 'Method B': [19.04, 11.40, 6.23, 4.46, 3.41]}
    }
}

# Function to plot speedup for a dataset size
def plot_speedup(dataset_size, dataset_patterns):
    plt.figure(figsize=(10, 6))
    for dataset_pattern, methods in dataset_patterns.items():
        for method, times in methods.items():
            speedup = [times[0] / t for t in times]  # Calculate speedup
            plt.plot(threads, speedup, label=f'{method} - {dataset_pattern}', marker='o')

    plt.xlabel('Number of Threads')
    plt.ylabel('Speedup')
    plt.title(f'Speedup Comparison for {dataset_size.capitalize()} Dataset (1MB, 100MB, 1GB)')
    plt.legend()
    plt.xticks(threads)
    plt.grid(True)
    plt.tight_layout()
    # Save each plot as an image
    plt.savefig(f'speedup_comparison_{dataset_size}.png')
    plt.show()

# Plot each dataset size
for size, data in execution_time_data.items():
    plot_speedup(size, data)
