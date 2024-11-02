import matplotlib.pyplot as plt
# For each method and pattern combination, insert values in the specified order

# Method A, KMP-Informed
efficiency_a_kmp_informed_pattern1_1mb = [1.00,0.50,0.25,0.13,0.05]  # data1-1mb + pattern1
efficiency_a_kmp_informed_pattern1_100mb = [1.00,0.53,0.29,0.17,0.05]  # data1-100mb + pattern1
efficiency_a_kmp_informed_pattern2_1mb = [1.00,0.50,0.25,0.13,0.06]  # data1-1mb + pattern2
efficiency_a_kmp_informed_pattern2_100mb = [1.00,0.55,0.28,0.14,0.07]  # data1-100mb + pattern2
efficiency_a_kmp_informed_pattern1_1gb = [1.00,0.69,0.30,0.14,0.07]  # data-1gb + pattern1
efficiency_a_kmp_informed_pattern2_1gb = [1.00,0.50,0.26,0.13,0.07]  # data-1gb + pattern 2

# Method A, KMP-Full
efficiency_a_kmp_full_pattern1_1mb = [1.00,1.50,0.75,0.19,0.02]  # data1-1mb + pattern1
efficiency_a_kmp_full_pattern1_100mb = [1.00,1.03,0.88,0.40,0.34]  # data1-100mb + pattern1
efficiency_a_kmp_full_pattern2_1mb = [1.00,1.00,0.50,0.06,0.02]  # data1-1mb + pattern2
efficiency_a_kmp_full_pattern2_100mb = [1.00,0.99,0.91,0.56,0.33]  # data1-100mb + pattern2
efficiency_a_kmp_full_pattern1_1gb = [1.00,0.93,0.78,0.41,0.17]  # data-1gb + pattern1
efficiency_a_kmp_full_pattern2_1gb = [1.00,0.84,0.76,0.51,0.35]  # data-1gb + pattern 2

# Method B, KMP-Informed
efficiency_b_kmp_informed_pattern1_1mb = [1.00,0.42,0.42,0.16,0.04]  # data1-1mb + pattern1
efficiency_b_kmp_informed_pattern1_100mb = [1.00,0.51,0.82,0.62,0.40]  # data1-100mb + pattern1
efficiency_b_kmp_informed_pattern2_1mb = [1.00,0.75,0.28,0.38,0.11]  # data1-1mb + pattern2
efficiency_b_kmp_informed_pattern2_100mb = [1.00,0.68,0.60,0.71,0.30]  # data1-100mb + pattern2
efficiency_b_kmp_informed_pattern1_1gb = [1.00,0.96,0.76,0.28,0.18]  # data-1gb + pattern1
efficiency_b_kmp_informed_pattern2_1gb = [1.00,0.84,0.44,0.58,0.38]  # data-1gb + pattern 2

# Method B, KMP-Full
efficiency_b_kmp_full_pattern1_1mb = [1.00,0.67,0.40,0.25,0.08]  # data1-1mb + pattern1
efficiency_b_kmp_full_pattern1_100mb = [1.00,0.71,0.76,0.64,0.54]  # data1-100mb + pattern1
efficiency_b_kmp_full_pattern2_1mb = [1.00,0.75,0.75,0.25,0.09]  # data1-1mb + pattern2
efficiency_b_kmp_full_pattern2_100mb = [1.00,0.84,0.65,0.66,0.31]  # data1-100mb + pattern2
efficiency_b_kmp_full_pattern1_1gb = [1.00,0.98,0.59,0.49,0.52]  # data-1gb + pattern1
efficiency_b_kmp_full_pattern2_1gb = [1.00,0.84,0.48,0.40,0.40]  # data-1gb + pattern 2

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
