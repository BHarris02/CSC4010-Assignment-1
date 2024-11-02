import matplotlib.pyplot as plt
# For each method and pattern combination, insert values in the specified order

# Method A, ac-Informed
efficiency_a_ac_informed_pattern1_1mb = [100, 72.22, 3250, 16.25, 27.08]
efficiency_a_ac_informed_pattern1_100mb = [100, 83.33, 75, 34.72, 27.57]
efficiency_a_ac_informed_pattern2_1mb = [100, 33.33, 1000, 4.16, 8.33]
efficiency_a_ac_informed_pattern2_100mb = [100, 89.36, 91.30, 35, 30.88]
efficiency_a_ac_informed_pattern1_1gb = [100, 65.96, 43.32, 25.66, 15.12]
efficiency_a_ac_informed_pattern2_1gb = [100, 85.94, 101.55, 72.25, 60.16]

# Method A, ac-Full
efficiency_a_ac_full_pattern1_1mb = [100, 75, 500, 2.67, 1.44]
efficiency_a_ac_full_pattern1_100mb = [100, 110.85, 82.59, 54.00, 35.69]
efficiency_a_ac_full_pattern2_1mb = [100, 100, 625, 1.78, 1.04]
efficiency_a_ac_full_pattern2_100mb = [100, 82.45, 51.64, 40.51, 19.91]
efficiency_a_ac_full_pattern1_1gb = [100, 62.69, 60.14, 7.19, 3.61]
efficiency_a_ac_full_pattern2_1gb = [100, 69.63, 61.42, 51.80, 28.47]

# Method B, ac-Informed
efficiency_b_ac_informed_pattern1_1mb = [100, 50, 175, 9.72, 10.93]
efficiency_b_ac_informed_pattern1_100mb =  [100, 50, 27.84, 10.89, 7.23]
efficiency_b_ac_informed_pattern2_1mb =  [100, 30, 75, 5.35, 6.25]
efficiency_b_ac_informed_pattern2_100mb = [100, 48.94, 28.01, 11.86, 7.17]
efficiency_b_ac_informed_pattern1_1gb =  [100, 50.74, 28.74, 14.46, 6.88]
efficiency_b_ac_informed_pattern2_1gb = [100, 50.95, 28.96, 16.55, 7.03]

# Method B, ac-Full
efficiency_b_ac_full_pattern1_1mb = [100, 5, 0.625, 0.125, 0.089]
efficiency_b_ac_full_pattern1_100mb = [100, 43.24, 17.77, 9.30, 5.55]
efficiency_b_ac_full_pattern2_1mb = [100, 5, 0.41, 0.20, 0.10]
efficiency_b_ac_full_pattern2_100mb = [100, 39.88, 18.61, 9.41, 5.43]
efficiency_b_ac_full_pattern1_1gb = [100, 50.59, 27.16, 14.33, 7.15]
efficiency_b_ac_full_pattern2_1gb =  [100, 50.56, 26.83, 14.25, 7.06]

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
    plt.xticks(threads)
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
