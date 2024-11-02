import matplotlib.pyplot as plt

# Thread counts to plot on x-axis
threads = [1, 2, 4, 8, 16]
# Wall clock times for 100MB dataset + Pattern 1
method_a_kmp_informed_pattern1 = [0.75, 0.45, 0.25, 0.27, 0.17]  
method_a_kmp_full_pattern1 = [3.37, 1.52, 1.02, 0.78, 0.59]      
method_b_kmp_informed_pattern1 = [0.88, 0.88, 0.79, 1.01, 0.76]  
method_b_kmp_full_pattern1 = [0.64, 0.74, 0.9, 0.86, 0.72]      

# Wall clock times for 100MB dataset + Pattern 2
method_a_kmp_informed_pattern2 = [0.84, 0.47, 0.23, 0.3, 0.17]  
method_a_kmp_full_pattern2 = [1.88, 1.14, 0.91, 0.58, 0.59]      
method_b_kmp_informed_pattern2 = [0.93, 0.95, 0.83, 0.98, 0.81]  
method_b_kmp_full_pattern2 = [0.67, 0.84, 0.9, 0.89, 0.77]      

# Plot for 100MB dataset + Pattern 1
plt.figure(figsize=(10, 6))
plt.plot(threads, method_a_kmp_informed_pattern1, marker='o', color='blue', label="Method A AC-Informed")
plt.plot(threads, method_a_kmp_full_pattern1, marker='o', color='orange', label="Method A AC-Full")
plt.plot(threads, method_b_kmp_informed_pattern1, marker='o', color='green', label="Method B AC-Informed")
plt.plot(threads, method_b_kmp_full_pattern1, marker='o', color='red', label="Method B AC-Full")
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
plt.plot(threads, method_a_kmp_informed_pattern2, marker='o', color='blue', label="Method A AC-Informed")
plt.plot(threads, method_a_kmp_full_pattern2, marker='o', color='orange', label="Method A AC-Full")
plt.plot(threads, method_b_kmp_informed_pattern2, marker='o', color='green', label="Method B AC-Informed")
plt.plot(threads, method_b_kmp_full_pattern2, marker='o', color='red', label="Method B AC-Full")
plt.title("Wall Clock Time for 100MB Dataset + Pattern 2")
plt.xlabel("Number of Threads")
plt.ylabel("Wall Clock Time (s)")
plt.xticks(threads)
plt.legend()
plt.grid(True)
plt.savefig("100MB_Pattern2_WallClockTime.png")
plt.show()
