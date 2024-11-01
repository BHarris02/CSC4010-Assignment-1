import matplotlib.pyplot as plt

# Sample data structure for plotting with dataset, pattern, method, and threads
threads = [1, 2, 4, 8, 16]
execution_time_data = {
    'data1-1GB + pattern1': {
        'Method A': [26.31, 13.42, 7.89, 5.50, 3.83],
        'Method B': [25.82, 13.65, 7.41, 5.11, 3.43]
    },
    'data1-1GB + pattern2': {
        'Method A': [19.31, 11.77, 6.05, 3.62, 3.74],
        'Method B': [19.04, 11.40, 6.23, 4.46, 3.41]
    }
}

# Generate plots for each dataset and pattern combination, comparing Method A and Method B
for dataset_pattern, methods in execution_time_data.items():
    plt.figure()
    for method, times in methods.items():
        plt.plot(threads, times, label=method, marker='o')
    plt.xlabel('Number of Threads')
    plt.ylabel('Wall Clock Time (s)')
    plt.title(f'Execution Time Comparison for {dataset_pattern}')
    plt.legend()
    plt.xticks(threads)
    plt.grid(True)
    # Save each plot as a PNG file
    plt.savefig(f'execution_time_comparison_{dataset_pattern.replace(" ", "_").replace("+", "and")}.png')
    plt.show()
