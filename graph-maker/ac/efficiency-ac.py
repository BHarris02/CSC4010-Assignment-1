import matplotlib.pyplot as plt
# For each method and pattern combination, insert values in the specified order

# Method A, ac-Informed
efficiency_a_ac_informed_pattern1_1mb = [23.08, 16.67, 750, 3.75, 6.25]  # data1-1mb + pattern1
efficiency_a_ac_informed_pattern1_100mb = [4, 3.33, 3, 1.39, 1.10]  # data1-100mb + pattern1
efficiency_a_ac_informed_pattern2_1mb = [75, 25, 750, 3.12, 6.25]  # data1-1mb + pattern2
efficiency_a_ac_informed_pattern2_100mb = [3.57, 3.19, 3.26, 1.25, 1.10]  # data1-100mb + pattern2
efficiency_a_ac_informed_pattern1_1gb = [0.10, 0.07, 0.04, 0.02, 0.01]  # data-1gb + pattern1
efficiency_a_ac_informed_pattern2_1gb = [0.13, 0.12, 0.014, 0.10, 0.08]  # data-1gb + pattern 2

# Method A, ac-Full
efficiency_a_ac_full_pattern1_1mb = [100, 75, 5, 2.68, 1.44]  # data1-1mb + pattern1
efficiency_a_ac_full_pattern1_100mb = [0.89, 0.97, 0.73, 0.48, 0.32]  # data1-100mb + pattern1
efficiency_a_ac_full_pattern2_1mb = [150, 150, 9.37, 2.68, 1.56]  # data1-1mb + pattern2
efficiency_a_ac_full_pattern2_100mb = [1.59, 1.31, 0.82, 0.65, 0.32]  # data1-100mb + pattern2
efficiency_a_ac_full_pattern1_1gb = [0.46, 0.29, 0.28, 0.03, 0.02]  # data-1gb + pattern1
efficiency_a_ac_full_pattern2_1gb = [0.44, 0.30, 0.27, 0.22, 0.12]  # data-1gb + pattern 2

# Method B, ac-Informed
efficiency_b_ac_informed_pattern1_1mb = [42.86, 21.43, 75, 4.17, 4.69]  # data1-1mb + pattern1
efficiency_b_ac_informed_pattern1_100mb = [3.41, 1.70, 0.99, 0.37, 0.25]  # data1-100mb + pattern1
efficiency_b_ac_informed_pattern2_1mb = [100, 30, 75, 5.38, 6.25]  # data1-1mb + pattern2
efficiency_b_ac_informed_pattern2_100mb = [3.22, 1.58, 0.90, 0.38, 0.23]  # data1-100mb + pattern2
efficiency_b_ac_informed_pattern1_1gb = [0.40, 0.20, 0.11, 0.06, 0.03]  # data-1gb + pattern1
efficiency_b_ac_informed_pattern2_1gb = [0.37, 0.19, 0.11, 0.06, 0.03]  # data-1gb + pattern 2

# Method B, ac-Full
efficiency_b_ac_full_pattern1_1mb = [3000, 150, 18.75, 3.75, 0.43]  # data1-1mb + pattern1
efficiency_b_ac_full_pattern1_100mb = [4.69, 2.03, 0.83, 0.44, 0.26]  # data1-100mb + pattern1
efficiency_b_ac_full_pattern2_1mb = [3000, 150, 12.5, 6.25, 3.125]  # data1-1mb + pattern2
efficiency_b_ac_full_pattern2_100mb = [4.48, 1.78, 0.83, 0.42, 0.24]  # data1-100mb + pattern2
efficiency_b_ac_full_pattern1_1gb = [0.39, 0.20, 0.11, 0.06, 0.03]  # data-1gb + pattern1
efficiency_b_ac_full_pattern2_1gb = [0.37, 0.19, 0.10, 0.05, 0.03]  # data-1gb + pattern 2

# Thread counts for x-axis
threads = [1, 2, 4, 8, 16]

# Function for plotting parallel efficiency
def plot_parallel_efficiency(method, dataset_size, pattern1_informed, pattern1_full, pattern2_informed, pattern2_full):
    plt.figure(figsize=(10, 6))
    plt.plot(threads, pattern1_informed, label=f'{method} ac-Informed Pattern 1', marker='o')
    plt.plot(threads, pattern1_full, label=f'{method} ac-Full Pattern 1', marker='o')
    plt.plot(threads, pattern2_informed, label=f'{method} ac-Informed Pattern 2', marker='o')
    plt.plot(threads, pattern2_full, label=f'{method} ac-Full Pattern 2', marker='o')
    plt.xlabel('Number of Threads')
    plt.ylabel('Parallel Efficiency')
    plt.title(f'Parallel Efficiency for {method} on {dataset_size} Dataset')
    plt.legend()
    plt.grid(True)
    plt.savefig(f"ac-Efficiency-{method}-{dataset_size}.png")
    plt.show()

# Plot for each dataset
plot_parallel_efficiency('Method A', '1MB', efficiency_a_ac_informed_pattern1_1mb, efficiency_a_ac_full_pattern1_1mb, efficiency_a_ac_informed_pattern2_1mb, efficiency_a_ac_full_pattern2_1mb)
plot_parallel_efficiency('Method B', '1MB', efficiency_b_ac_informed_pattern1_1mb, efficiency_b_ac_full_pattern1_1mb, efficiency_b_ac_informed_pattern2_1mb, efficiency_b_ac_full_pattern2_1mb)

plot_parallel_efficiency('Method A', '100MB', efficiency_a_ac_informed_pattern1_100mb, efficiency_a_ac_full_pattern1_100mb, efficiency_a_ac_informed_pattern2_100mb, efficiency_a_ac_full_pattern2_100mb)
plot_parallel_efficiency('Method B', '100MB', efficiency_b_ac_informed_pattern1_100mb, efficiency_b_ac_full_pattern1_100mb, efficiency_b_ac_informed_pattern2_100mb, efficiency_b_ac_full_pattern2_100mb)

plot_parallel_efficiency('Method A', '1GB', efficiency_a_ac_informed_pattern1_1gb, efficiency_a_ac_full_pattern1_1gb, efficiency_a_ac_informed_pattern2_1gb, efficiency_a_ac_full_pattern2_1gb)
plot_parallel_efficiency('Method B', '1GB', efficiency_b_ac_informed_pattern1_1gb, efficiency_b_ac_full_pattern1_1gb, efficiency_b_ac_informed_pattern2_1gb, efficiency_b_ac_full_pattern2_1gb)
