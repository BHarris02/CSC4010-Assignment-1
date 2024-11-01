import matplotlib.pyplot as plt
# For each method and pattern combination, insert values in the specified order

# Method A, KMP-Informed
efficiency_a_kmp_informed_pattern1_1mb = [100, 50, 25, 12.5, 4.69]  # data1-1mb + pattern1
efficiency_a_kmp_informed_pattern1_100mb = [94.25, 50, 27.42, 15.95, 4.63]  # data1-100mb + pattern1
efficiency_a_kmp_informed_pattern2_1mb = [100, 50, 25, 12.5, 6.25]  # data1-1mb + pattern2
efficiency_a_kmp_informed_pattern2_100mb = [90.73, 50.21, 25.77, 12.83, 6.02]  # data1-100mb + pattern2
efficiency_a_kmp_informed_pattern1_1gb = [60.91, 41.96, 18.2, 8.24, 4.56]  # data-1gb + pattern1
efficiency_a_kmp_informed_pattern2_1gb = [87.22, 43.42, 22.83, 11.26, 5.96]  # data-1gb + pattern 2

# Method A, KMP-Full
efficiency_a_kmp_full_pattern1_1mb = [60, 25, 25, 9.37, 2.34]  # data1-1mb + pattern1
efficiency_a_kmp_full_pattern1_100mb = [65.34, 33.54, 53.59, 40.59, 25.95]  # data1-100mb + pattern1
efficiency_a_kmp_full_pattern2_1mb = [22.22, 16.67, 6.25, 8.33, 2.5]  # data1-1mb + pattern2
efficiency_a_kmp_full_pattern2_100mb = [64.92, 44.01, 38.91, 45.9, 19.58]  # data1-100mb + pattern2
efficiency_a_kmp_full_pattern1_1gb = [59.61, 57.35, 45.33, 16.62, 10.46]  # data-1gb + pattern1
efficiency_a_kmp_full_pattern2_1gb = [61.45, 51.39, 26.84, 35.39, 23.31]  # data-1gb + pattern 2

# Method B, KMP-Informed
efficiency_b_kmp_informed_pattern1_1mb = [100, 150, 75, 18.75, 2.08]  # data1-1mb + pattern1
efficiency_b_kmp_informed_pattern1_100mb = [95.94, 99.10, 84.44, 38.67, 32.32]  # data1-100mb + pattern1
efficiency_b_kmp_informed_pattern2_1mb = [100, 100, 50, 6.25, 1.78]  # data1-1mb + pattern2
efficiency_b_kmp_informed_pattern2_100mb = [90.55, 89.84, 82.14, 50.43, 29.95]  # data1-100mb + pattern2
efficiency_b_kmp_informed_pattern1_1gb = [89.53, 83.01, 69.92, 36.41, 14.90]  # data-1gb + pattern1
efficiency_b_kmp_informed_pattern2_1gb = [87.99, 74.32, 67.2, 44.45, 30.50]  # data-1gb + pattern 2

# Method B, KMP-Full
efficiency_b_kmp_full_pattern1_1mb = [37.5, 25, 15, 9.37, 3.12]  # data1-1mb + pattern1
efficiency_b_kmp_full_pattern1_100mb = [69.54, 49.25, 52.71, 44.5, 37.61]  # data1-100mb + pattern1
efficiency_b_kmp_full_pattern2_1mb = [33.33, 25, 25, 8.33, 3.12]  # data1-1mb + pattern2
efficiency_b_kmp_full_pattern2_100mb = [67.85, 56.93, 43.98, 44.92, 20.83]  # data1-100mb + pattern2
efficiency_b_kmp_full_pattern1_1gb = [62.23, 61.19, 36.53, 30.47, 32.57]  # data-1gb + pattern1
efficiency_b_kmp_full_pattern2_1gb = [63.43, 53.55, 30.42, 25.14, 25.66]  # data-1gb + pattern 2

# Thread counts for x-axis
threads = [1, 2, 4, 8, 16]

# Function for plotting parallel efficiency
def plot_parallel_efficiency(method, dataset_size, pattern1_informed, pattern1_full, pattern2_informed, pattern2_full):
    plt.figure(figsize=(10, 6))
    plt.plot(threads, pattern1_informed, label=f'{method} KMP-Informed Pattern 1', marker='o')
    plt.plot(threads, pattern1_full, label=f'{method} KMP-Full Pattern 1', marker='o')
    plt.plot(threads, pattern2_informed, label=f'{method} KMP-Informed Pattern 2', marker='o')
    plt.plot(threads, pattern2_full, label=f'{method} KMP-Full Pattern 2', marker='o')
    plt.xlabel('Number of Threads')
    plt.ylabel('Parallel Efficiency')
    plt.title(f'Parallel Efficiency for {method} on {dataset_size} Dataset')
    plt.legend()
    plt.grid(True)
    plt.savefig(f"KMP-Efficiency-{method}-{dataset_size}.png")
    plt.show()

# Plot for each dataset
plot_parallel_efficiency('Method A', '1MB', efficiency_a_kmp_informed_pattern1_1mb, efficiency_a_kmp_full_pattern1_1mb, efficiency_a_kmp_informed_pattern2_1mb, efficiency_a_kmp_full_pattern2_1mb)
plot_parallel_efficiency('Method B', '1MB', efficiency_b_kmp_informed_pattern1_1mb, efficiency_b_kmp_full_pattern1_1mb, efficiency_b_kmp_informed_pattern2_1mb, efficiency_b_kmp_full_pattern2_1mb)

plot_parallel_efficiency('Method A', '100MB', efficiency_a_kmp_informed_pattern1_100mb, efficiency_a_kmp_full_pattern1_100mb, efficiency_a_kmp_informed_pattern2_100mb, efficiency_a_kmp_full_pattern2_100mb)
plot_parallel_efficiency('Method B', '100MB', efficiency_b_kmp_informed_pattern1_100mb, efficiency_b_kmp_full_pattern1_100mb, efficiency_b_kmp_informed_pattern2_100mb, efficiency_b_kmp_full_pattern2_100mb)

plot_parallel_efficiency('Method A', '1GB', efficiency_a_kmp_informed_pattern1_1gb, efficiency_a_kmp_full_pattern1_1gb, efficiency_a_kmp_informed_pattern2_1gb, efficiency_a_kmp_full_pattern2_1gb)
plot_parallel_efficiency('Method B', '1GB', efficiency_b_kmp_informed_pattern1_1gb, efficiency_b_kmp_full_pattern1_1gb, efficiency_b_kmp_informed_pattern2_1gb, efficiency_b_kmp_full_pattern2_1gb)
