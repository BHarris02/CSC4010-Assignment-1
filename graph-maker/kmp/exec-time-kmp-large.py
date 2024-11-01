import matplotlib.pyplot as plt

# Sample data for 1GB dataset (replace these lists with actual values if different)
threads = [1, 2, 4, 8, 16]
method_a_kmp_informed_pattern1 = [44.16, 31.33, 36.12, 39.88, 36.03]
method_a_kmp_full_pattern1 = [44.10, 22.92, 14.50, 19.77, 15.70]
method_b_kmp_informed_pattern1 = [29.80, 16.07, 9.54, 9.16, 11.19]
method_b_kmp_full_pattern1 = [42.87, 21.80, 18.26, 10.95, 5.12]

method_a_kmp_informed_pattern2 = [22.92, 23.02, 21.89, 22.18, 20.96]
method_a_kmp_full_pattern2 = [32.53, 19.45, 18.62, 7.06, 5.36]
method_b_kmp_informed_pattern2 = [21.74, 12.87, 7.12, 5.38, 3.92]
method_b_kmp_full_pattern2 = [30.16, 17.86, 15.72, 9.51, 4.66]

# Plotting 1GB dataset + Pattern 1
plt.figure(figsize=(10, 6))
plt.plot(threads, method_a_kmp_informed_pattern1, 'o-', label="Method A KMP-Informed", color="blue")
plt.plot(threads, method_a_kmp_full_pattern1, 'o-', label="Method A KMP-Full", color="orange")
plt.plot(threads, method_b_kmp_informed_pattern1, 'o-', label="Method B KMP-Informed", color="green")
plt.plot(threads, method_b_kmp_full_pattern1, 'o-', label="Method B KMP-Full", color="red")
plt.xticks(threads)
plt.xlabel("Number of Threads")
plt.ylabel("Wall Clock Time (s)")
plt.title("Wall Clock Time for 1GB Dataset + Pattern 1")
plt.legend()
plt.grid(True)
plt.savefig("Wall_Clock_Time_1GB_Dataset_Pattern1.png")
plt.show()

# Plotting 1GB dataset + Pattern 2
plt.figure(figsize=(10, 6))
plt.plot(threads, method_a_kmp_informed_pattern2, 'o-', label="Method A KMP-Informed", color="blue")
plt.plot(threads, method_a_kmp_full_pattern2, 'o-', label="Method A KMP-Full", color="orange")
plt.plot(threads, method_b_kmp_informed_pattern2, 'o-', label="Method B KMP-Informed", color="green")
plt.plot(threads, method_b_kmp_full_pattern2, 'o-', label="Method B KMP-Full", color="red")
plt.xticks(threads)
plt.xlabel("Number of Threads")
plt.ylabel("Wall Clock Time (s)")
plt.title("Wall Clock Time for 1GB Dataset + Pattern 2")
plt.legend()
plt.grid(True)
plt.savefig("Wall_Clock_Time_1GB_Dataset_Pattern2.png")
plt.show()
