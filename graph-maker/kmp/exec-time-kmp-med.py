import matplotlib.pyplot as plt

# Thread counts to plot on x-axis
threads = [1, 2, 4, 8, 16]

# Wall clock times for 100MB dataset + Pattern 1
method_a_kmp_informed_pattern1 = [3.48, 3.28, 2.99, 2.57, 4.43]  # Method A KMP-Informed
method_a_kmp_full_pattern1 = [5.02, 4.89, 1.53, 1.01, 0.79]      # Method A KMP-Full
method_b_kmp_informed_pattern1 = [3.45, 1.67, 0.98, 1.07, 0.64]  # Method B KMP-Informed
method_b_kmp_full_pattern1 = [4.76, 3.36, 1.57, 0.93, 0.55]      # Method B KMP-Full

# Wall clock times for 100MB dataset + Pattern 2
method_a_kmp_informed_pattern2 = [2.59, 2.34, 2.28, 2.29, 2.44]  # Method A KMP-Informed
method_a_kmp_full_pattern2 = [3.62, 2.67, 1.51, 0.64, 0.75]      # Method A KMP-Full
method_b_kmp_informed_pattern2 = [2.54, 1.28, 0.70, 0.57, 0.48]  # Method B KMP-Informed
method_b_kmp_full_pattern2 = [3.39, 2.02, 1.31, 0.64, 0.69]      # Method B KMP-Full

# Plot for 100MB dataset + Pattern 1
plt.figure(figsize=(10, 6))
plt.plot(threads, method_a_kmp_informed_pattern1, marker='o', color='blue', label="Method A KMP-Informed")
plt.plot(threads, method_a_kmp_full_pattern1, marker='o', color='orange', label="Method A KMP-Full")
plt.plot(threads, method_b_kmp_informed_pattern1, marker='o', color='green', label="Method B KMP-Informed")
plt.plot(threads, method_b_kmp_full_pattern1, marker='o', color='red', label="Method B KMP-Full")
plt.title("Wall Clock Time for 100MB Dataset + Pattern 1")
plt.xlabel("Number of Threads")
plt.ylabel("Wall Clock Time (s)")
plt.xticks(threads)
plt.legend()
plt.grid(True)
plt.savefig("100MB_Pattern1_WallClockTime.png")
plt.show()

# Plot for 100MB dataset + Pattern 2
plt.figure(figsize=(10, 6))
plt.plot(threads, method_a_kmp_informed_pattern2, marker='o', color='blue', label="Method A KMP-Informed")
plt.plot(threads, method_a_kmp_full_pattern2, marker='o', color='orange', label="Method A KMP-Full")
plt.plot(threads, method_b_kmp_informed_pattern2, marker='o', color='green', label="Method B KMP-Informed")
plt.plot(threads, method_b_kmp_full_pattern2, marker='o', color='red', label="Method B KMP-Full")
plt.title("Wall Clock Time for 100MB Dataset + Pattern 2")
plt.xlabel("Number of Threads")
plt.ylabel("Wall Clock Time (s)")
plt.xticks(threads)
plt.legend()
plt.grid(True)
plt.savefig("100MB_Pattern2_WallClockTime.png")
plt.show()
